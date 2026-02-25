import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QMainWindow, QLabel, QLineEdit, QPushButton,
    QGridLayout, QVBoxLayout, QHBoxLayout, QComboBox, QTextEdit, QGroupBox
)
from PyQt6.QtCore import Qt


class FiestraPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exame 17-11-2025 Grupo A")


        self.albaras = [
            ["1111nn", "02/11/2024", "1111", "Ana", "Ruiz"],
            ["2222oo", "08/03/2024", "2222", "Pedro", "Diz"],
            ["3333qq", "23/10/2025", "3333", "Rosa", "Sanz"]
        ]


        layout = QVBoxLayout()


        gpbCliente = QGroupBox("Cliente")
        grid = QGridLayout()

        # Labels
        lblNumero = QLabel("Número Cliente")
        lblNome = QLabel("Nome Cliente")
        lblApelidos = QLabel("Apelidos")
        lblData = QLabel("Data")
        lblNumAlbara = QLabel("Número de albará")

        # Campos
        self.txtNumero = QLineEdit()
        self.txtNome = QLineEdit()
        self.txtApelidos = QLineEdit()
        self.txtData = QLineEdit()

        # ComboBox
        self.cmbAlbara = QComboBox()
        self.cmbAlbara.currentIndexChanged.connect(self.rellenar_campos)

        # ---- Añadir widgets al grid ----
        grid.addWidget(lblNumero, 0, 0)
        grid.addWidget(self.txtNumero, 0, 1)

        grid.addWidget(lblData, 0, 2)
        grid.addWidget(self.txtData, 0, 3)

        grid.addWidget(lblNome, 1, 0)
        grid.addWidget(self.txtNome, 1, 1)

        grid.addWidget(lblApelidos, 1, 2)
        grid.addWidget(self.txtApelidos, 1, 3)

        grid.addWidget(lblNumAlbara, 2, 0)
        grid.addWidget(self.cmbAlbara, 2, 1, 1, 3)

        gpbCliente.setLayout(grid)
        layout.addWidget(gpbCliente)

        # ============================
        #   LISTA (QTextEdit)
        # ============================
        self.txtLista = QTextEdit()
        self.txtLista.setReadOnly(True)
        layout.addWidget(self.txtLista)

        # ============================
        #   BOTONES EDITAR / BORRAR / ENGADIR
        # ============================
        cajaBtns = QHBoxLayout()

        self.btnEngadir = QPushButton("Engadir")
        self.btnEditar = QPushButton("Editar")
        self.btnBorrar = QPushButton("Borrar")

        self.btnEditar.clicked.connect(self.func_editar)

        cajaBtns.addWidget(self.btnEngadir)
        cajaBtns.addWidget(self.btnEditar)
        cajaBtns.addWidget(self.btnBorrar)

        layout.addLayout(cajaBtns)

        # ============================
        #   BOTONES ACEPTAR / CANCELAR
        # ============================
        cajaInf = QHBoxLayout()

        self.btnCancelar = QPushButton("Cancelar")
        self.btnCancelar.clicked.connect(self.close)

        self.btnAceptar = QPushButton("Aceptar")
        self.btnAceptar.setEnabled(False)  # Desactivado al inicio

        cajaInf.addStretch()
        cajaInf.addWidget(self.btnCancelar)
        cajaInf.addWidget(self.btnAceptar)

        layout.addLayout(cajaInf)

        # ============================
        #   CONTENEDOR FINAL
        # ============================
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Cargar albarás al combo
        self.cargar_albaras()



    def cargar_albaras(self):
        """Punto 3: cargar los números de albará en el ComboBox"""
        for entrada in self.albaras:
            self.cmbAlbara.addItem(entrada[0])  # primer elemento es el nº albará

    def rellenar_campos(self):
        """Punto 4: al seleccionar albará → rellenar los campos"""
        idx = self.cmbAlbara.currentIndex()
        if idx < 0:
            return

        numalb, data, numcli, nome, apelidos = self.albaras[idx]

        self.txtNumero.setText(numcli)
        self.txtNome.setText(nome)
        self.txtApelidos.setText(apelidos)
        self.txtData.setText(data)

    def func_editar(self):
        """Punto 5: pulsar Editar → añadir línea al QTextEdit"""
        numero = self.txtNumero.text()
        nome = self.txtNome.text()
        apelidos = self.txtApelidos.text()
        data = self.txtData.text()
        alb = self.cmbAlbara.currentText()

        linea = f"{alb} - {numero} - {nome} {apelidos} - {data}"

        self.txtLista.append(linea)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = FiestraPrincipal()
    ventana.show()
    sys.exit(app.exec())
