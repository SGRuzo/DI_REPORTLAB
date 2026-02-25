import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QLabel, QPushButton,
                             QComboBox, QLineEdit, QGroupBox, QTextEdit,
                             QGridLayout, QWidget, QVBoxLayout, QHBoxLayout)


class FiestraPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Examen 16-11-2025 group A")

        maia = QGridLayout()
        layout_principal = QVBoxLayout()

        gpbAlbara = QGroupBox("Albará")

        self.lista_Albarras = [
            ["1111nm", "02/11/2024", "1111", "Ana", "Ruiz"],
            ["2222io", "09/03/2024", "2222", "Pedro", "Diz"],
            ["3333qw", "23/10/2025", "3333", "Rosa", "Sanz"]
        ]

        lblNumeroAlbara = QLabel("Número Albará")
        lblDataAlbara = QLabel("Data")
        lblNumeroCliente = QLabel("Número cliente")
        lblNomeCliente = QLabel("Nome Cliente")
        lblApelidosCliente = QLabel("Apelidos")

        self.cmbNumeroAlbara = QComboBox()
        self.cmbNumeroAlbara.addItems([albara[0]for albara in self.lista_Albarras]) # Engadir números de albarás ao combo box
        self.cmbNumeroAlbara.setCurrentIndex(-1)  # que no seleccione ningún elemento por defecto
        self.cmbNumeroAlbara.currentIndexChanged.connect(self.on_cmbNumeroAlbara_changed) # connect selection change to updater


        self.txtDataAlbara = QLineEdit()
        self.txtNumeroCliente = QLineEdit()
        self.txtNomeCliente = QLineEdit()
        self.txtApelidosCliente = QLineEdit()

        btnEngadir = QPushButton("Engadir")
        btnEditar = QPushButton("Editar")
        btnEditar.clicked.connect(self.onClick_btnEditar) # conectar o evento de clic a unha función

        btnBorrar = QPushButton("Borrar")

        txtCodigoProducto = QLineEdit()
        txtCantidade = QLineEdit()
        txtPrezoUnitario = QLineEdit()

        self.txeCadroTexto = QTextEdit()

        btnAceptar = QPushButton("Aceptar")
        btnAceptar.setDisabled(True) # Botón deshabilitado
        btnCancelar = QPushButton("Cancelar")
        btnCancelar.clicked.connect(self.btnCancelar_onClick) # Conectar o evento de clic a la función

        maia.addWidget(lblNumeroAlbara, 0, 0)
        maia.addWidget(self.cmbNumeroAlbara, 0, 1)
        maia.addWidget(lblDataAlbara, 0, 2)
        maia.addWidget(self.txtDataAlbara, 0, 3)

        maia.addWidget(lblNumeroCliente, 1, 0)
        maia.addWidget(self.txtNumeroCliente, 1, 1)
        maia.addWidget(lblNomeCliente, 1, 2)
        maia.addWidget(self.txtNomeCliente, 1, 3)

        maia.addWidget(lblApelidosCliente, 2, 0)
        maia.addWidget(self.txtApelidosCliente, 2, 1, 1, 3)
        gpbAlbara.setLayout(maia)
        layout_principal.addWidget(gpbAlbara)

        btn_layout = QHBoxLayout()
        btn_layout.addWidget(btnEngadir)
        btn_layout.addWidget(btnEditar)
        btn_layout.addWidget(btnBorrar)

        layout_principal.addLayout(btn_layout)
        layout_principal.addWidget(self.txeCadroTexto)

        layout_abajo = QHBoxLayout()
        layout_abajo.addStretch() # Engadir un espazo flexible á esquerda

        layout_abajo.addWidget(btnCancelar)
        layout_abajo.addWidget(btnAceptar)
        #layout_abajo.addStretch() # Engadir un espazo flexible á dereita

        layout_principal.addLayout(layout_abajo)

        container = QWidget()
        container.setLayout(layout_principal)
        self.setCentralWidget(container)


    # funcion que cieera la aplicacion
    def btnCancelar_onClick(self):
        self.close()

    # función que se ejecuta al hacer clic en el botón "Editar"
    def onClick_btnEditar(self):
        # comprobar que hay un albará seleccionado si no es así, salir de la función
        if self.cmbNumeroAlbara.currentIndex() < 0:
            return

        nAlbara = self.cmbNumeroAlbara.currentText() # obtener el número de albará seleccionado
        data = self.txtDataAlbara.text() # convertir a texto los campos
        nCliente = self.txtNumeroCliente.text()
        nome = self.txtNomeCliente.text()
        apell = self.txtApelidosCliente.text()



        linea = f"{nAlbara}, {data}, {nCliente}, {nome}, {apell}"
        self.txeCadroTexto.append(linea)



    # rellena los campos según la selección del combo box
    def on_cmbNumeroAlbara_changed(self, index: int):
        if index is None or index < 0 or index >= len(self.lista_Albarras): # esto se puede simplificar a "if index < 0:" (creo)
            # clear fields when nothing selected
            self.txtDataAlbara.clear()
            self.txtNumeroCliente.clear()
            self.txtNomeCliente.clear()
            self.txtApelidosCliente.clear()
            return

        albara = self.lista_Albarras[index] # para el índice seleccionado, obtener la albará correspondiente
        # albara structure: [numero, data, numero_cliente, nome, apelidos]
        self.txtDataAlbara.setText(albara[1])
        self.txtNumeroCliente.setText(albara[2])
        self.txtNomeCliente.setText(albara[3])
        self.txtApelidosCliente.setText(albara[4])

if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    fiestra = FiestraPrincipal()
    fiestra.show()
    sys.exit(aplicacion.exec())
