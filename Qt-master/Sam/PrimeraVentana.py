import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtCore import QTimer



class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mi primera ventana con PyQt")
        self.setMinimumSize(400, 300)


        self.lblEtiqueta = QLabel("Hola")                                                         # Crea unha etiqueta con texto
        self.lblEtiqueta.setText("Introduza su nombre:")                                          # setText cambia o texto da etiqueta
        self.lblEtiqueta.setStyleSheet("font-size: 16px; color: blue; font_weight: bold")         # Cambia o estilo da etiqueta
        self.lblEtiqueta.setAlignment(Qt.AlignmentFlag.AlignCenter)                               # Centra o texto da etiqueta

        self.lineaTexto = QLineEdit()                                                                  # Caixa de texto para introducir texto

        btnSaudo = QPushButton("Saludar")                                                         # Botón
        btnSaudo.setStyleSheet("background-color: lightblue;")
        btnSaudo.clicked.connect(self.saludar)

        btnOtraVentana = QPushButton("Abrir otra ventana")
        btnOtraVentana.setStyleSheet("background-color: lightgreen;")
        btnOtraVentana.clicked.connect(self.abrirventanahija)


        caixa = QVBoxLayout()
        caixa.addWidget(self.lblEtiqueta)
        caixa.addWidget(self.lineaTexto)
        caixa.addWidget(btnSaudo)
        caixa.addWidget(btnOtraVentana)



        container = QWidget()
        container.setLayout(caixa)

        self.setCentralWidget(container)

        self.show()




    def saludar(self):
        nome = self.lineaTexto.text()
        self.lineaTexto.clear()
        nome = nome.strip()
        if nome == "" or nome.isdigit():
            self.lblEtiqueta.setStyleSheet("font-weight: bold; color: red")
            nome = "Porfavor introduce un nombre"
            self.lblEtiqueta.setText(f"{nome}!")
        else:
            self.lblEtiqueta.setText(f"Hola {nome}!")           # Cambia o texto da etiqueta



    def abrirventanahija (self):
        self.close()
        from SegundaVentana import SegundaVentana
        self.segundav = SegundaVentana()
        self.segundav.show()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())