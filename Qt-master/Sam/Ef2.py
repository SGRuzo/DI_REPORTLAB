import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QPushButton, QListView, QTextEdit, QGroupBox, QGridLayout,
    QLineEdit, QComboBox
)
from PyQt6.QtGui import QStandardItemModel, QStandardItem


class VentanaClientes(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gestión de Clientes - Versión PRO")

        # ====== ESTADO INTERNO ======
        self.modo = None      # 'nuevo' o 'editar'
        self.indice_editando = None

        # ====== MODELO LISTA ======
        self.modelo = QStandardItemModel()

        # ====== DATOS BASE ======
        self.datos_albaranes = [
            ["11111", "02/11/2024", "Ana", "Ruiz", "Madrid"],
            ["22220", "08/03/2024", "Pedro", "Diz", "Vigo"],
            ["33333", "23/10/2025", "Rosa", "Sanz", "Ourense"]
        ]

        # Cargar datos iniciales
        for al in self.datos_albaranes:
            texto = f"{al[0]} - {al[2]} {al[3]} - {al[1]}"
            self.modelo.appendRow(QStandardItem(texto))

        # ====== WIDGETS FORMULARIO ======
        form_group = QGroupBox("Datos del Cliente")
        form_layout = QGridLayout()

        self.txtAlbara = QLineEdit()
        self.txtData = QLineEdit()
        self.txtNome = QLineEdit()
        self.txtApelido = QLineEdit()
        self.txtCidade = QLineEdit()

        self.cmbAlbaranes = QComboBox()
        self.cmbAlbaranes.addItems([x[0] for x in self.datos_albaranes])
        self.cmbAlbaranes.currentIndexChanged.connect(self.rellenar_datos_desde_combo)

        form_layout.addWidget(QLabel("Nº Albará:"), 0, 0)
        form_layout.addWidget(self.cmbAlbaranes, 0, 1)

        form_layout.addWidget(QLabel("Data:"), 1, 0)
        form_layout.addWidget(self.txtData, 1, 1)

        form_layout.addWidget(QLabel("Nome:"), 2, 0)
        form_layout.addWidget(self.txtNome, 2, 1)

        form_layout.addWidget(QLabel("Apelido:"), 3, 0)
        form_layout.addWidget(self.txtApelido, 3, 1)

        form_layout.addWidget(QLabel("Cidade:"), 4, 0)
        form_layout.addWidget(self.txtCidade, 4, 1)

        form_group.setLayout(form_layout)

        # ====== LISTA ======
        self.lista = QListView()
        self.lista.setModel(self.modelo)

        # ====== TEXTO FINAL ======
        self.texto = QTextEdit()
        self.texto.setReadOnly(True)

        # ====== BOTONES ======
        btn_group = QHBoxLayout()
        self.btnNuevo = QPushButton("Nuevo")
        self.btnEditar = QPushButton("Editar")
        self.btnEliminar = QPushButton("Eliminar")
        self.btnCancelar = QPushButton("Cancelar")
        self.btnAceptar = QPushButton("Aceptar")

        btn_group.addWidget(self.btnNuevo)
        btn_group.addWidget(self.btnEditar)
        btn_group.addWidget(self.btnEliminar)
        btn_group.addStretch()
        btn_group.addWidget(self.btnCancelar)
        btn_group.addWidget(self.btnAceptar)

        # Conectar señales
        self.btnNuevo.clicked.connect(self.nuevo)
        self.btnEditar.clicked.connect(self.editar)
        self.btnEliminar.clicked.connect(self.eliminar)
        self.btnAceptar.clicked.connect(self.aceptar)
        self.btnCancelar.clicked.connect(self.cancelar)

        # ====== LAYOUT PRINCIPAL ======
        layout = QVBoxLayout()
        layout.addWidget(form_group)
        layout.addWidget(self.lista)
        layout.addWidget(QLabel("Rexistro final:"))
        layout.addWidget(self.texto)
        layout.addLayout(btn_group)

        self.setLayout(layout)

        # Deshabilitar campos al inicio
        self.habilitar_formulario(False)

    # ======================================================
    #   FUNCIONES DE FORMULARIO
    # ======================================================

    def habilitar_formulario(self, enabled):
        self.txtData.setEnabled(enabled)
        self.txtNome.setEnabled(enabled)
        self.txtApelido.setEnabled(enabled)
        self.txtCidade.setEnabled(enabled)
        self.cmbAlbaranes.setEnabled(enabled)
        self.btnAceptar.setEnabled(enabled)
        self.btnCancelar.setEnabled(enabled)

    def limpiar_formulario(self):
        self.txtData.clear()
        self.txtNome.clear()
        self.txtApelido.clear()
        self.txtCidade.clear()

    # ======================================================
    #   FUNCIONES PRINCIPALES
    # ======================================================

    def nuevo(self):
        self.modo = "nuevo"
        self.limpiar_formulario()
        self.habilitar_formulario(True)

    def editar(self):
        index = self.lista.currentIndex()
        if not index.isValid():
            return

        self.indice_editando = index.row()
        self.modo = "editar"
        self.habilitar_formulario(True)

        # Cargar datos existentes
        codigo = self.datos_albaranes[self.indice_editando]
        self.txtData.setText(codigo[1])
        self.txtNome.setText(codigo[2])
        self.txtApelido.setText(codigo[3])
        self.txtCidade.setText(codigo[4])

    def eliminar(self):
        index = self.lista.currentIndex()
        if not index.isValid():
            return

        fila = index.row()
        self.modelo.removeRow(fila)
        del self.datos_albaranes[fila]

    def aceptar(self):
        data = self.txtData.text()
        nome = self.txtNome.text()
        apelido = self.txtApelido.text()
        cidade = self.txtCidade.text()
        numero = self.cmbAlbaranes.currentText()

        texto_item = f"{numero} - {nome} {apelido} - {data}"

        if self.modo == "nuevo":
            self.modelo.appendRow(QStandardItem(texto_item))
            self.datos_albaranes.append([numero, data, nome, apelido, cidade])

        elif self.modo == "editar":
            self.modelo.setItem(self.indice_editando, QStandardItem(texto_item))
            self.datos_albaranes[self.indice_editando] = [numero, data, nome, apelido, cidade]

        # Mostrar en QTextEdit
        self.texto.append(texto_item)

        self.cancelar()

    def cancelar(self):
        self.modo = None
        self.indice_editando = None
        self.habilitar_formulario(False)
        self.limpiar_formulario()

    # ======================================================
    #   FUNCION COMBOBOX
    # ======================================================

    def rellenar_datos_desde_combo(self):
        i = self.cmbAlbaranes.currentIndex()
        datos = self.datos_albaranes[i]

        self.txtData.setText(datos[1])
        self.txtNome.setText(datos[2])
        self.txtApelido.setText(datos[3])
        self.txtCidade.setText(datos[4])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaClientes()
    ventana.show()
    sys.exit(app.exec())
