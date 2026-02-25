import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton,
    QVBoxLayout, QHBoxLayout, QComboBox, QTextEdit
)


class FiestraPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exame PyQt6 – Sen Grid")

        # --------------------------------------------------------
        # DATOS DO EXAME
        # --------------------------------------------------------
        self.albaras = [
            ["11111", "02/11/2024", "11111", "Ana", "Ruiz"],
            ["22220", "08/03/2024", "22220", "Pedro", "Diz"],
            ["33333", "23/10/2025", "33333", "Rosa", "Sanz"]
        ]


        layout_principal = QVBoxLayout()


        caja_albara = QHBoxLayout()
        caja_albara.addWidget(QLabel("Número de albará:"))
        self.cmbNumero = QComboBox()
        self.cmbNumero.addItems([fila[0] for fila in self.albaras])  # primeiro elemento
        self.cmbNumero.currentIndexChanged.connect(self.cargar_datos)
        caja_albara.addWidget(self.cmbNumero)
        layout_principal.addLayout(caja_albara)

        # DATA
        caja_data = QHBoxLayout()
        caja_data.addWidget(QLabel("Data:"))
        self.txtData = QLineEdit()
        caja_data.addWidget(self.txtData)
        layout_principal.addLayout(caja_data)

        # Nº CLIENTE
        caja_cliente = QHBoxLayout()
        caja_cliente.addWidget(QLabel("Número cliente:"))
        self.txtNumeroCliente = QLineEdit()
        caja_cliente.addWidget(self.txtNumeroCliente)
        layout_principal.addLayout(caja_cliente)

        # NOME
        caja_nome = QHBoxLayout()
        caja_nome.addWidget(QLabel("Nome:"))
        self.txtNome = QLineEdit()
        caja_nome.addWidget(self.txtNome)
        layout_principal.addLayout(caja_nome)

        # APELIDO
        caja_apelido = QHBoxLayout()
        caja_apelido.addWidget(QLabel("Apelido:"))
        self.txtApelido = QLineEdit()
        caja_apelido.addWidget(self.txtApelido)
        layout_principal.addLayout(caja_apelido)

        # CIDADE
        caja_cidade = QHBoxLayout()
        caja_cidade.addWidget(QLabel("Cidade:"))
        self.txtCidade = QLineEdit()
        caja_cidade.addWidget(self.txtCidade)
        layout_principal.addLayout(caja_cidade)

        # --------------------------------------------------------
        # 2. QTextEdit
        # --------------------------------------------------------
        self.txeClientes = QTextEdit()
        layout_principal.addWidget(self.txeClientes)

        # --------------------------------------------------------
        # 3. BOTÓNS
        # --------------------------------------------------------
        caja_botons = QHBoxLayout()

        self.btnEngadir = QPushButton("Engadir")
        self.btnEngadir.clicked.connect(self.on_engadir)   # ⬅️ CONECTADO
        caja_botons.addWidget(self.btnEngadir)

        self.btnEditar = QPushButton("Editar")
        self.btnEditar.clicked.connect(self.on_editar)
        caja_botons.addWidget(self.btnEditar)

        self.btnBorrar = QPushButton("Borrar")
        caja_botons.addWidget(self.btnBorrar)

        caja_botons.addStretch()  # empurrar Aceptar/Cancelar á dereita

        self.btnCancelar = QPushButton("Cancelar")
        self.btnCancelar.clicked.connect(self.close)
        caja_botons.addWidget(self.btnCancelar)

        self.btnAceptar = QPushButton("Aceptar")
        self.btnAceptar.setEnabled(False)  # DESHABILITADO COMO DI O EXAME
        caja_botons.addWidget(self.btnAceptar)

        layout_principal.addLayout(caja_botons)

        # --------------------------------------------------------
        # CONTENEDOR CENTRAL
        # --------------------------------------------------------
        cont = QWidget()
        cont.setLayout(layout_principal)
        self.setCentralWidget(cont)

        # Cargar os datos do primeiro albará
        self.cargar_datos(0)

    # --------------------------------------------------------
    # FUNCIÓN 3 – Cargar datos nos QLineEdit
    # --------------------------------------------------------
    def cargar_datos(self, indice):
        cod, data, numcl, nome, apelido = self.albaras[indice]
        self.txtData.setText(data)
        self.txtNumeroCliente.setText(numcl)
        self.txtNome.setText(nome)
        self.txtApelido.setText(apelido)
        self.txtCidade.setText("")

    # --------------------------------------------------------
    # FUNCIÓN 4 – Editar → escribir no QTextEdit
    # --------------------------------------------------------
    def on_editar(self):
        codigo = self.cmbNumero.currentText()
        data = self.txtData.text()
        nome = self.txtNome.text()
        apelido = self.txtApelido.text()

        texto = f"[EDITAR] {codigo} - {nome} {apelido} - {data}"
        self.txeClientes.append(texto)

    # --------------------------------------------------------
    # FUNCIÓN EXTRA – Engadir → escribir no QTextEdit tamén
    # --------------------------------------------------------
    def on_engadir(self):
        codigo = self.cmbNumero.currentText()
        data = self.txtData.text()
        nome = self.txtNome.text()
        apelido = self.txtApelido.text()
        cidade = self.txtCidade.text()

        # Incluímos a cidade para darlle algo de sentido a "Engadir"
        texto = f"[ENGADIR] {codigo} - {nome} {apelido} - {data} - {cidade}"
        self.txeClientes.append(texto)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    fiestra = FiestraPrincipal()
    fiestra.show()
    sys.exit(app.exec())
