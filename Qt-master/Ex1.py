import sys

from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QGridLayout, QVBoxLayout, QHBoxLayout, QWidget,
    QLabel, QListWidget, QPushButton, QComboBox, QLineEdit,
    QGroupBox, QTextEdit
)


class FiestraPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Xestión de Clientes")
        self.setMinimumSize(700, 500)

        # ================================
        #  WIDGETS DEL FORMULARIO CLIENTE
        # ================================
        gpbCliente = QGroupBox("Cliente")

        lblNumeroCliente = QLabel("Número Cliente")
        lblNomeCliente = QLabel("Nome")
        lblApelidosCliente = QLabel("Apelidos")
        lblDirección = QLabel("Dirección")
        lblCidade = QLabel("Cidade")
        lblProvinciaEstado = QLabel("Provincia")

        self.txtNumeroCliente = QLineEdit()
        self.txtNomeCliente = QLineEdit()
        self.txtApelidosCliente = QLineEdit()
        self.txtDireccion = QLineEdit()
        self.txtCidade = QLineEdit()

        self.cmbProvincia = QComboBox()
        self.cmbProvincia.addItems(["A Coruña", "Lugo", "Ourense", "Pontevedra"])

        # ================================
        #  LISTA DE CLIENTES
        # ================================
        self.lstClientes = QListWidget()

        # ================================
        #  BOTONES PRINCIPALES
        # ================================
        btnEngadir = QPushButton("Engadir")
        btnEditar = QPushButton("Editar")
        btnBorrar = QPushButton("Borrar")

        btnAceptar = QPushButton("Aceptar")
        btnCancelar = QPushButton("Cancelar")

        # Rellenar datos ejemplo
        self.txeClientes = QTextEdit()
        self.txeClientes.setPlaceholderText("Detalles do cliente seleccionado...")

        # ================================
        #  LAYOUT DEL GRUPO CLIENTE
        # ================================
        grid = QGridLayout()

        grid.addWidget(lblNumeroCliente, 0, 0)
        grid.addWidget(self.txtNumeroCliente, 0, 1)

        grid.addWidget(lblNomeCliente, 1, 0)
        grid.addWidget(self.txtNomeCliente, 1, 1)

        grid.addWidget(lblApelidosCliente, 2, 0)
        grid.addWidget(self.txtApelidosCliente, 2, 1)

        grid.addWidget(lblDirección, 3, 0)
        grid.addWidget(self.txtDireccion, 3, 1)

        grid.addWidget(lblCidade, 4, 0)
        grid.addWidget(self.txtCidade, 4, 1)

        grid.addWidget(lblProvinciaEstado, 5, 0)
        grid.addWidget(self.cmbProvincia, 5, 1)

        gpbCliente.setLayout(grid)

        # ================================
        #  LAYOUT BOTONES CRUD
        # ================================
        cajaBotones = QHBoxLayout()
        cajaBotones.addWidget(btnEngadir)
        cajaBotones.addWidget(btnEditar)
        cajaBotones.addWidget(btnBorrar)

        # ================================
        #  LAYOUT ACEPTAR / CANCELAR
        # ================================
        cajaAceptar = QHBoxLayout()
        cajaAceptar.addStretch()
        cajaAceptar.addWidget(btnCancelar)
        cajaAceptar.addWidget(btnAceptar)

        # ================================
        #  LAYOUT PRINCIPAL
        # ================================
        layoutPrincipal = QGridLayout()
        layoutPrincipal.addWidget(gpbCliente, 0, 0, 1, 2)
        layoutPrincipal.addWidget(self.lstClientes, 1, 0)
        layoutPrincipal.addWidget(self.txeClientes, 1, 1)
        layoutPrincipal.addLayout(cajaBotones, 2, 0)
        layoutPrincipal.addLayout(cajaAceptar, 2, 1)

        container = QWidget()
        container.setLayout(layoutPrincipal)
        self.setCentralWidget(container)

        # ================================
        #  SEÑALES
        # ================================
        btnEngadir.clicked.connect(self.engadirCliente)
        btnBorrar.clicked.connect(self.borrarCliente)
        btnEditar.clicked.connect(self.editarCliente)

        self.lstClientes.itemSelectionChanged.connect(self.mostrarDetalles)

        btnCancelar.clicked.connect(self.limpiarFormulario)
        btnAceptar.clicked.connect(self.aceptarCambios)

        self.editando = False


    # ================================
    #  FUNCIONES CRUD
    # ================================

    def engadirCliente(self):
        numero = self.txtNumeroCliente.text().strip()
        nome = self.txtNomeCliente.text().strip()
        apelidos = self.txtApelidosCliente.text().strip()

        if numero == "" or nome == "":
            return

        texto = f"{numero} - {nome} {apelidos}"
        self.lstClientes.addItem(texto)
        self.limpiarFormulario()

    def borrarCliente(self):
        item = self.lstClientes.currentItem()
        if item:
            fila = self.lstClientes.row(item)
            self.lstClientes.takeItem(fila)
            self.txeClientes.clear()

    def editarCliente(self):
        item = self.lstClientes.currentItem()
        if not item:
            return

        datos = item.text().split(" - ")
        numero = datos[0]
        nome_apelidos = datos[1].split(" ")

        self.txtNumeroCliente.setText(numero)
        self.txtNomeCliente.setText(nome_apelidos[0])
        self.txtApelidosCliente.setText(" ".join(nome_apelidos[1:]))

        self.editando = True

    def aceptarCambios(self):
        if not self.editando:
            return

        item = self.lstClientes.currentItem()
        if not item:
            return

        numero = self.txtNumeroCliente.text()
        nome = self.txtNomeCliente.text()
        apelidos = self.txtApelidosCliente.text()

        item.setText(f"{numero} - {nome} {apelidos}")

        self.editando = False
        self.limpiarFormulario()

    def mostrarDetalles(self):
        item = self.lstClientes.currentItem()
        if not item:
            return

        self.txeClientes.setText(item.text())

    def limpiarFormulario(self):
        self.txtNumeroCliente.clear()
        self.txtNomeCliente.clear()
        self.txtApelidosCliente.clear()
        self.txtDireccion.clear()
        self.txtCidade.clear()
        self.cmbProvincia.setCurrentIndex(0)


if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    fiestra = FiestraPrincipal()
    fiestra.show()
    aplicacion.exec()
