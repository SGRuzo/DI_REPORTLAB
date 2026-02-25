import sys
import ExemplosCor
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QVBoxLayout, QHBoxLayout

class EjemploVHLayout(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ejemplo con QVBoxLayout y QHBoxLayout")

        # Crear el layout vertical principal
        layout_HorizontalPrincial = QHBoxLayout()

        # Añadir un layout horizontal dentro del layout vertical
        layout_vertical1 = QVBoxLayout()
        layout_vertical1.addWidget(ExemplosCor.CaixaCor("red"))
        layout_vertical1.addWidget(ExemplosCor.CaixaCor("yellow"))
        layout_vertical1.addWidget(ExemplosCor.CaixaCor("purple"))
        layout_HorizontalPrincial.addLayout(layout_vertical1)

        layout_vertical2 = QVBoxLayout()
        layout_vertical2.addWidget(ExemplosCor.CaixaCor("green"))
        layout_HorizontalPrincial.addLayout(layout_vertical2)

        layout_vertical3 = QVBoxLayout()
        layout_vertical3.addWidget(ExemplosCor.CaixaCor("red"))
        layout_vertical3.addWidget(ExemplosCor.CaixaCor("purple"))
        layout_HorizontalPrincial.addLayout(layout_vertical3)





        container = QWidget()
        container.setLayout(layout_HorizontalPrincial)
        self.setCentralWidget(container)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = EjemploVHLayout()
    ventana.show()
    sys.exit(app.exec())