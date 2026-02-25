import sys

from PyQt6.QtCore import QLine
from PyQt6.QtWidgets import (
    QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout,
    QStackedLayout, QRadioButton, QCheckBox, QLabel, QMainWindow, QLineEdit, QTextEdit
)
from PyQt6.QtGui import QColor, QPalette


class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("EJEMPLO DE COMO EMPEZAR")

        # --- Layout principal ---
        layout_principal = QVBoxLayout()



        container = QWidget()
        container.setLayout(layout_principal)
        self.setCentralWidget(container)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())
