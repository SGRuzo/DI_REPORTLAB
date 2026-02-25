import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QVBoxLayout, QHBoxLayout, QGridLayout,
    QLabel, QPushButton, QLineEdit, QTextEdit,
    QComboBox, QGroupBox, QTabWidget, QMessageBox
)
from PyQt6.QtGui import QColor


# ============================================================
#  PESTAÑA 1: EJEMPLOS BÁSICOS
# ============================================================

class TabBotonesBasicos(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.lbl = QLabel("Texto de ejemplo")
        layout.addWidget(self.lbl)

        fila1 = QHBoxLayout()
        fila2 = QHBoxLayout()

        # Cambiar colores
        btnColorRojo = QPushButton("Texto Rojo")
        btnColorRojo.clicked.connect(lambda: self.lbl.setStyleSheet("color: red;"))
        fila1.addWidget(btnColorRojo)

        btnAzul = QPushButton("Texto Azul")
        btnAzul.clicked.connect(lambda: self.lbl.setStyleSheet("color: blue;"))
        fila1.addWidget(btnAzul)

        btnFondo = QPushButton("Fondo Verde")
        btnFondo.clicked.connect(lambda: self.setStyleSheet("background-color: lightgreen;"))
        fila1.addWidget(btnFondo)

        # Habilitar / deshabilitar botones
        self.btnDeshabilitar = QPushButton("Deshabilitar Botón Azul")
        self.btnDeshabilitar.clicked.connect(self.toggle_btn)

        fila2.addWidget(self.btnDeshabilitar)

        layout.addLayout(fila1)
        layout.addLayout(fila2)

        self.btnAux = btnAzul  # botón a deshabilitar/habilitar
        self.setLayout(layout)

    def toggle_btn(self):
        estado = self.btnAux.isEnabled()
        self.btnAux.setEnabled(not estado)
        self.btnDeshabilitar.setText(
            "Habilitar Botón Azul" if estado else "Deshabilitar Botón Azul"
        )


# ============================================================
#  PESTAÑA 2: EJEMPLOS AVANZADOS
# ============================================================

class OtraVentana(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana Secundaria")
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Esta es otra ventana."))
        self.setLayout(layout)


class TabAvanzados(QWidget):
    def __init__(self):
        super().__init__()

        principal = QVBoxLayout()

        # ----------------------------------------
        # GroupBox de demostración
        # ----------------------------------------
        gpb = QGroupBox("GroupBox de Ejemplo")
        grid = QGridLayout()
        grid.addWidget(QLabel("Fila 0 Col 0"), 0, 0)
        grid.addWidget(QLabel("Fila 0 Col 1"), 0, 1)
        grid.addWidget(QPushButton("Botón A"), 1, 0)
        grid.addWidget(QPushButton("Botón B"), 1, 1)
        gpb.setLayout(grid)

        principal.addWidget(gpb)

        # ----------------------------------------
        # ComboBox avanzado
        # ----------------------------------------
        h = QHBoxLayout()
        self.cmb = QComboBox()
        self.cmb.addItems(["Manzana", "Pera", "Fresa"])
        h.addWidget(self.cmb)

        self.txtNuevo = QLineEdit()
        h.addWidget(self.txtNuevo)

        btnAdd = QPushButton("Añadir")
        btnAdd.clicked.connect(self.add_item)
        h.addWidget(btnAdd)

        btnDel = QPushButton("Eliminar seleccionado")
        btnDel.clicked.connect(self.del_item)
        h.addWidget(btnDel)

        btnOrd = QPushButton("Ordenar")
        btnOrd.clicked.connect(self.ordenar)
        h.addWidget(btnOrd)

        principal.addLayout(h)

        # ----------------------------------------
        # Mover texto entre QTextEdits
        # ----------------------------------------
        mover = QHBoxLayout()

        self.txt1 = QTextEdit()
        self.txt2 = QTextEdit()

        mover.addWidget(self.txt1)

        botonesMover = QVBoxLayout()
        btnToRight = QPushButton("→")
        btnToRight.clicked.connect(self.moveToRight)
        botonesMover.addWidget(btnToRight)

        btnToLeft = QPushButton("←")
        btnToLeft.clicked.connect(self.moveToLeft)
        botonesMover.addWidget(btnToLeft)

        mover.addLayout(botonesMover)
        mover.addWidget(self.txt2)

        principal.addLayout(mover)

        # ----------------------------------------
        # Abrir otra ventana
        # ----------------------------------------
        self.segundaVentana = OtraVentana()
        btnNueva = QPushButton("Abrir otra ventana")
        btnNueva.clicked.connect(self.segundaVentana.show)
        principal.addWidget(btnNueva)

        # ----------------------------------------
        # Cerrar aplicación
        # ----------------------------------------
        btnCerrar = QPushButton("Cerrar aplicación")
        btnCerrar.clicked.connect(lambda: self.window().close())
        principal.addWidget(btnCerrar)

        self.setLayout(principal)

    # ------- funciones extra -------

    def add_item(self):
        texto = self.txtNuevo.text().strip()
        if texto:
            self.cmb.addItem(texto)
            self.txtNuevo.clear()

    def del_item(self):
        idx = self.cmb.currentIndex()
        if idx >= 0:
            self.cmb.removeItem(idx)

    def ordenar(self):
        items = [self.cmb.itemText(i) for i in range(self.cmb.count())]
        items.sort()
        self.cmb.clear()
        self.cmb.addItems(items)

    def moveToRight(self):
        self.txt2.setPlainText(self.txt1.toPlainText())

    def moveToLeft(self):
        self.txt1.setPlainText(self.txt2.toPlainText())


# ============================================================
#  PESTAÑA 3: CLIENTES GRUPO B (tu ejercicio, sin tocar)
# ============================================================

class TabClientesGrupoB(QWidget):
    def __init__(self):
        super().__init__()

        layout_principal = QVBoxLayout()
        maia = QGridLayout()

        self.lista_provincias = ["A Coruña", "Lugo", "Ourense", "Pontevedra"]

        gpbCliente = QGroupBox("Cliente")

        self.lblNumeroCliente = QLabel("Número Cliente")
        self.lblNomeCliente = QLabel("Nome")
        self.lblApelidosCliente = QLabel("Apelidos")
        self.lblDireccion = QLabel("Dirección")
        self.lblCidade = QLabel("Cidade")
        self.lblProvinciaEstado = QLabel("Provincia")

        self.txtNumeroCliente = QLineEdit()
        self.txtNomeCliente = QLineEdit()
        self.txtApelidosCliente = QLineEdit()
        self.txtDireccion = QLineEdit()
        self.txtCidade = QLineEdit()

        self.cmbProvincia = QComboBox()
        self.cmbProvincia.addItems(self.lista_provincias)
        self.cmbProvincia.setCurrentIndex(-1)

        maia.addWidget(self.lblNumeroCliente, 0, 0)
        maia.addWidget(self.txtNumeroCliente, 0, 1)
        maia.addWidget(self.lblNomeCliente, 0, 2)
        maia.addWidget(self.txtNomeCliente, 0, 3)

        maia.addWidget(self.lblApelidosCliente, 1, 0)
        maia.addWidget(self.txtApelidosCliente, 1, 1, 1, 3)

        maia.addWidget(self.lblDireccion, 2, 0)
        maia.addWidget(self.txtDireccion, 2, 1, 1, 3)

        maia.addWidget(self.lblCidade, 3, 0)
        maia.addWidget(self.txtCidade, 3, 1)
        maia.addWidget(self.lblProvinciaEstado, 3, 2)
        maia.addWidget(self.cmbProvincia, 3, 3)

        gpbCliente.setLayout(maia)
        layout_principal.addWidget(gpbCliente)

        layout_medio = QHBoxLayout()
        layout_principal.addLayout(layout_medio)

        self.txeClientes = QTextEdit()
        layout_medio.addWidget(self.txeClientes)

        layout_botones = QVBoxLayout()

        btnEngadir = QPushButton("Engadir")
        btnEngadir.clicked.connect(self.btnEngadir_onClick)

        btnBorrar = QPushButton("Borrar")
        btnBorrar.clicked.connect(self.btn_Borrar_onClick)

        layout_botones.addWidget(btnEngadir)
        layout_botones.addWidget(btnBorrar)
        layout_botones.addStretch()

        layout_medio.addLayout(layout_botones)

        self.setLayout(layout_principal)

    def btnEngadir_onClick(self):
        if not self.comprobarCampos():
            return

        linea = f"{self.txtNumeroCliente.text()}, {self.txtNomeCliente.text()}, " \
                f"{self.txtApelidosCliente.text()}, {self.txtDireccion.text()}, {self.txtCidade.text()}, " \
                f"{self.cmbProvincia.currentText()}"
        self.txeClientes.append(linea)
        self.limpiarFormulario()

    def comprobarCampos(self):
        todo = True

        controles = [
            (self.txtNumeroCliente, self.lblNumeroCliente),
            (self.txtNomeCliente, self.lblNomeCliente),
            (self.txtApelidosCliente, self.lblApelidosCliente),
            (self.txtDireccion, self.lblDireccion),
            (self.txtCidade, self.lblCidade),
        ]

        for txt, lbl in controles:
            if txt.text().strip() == "":
                lbl.setStyleSheet("color:red;")
                todo = False
            else:
                lbl.setStyleSheet("color:black;")

        if self.cmbProvincia.currentIndex() == -1:
            self.lblProvinciaEstado.setStyleSheet("color:red;")
            todo = False
        else:
            self.lblProvinciaEstado.setStyleSheet("color:black;")

        return todo

    def limpiarFormulario(self):
        self.txtNumeroCliente.clear()
        self.txtNomeCliente.clear()
        self.txtApelidosCliente.clear()
        self.txtDireccion.clear()
        self.txtCidade.clear()
        self.cmbProvincia.setCurrentIndex(-1)

    def btn_Borrar_onClick(self):
        num = self.txtNumeroCliente.text().strip()
        if not num:
            return

        nuevas = []
        for liña in self.txeClientes.toPlainText().split("\n"):
            if liña.strip() == "":
                continue
            if liña.split(",")[0].strip() != num:
                nuevas.append(liña)

        self.txeClientes.setPlainText("\n".join(nuevas))
        self.limpiarFormulario()


# ============================================================
#  PESTAÑA 4: ALBARÁS GRUPO A (sin tocar)
# ============================================================

class TabAlbarrasGrupoA(QWidget):
    def __init__(self):
        super().__init__()

        maia = QGridLayout()
        layout_principal = QVBoxLayout()

        gpbAlbara = QGroupBox("Albará")

        self.lista_Albarras = [
            ["1111nm", "02/11/2024", "1111", "Ana", "Ruiz"],
            ["2222io", "09/03/2024", "2222", "Pedro", "Diz"],
            ["3333qw", "23/10/2025", "3333", "Rosa", "Sanz"]
        ]

        lblNumeroAlbara = QLabel("Número Albará")
        lblDataAlbara = QLabel("Data")
        lblNumeroCliente = QLabel("Número cliente")
        lblNomeCliente = QLabel("Nome Cliente")
        lblApelidosCliente = QLabel("Apelidos")

        self.cmbNumeroAlbara = QComboBox()
        self.cmbNumeroAlbara.addItems([albara[0] for albara in self.lista_Albarras])
        self.cmbNumeroAlbara.setCurrentIndex(-1)
        self.cmbNumeroAlbara.currentIndexChanged.connect(self.on_cmbNumeroAlbara_changed)

        self.txtDataAlbara = QLineEdit()
        self.txtNumeroCliente = QLineEdit()
        self.txtNomeCliente = QLineEdit()
        self.txtApelidosCliente = QLineEdit()

        btnEditar = QPushButton("Editar")
        btnEditar.clicked.connect(self.onClick_btnEditar)

        self.txeCadroTexto = QTextEdit()

        btnCancelar = QPushButton("Cancelar")
        btnCancelar.clicked.connect(lambda: self.window().close())

        maia.addWidget(lblNumeroAlbara, 0, 0)
        maia.addWidget(self.cmbNumeroAlbara, 0, 1)
        maia.addWidget(lblDataAlbara, 0, 2)
        maia.addWidget(self.txtDataAlbara, 0, 3)

        maia.addWidget(lblNumeroCliente, 1, 0)
        maia.addWidget(self.txtNumeroCliente, 1, 1)
        maia.addWidget(lblNomeCliente, 1, 2)
        maia.addWidget(self.txtNomeCliente, 1, 3)

        maia.addWidget(lblApelidosCliente, 2, 0)
        maia.addWidget(self.txtApelidosCliente, 2, 1, 1, 3)

        gpbAlbara.setLayout(maia)
        layout_principal.addWidget(gpbAlbara)

        layout_principal.addWidget(btnEditar)
        layout_principal.addWidget(self.txeCadroTexto)
        layout_principal.addWidget(btnCancelar)

        self.setLayout(layout_principal)

    def onClick_btnEditar(self):
        if self.cmbNumeroAlbara.currentIndex() < 0:
            return

        nAlbara = self.cmbNumeroAlbara.currentText()
        linea = f"{nAlbara}, {self.txtDataAlbara.text()}, {self.txtNumeroCliente.text()}, {self.txtNomeCliente.text()}, {self.txtApelidosCliente.text()}"
        self.txeCadroTexto.append(linea)

    def on_cmbNumeroAlbara_changed(self, index: int):
        if index < 0:
            self.txtDataAlbara.clear()
            self.txtNumeroCliente.clear()
            self.txtNomeCliente.clear()
            self.txtApelidosCliente.clear()
            return

        albara = self.lista_Albarras[index]
        self.txtDataAlbara.setText(albara[1])
        self.txtNumeroCliente.setText(albara[2])
        self.txtNomeCliente.setText(albara[3])
        self.txtApelidosCliente.setText(albara[4])


# ============================================================
#  VENTANA PRINCIPAL
# ============================================================

class PracticaComleta(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PracticaComleta - Demostraciones Qt6")

        tabs = QTabWidget()
        tabs.addTab(TabBotonesBasicos(), "Básicos")
        tabs.addTab(TabAvanzados(), "Avanzados")
        tabs.addTab(TabClientesGrupoB(), "Clientes")
        tabs.addTab(TabAlbarrasGrupoA(), "Albarás")

        container = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(tabs)
        container.setLayout(layout)

        self.setCentralWidget(container)


# ============================================================
#  MAIN
# ============================================================

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = PracticaComleta()
    ventana.show()
    sys.exit(app.exec())
