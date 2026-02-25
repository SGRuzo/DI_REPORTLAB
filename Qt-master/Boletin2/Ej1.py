import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QPushButton, QVBoxLayout,
    QStackedLayout, QRadioButton, QCheckBox, QHBoxLayout, QLabel
)
from PyQt6.QtGui import QPalette, QColor


class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QStackedLayout + Cores")

        # --- Layout principal ---
        layout_principal = QVBoxLayout()

        # --- Selector de páxinas ---
        boto1 = QPushButton("Ir á páxina 1")
        boto2 = QPushButton("Ir á páxina 2")

        boto1.clicked.connect(lambda: self.cambiar_paxina(0))
        boto2.clicked.connect(lambda: self.cambiar_paxina(1))

        layout_principal.addWidget(boto1)
        layout_principal.addWidget(boto2)

        # --- Controis de cor ---
        self.radio_vermello = QRadioButton("Vermello")
        self.radio_verde = QRadioButton("Verde")
        self.check_azul = QCheckBox("Azul (activar/desactivar)")

        self.radio_vermello.toggled.connect(self.actualizar_cor)
        self.radio_verde.toggled.connect(self.actualizar_cor)
        self.check_azul.stateChanged.connect(self.actualizar_cor)

        controles_cor = QHBoxLayout()
        controles_cor.addWidget(self.radio_vermello)
        controles_cor.addWidget(self.radio_verde)
        controles_cor.addWidget(self.check_azul)

        layout_principal.addLayout(controles_cor)

        # --- PÁXINAS ---
        pax1 = QLabel("Páxina 1")
        pax1.setAutoFillBackground(True)

        pax2 = QLabel("Páxina 2")
        pax2.setAutoFillBackground(True)

        # Stacked layout
        self.stacked = QStackedLayout()
        self.stacked.addWidget(pax1)
        self.stacked.addWidget(pax2)

        layout_principal.addLayout(self.stacked)

        self.setLayout(layout_principal)

    # --- Cambiar páxina ---
    def cambiar_paxina(self, indice):
        self.stacked.setCurrentIndex(indice)
        self.actualizar_cor()

    # --- Cambiar cor ---
    def actualizar_cor(self):
        widget = self.stacked.currentWidget()
        paleta = widget.palette()

        if self.radio_vermello.isChecked():
            paleta.setColor(QPalette.ColorRole.Window, QColor("red"))
        elif self.radio_verde.isChecked():
            paleta.setColor(QPalette.ColorRole.Window, QColor("lightgreen"))
        else:
            paleta.setColor(QPalette.ColorRole.Window, QColor("white"))

        if self.check_azul.isChecked():
            paleta.setColor(QPalette.ColorRole.Window, QColor("lightblue"))

        widget.setPalette(paleta)


app = QApplication(sys.argv)
win = Ventana()
win.show()
sys.exit(app.exec())
