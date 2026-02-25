import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QGridLayout, QVBoxLayout, QHBoxLayout,
    QLabel, QListView, QPushButton, QComboBox, QLineEdit,
    QTextEdit, QGroupBox
)
from PyQt6.QtGui import QStandardItemModel, QStandardItem


class FiestraPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Xestión de Clientes")
        self.setMinimumSize(600, 500)

        layout_principal = QVBoxLayout()

        # ======================================================
        #   FORMULARIO
        # ======================================================

        gpbCliente = QGroupBox("Datos do Cliente")
        layout_form = QGridLayout()

        self.txtNumero = QLineEdit()
        self.txtNome = QLineEdit()
        self.txtApelidos = QLineEdit()
        self.txtDireccion = QLineEdit()
        self.txtCidade = QLineEdit()
        self.cmbProvincia = QComboBox()
        self.cmbProvincia.addItems(["A Coruña", "Lugo", "Ourense", "Pontevedra"])

        layout_form.addWidget(QLabel("Número Cliente"), 0, 0)
        layout_form.addWidget(self.txtNumero, 0, 1)

        layout_form.addWidget(QLabel("Nome"), 1, 0)
        layout_form.addWidget(self.txtNome, 1, 1)

        layout_form.addWidget(QLabel("Apelidos"), 2, 0)
        layout_form.addWidget(self.txtApelidos, 2, 1)

        layout_form.addWidget(QLabel("Dirección"), 3, 0)
        layout_form.addWidget(self.txtDireccion, 3, 1)

        layout_form.addWidget(QLabel("Cidade"), 4, 0)
        layout_form.addWidget(self.txtCidade, 4, 1)

        layout_form.addWidget(QLabel("Provincia"), 5, 0)
        layout_form.addWidget(self.cmbProvincia, 5, 1)

        gpbCliente.setLayout(layout_form)
        layout_principal.addWidget(gpbCliente)

        # ======================================================
        #   LISTA + MODELO
        # ======================================================

        self.modelo = QStandardItemModel()
        self.listaClientes = QListView()
        self.listaClientes.setModel(self.modelo)

        grupo_lista = QGroupBox("Clientes Rexistrados")
        caja_lista = QVBoxLayout()
        caja_lista.addWidget(self.listaClientes)
        grupo_lista.setLayout(caja_lista)
        layout_principal.addWidget(grupo_lista)

        # ======================================================
        #   BOTONES
        # ======================================================

        grupo_botones = QGroupBox("Accións")
        caja_botones = QHBoxLayout()

        self.btnEngadir = QPushButton("Engadir")
        self.btnBorrarUltimo = QPushButton("Borrar Último")
        self.btnBorrarSeleccionado = QPushButton("Borrar Seleccionado")
        self.btnEditar = QPushButton("Editar Seleccionado")
        self.btnLimparTodo = QPushButton("Limpar Todo")
        self.lblInfo = QLabel("Elementos: 0")

        caja_botones.addWidget(self.btnEngadir)
        caja_botones.addWidget(self.btnBorrarUltimo)
        caja_botones.addWidget(self.btnBorrarSeleccionado)
        caja_botones.addWidget(self.btnEditar)
        caja_botones.addWidget(self.btnLimparTodo)
        caja_botones.addWidget(self.lblInfo)

        grupo_botones.setLayout(caja_botones)
        layout_principal.addWidget(grupo_botones)

        # ======================================================
        #   SEÑALES
        # ======================================================

        self.btnEngadir.clicked.connect(self.engadir_cliente)
        self.btnBorrarUltimo.clicked.connect(self.borrar_ultimo)
        self.btnBorrarSeleccionado.clicked.connect(self.borrar_seleccionado)
        self.btnEditar.clicked.connect(self.editar_seleccionado)
        self.btnLimparTodo.clicked.connect(self.limpar_todo)

        self.listaClientes.selectionModel().selectionChanged.connect(self.actualizar_seleccion)

        # ======================================================
        #   WIDGET CENTRAL
        # ======================================================

        widget = QWidget()
        widget.setLayout(layout_principal)
        self.setCentralWidget(widget)

        self.actualizar_contador()

    # ======================================================
    #   LÓGICA FINAL (MESMA DO EXEMPLO)
    # ======================================================

    def engadir_cliente(self):
        numero = self.txtNumero.text().strip()
        nome = self.txtNome.text().strip()
        apelidos = self.txtApelidos.text().strip()

        if numero == "" or nome == "":
            return

        texto = f"{numero} - {nome} {apelidos}"
        self.modelo.appendRow(QStandardItem(texto))

        self.txtNumero.clear()
        self.txtNome.clear()
        self.txtApelidos.clear()

        self.actualizar_contador()

        # Seleccionar o engadido
        index = self.modelo.index(self.modelo.rowCount() - 1, 0)
        self.listaClientes.setCurrentIndex(index)

    def borrar_ultimo(self):
        if self.modelo.rowCount() > 0:
            self.modelo.removeRow(self.modelo.rowCount() - 1)
            self.actualizar_contador()

    def borrar_seleccionado(self):
        index = self.listaClientes.currentIndex()
        if index.isValid():
            self.modelo.removeRow(index.row())
            self.actualizar_contador()

    def editar_seleccionado(self):
        index = self.listaClientes.currentIndex()
        if index.isValid():
            self.listaClientes.edit(index)

    def limpar_todo(self):
        self.modelo.clear()
        self.actualizar_contador()

    def actualizar_seleccion(self):
        index = self.listaClientes.currentIndex()
        if index.isValid():
            texto = self.modelo.itemFromIndex(index).text()
            self.lblInfo.setText(f"Seleccionado: {texto}")

    def actualizar_contador(self):
        total = self.modelo.rowCount()
        self.lblInfo.setText(f"Elementos: {total}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = FiestraPrincipal()
    ventana.show()
    sys.exit(app.exec())
