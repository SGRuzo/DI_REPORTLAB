import sys
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton, QVBoxLayout, QListView


class VentanaListas(QWidget):
    def __init__(self):
        super().__init__()

        # ----- MODELOS -----
        self.modelo = QStandardItemModel()
        self.modeloOcultas = QStandardItemModel()

        # Engadir elementos ao modelo principal
        for texto in ["Hoja 1", "Hoja 2", "Hoja 3", "Hoja 4", "Hoja 5"]:
            self.modelo.appendRow(QStandardItem(texto))

        # ----- LISTAS -----
        self.listaVisibles = QListView()
        self.listaVisibles.setModel(self.modelo)

        self.listaOcultas = QListView()
        self.listaOcultas.setModel(self.modeloOcultas)

        # ----- BOTÓNS -----
        self.botonOcultar = QPushButton("Ocultar>>")
        self.botonMostrar = QPushButton("<<Mostrar")

        self.botonOcultar.clicked.connect(self.ocultar)
        self.botonMostrar.clicked.connect(self.mostrar)

        # Layout vertical para botóns
        self.cajaVertical = QVBoxLayout()
        self.cajaVertical.addWidget(self.botonOcultar)
        self.cajaVertical.addWidget(self.botonMostrar)

        # Layout principal
        self.cajaHorizontal = QHBoxLayout()
        self.cajaHorizontal.addWidget(self.listaVisibles)
        self.cajaHorizontal.addLayout(self.cajaVertical)
        self.cajaHorizontal.addWidget(self.listaOcultas)

        self.setLayout(self.cajaHorizontal)
        self.setWindowTitle("Listas Visibles/Ocultas")
        self.show()

    # ----- FUNCIÓNS -----
    def mostrar(self):
        self.mover(self.modeloOcultas, self.modelo, self.listaOcultas)

    def ocultar(self):
        self.mover(self.modelo, self.modeloOcultas, self.listaVisibles)

    def mover(self, origen_modelo, destino_modelo, lista_view):
        indexes = lista_view.selectionModel().selectedIndexes()
        if not indexes:
            return

        rows = sorted({i.row() for i in indexes}, reverse=True)
        for row in rows:
            destino_modelo.appendRow(origen_modelo.takeRow(row))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaListas()
    sys.exit(app.exec())
