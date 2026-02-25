import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QTableWidget, \
    QTableWidgetItem


class Interfaz(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Exercicio Interfaz")

        cajaPrincipal = QVBoxLayout()
        centralWidget = QWidget()
        centralWidget.setLayout(cajaPrincipal)
        self.setCentralWidget(centralWidget)

        cajaSuperior = QHBoxLayout()
        cajaPrincipal.addLayout(cajaSuperior)
        cajaCentralBotones = QVBoxLayout()
        cajaSuperior.addLayout(cajaCentralBotones)



        self.tabla = QTableWidget()
        cajaSuperior.addWidget(self.tabla)
        self.tabla.setColumnCount(1)
        self.tabla.setHorizontalHeaderLabels(["Hojas visibles"])
        self.tabla.setRowCount(3)
        datos = [("Hoja1"), ("Hoja2"), ("Hoja3")]
        for fila, nombre in enumerate(datos):
            self.tabla.setItem(fila, 0, QTableWidgetItem(nombre))




        moverdatos = QPushButton("Mover datos >>")
        moverdatos.clicked.connect(self.moverDatos)
        moverdatos.setStyleSheet("background-color: lightgreen;")
        cajaSuperior.addWidget(moverdatos)


        cajaSuperior.addSpacing(100)




        devolverdatos = QPushButton("<< Devolver datos")
        devolverdatos.clicked.connect(self.devolverDatos)  # Nuevo método
        devolverdatos.setStyleSheet("background-color: lightblue;")
        cajaSuperior.addWidget(devolverdatos)



        cajaCentralBotones.addStretch()
        self.tabla2 = QTableWidget()
        cajaSuperior.addWidget(self.tabla2)
        self.tabla2.setColumnCount(1)
        self.tabla2.setHorizontalHeaderLabels(["Hojas Ocultas"])
        self.tabla2.setRowCount(1)
        datos2 = [("HojaA")]
        for fila, nombre in enumerate(datos2):
            self.tabla2.setItem(fila, 0, QTableWidgetItem(nombre))




        cajaInferior = QHBoxLayout()
        cajaPrincipal.addLayout(cajaInferior)

        cerrar = QPushButton("Cerrar")
        cerrar.clicked.connect(self.close)
        cerrar.setStyleSheet("background-color: red;")

        cajaInferior.addStretch()
        cajaInferior.addWidget(cerrar)

        self.show()


    def moverDatos(self):
        self.moverHoja(self.tabla, self.tabla2)
        print("Datos movidos a Hojas Ocultas.")

    def devolverDatos(self):
        self.moverHoja(self.tabla2, self.tabla)
        print("Datos devueltos a Hojas visibles.")

    def moverHoja(self, TablaOrigen, TablaDestinp):
        seleccionUsuario = TablaOrigen.selectedItems()

        if not seleccionUsuario:
            return

        SeleccionAmover = seleccionUsuario[0]
        TextoAmover = SeleccionAmover.text()
        FilaAelminar = SeleccionAmover.row()

        TablaOrigen.removeRow(FilaAelminar)

        NuevaFila = TablaDestinp.rowCount()
        TablaDestinp.insertRow(NuevaFila)

        nuevo_item = QTableWidgetItem(TextoAmover)
        TablaDestinp.setItem(NuevaFila, 0, nuevo_item)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Interfaz()
    sys.exit(app.exec())