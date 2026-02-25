import string
import sys
import random
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication, QWidget, QPushButton, QVBoxLayout, QLabel,
    QMainWindow, QLineEdit, QSlider, QHBoxLayout
)


class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Xerador de contrasinais")

        layout_principal = QVBoxLayout()
        layout_principal.setSpacing(12)
        layout_principal.setContentsMargins(20, 20, 20, 20)

        # --------------------
        #    LONXITUDE + SLIDER
        # --------------------
        fila_lonxitude = QHBoxLayout()
        self.lbl_lonxitude = QLabel("Lonxitude: 12")

        self.slider_lonxitude = QSlider(Qt.Orientation.Horizontal)
        self.slider_lonxitude.setRange(6, 20)
        self.slider_lonxitude.setValue(12)
        self.slider_lonxitude.setFixedWidth(200)
        self.slider_lonxitude.valueChanged.connect(self.actualizar_lonxitude)

        fila_lonxitude.addWidget(self.lbl_lonxitude)
        fila_lonxitude.addWidget(self.slider_lonxitude)

        # --------------------
        #    TEXTO RESULTADO
        # --------------------
        lbl_titulo = QLabel("Contrasinal xerado:")
        self.cadro_contrasinal = QLineEdit()
        self.cadro_contrasinal.setReadOnly(True)

        # --------------------
        #    BOTÓN
        # --------------------
        btn_xerar = QPushButton("Xerar nova contrasinal")
        btn_xerar.clicked.connect(self.xerar_contrasinal)

        # --------------------
        #    AÑADIR A LA INTERFAZ
        # --------------------
        layout_principal.addLayout(fila_lonxitude)
        layout_principal.addSpacing(10)
        layout_principal.addWidget(lbl_titulo)
        layout_principal.addWidget(self.cadro_contrasinal)
        layout_principal.addSpacing(10)
        layout_principal.addWidget(btn_xerar)

        container = QWidget()
        container.setLayout(layout_principal)
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
