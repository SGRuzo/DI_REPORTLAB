import sys
from PyQt6.QtWidgets import QMainWindow, QPushButton, QHBoxLayout, QWidget, QApplication, QVBoxLayout


class QVBoxEjemplo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ejemplo QVBoxLayout")

        boton1 = QPushButton("Top")
        boton2 = QPushButton("Center")
        boton3 = QPushButton("Botton")

        layout_vertical = QVBoxLayout()
        layout_vertical.addWidget(boton1)
        layout_vertical.addWidget(boton2)
        layout_vertical.addWidget(boton3)

        container = QWidget()
        container.setLayout(layout_vertical)
        self.setCentralWidget(container)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = QVBoxEjemplo()
    ventana.show()
    sys.exit(app.exec())

