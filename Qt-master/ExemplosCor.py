# ExemplosCor.py
from PyQt6.QtGui import QColor, QPalette
from PyQt6.QtWidgets import QWidget

class CaixaCor(QWidget):
    def __init__(self, cor):
        super().__init__()
        self.setAutoFillBackground(True)
        paleta = self.palette()
        paleta.setColor(QPalette.ColorRole.Window, QColor(cor))
        self.setPalette(paleta)
        # Tamaño mínimo para que se vea bien
        self.setMinimumSize(100, 100)
