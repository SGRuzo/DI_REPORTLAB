import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout,
    QStackedLayout, QRadioButton, QCheckBox, QLabel
)
from PyQt6.QtGui import QColor, QPalette


class Ventana(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Coherencia total entre botóns / radio / checkbox")

        # Estado de cor centralizado
        self.cor_actual = QColor(255, 255, 255)

        layout_principal = QVBoxLayout()

        # --- Botóns que cambian cor ---
        btn_r = QPushButton("Vermello")
        btn_g = QPushButton("Verde")
        btn_b = QPushButton("Azul")

        btn_r.clicked.connect(lambda: self.seleccionar_cor("red"))
        btn_g.clicked.connect(lambda: self.seleccionar_cor("green"))
        btn_b.clicked.connect(lambda: self.seleccionar_cor("blue"))

        box_btn = QHBoxLayout()
        box_btn.addWidget(btn_r)
        box_btn.addWidget(btn_g)
        box_btn.addWidget(btn_b)
        layout_principal.addLayout(box_btn)

        # --- RADIOBUTTONS ---
        self.radio_r = QRadioButton("Vermello")
        self.radio_g = QRadioButton("Verde")
        self.radio_b = QRadioButton("Azul")

        self.radio_r.toggled.connect(lambda: self.se_radio("red"))
        self.radio_g.toggled.connect(lambda: self.se_radio("green"))
        self.radio_b.toggled.connect(lambda: self.se_radio("blue"))

        box_radios = QHBoxLayout()
        box_radios.addWidget(self.radio_r)
        box_radios.addWidget(self.radio_g)
        box_radios.addWidget(self.radio_b)
        layout_principal.addLayout(box_radios)

        # --- CHECKBOXES ---
        self.check_r = QCheckBox("Vermello")
        self.check_g = QCheckBox("Verde")
        self.check_b = QCheckBox("Azul")

        self.check_r.stateChanged.connect(self.se_checks)
        self.check_g.stateChanged.connect(self.se_checks)
        self.check_b.stateChanged.connect(self.se_checks)

        box_checks = QHBoxLayout()
        box_checks.addWidget(self.check_r)
        box_checks.addWidget(self.check_g)
        box_checks.addWidget(self.check_b)
        layout_principal.addLayout(box_checks)

        # --- 2 PÁXINAS ---
        pag1 = QLabel("Páxina 1")
        pag1.setAutoFillBackground(True)
        pag2 = QLabel("Páxina 2")
        pag2.setAutoFillBackground(True)

        self.stacked = QStackedLayout()
        self.stacked.addWidget(pag1)
        self.stacked.addWidget(pag2)

        layout_principal.addLayout(self.stacked)

        # Cambio manual de páxinas
        boto1 = QPushButton("Páxina 1")
        boto2 = QPushButton("Páxina 2")
        boto1.clicked.connect(lambda: self.cambiar_paxina(0))
        boto2.clicked.connect(lambda: self.cambiar_paxina(1))
        layout_principal.addWidget(boto1)
        layout_principal.addWidget(boto2)

        self.setLayout(layout_principal)

    # --------------- FUNCIÓNS DE COHERENCIA --------------------

    def seleccionar_cor(self, cor):
        """Seleccionada dende botón ou radio → cambia todo."""
        if cor == "red":
            self.cor_actual = QColor(255, 0, 0)
        elif cor == "green":
            self.cor_actual = QColor(0, 255, 0)
        elif cor == "blue":
            self.cor_actual = QColor(0, 0, 255)

        self.actualizar_todo()

    def se_radio(self, cor):
        """Cando tocas un Radio, se está activado → actualizar todo."""
        radio = {
            "red": self.radio_r,
            "green": self.radio_g,
            "blue": self.radio_b
        }[cor]

        if radio.isChecked():
            self.seleccionar_cor(cor)

    def se_checks(self):
        """Cando se tocan checkboxes → combinación e actualización total."""
        r = 255 if self.check_r.isChecked() else 0
        g = 255 if self.check_g.isChecked() else 0
        b = 255 if self.check_b.isChecked() else 0

        # Ningún → branco
        if r == g == b == 0:
            self.cor_actual = QColor(255, 255, 255)

        # Todos → negro
        elif r == 255 and g == 255 and b == 255:
            self.cor_actual = QColor(0, 0, 0)

        else:
            self.cor_actual = QColor(r, g, b)

        self.actualizar_todo()

    def cambiar_paxina(self, idx):
        self.stacked.setCurrentIndex(idx)
        self.actualizar_todo()

    # ---- ACTUALIZA TODO SEGUNDO A COR CENTRAL ----
    def actualizar_todo(self):
        # 1. Actualizar fondo
        widget = self.stacked.currentWidget()
        paleta = widget.palette()
        paleta.setColor(QPalette.ColorRole.Window, self.cor_actual)
        widget.setPalette(paleta)

        # 2. Actualizar radios
        r, g, b = self.cor_actual.red(), self.cor_actual.green(), self.cor_actual.blue()

        self.radio_r.setChecked(r == 255 and g == 0 and b == 0)
        self.radio_g.setChecked(r == 0 and g == 255 and b == 0)
        self.radio_b.setChecked(r == 0 and g == 0 and b == 255)

        # 3. Actualizar checkboxes
        self.check_r.setChecked(r == 255)
        self.check_g.setChecked(g == 255)
        self.check_b.setChecked(b == 255)


# --------------------------------------------------------

app = QApplication(sys.argv)
win = Ventana()
win.show()
sys.exit(app.exec())
