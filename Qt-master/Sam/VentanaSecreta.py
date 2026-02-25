
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtCore import QTimer

class VentanaSecreta(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ventana Secreta")
        self.setMinimumSize(400, 300)

        caixa = QVBoxLayout()

        self.lblEtiqueta = QLabel("Ola")
        self.lblEtiqueta.setText("Estas en tu lugar secreto")
        self.lblEtiqueta.setStyleSheet("font-weight: bold; color: purple;")
        self.lblEtiqueta.setAlignment(Qt.AlignmentFlag.AlignCenter)


        self.lblEtiqueta2 = QLabel("Ola2")
        self.lblEtiqueta2.setText("este texto se puede pasar a en mayusculas y minusculas")
        self.lblEtiqueta2.setStyleSheet("font-weight: bold; color: orange;")
        self.lblEtiqueta2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.lblEtiqueta3 = QLabel("Ola3")
        self.lblEtiqueta3.setText("este texto se puede esconder")
        self.lblEtiqueta3.setStyleSheet("font-weight: bold; color: blue;")
        self.lblEtiqueta3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        btnSaudo = QPushButton("Abrir la ventana padre")
        btnSaudo.setStyleSheet("background-color: lightblue;")
        btnSaudo.clicked.connect(self.abrirventanapadre)



        btnMayusculas = QPushButton("Boton Mayusculas/Minusculas")
        btnMayusculas.setStyleSheet("background-color: lightgray;")  # Corregido 'lightgrey' a 'lightgray'
        btnMayusculas.setCheckable(True)
        btnMayusculas.setChecked(True)

        btnMayusculas.toggled.connect(lambda: self.lblEtiqueta2.setText(
            self.pasaramayusculas(self.lblEtiqueta2.text(), btnMayusculas)))



        btnOcultarTexto = QPushButton("Boton Ocultar Texto")
        btnOcultarTexto.setStyleSheet("background-color: yellow;")
        btnOcultarTexto.setCheckable(True)
        btnOcultarTexto.setChecked(True)

        btnOcultarTexto.toggled.connect(lambda: self.lblEtiqueta3.setText(
            self.ocultartexto(self.lblEtiqueta3.text(), btnOcultarTexto)))


        caixa.addWidget(self.lblEtiqueta3)
        caixa.addWidget(self.lblEtiqueta2)
        caixa.addWidget(self.lblEtiqueta)
        caixa.addWidget(btnSaudo)
        caixa.addWidget(btnMayusculas)
        caixa.addWidget(btnOcultarTexto)

        container = QWidget()
        container.setLayout(caixa)

        self.setCentralWidget(container)

        self.show()




    def abrirventanapadre (self):
        self.close()
        from PrimeraVentana import VentanaPrincipal
        self.vp = VentanaPrincipal()
        self.vp.show()

    def pasaramayusculas(self, texto, btnMayusculas=None):
        if texto == "":
            return "No hay texto"
        if btnMayusculas.isChecked():
            return texto.lower()
        else:
            return texto.upper()


    def ocultartexto(self, texto, btnOcultarTexto=None):

        if texto == "" :
            return "No hay texto"

        if btnOcultarTexto.isChecked():
            return texto
        else:
            return "*" * len(texto)


    def abrirventanasecreta(self):
        self.close()
        from VentanaSecreta import VentanaSecreta
        self.vs = VentanaSecreta()
        self.vs.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaSecreta()
    sys.exit(app.exec())