import string
import sys
import random
from PyQt6.QtCore import QLine, Qt
from PyQt6.QtWidgets import (
    QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout,
    QStackedLayout, QRadioButton, QCheckBox, QLabel, QMainWindow, QLineEdit, QTextEdit, QSlider
)
from PyQt6.QtGui import QColor, QPalette
""""
Deseña unha ferramenta que xere contrasinais aleatorias ao premer un botón.
A interface debe incluír:
Unha etiqueta que diga: “Contrasinal xerado:”
Un cadro de texto (só de lectura) que amose a contrasinal.
Un botón “Xerar nova contrasinal”
Un control deslizante (QSlider) para escoller a lonxitude (de 6 a 20 caracteres).
Funcionalidade:
Ao mover o control deslizante, actualízase unha etiqueta co número actual (ex: “Lonxitude: 12”).
Ao premer o botón, xérase unha contrasinal aleatoria con letras, números e símbolos, da lonxitude seleccionada.
"""


class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Xerador de contrasinais")

        # --- Layout principal ---
        layout_principal = QVBoxLayout()

        # Etiqueta de lonxitude
        self.lbl_lonxitude = QLabel("Lonxitude: 12")

        # Slider para escoller lonxitude (6 a 20)
        self.slider_lonxitude = QSlider(Qt.Orientation.Horizontal)
        self.slider_lonxitude.setMinimum(6) # valor mínimo
        self.slider_lonxitude.setMaximum(20) # valor máximo
        self.slider_lonxitude.setValue(12)  # valor inicial
        self.slider_lonxitude.valueChanged.connect(self.actualizar_lonxitude)

        # Etiqueta "Contrasinal xerado:"
        lbl_titulo = QLabel("Contrasinal xerado:")

        # Cadro de texto só lectura
        self.cadro_contrasinal = QLineEdit()
        self.cadro_contrasinal.setReadOnly(True) # só lectura

        # Botón para xerar
        btn_xerar = QPushButton("Xerar nova contrasinal")
        btn_xerar.clicked.connect(self.xerar_contrasinal)

        # Engadir widgets ao layout
        layout_principal.addWidget(self.lbl_lonxitude)
        layout_principal.addWidget(self.slider_lonxitude)
        layout_principal.addWidget(lbl_titulo)
        layout_principal.addWidget(self.cadro_contrasinal)
        layout_principal.addWidget(btn_xerar)

        # Contedor central
        container = QWidget()
        container.setLayout(layout_principal)
        self.setCentralWidget(container)

    def actualizar_lonxitude(self, valor):
        self.lbl_lonxitude.setText(f"Lonxitude: {valor}")

    def xerar_contrasinal(self):
        # Lonxitude que seleccionou o usuario
        lonxitude = self.slider_lonxitude.value()

        # Caracteres permitidos
        chars = string.ascii_letters + string.digits + string.punctuation

        # Xeración rápida da contrasinal
        contrasinal = "".join(random.choice(chars) for _ in range(lonxitude))

        # Amosar resultado
        self.cadro_contrasinal.setText(contrasinal)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())