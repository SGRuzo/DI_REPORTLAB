import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QTextEdit, QPushButton, QGridLayout, QMessageBox)
import operator

# Diccionario para mapear los operadores a las funciones correspondientes
# Esto trabaja con strings para facilitar la selección del operador
operation = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializarUI()
        self.primerValor = ""
        self.segundoValor = ""
        self.operacion = ""
        self.pointer_flag = "1"
        self.after_equal = False
        self.after_operator = False

    def inicializarUI(self):
        self.setGeometry(100,100,600, 400)
        self.setWindowTitle("Calculadora Simple")
        self.generar_interfaz()
        self.show()

    def generar_interfaz(self):
        self.pantalla = QTextEdit(self)
        self.pantalla.setDisabled(True)
        boton_1 = QPushButton("1")
        boton_2 = QPushButton("2")
        boton_3 = QPushButton("3")
        boton_4 = QPushButton("4")
        boton_5 = QPushButton("5")
        boton_6 = QPushButton("6")
        boton_7 = QPushButton("7")
        boton_8 = QPushButton("8")
        boton_9 = QPushButton("9")
        boton_0 = QPushButton("0")
        boton_00 = QPushButton("00")
        boton_punto = QPushButton(".")

        # Conectamos los botones numéricos a la función ingresar_datos
        boton_1.clicked.connect(self.ingresar_datos)
        boton_2.clicked.connect(self.ingresar_datos)
        boton_3.clicked.connect(self.ingresar_datos)
        boton_4.clicked.connect(self.ingresar_datos)
        boton_5.clicked.connect(self.ingresar_datos)
        boton_6.clicked.connect(self.ingresar_datos)
        boton_7.clicked.connect(self.ingresar_datos)
        boton_8.clicked.connect(self.ingresar_datos)
        boton_9.clicked.connect(self.ingresar_datos)
        boton_0.clicked.connect(self.ingresar_datos)
        boton_00.clicked.connect(self.ingresar_datos)
        boton_punto.clicked.connect(self.ingresar_datos)

        boton_suma = QPushButton("+")
        boton_resta = QPushButton("-")
        boton_multiplicacion = QPushButton("*")
        boton_division = QPushButton("/")
        boton_igual = QPushButton("=")
        boton_clear = QPushButton("CE")
        boton_borrar = QPushButton("<-")

        boton_suma.clicked.connect(self.ingresar_operador)
        boton_resta.clicked.connect(self.ingresar_operador)
        boton_multiplicacion.clicked.connect(self.ingresar_operador)
        boton_division.clicked.connect(self.ingresar_operador)

        boton_clear.clicked.connect(self.borrar_todo)
        boton_borrar.clicked.connect(self.borrar_parcial)
        boton_igual.clicked.connect(self.calcular_resultado)

        self.main_grid = QGridLayout()
        self.main_grid.addWidget(self.pantalla,0,0,2,4) # 0 fila, 0 columna, ocupa 2 filas y 4 columnas
        self.main_grid.addWidget(boton_clear, 2,0, 1,2) # 2 fila, 0 columna, ocupa 1 fila y 2 columnas
        self.main_grid.addWidget(boton_borrar,2,2) # 2 fila, 2 columna(ocupa 1 fila y 1 columna por defecto)
        self.main_grid.addWidget(boton_suma,2,3) # 2 fila, 3 columna
        self.main_grid.addWidget(boton_7,3,0) # 3 fila 0 columna
        self.main_grid.addWidget(boton_8,3,1) # 3 fila 1 columna
        self.main_grid.addWidget(boton_9,3,2) # 3 fila 2 columna
        self.main_grid.addWidget(boton_division,3, 3) # 3 fila 3 columna
        self.main_grid.addWidget(boton_4,4,0) # 4 fila 0 columna
        self.main_grid.addWidget(boton_5,4,1) # 4 fila
        self.main_grid.addWidget(boton_6,4,2) # 4 fila 2 columna
        self.main_grid.addWidget(boton_multiplicacion,4,3) # 4 fila 3 columna
        self.main_grid.addWidget(boton_1,5,0) # 5 fila 0 columna
        self.main_grid.addWidget(boton_2,5,1) # 5 fila 1 columna
        self.main_grid.addWidget(boton_3,5,2) # 5 fila 2 columna
        self.main_grid.addWidget(boton_resta,5,3) # 5 fila 3 columna
        self.main_grid.addWidget(boton_0,6,0) # 6 fila 0 columna
        self.main_grid.addWidget(boton_00,6,1) # 6 fila 1 columna
        self.main_grid.addWidget(boton_punto,6,2) # 6 fila 2 columna
        self.main_grid.addWidget(boton_igual,6,3) # 6 fila 3 columna

        self.setLayout(self.main_grid)

    def ingresar_datos(self):
        boton_text = self.sender().text()
        if self.after_equal:
            self.primerValor = ""
            self.pantalla.setText(self.primerValor)
            self.after_equal = False
            self.pointer_flag = "1"
        if self.pointer_flag == "1":
            self.primerValor += boton_text
            self.pantalla.setText(self.primerValor)
        else:
            self.segundoValor += boton_text
            self.pantalla.setText(self.pantalla.toPlainText()+boton_text)

    def ingresar_operador(self):
        boton_text = self.sender().text()
        self.operacion = boton_text
        self.pointer_flag = "2"

        if self.after_operator == True and self.segundoValor != "":
            self.calcular_resultado()
            self.pantalla.setText(self.primerValor + " "+self.sender().text()+"" + self.operacion + " ")
        else:
            self.pantalla.setText(self.pantalla.toPlainText() + " " + self.operacion + " ")

        self.after_operator = True
        self.after_equal = False

    def borrar_todo(self):
        self.primerValor = ""
        self.segundoValor = ""
        self.operacion = ""
        self.pointer_flag = "1"
        self.after_equal = False
        self.after_operator = False
        self.pantalla.setText("")

    def borrar_parcial(self):
        if self.after_equal:
            self.borrar_todo()
        if self.pointer_flag == "1":
            self.primerValor = self.primerValor[:-1]
            self.pantalla.setText(self.primerValor)
        else:
            self.segundoValor = self.segundoValor[:-1]
            self.pantalla.setText(self.segundoValor)

    def calcular_resultado(self):
        resultado = str(operation[self.operacion](float(self.primerValor), float(self.segundoValor)))
        self.pantalla.setText(resultado)
        self.primerValor = resultado
        self.segundoValor = ""
        self.operacion = ""
        self.after_equal = True
        self.after_operator = False

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = MainWindow()
    sys.exit(app.exec())