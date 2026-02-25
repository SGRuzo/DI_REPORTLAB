import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget


class SegundaVentana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi segunda ventana")
        self.setMinimumSize(400, 300)

        caixa = QVBoxLayout()

        self.lblEtiqueta = QLabel("Hola")
        self.lblEtiqueta.setText("Esta es la segunda ventana")
        self.lblEtiqueta.setStyleSheet("font-weight: bold; color: red;")
        self.lblEtiqueta.setAlignment(Qt.AlignmentFlag.AlignCenter)

        btnSaudo = QPushButton("Abrir la ventana padre")
        btnSaudo.setStyleSheet("background-color: lightblue;")
        btnSaudo.clicked.connect(self.abrirventanapadre)

        caixa.addWidget(self.lblEtiqueta)
        caixa.addWidget(btnSaudo)




        container = QWidget()
        container.setLayout(caixa)

        self.setCentralWidget(container)

        self.show()



    def abrirventanapadre (self):
        self.close()
        from PrimeraVentana import VentanaPrincipal
        self.vp = VentanaPrincipal()
        self.vp.show()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = SegundaVentana()
    sys.exit(app.exec())