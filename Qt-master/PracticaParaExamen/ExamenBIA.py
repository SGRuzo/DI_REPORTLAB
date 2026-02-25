import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QGroupBox, QLabel, QLineEdit, QComboBox, QTextEdit,
    QPushButton, QGridLayout, QVBoxLayout, QHBoxLayout
)


class FiestraPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exame 16-11-2025 grupo B")

        # --- Central widget y layout principal ---
        central = QWidget()
        self.setCentralWidget(central)

        layout_principal = QVBoxLayout()
        central.setLayout(layout_principal)

        # =========================================================
        # 1) GROUPBOX CLIENTE (parte superior)
        # =========================================================
        gpbCliente = QGroupBox("Cliente")
        layout_form = QGridLayout()
        gpbCliente.setLayout(layout_form)

        # Fila 0: Número Cliente | Nome
        layout_form.addWidget(QLabel("Número Cliente"), 0, 0)
        self.txtNumeroCliente = QLineEdit()
        layout_form.addWidget(self.txtNumeroCliente, 0, 1)

        layout_form.addWidget(QLabel("Nome"), 0, 2)
        self.txtNome = QLineEdit()
        layout_form.addWidget(self.txtNome, 0, 3)

        # Fila 1: Apelidos (campo largo)
        layout_form.addWidget(QLabel("Apelidos"), 1, 0)
        self.txtApelidos = QLineEdit()
        layout_form.addWidget(self.txtApelidos, 1, 1, 1, 3)

        # Fila 2: Dirección (campo largo)
        layout_form.addWidget(QLabel("Dirección"), 2, 0)
        self.txtDireccion = QLineEdit()
        layout_form.addWidget(self.txtDireccion, 2, 1, 1, 3)

        # Fila 3: Cidade | Provincia (combo)
        layout_form.addWidget(QLabel("Cidade"), 3, 0)
        self.txtCidade = QLineEdit()
        layout_form.addWidget(self.txtCidade, 3, 1)

        layout_form.addWidget(QLabel("Provincia"), 3, 2)
        self.cmbProvincia = QComboBox()
        layout_form.addWidget(self.cmbProvincia, 3, 3)

        layout_principal.addWidget(gpbCliente)

        # =========================================================
        # 2) ZONA CENTRAL: QTextEdit + botones Engadir/Editar/Borrar
        # =========================================================
        zona_central = QHBoxLayout()
        layout_principal.addLayout(zona_central)

        self.txtListado = QTextEdit()
        zona_central.addWidget(self.txtListado)

        caja_botones = QVBoxLayout()
        zona_central.addLayout(caja_botones)

        self.btnEngadir = QPushButton("Engadir")
        self.btnEditar = QPushButton("Editar")
        self.btnBorrar = QPushButton("Borrar")

        caja_botones.addWidget(self.btnEngadir)
        caja_botones.addWidget(self.btnEditar)
        caja_botones.addWidget(self.btnBorrar)
        caja_botones.addStretch()

        # =========================================================
        # 3) BOTONES INFERIORES: Cancelar | Aceptar
        # =========================================================
        caja_inferior = QHBoxLayout()
        layout_principal.addLayout(caja_inferior)

        caja_inferior.addStretch()
        self.btnCancelar = QPushButton("Cancelar")
        self.btnAceptar = QPushButton("Aceptar")
        caja_inferior.addWidget(self.btnCancelar)
        caja_inferior.addWidget(self.btnAceptar)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = FiestraPrincipal()
    ventana.show()
    sys.exit(app.exec())
