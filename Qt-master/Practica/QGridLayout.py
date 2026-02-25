import sys
from PyQt6.QtWidgets import QMainWindow, QPushButton, QHBoxLayout, QWidget, QApplication, QGridLayout


class QGridLayoutExample(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ejemplo QGridLayout")

        boton1 = QPushButton("Boton a (0, 0)")
        boton2 = QPushButton("Boton a (0, 1)")
        boton3 = QPushButton("Boton a (0, 2)")
        boton4 = QPushButton("Boton a (1, 0)")
        boton5 = QPushButton("Boton a (1, 1)")
        boton6 = QPushButton("Boton a (1, 2)")
        boton7 = QPushButton("Boton a (2, 0)")

        layout_grid = QGridLayout()
        layout_grid.addWidget(boton1, 0, 0)
        layout_grid.addWidget(boton2, 0, 1)
        layout_grid.addWidget(boton3, 0, 2)
        layout_grid.addWidget(boton4, 1, 0)
        layout_grid.addWidget(boton5, 1, 1)
        layout_grid.addWidget(boton6, 1, 2)
        layout_grid.addWidget(boton7, 2, 0, 1, 2) # columna, fila, rowspan, colspan

        container = QWidget()
        container.setLayout(layout_grid)
        self.setCentralWidget(container)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = QGridLayoutExample()
    ventana.show()
    sys.exit(app.exec())
