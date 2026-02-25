import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QLabel, QLineEdit, QComboBox, QListWidget,
    QPushButton, QWidget, QGridLayout, QVBoxLayout, QHBoxLayout, QListWidgetItem,
    QRadioButton, QButtonGroup
)


class FiestraPrincipal(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exame 10-12_2024")

        # ----------------------------------------------------
        # LAYOUT PRINCIPAL: GRID
        # ----------------------------------------------------
        maia = QGridLayout()

        # ----------------------------------------------------
        # BLOQUE 1: Nome + Apelido
        # ----------------------------------------------------
        caixa_nome = QHBoxLayout()
        self.txtNome = QLineEdit()
        caixa_nome.addWidget(QLabel("Nome"))
        caixa_nome.addWidget(self.txtNome)

        caixa_apelido = QHBoxLayout()
        self.txtApelido = QLineEdit()
        caixa_apelido.addWidget(QLabel("Apelido"))
        caixa_apelido.addWidget(self.txtApelido)

        caixa_vertical_datos1 = QVBoxLayout()
        caixa_vertical_datos1.addLayout(caixa_nome)
        caixa_vertical_datos1.addLayout(caixa_apelido)

        # ----------------------------------------------------
        # BLOQUE 2: Tratamento + Usuario
        # ----------------------------------------------------
        caixa_tratamento = QGridLayout()
        self.txtTratamento = QLineEdit()
        self.txtUsuario = QLineEdit()

        caixa_tratamento.addWidget(QLabel("Tratamento"), 0, 0)
        caixa_tratamento.addWidget(self.txtTratamento, 1, 0)
        caixa_tratamento.addWidget(QLabel("Usuario"), 0, 1)
        caixa_tratamento.addWidget(self.txtUsuario, 1, 1)

        caixa_vertical_datos1.addLayout(caixa_tratamento)

        # ----------------------------------------------------
        # BLOQUE 3: Formato (ComboBox)
        # ----------------------------------------------------
        caixa_formato = QHBoxLayout()
        self.cmbFormato = QComboBox()
        self.cmbFormato.addItems(["HTML", "Texto Plano", "Personalizado"])
        self.cmbFormato.currentIndexChanged.connect(self.cmbFormatoChanged)

        caixa_formato.addWidget(QLabel("Formato:"))
        caixa_formato.addWidget(self.cmbFormato)

        caixa_vertical_datos1.addLayout(caixa_formato)

        # Insertamos bloque 1+2+3 en el grid
        maia.addLayout(caixa_vertical_datos1, 0, 0)

        # ----------------------------------------------------
        # BLOQUE 4: Lista de correos + botones
        # ----------------------------------------------------
        self.lstDireccionC = QListWidget()

        self.txtDireccionC = QLineEdit()
        lblDireccionC = QLabel("Dirección de correo")

        # Botones
        self.btnEngadir = QPushButton("Engadir")
        self.btnEditar = QPushButton("Editar")
        self.btnBorrar = QPushButton("Borrar")
        self.btnPorDefecto = QPushButton("Por Defecto")

        self.btnEngadir.clicked.connect(self.addUser)
        self.btnBorrar.clicked.connect(self.deleteUser)

        caixa_botons = QVBoxLayout()
        caixa_botons.addWidget(self.btnEngadir)
        caixa_botons.addWidget(self.btnEditar)
        caixa_botons.addWidget(self.btnBorrar)
        caixa_botons.addWidget(self.btnPorDefecto)

        # ----------------------------------------------------
        # BLOQUE 5: RadioButtons (Formato correo)
        # ----------------------------------------------------
        caixa_radios = QVBoxLayout()
        caixa_radios.addWidget(QLabel("Formato de Correo:"))

        self.rbtHtml = QRadioButton("HTML")
        self.rbtTextoPlano = QRadioButton("Texto Plano")
        self.rbtPersonalizado = QRadioButton("Personalizado")

        grupo_radios = QButtonGroup(self)
        grupo_radios.addButton(self.rbtHtml)
        grupo_radios.addButton(self.rbtTextoPlano)
        grupo_radios.addButton(self.rbtPersonalizado)

        self.rbtHtml.setChecked(True)

        self.rbtHtml.clicked.connect(lambda: self.cmbFormato.setCurrentIndex(0))
        self.rbtTextoPlano.clicked.connect(lambda: self.cmbFormato.setCurrentIndex(1))
        self.rbtPersonalizado.clicked.connect(lambda: self.cmbFormato.setCurrentIndex(2))

        caixa_radios.addWidget(self.rbtHtml)
        caixa_radios.addWidget(self.rbtTextoPlano)
        caixa_radios.addWidget(self.rbtPersonalizado)

        # Columna de botones + radios
        caixa_lateral_dereita = QVBoxLayout()
        caixa_lateral_dereita.addLayout(caixa_botons)
        caixa_lateral_dereita.addLayout(caixa_radios)

        # Insertamos lista + columna de botones
        caixa_listado = QHBoxLayout()
        caixa_listado.addWidget(self.lstDireccionC)
        caixa_listado.addLayout(caixa_lateral_dereita)

        maia.addLayout(caixa_listado, 0, 1)

        # ----------------------------------------------------
        # BLOQUE 6: Dirección correo + Aceptar / Cancelar
        # ----------------------------------------------------
        caixa_direccion = QVBoxLayout()
        caixa_direccion.addWidget(lblDireccionC)
        caixa_direccion.addWidget(self.txtDireccionC)

        caixa_confirmar = QHBoxLayout()
        btnAceptar = QPushButton("Aceptar")
        btnCancelar = QPushButton("Cancelar")
        caixa_confirmar.addStretch()
        caixa_confirmar.addWidget(btnCancelar)
        caixa_confirmar.addWidget(btnAceptar)

        caixa_direccion.addLayout(caixa_confirmar)

        maia.addLayout(caixa_direccion, 1, 0, 1, 2)

        # ----------------------------------------------------
        # Container
        # ----------------------------------------------------
        container = QWidget()
        container.setLayout(maia)
        self.setCentralWidget(container)

        self.show()

    # --------------------------------------------------------
    # FUNCIONES
    # --------------------------------------------------------

    def addUser(self):
        nome = self.txtNome.text().strip()
        apelido = self.txtApelido.text().strip()
        direccion = self.txtDireccionC.text().strip()

        if nome or apelido or direccion:
            texto = f"{nome} {apelido} - {direccion}"
            self.lstDireccionC.addItem(QListWidgetItem(texto))

        self.txtNome.clear()
        self.txtApelido.clear()
        self.txtDireccionC.clear()

    def deleteUser(self):
        item = self.lstDireccionC.currentItem()
        if item:
            row = self.lstDireccionC.row(item)
            self.lstDireccionC.takeItem(row)

    def cmbFormatoChanged(self):
        index = self.cmbFormato.currentIndex()
        self.rbtHtml.setChecked(index == 0)
        self.rbtTextoPlano.setChecked(index == 1)
        self.rbtPersonalizado.setChecked(index == 2)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = FiestraPrincipal()
    ventana.show()
    sys.exit(app.exec())
