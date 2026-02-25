import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QRadioButton, QVBoxLayout, QHBoxLayout, QTextEdit


class VentanaConRadioButton(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializarUI()
        self.show()

    def inicializarUI(self):
        self.setWindowTitle("Radio Buttons")
        self.cajaHorizontal = QHBoxLayout()

        self.boton1 = QRadioButton("Mostrar Nombre")
        self.boton2 = QRadioButton("Mostrar edad")
        self.boton3 = QRadioButton("Pasar texto a label")
        self.boton4 = QRadioButton("Pasar texto a mayusculas")


        self.cajaHorizontal.addWidget(self.boton1)
        self.cajaHorizontal.addWidget(self.boton2)
        self.cajaHorizontal.addWidget(self.boton3)
        self.cajaHorizontal.addWidget(self.boton4)

        self.panelParaEscribir = QTextEdit()
        self.panelParaMostrar = QTextEdit()
        self.panelParaMostrar.setDisabled(True)

        self.cajaVertical = QVBoxLayout()

        self.cajaVertical.addLayout(self.cajaHorizontal)
        self.cajaVertical.addWidget(self.panelParaEscribir)
        self.cajaVertical.addWidget(self.panelParaMostrar)

        self.boton1.clicked.connect(self.mostrarNombre)
        self.boton2.clicked.connect(self.mostrarEdad)
        self.boton3.clicked.connect(self.pasarTextoALabel)
        self.boton4.clicked.connect(self.pasarTextoAMayusculas)

        self.setLayout(self.cajaVertical)


    def mostrarNombre(self):
        self.panelParaMostrar.setPlainText("Daniel")
    def mostrarEdad(self):
        self.panelParaMostrar.setPlainText("22")

    def pasarTextoALabel(self):
        texto = self.panelParaEscribir.toPlainText()
        self.panelParaMostrar.setPlainText(texto)

    def pasarTextoAMayusculas(self):
        texto = self.panelParaMostrar.toPlainText()
        self.panelParaMostrar.setPlainText(texto.upper())






if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaConRadioButton()
    sys.exit(app.exec())