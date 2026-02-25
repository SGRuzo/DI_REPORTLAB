import sys

from PyQt6.QtWidgets import (QApplication, QMainWindow, QGridLayout, QVBoxLayout, QHBoxLayout, QWidget,
                             QLabel, QListWidget, QPushButton, QComboBox, QLineEdit,
                             QRadioButton, QGroupBox, QTableView, QAbstractItemView, QTextEdit)

class FiestraPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Examen 16-11-2025 group B")

        layout_principal = QVBoxLayout()
        maia = QGridLayout()

        self.lista_provincias = ["A Coruña", "Lugo", "Ourense", "Pontevedra"] # Lista de provincias


        gpbCliente = QGroupBox("Cliente")

        self.lblNumeroCliente = QLabel("Número Cliente")
        self.lblNomeCliente = QLabel("Nome")
        self.lblApelidosCliente = QLabel("Apelidos")
        self.lblDireccion = QLabel("Dirección")
        self.lblCidade = QLabel("Cidade")
        self.lblProvinciaEstado = QLabel("Provincia")

        self.txtNumeroCliente = QLineEdit()
        self.txtNomeCliente = QLineEdit()
        self.txtApelidosCliente = QLineEdit()
        self.txtDireccion = QLineEdit()
        self.txtCidade = QLineEdit()

        self.cmbProvincia = QComboBox()
        self.cmbProvincia.addItems(self.lista_provincias) # Engadir provincias ao combo box
        self.cmbProvincia.setCurrentIndex(-1) # que no seleccione ningún elemento por defecto

        maia.addWidget(self.lblNumeroCliente, 0, 0)
        maia.addWidget(self.txtNumeroCliente, 0, 1)
        maia.addWidget(self.lblNomeCliente, 0, 2)
        maia.addWidget(self.txtNomeCliente, 0, 3)
        maia.addWidget(self.lblApelidosCliente, 1, 0)
        maia.addWidget(self.txtApelidosCliente, 1, 1, 1, 3)
        maia.addWidget(self.lblDireccion, 2, 0)
        maia.addWidget(self.txtDireccion, 2, 1, 1, 3)
        maia.addWidget(self.lblCidade, 3, 0)
        maia.addWidget(self.txtCidade, 3, 1)
        maia.addWidget(self.lblProvinciaEstado, 3, 2)
        maia.addWidget(self.cmbProvincia, 3, 3)

        gpbCliente.setLayout(maia)
        layout_principal.addWidget(gpbCliente)

        layout_medio = QHBoxLayout()
        layout_principal.addLayout(layout_medio)


        self.txeClientes = QTextEdit()
        layout_medio.addWidget(self.txeClientes)

        layout_botones = QVBoxLayout()

        btnEngadir = QPushButton("Engadir")
        btnEngadir.clicked.connect(self.btnEngadir_onClick)
        btnEditar = QPushButton("Editar")
        btnBorrar = QPushButton("Borrar")
        btnBorrar.clicked.connect(self.btn_Borrar_onClick)

        layout_botones.addWidget(btnEngadir)
        layout_botones.addWidget(btnEditar)
        layout_botones.addWidget(btnBorrar)
        layout_botones.addStretch() # Engadir un espazo flexible para empurrar os botóns cara arriba

        layout_medio.addLayout(layout_botones)


        layout_abajo = QHBoxLayout()
        layout_principal.addLayout(layout_abajo)
        layout_abajo.addStretch() # Engadir un espazo flexible á esquerda

        btnAceptar = QPushButton("Aceptar")
        btnCancelar = QPushButton("Cancelar")
        layout_abajo.addWidget(btnCancelar)
        layout_abajo.addWidget(btnAceptar)


        container = QWidget()
        container.setLayout(layout_principal)
        self.setCentralWidget(container)

    def btnEngadir_onClick(self):

        if not self.comprobarCampos():
            return

        numero_cliente = self.txtNumeroCliente.text().strip()
        nome = self.txtNomeCliente.text().strip()
        apelidos = self.txtApelidosCliente.text().strip()
        direccion = self.txtDireccion.text().strip()
        cidade = self.txtCidade.text().strip()
        provincia = self.cmbProvincia.currentText().strip()

        linea = f"{numero_cliente}, {nome}, {apelidos}, {direccion}, {cidade}, {provincia}"

        self.txeClientes.append(linea)
        self.limpiarFormulario()

    def comprobarCampos(self):
        todo_cuberto = True  # al principio asumimos que todos los campos están completos y si no se cambia en el proceso

        if self.txtNumeroCliente.text().strip() == "":
            self.lblNumeroCliente.setStyleSheet("color: red;")
            todo_cuberto = False
        else:
            self.lblNumeroCliente.setStyleSheet("color: black;")

        if self.txtNomeCliente.text().strip() == "":
            self.lblNomeCliente.setStyleSheet("color: red;")
            todo_cuberto = False
        else:
            self.lblNomeCliente.setStyleSheet("color: black;")

        if self.txtApelidosCliente.text().strip() == "":
            self.lblApelidosCliente.setStyleSheet("color: red;")
            todo_cuberto = False
        else:
            self.lblApelidosCliente.setStyleSheet("color: black;")

        if self.txtDireccion.text().strip() == "":
            self.lblDireccion.setStyleSheet("color: red;")
            todo_cuberto = False
        else:
            self.lblDireccion.setStyleSheet("color: black;")

        if self.txtCidade.text().strip() == "":
            self.lblCidade.setStyleSheet("color: red;")
            todo_cuberto = False
        else:
            self.lblCidade.setStyleSheet("color: black;")

        if self.cmbProvincia.currentIndex() == -1:
            self.lblProvinciaEstado.setStyleSheet("color: red;")
            todo_cuberto = False
        else:
            self.lblProvinciaEstado.setStyleSheet("color: black;")

        return todo_cuberto

    def limpiarFormulario(self):
        self.txtNumeroCliente.clear()
        self.txtNomeCliente.clear()
        self.txtApelidosCliente.clear()
        self.txtDireccion.clear()
        self.txtCidade.clear()
        self.cmbProvincia.setCurrentIndex(-1)

    def btn_Borrar_onClick(self):
        numero_borrar= self.txtNumeroCliente.text().strip()
        if numero_borrar == "": # Si no hay número de cliente, no hace nada
            return

        lineas = self.txeClientes.toPlainText().strip().split("\n")  # Obtemos todo o texto e dividimos en liñas separadas por saltos de liña

        novas = [liña for liña in lineas if liña.split(",")[0].strip() != numero_borrar] # nueva lista sin las líneas que coinciden con el número de cliente


        self.txeClientes.setPlainText("\n".join(novas)) # Reescribimos o QTextEdit coas liñas non borradas

        # Limpiamos os controis
        self.limpiarFormulario()



if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    fiestra = FiestraPrincipal()
    fiestra.show()
    sys.exit(aplicacion.exec())
