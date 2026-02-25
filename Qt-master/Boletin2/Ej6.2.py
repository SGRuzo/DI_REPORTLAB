import string
import sys
import random
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication, QWidget, QPushButton, QVBoxLayout, QLabel,
    QMainWindow, QLineEdit, QSlider, QFrame, QTextEdit
)


class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Xerador de contrasinais")

        layout = QVBoxLayout()
        layout.setSpacing(15)      # Espaciado entre os elementos
        layout.setContentsMargins(30, 20, 30, 20)  # Márxenes

        # ----- LONXITUDE -----
        self.lbl_lonxitude = QTextEdit()
        self.lbl_lonxitude.setStyleSheet("font-size: 14px;")

        self.slider_lonxitude = QSlider(Qt.Orientation.Horizontal)
        self.slider_lonxitude.setRange(6, 20)
        self.slider_lonxitude.setValue(12)
        self.slider_lonxitude.valueChanged.connect(self.actualizar_lonxitude)

        # Separador visual
        separador1 = QFrame()
        separador1.setFrameShape(QFrame.Shape.HLine)
        separador1.setFrameShadow(QFrame.Shadow.Sunken)

        # ----- CONSTRASINAL -----
        lbl_titulo = QLabel("Contrasinal xerado:")
        lbl_titulo.setStyleSheet("font-size: 14px; font-weight: bold;")

        self.cadro_contrasinal = QLineEdit()
        self.cadro_contrasinal.setReadOnly(True)
        self.cadro_contrasinal.setStyleSheet("font-size: 16px; padding: 5px;")

        # ----- BOTÓN -----
        btn_xerar = QPushButton("Xerar nova contrasinal")
        btn_xerar.clicked.connect(self.xerar_contrasinal)
        btn_xerar.setStyleSheet("padding: 8px; font-size: 14px;")

        # Engadir todo ordenado
        layout.addWidget(self.lbl_lonxitude)
        layout.addWidget(self.slider_lonxitude)
        layout.addWidget(separador1)
        layout.addWidget(lbl_titulo)
        layout.addWidget(self.cadro_contrasinal)
        layout.addWidget(btn_xerar)

        # Contedor
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def actualizar_lonxitude(self, valor):
        self.lbl_lonxitude.setText(f"Lonxitude: {valor}")

    def xerar_contrasinal(self):
        chars = string.ascii_letters + string.digits + string.punctuation
        lonx = self.slider_lonxitude.value()
        contrasinal = "".join(random.choice(chars) for _ in range(lonx))
        self.cadro_contrasinal.setText(contrasinal)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())
