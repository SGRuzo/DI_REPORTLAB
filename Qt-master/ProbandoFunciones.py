import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QPushButton, QListView, QTextEdit, QGroupBox
)
from PyQt6.QtGui import QStandardItemModel, QStandardItem


class VentanaConListas(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Lista con Model-View")
        self.setGeometry(200, 200, 500, 400)

        # ======================================================
        #   WIDGETS
        # ======================================================

        # Área de escritura
        self.cuadro_texto = QTextEdit()
        self.cuadro_texto.setMaximumHeight(60)
        self.cuadro_texto.setPlaceholderText("Escribe el texto del nuevo elemento...")

        # Botones principales
        self.btn_añadir = QPushButton("Añadir")
        self.btn_borrar_ultimo = QPushButton("Borrar Último")
        self.btn_limpiar_todo = QPushButton("Limpiar Todo")

        # Modelo y lista
        self.modelo = QStandardItemModel()
        self.lista = QListView()
        self.lista.setModel(self.modelo)

        # Controles avanzados
        self.btn_borrar_sel = QPushButton("Borrar Seleccionado")
        self.btn_editar_sel = QPushButton("Editar Seleccionado")
        self.btn_contar = QPushButton("Contar Elementos")
        self.lbl_info = QLabel("Elementos: 0")

        # Cargar elementos de ejemplo
        for t in ["Elemento de ejemplo 1", "Elemento de ejemplo 2"]:
            self.modelo.appendRow(QStandardItem(t))

        # ======================================================
        #   LAYOUTS
        # ======================================================

        # Grupo de entrada
        caja_entrada = QHBoxLayout()
        caja_entrada.addWidget(self.cuadro_texto)
        caja_entrada.addWidget(self.btn_añadir)
        caja_entrada.addWidget(self.btn_borrar_ultimo)
        caja_entrada.addWidget(self.btn_limpiar_todo)

        grupo_entrada = QGroupBox("Añadir elementos a la lista")
        grupo_entrada.setLayout(caja_entrada)

        # Grupo lista
        caja_lista = QVBoxLayout()
        caja_lista.addWidget(self.lista)

        grupo_lista = QGroupBox("Lista de elementos")
        grupo_lista.setLayout(caja_lista)

        # Grupo controles
        caja_controles = QHBoxLayout()
        caja_controles.addWidget(self.btn_borrar_sel)
        caja_controles.addWidget(self.btn_editar_sel)
        caja_controles.addWidget(self.btn_contar)
        caja_controles.addWidget(self.lbl_info)

        grupo_controles = QGroupBox("Controles de la Lista")
        grupo_controles.setLayout(caja_controles)

        # Layout principal
        layout_principal = QVBoxLayout()
        layout_principal.addWidget(grupo_entrada)
        layout_principal.addWidget(grupo_lista)
        layout_principal.addWidget(grupo_controles)

        self.setLayout(layout_principal)

        # ======================================================
        #   SEÑALES
        # ======================================================

        self.btn_añadir.clicked.connect(self.anadir_elemento)
        self.btn_borrar_ultimo.clicked.connect(self.borrar_ultimo)
        self.btn_limpiar_todo.clicked.connect(self.limpiar_todo)

        self.btn_borrar_sel.clicked.connect(self.borrar_seleccionado)
        self.btn_editar_sel.clicked.connect(self.editar_seleccionado)
        self.btn_contar.clicked.connect(self.actualizar_contador)

        self.lista.selectionModel().selectionChanged.connect(self.seleccion_cambiada)

        # Actualizar contador al inicio
        self.actualizar_contador()

    # ======================================================
    #   LÓGICA
    # ======================================================

    def anadir_elemento(self):
        texto = self.cuadro_texto.toPlainText().strip()
        if texto == "":
            return

        self.modelo.appendRow(QStandardItem(texto))
        self.cuadro_texto.clear()
        self.actualizar_contador()

        index = self.modelo.index(self.modelo.rowCount() - 1, 0)
        self.lista.setCurrentIndex(index)

    def borrar_ultimo(self):
        if self.modelo.rowCount() > 0:
            self.modelo.removeRow(self.modelo.rowCount() - 1)
            self.actualizar_contador()

    def borrar_seleccionado(self):
        index = self.lista.currentIndex()
        if index.isValid():
            self.modelo.removeRow(index.row())
            self.actualizar_contador()

    def editar_seleccionado(self):
        index = self.lista.currentIndex()
        if index.isValid():
            self.lista.edit(index)

    def limpiar_todo(self):
        self.modelo.clear()
        self.modelo.setHorizontalHeaderLabels(["Elementos de la Lista"])
        self.actualizar_contador()

    def seleccion_cambiada(self):
        index = self.lista.currentIndex()
        if index.isValid():
            texto = self.modelo.itemFromIndex(index).text()
            self.lbl_info.setText(f"Seleccionado: {texto}")

    def actualizar_contador(self):
        total = self.modelo.rowCount()
        self.lbl_info.setText(f"Elementos: {total}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaConListas()
    ventana.show()
    sys.exit(app.exec())
