import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (QApplication, QMainWindow,
                             QLabel, QListWidget, QPushButton, QComboBox, QLineEdit,
                             QRadioButton, QVBoxLayout, QWidget, QHBoxLayout, QGridLayout, QListWidgetItem,
                             QAbstractItemView)


class FiestraPrincipal (QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Exame 10-12_2024")

        # Labels
        lblNome = QLabel("Nome")
        lblApelido = QLabel("Apelido")
        lblTratamento = QLabel("Tratamento")
        lblUsuario = QLabel("Usuario")

        # Entradas de texto
        self.txtNome = QLineEdit()
        self.txtApelido = QLineEdit()
        self.txtTratamento = QLineEdit()
        self.txtUsuario = QLineEdit()

        # ComboBox
        self.cmbFormato = QComboBox()
        self.cmbFormato.addItem("HTML")
        self.cmbFormato.addItem("Texto Plano")
        self.cmbFormato.addItem("Personalizado")
        self.cmbFormato.currentIndexChanged.connect(self.cmbFormatoChanged)

        lblFormatoC = QLabel("Formato de Correo:")

        lblDireccionC = QLabel("Dirección de correo")
        self.txtDireccionC = QLineEdit()

        self.lstDireccionC = QListWidget()
        self.lstDireccionC.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)

        # Botones principales
        self.btnEngadir = QPushButton("Engadir")
        self.btnEditar = QPushButton("Editar")
        self.btnBorrar = QPushButton("Borrar")
        self.btnPorDefecto = QPushButton("Por Defecto")

        self.btnEngadir.clicked.connect(self.addUser)
        self.btnBorrar.clicked.connect(self.deleteUser)

        # RadioButtons
        lblFormato = QLabel("Formato:")
        self.rbtHtml = QRadioButton("HTML")
        self.rbtTextoPlano = QRadioButton("Texto Plano")
        self.rbtPersonalizado = QRadioButton("Personalizado")

        self.rbtHtml.clicked.connect(self.cmbFormatoChangeOptionH)
        self.rbtTextoPlano.clicked.connect(self.cmbFormatoChangeOptionTP)
        self.rbtPersonalizado.clicked.connect(self.cmbFormatoChangeOptionP)

        # Aceptar / Cancelar
        btnAceptar = QPushButton("Aceptar")
        btnCancelar = QPushButton("Cancelar")

        # Layout principal
        caja_v = QVBoxLayout()
        container = QWidget()
        container.setLayout(caja_v)
        self.setCentralWidget(container)

        # Layouts personalizados (mantengo tu estructura EXACTA)
        nome_v = NomeLayout(lblNome, self.txtNome)
        apellido_v = ApellidoLayout(lblApelido, self.txtApelido)
        tratamento_g = TratamentoLayout(lblTratamento, self.txtTratamento, lblUsuario, self.txtUsuario)
        formato_h = FormatoLayout(lblFormato, self.cmbFormato)
        body_h = BodyLayout(self.lstDireccionC, self.btnEngadir, self.btnEditar, self.btnBorrar, self.btnPorDefecto,
                            lblFormatoC, self.rbtHtml, self.rbtTextoPlano, self.rbtPersonalizado)
        bot_v = BotLayout(lblDireccionC, self.txtDireccionC, btnAceptar, btnCancelar)

        # Añadimos layouts al principal
        caja_v.addLayout(nome_v)
        caja_v.addLayout(apellido_v)
        caja_v.addLayout(tratamento_g)
        caja_v.addLayout(formato_h)
        caja_v.addLayout(body_h)
        caja_v.addLayout(bot_v)

        self.show()

    # ----------------------------------------------------
    # FUNCIONES CORREGIDAS
    # ----------------------------------------------------

    def addUser(self):
        """ Añade usuario a la lista (corregido: no sobrescribe texto) """
        nome = self.txtNome.text().strip()
        apelido = self.txtApelido.text().strip()
        direccion = self.txtDireccionC.text().strip()

        if nome or apelido or direccion:
            texto = f"{nome} {apelido} - {direccion}"
            newItem = QListWidgetItem(texto)
            self.lstDireccionC.addItem(newItem)

        # Limpiar campos
        self.txtNome.clear()
        self.txtApelido.clear()
        self.txtDireccionC.clear()

    def deleteUser(self):
        """ Borra correcto: takeItem(row) """
        items = self.lstDireccionC.selectedItems()
        if items:
            for item in items:
                row = self.lstDireccionC.row(item)
                self.lstDireccionC.takeItem(row)

    def cmbFormatoChanged(self):
        """ Sincroniza ComboBox → RadioButtons """
        index = self.cmbFormato.currentIndex()
        self.rbtHtml.setChecked(index == 0)
        self.rbtTextoPlano.setChecked(index == 1)
        self.rbtPersonalizado.setChecked(index == 2)

    def cmbFormatoChangeOptionH(self):
        self.cmbFormato.setCurrentIndex(0)

    def cmbFormatoChangeOptionTP(self):
        self.cmbFormato.setCurrentIndex(1)

    def cmbFormatoChangeOptionP(self):
        self.cmbFormato.setCurrentIndex(2)


# ---------------------------------------------------------
# TUS LAYOUTS → Los mantengo EXACTAMENTE igual que tú
# ---------------------------------------------------------

class NomeLayout(QHBoxLayout):
    def __init__(self, lblNome, txtNome):
        super().__init__()
        self.addWidget(lblNome)
        self.addSpacing(50)
        self.addWidget(txtNome)

class ApellidoLayout(QHBoxLayout):
    def __init__(self, lblApelido, txtApelido):
        super().__init__()
        self.addWidget(lblApelido)
        self.addSpacing(40)
        self.addWidget(txtApelido)

class TratamentoLayout(QGridLayout):
    def __init__(self, lblTratamento, txtTratamento, lblUsuario, txtUsuario):
        super().__init__()
        self.addWidget(lblTratamento, 0, 0)
        self.addWidget(txtTratamento, 1, 0)
        self.addWidget(lblUsuario, 0, 1)
        self.addWidget(txtUsuario, 1, 1)

class FormatoLayout(QHBoxLayout):
    def __init__(self, lblFormato, cmbFormato):
        super().__init__()
        self.addWidget(lblFormato)
        self.addWidget(cmbFormato)

class BodyLayout(QHBoxLayout):
    def __init__(self, lstDireccionC, btnEngadir, btnEditar, btnBorrar, btnPorDefecto,
                 lblFormatoC, rbtHtml, rbtTextoPlano, rbtPersonalizado):
        super().__init__()
        bodyLeft_v = BodyLeftLayout(btnEngadir, btnEditar, btnBorrar, btnPorDefecto,
                                    lblFormatoC, rbtHtml, rbtTextoPlano, rbtPersonalizado)
        self.addWidget(lstDireccionC)
        self.addLayout(bodyLeft_v)

class BodyLeftLayout(QVBoxLayout):
    def __init__(self, btnEngadir, btnEditar, btnBorrar, btnPorDefecto,
                 lblFormatoC, rbtHtml, rbtTextoPlano, rbtPersonalizado):
        super().__init__()
        buttons_v = ButtonsLayout(btnEngadir, btnEditar, btnBorrar, btnPorDefecto)
        radioButtons_v = RadioButtonsLayout(lblFormatoC, rbtHtml, rbtTextoPlano, rbtPersonalizado)
        self.addLayout(buttons_v)
        self.addLayout(radioButtons_v)

class ButtonsLayout(QVBoxLayout):
    def __init__(self, btnEngadir, btnEditar, btnBorrar, btnPorDefecto):
        super().__init__()
        self.addWidget(btnEngadir)
        self.addWidget(btnEditar)
        self.addWidget(btnBorrar)
        self.addWidget(btnPorDefecto)

class RadioButtonsLayout(QVBoxLayout):
    def __init__(self, lblFormatoC, rbtHtml, rbtTextoPlano, rbtPersonalizado):
        super().__init__()
        self.addWidget(lblFormatoC)
        self.addWidget(rbtHtml)
        self.addWidget(rbtTextoPlano)
        self.addWidget(rbtPersonalizado)

class BotLayout(QVBoxLayout):
    def __init__(self, lblDireccionC, txtDireccionC, btnAceptar, btnCancelar):
        super().__init__()
        confirmar_h = ConfirmarLayout(btnAceptar, btnCancelar)
        self.addWidget(lblDireccionC)
        self.addWidget(txtDireccionC)
        self.addLayout(confirmar_h)

class ConfirmarLayout(QHBoxLayout):
    def __init__(self, btnAceptar, btnCancelar):
        super().__init__()
        self.addStretch()
        self.addWidget(btnCancelar)
        self.addWidget(btnAceptar)


if __name__=="__main__":
    aplicacion = QApplication(sys.argv)
    fiestra = FiestraPrincipal()
    aplicacion.exec()
