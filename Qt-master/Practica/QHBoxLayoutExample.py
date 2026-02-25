import sys
from PyQt6.QtWidgets import QMainWindow, QPushButton, QHBoxLayout, QWidget, QApplication


class QHBoxLayoutExample(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ejemplo QHBox")

        boton1 = QPushButton("Left-Most")
        boton2 = QPushButton("Center")
        boton3 = QPushButton("Right-Most")

        layout_horizontal = QHBoxLayout()
        layout_horizontal.addWidget(boton1)
        layout_horizontal.addWidget(boton2)
        layout_horizontal.addWidget(boton3)


        container = QWidget()
        container.setLayout(layout_horizontal)
        self.setCentralWidget(container)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = QHBoxLayoutExample()
    ventana.show()
    sys.exit(app.exec())



