import sys
import os
import sqlite3
import platform
from datetime import datetime
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                             QHBoxLayout, QLabel, QLineEdit, QPushButton,
                             QMessageBox, QFrame, QTableWidget, QTableWidgetItem,
                             QHeaderView, QDialog, QComboBox, QSpinBox)
from PyQt6.QtCore import Qt

# --- REPORTLAB ---
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie


# --- DIÁLOGO PARA AÑADIR FACTURA ---
class DialogoFactura(QDialog):
    def __init__(self, id_cliente, nombre_cliente, db_path):
        super().__init__()
        self.setWindowTitle(f"Nueva Factura para: {nombre_cliente}")
        self.db_path = db_path
        self.id_cliente = id_cliente
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Seleccionar Producto:"))
        self.combo_producto = QComboBox()
        self.cargar_productos()
        layout.addWidget(self.combo_producto)

        layout.addWidget(QLabel("Cantidad:"))
        self.spin_cantidad = QSpinBox()
        self.spin_cantidad.setRange(1, 100)
        layout.addWidget(self.spin_cantidad)

        btn_guardar = QPushButton("Generar Factura")
        btn_guardar.clicked.connect(self.accept)
        layout.addWidget(btn_guardar)
        self.setLayout(layout)

    def cargar_productos(self):
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute("SELECT id_produto, nome, prezo FROM produtos")
            for id_p, nombre, precio in cursor.fetchall():
                self.combo_producto.addItem(f"{nombre} ({precio}€)", (id_p, precio))
            conn.close()
        except:
            pass


# --- VENTANA PRINCIPAL ---
class VentanaGestion(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestión de Facturación Pro")
        self.setMinimumSize(900, 750)
        self.db_path = 'bdTendaOrdeadoresBig.bd'
        self.init_ui()
        self.actualizar_tabla_visual()

    def init_ui(self):
        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)

        # Registro de Cliente
        layout.addWidget(QLabel("<b>Añadir Cliente</b>"))
        form_h = QHBoxLayout()
        self.in_nom = QLineEdit();
        self.in_nom.setPlaceholderText("Nombre")
        self.in_nif = QLineEdit();
        self.in_nif.setPlaceholderText("NIF")
        btn_reg = QPushButton("Registrar");
        btn_reg.clicked.connect(self.agregar_cliente)
        form_h.addWidget(self.in_nom);
        form_h.addWidget(self.in_nif);
        form_h.addWidget(btn_reg)
        layout.addLayout(form_h)

        # Tabla Principal
        layout.addWidget(QLabel("<b>Clientes (Doble clic para facturar)</b>"))
        self.tabla = QTableWidget()
        self.tabla.setColumnCount(5)
        self.tabla.setHorizontalHeaderLabels(["ID", "Cliente", "NIF", "Facturas", "Total (€)"])
        self.tabla.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        self.tabla.doubleClicked.connect(self.abrir_editor_factura)
        layout.addWidget(self.tabla)

        # Panel de Reportes
        layout.addWidget(QLabel("<b>Exportar Informes PDF (Top 5 Clientes)</b>"))
        btn_box = QHBoxLayout()

        btn_tabla = QPushButton("Solo Tabla")
        btn_tabla.clicked.connect(lambda: self.generar_pdf(incluir_tabla=True, incluir_grafico=False))

        btn_grafico = QPushButton("Solo Gráfico")
        btn_grafico.clicked.connect(lambda: self.generar_pdf(incluir_tabla=False, incluir_grafico=True))

        btn_unificado = QPushButton("Informe Unificado")
        btn_unificado.setStyleSheet("background-color: #27ae60; color: white; font-weight: bold; padding: 10px;")
        btn_unificado.clicked.connect(lambda: self.generar_pdf(incluir_tabla=True, incluir_grafico=True))

        btn_box.addWidget(btn_tabla);
        btn_box.addWidget(btn_grafico);
        btn_box.addWidget(btn_unificado)
        layout.addLayout(btn_box)

    def actualizar_tabla_visual(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        query = """SELECT c.id_cliente, c.nome, c.nif, COUNT(DISTINCT f.id_factura),
                   SUM(lf.cantidade * lf.prezo_unitario * (1 - lf.desconto/100) * (1 + p.iva/100))
                   FROM clientes c
                   LEFT JOIN facturas f ON c.id_cliente = f.id_cliente
                   LEFT JOIN linhas_factura lf ON f.id_factura = lf.id_factura
                   LEFT JOIN produtos p ON lf.id_produto = p.id_produto
                   GROUP BY c.id_cliente ORDER BY 5 DESC"""
        cursor.execute(query)
        self.tabla.setRowCount(0)
        for r_idx, row in enumerate(cursor.fetchall()):
            self.tabla.insertRow(r_idx)
            for c_idx, val in enumerate(row):
                v = f"{val:,.2f}" if c_idx == 4 and val else (
                    "0.00" if c_idx == 4 else str(val if val is not None else 0))
                self.tabla.setItem(r_idx, c_idx, QTableWidgetItem(v))
        conn.close()

    def agregar_cliente(self):
        if not self.in_nom.text() or not self.in_nif.text(): return
        conn = sqlite3.connect(self.db_path)
        conn.execute("INSERT INTO clientes (nome, nif) VALUES (?,?)", (self.in_nom.text(), self.in_nif.text()))
        conn.commit();
        conn.close()
        self.in_nom.clear();
        self.in_nif.clear()
        self.actualizar_tabla_visual()

    def abrir_editor_factura(self, index):
        id_cliente = self.tabla.item(index.row(), 0).text()
        nombre_cliente = self.tabla.item(index.row(), 1).text()
        dialogo = DialogoFactura(id_cliente, nombre_cliente, self.db_path)
        if dialogo.exec():
            id_prod, precio = dialogo.combo_producto.currentData()
            self.crear_factura_real(id_cliente, id_prod, precio, dialogo.spin_cantidad.value())

    def crear_factura_real(self, id_cli, id_prod, precio, cant):
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        num_f = f"FAC-{datetime.now().strftime('%Y%m%d%H%M%S')}"
        cur.execute("INSERT INTO facturas (numero_factura, id_cliente, data_factura) VALUES (?,?,?)",
                    (num_f, id_cli, datetime.now().strftime('%Y-%m-%d')))
        cur.execute("INSERT INTO linhas_factura (id_factura, id_produto, cantidade, prezo_unitario) VALUES (?,?,?,?)",
                    (cur.lastrowid, id_prod, cant, precio))
        conn.commit();
        conn.close()
        self.actualizar_tabla_visual()

    def generar_pdf(self, incluir_tabla, incluir_grafico):
        res = self.obtener_top_5()
        if not res:
            QMessageBox.warning(self, "Error", "No hay datos de facturación para el reporte.")
            return

        nombre_archivo = "Informe_Ventas.pdf"
        doc = SimpleDocTemplate(nombre_archivo, pagesize=A4)
        styles = getSampleStyleSheet()
        story = [Paragraph("REPORTE DE GESTIÓN COMERCIAL", styles['Title']), Spacer(1, 20)]

        if incluir_tabla:
            story.append(Paragraph("Ranking de Facturación por Cliente", styles['Heading2']))
            data = [["Cliente", "Facturas", "Total Facturado"]]
            for r in res:
                data.append([r[0], str(r[1]), f"{r[2]:,.2f} €"])

            t = Table(data, colWidths=[240, 80, 110])
            t.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (2, 1), (2, -1), 'RIGHT'),
                ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
                ('FONTSIZE', (0, 0), (-1, -1), 10),
            ]))
            story.append(t)
            story.append(Spacer(1, 30))

        if incluir_grafico:
            story.append(Paragraph("Distribución de Ingresos (€)", styles['Heading2']))
            d = Drawing(400, 250)
            pc = Pie()
            pc.x, pc.y, pc.width, pc.height = 150, 50, 160, 160
            pc.data = [float(r[2]) for r in res]
            pc.labels = [r[0] for r in res]
            pc.sideLabels = True
            d.add(pc)
            story.append(d)

        doc.build(story)
        self.abrir_archivo(nombre_archivo)

    def obtener_top_5(self):
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        cur.execute("""SELECT c.nome, COUNT(DISTINCT f.id_factura), 
                       SUM(lf.cantidade * lf.prezo_unitario * (1 - lf.desconto/100) * (1 + p.iva/100))
                       FROM clientes c JOIN facturas f ON c.id_cliente = f.id_cliente
                       JOIN linhas_factura lf ON f.id_factura = lf.id_factura
                       JOIN produtos p ON lf.id_produto = p.id_produto
                       GROUP BY c.id_cliente ORDER BY 3 DESC LIMIT 5""")
        res = cur.fetchall();
        conn.close();
        return res


    def abrir_archivo(self, path):
        try:
            if platform.system() == "Windows":
                os.startfile(path)
            elif platform.system() == "Linux":
                os.system(f"xdg-open {path}")
        except Exception as e:
            print(f"No se pudo abrir el archivo: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv);
    app.setStyle("Fusion")
    win = VentanaGestion();
    win.show();
    sys.exit(app.exec())