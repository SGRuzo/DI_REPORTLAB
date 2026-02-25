import sys

from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import (QApplication, QMainWindow, QGridLayout, QVBoxLayout, QHBoxLayout, QWidget,
                             QLabel, QListWidget, QPushButton, QComboBox, QLineEdit,
                             QRadioButton, QGroupBox, QTableView, QAbstractItemView, QTextEdit, QListView)


class FiestraPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exame 16-11-2025 grupo B")

        provincias = ["A Coruña", "Luego", "Ourense", "Pontevedra"]

        layout_principal = QVBoxLayout()
        layout_arriba = QVBoxLayout()

        gpbCliente = QGroupBox("Cliente")

        self.lblNumeroCliente = QLabel("Número Cliente")
        self.lblNomeCliente = QLabel("Nome")
        self.layout_numNom = QHBoxLayout()
        self.layout_numNom.addWidget(self.lblNomeCliente)
        self.layout_numNom.addWidget(self.lblNumeroCliente)

        self.lblApelidosCliente = QLabel("Apelidos")
        self.lblDirección = QLabel("Dirección")
        self.lblCidade = QLabel("Cidade")
        self.lblProvinciaEstado = QLabel("Provincia")

        self.txtNumeroCliente = QLineEdit()
        self.txtNomeCliente = QLineEdit()
        self.txtApelidosCliente = QLineEdit()
        self.txtDireccion = QLineEdit()
        self.txtCidade = QLineEdit()
        self.cmbProvincia = QComboBox()
        self.cmbProvincia.addItems( provincias)

        layout1 = QHBoxLayout()
        layout1.addWidget(self.lblNumeroCliente)
        layout1.addWidget(self.txtNumeroCliente)
        layout1.addWidget(self.lblNomeCliente)
        layout1.addWidget(self.txtNomeCliente)

        layout2 = QHBoxLayout()
        layout2.addWidget(self.lblApelidosCliente)
        layout2.addWidget(self.txtApelidosCliente)

        layout3 = QHBoxLayout()
        layout3.addWidget(self.lblDirección)
        layout3.addWidget(self.txtDireccion)

        layout4 = QHBoxLayout()
        layout4.addWidget(self.lblCidade)
        layout4.addWidget(self.txtCidade)
        layout4.addWidget(self.lblProvinciaEstado)
        layout4.addWidget(self.cmbProvincia)

        layout_arriba.addLayout(layout1)
        layout_arriba.addLayout(layout2)
        layout_arriba.addLayout(layout3)
        layout_arriba.addLayout(layout4)

        gpbCliente.setLayout(layout_arriba)

        self.txeClientes = QTextEdit()

        btnEngadir = QPushButton("Engadir")
        btnEngadir.clicked.connect(self.engadir_onClink)
        btnEngadir.clicked.connect(self.comprobar_campos)

        btnEditar = QPushButton("Editar")
        btnBorrar = QPushButton("Borrar")
        btnBorrar.clicked.connect(self.borrar_OnClick)


        layout_medio = QHBoxLayout()
        layout_medio.addWidget(self.txeClientes)

        layou_botones = QVBoxLayout()
        layou_botones.addWidget(btnEngadir)
        layou_botones.addWidget(btnEditar)
        layou_botones.addWidget(btnBorrar)

        layout_medio.addLayout(layou_botones)

        btnAceptar = QPushButton("Aceptar")
        btnCancelar = QPushButton("Cancelar")

        layout_abajo = QHBoxLayout()
        layout_abajo.addWidget(btnCancelar)
        layout_abajo.addWidget(btnAceptar)

        layout_principal.addWidget(gpbCliente)
        layout_principal.addLayout(layout_medio)
        layout_principal.addLayout(layout_abajo)

        self.modelo = QStandardItemModel()
        self.lista = QListView()
        self.lista.setModel(self.modelo)

        container = QWidget()
        container.setLayout(layout_principal)
        self.setCentralWidget(container)

    def engadir_onClink(self):
        nCliente = self.txtNomeCliente.text()
        nome = self.txtNumeroCliente.text()
        apell = self.txtApelidosCliente.text()
        direcion = self.txtDireccion.text()
        cidade = self.txtCidade.text()
        provincia = self.cmbProvincia.currentText()

        texto = f"{nCliente}, {nome}, {apell}, {direcion}, {cidade}, {provincia}"

        self.txeClientes.append(texto)
        self.limpiarFormulario()

    def limpiarFormulario(self):
        self.txtNumeroCliente.clear()
        self.txtNomeCliente.clear()
        self.txtApelidosCliente.clear()
        self.txtDireccion.clear()
        self.txtCidade.clear()
        self.cmbProvincia.setCurrentIndex(0)

    # Que borre la line de  QTextEdit que conincida con numeroCliente de QLineEDit TODO
    def borrar_OnClick(self):
        self.modelo.removeRow(self.modelo.rowCount() - 1)

    def comprobar_campos(self):
        nCliente = self.txtNomeCliente.text()
        nome = self.txtNomeCliente.text()
        apell = self.txtApelidosCliente.text()
        direcion = self.txtDireccion.text()
        cidade = self.txtCidade.text()

        if nCliente == "":
            self.lblNumeroCliente.setStyleSheet("font-weight: bold; color: red")
        if nome == "":
            self.lblNomeCliente.setStyleSheet("font-weight: bold; color: red")
        if apell == "":
            self.lblApelidosCliente.setStyleSheet("font-weight: bold; color: red")
        if direcion == "":
            self.lblDirección.setStyleSheet("font-weight: bold; color: red")
        if cidade == "":
            self.lblCidade.setStyleSheet("font-weight: bold; color: red")





if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = FiestraPrincipal()
    ventana.show()
    sys.exit(app.exec())
