from PyQt6.QtWidgets import (QApplication, QMainWindow, QGridLayout, QVBoxLayout, QHBoxLayout, QWidget)
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QLabel, QCheckBox, QLineEdit, QSlider
from PyQt6.uic import loadUi

class MinhaAplicacion:
    def __init__(self):
        self.aplicacion = QApplication(sys.argv)
        self.fiestra = loadUi('form.ui')

        self.txtapelido = self.fiestra.txtapelido
        self.btnEngadir = self.fiestra.btnEngadir
        self.cnbbynerocliente = self.fiestra.cnbbynerocliente
        self.btnEngadir.pressed.connect(self.on_btmEngadir_presed)

        self.fiestra.show()

    def on_btmEngadir_presed  (self):
        numCliente = self.cnbbynerocliente.currentText()
        self.txtapelido.setText(f"Cliente Engadido: {numCliente}")

    def run (self):
        sys.exit(self.aplicacion.exec())

if __name__ == "__main__":
    app = MinhaAplicacion()
    app.run()