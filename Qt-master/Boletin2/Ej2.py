import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout,
    QStackedLayout, QRadioButton, QCheckBox, QLabel
)
from PyQt6.QtGui import QColor, QPalette


class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cambio exclusivo con Radio e combinación con Check")

        layout_principal = QVBoxLayout()

        # --- Cambiar páxina ---
        btn1 = QPushButton("Ir á páxina 1")
        btn2 = QPushButton("Ir á páxina 2")

        btn1.clicked.connect(lambda: self.cambiar_paxina(0))
        btn2.clicked.connect(lambda: self.cambiar_paxina(1))

        layout_principal.addWidget(btn1)
        layout_principal.addWidget(btn2)

        # --- RADIOBUTTONS (Modo exclusivo) ---
        self.radio_vermello = QRadioButton("Vermello (Exclusivo)")
        self.radio_verde = QRadioButton("Verde (Exclusivo)")
        self.radio_azul = QRadioButton("Azul (Exclusivo)")

        self.radio_vermello.toggled.connect(self.actualizar_cor)
        self.radio_verde.toggled.connect(self.actualizar_cor)
        self.radio_azul.toggled.connect(self.actualizar_cor)

        box_radios = QHBoxLayout()
        box_radios.addWidget(self.radio_vermello)
        box_radios.addWidget(self.radio_verde)
        box_radios.addWidget(self.radio_azul)

        layout_principal.addLayout(box_radios)

        # --- CHECKBOXES (Modo combinación) ---
        self.check_r = QCheckBox("Vermello")
        self.check_g = QCheckBox("Verde")
        self.check_b = QCheckBox("Azul")

        self.check_r.stateChanged.connect(self.actualizar_cor)
        self.check_g.stateChanged.connect(self.actualizar_cor)
        self.check_b.stateChanged.connect(self.actualizar_cor)

        box_checks = QHBoxLayout()
        box_checks.addWidget(self.check_r)
        box_checks.addWidget(self.check_g)
        box_checks.addWidget(self.check_b)

        layout_principal.addLayout(box_checks)

        # ----- PÁXINAS -----
        pag1 = QLabel("Páxina 1")
        pag1.setAutoFillBackground(True)
        pag2 = QLabel("Páxina 2")
        pag2.setAutoFillBackground(True)

        self.stacked = QStackedLayout()
        self.stacked.addWidget(pag1)
        self.stacked.addWidget(pag2)

        layout_principal.addLayout(self.stacked)
        self.setLayout(layout_principal)

    # --- Cambio de páxina ---
    def cambiar_paxina(self, idx):
        self.stacked.setCurrentIndex(idx)
        self.actualizar_cor()

    # --- Cálculo da cor resultante ---
    def actualizar_cor(self):
        widget = self.stacked.currentWidget()
        paleta = widget.palette()

        # --- PRIORIDADE: se hai radio seleccionado ---
        if self.radio_vermello.isChecked():
            cor = QColor(255, 0, 0)
        elif self.radio_verde.isChecked():
            cor = QColor(0, 255, 0)
        elif self.radio_azul.isChecked():
            cor = QColor(0, 0, 255)
        else:
            # --- Sen radios → usar CHECKBOXES ---
            r = 255 if self.check_r.isChecked() else 0
            g = 255 if self.check_g.isChecked() else 0
            b = 255 if self.check_b.isChecked() else 0

            # Ningún check → branco
            if not (self.check_r.isChecked() or self.check_g.isChecked() or self.check_b.isChecked()):
                cor = QColor(255, 255, 255)
            # Todos checks → negro
            elif r and g and b:
                cor = QColor(0, 0, 0)
            else:
                # Unha combinación normal (RGB)
                cor = QColor(r, g, b)

        paleta.setColor(QPalette.ColorRole.Window, cor)
        widget.setPalette(paleta)


app = QApplication(sys.argv)
win = Ventana()
win.show()
sys.exit(app.exec())
