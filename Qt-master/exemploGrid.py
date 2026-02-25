# exemploGrid.py
import sys
import ExemplosCor
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QGridLayout

class ExemploBox(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exemplo con QGridLayout")

        # Crear el layout en cuadrícula
        maia = QGridLayout()


        # Añadir widgets de color (clase CaixaCor del módulo ExemplosCor)
        maia.addWidget(ExemplosCor.CaixaCor("red"))
        maia.addWidget(ExemplosCor.CaixaCor("blue"), 0, 1,1, 2)
        maia.addWidget(ExemplosCor.CaixaCor("green"), 1, 0,2,1)
        maia.addWidget(ExemplosCor.CaixaCor("pink"), 1, 1,1,2)
        maia.addWidget(ExemplosCor.CaixaCor("orange"), 1, 2,1,1)
        maia.addWidget(ExemplosCor.CaixaCor("yellow"), 2, 2,1,1)



        # Crear contenedor central
        container = QWidget()
        container.setLayout(maia)
        self.setCentralWidget(container)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = ExemploBox()
    ventana.show()
    sys.exit(app.exec())
