import sys
import ExemplosCor
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QGridLayout


class ExemploBox(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exemplo con QGridLayout")

        # Crear el layout en cuadrícula
        maia = QGridLayout()

        # Añadir widgets de color desde el módulo ExemplosCor
        maia.addWidget(ExemplosCor.CaixaCor("red"), 0, 0)
        maia.addWidget(ExemplosCor.CaixaCor("yellow"), 0, 1, 1, 2)
        maia.addWidget(ExemplosCor.CaixaCor("green"), 1, 0)
        maia.addWidget(ExemplosCor.CaixaCor("blue"), 1, 1  )

        # Contenedor central
        container = QWidget()
        container.setLayout(maia)
        self.setCentralWidget(container)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = ExemploBox()
    ventana.show()
    sys.exit(app.exec())
