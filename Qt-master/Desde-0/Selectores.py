import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QGroupBox,
    QRadioButton, QCheckBox, QPushButton, QLabel
)
from PySide6.QtCore import Qt


class SelectoresApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Selectores")
        self.setGeometry(100, 100, 450, 300)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # -----------------------------
        # GRUPO DE RADIOBUTTONS
        # -----------------------------
        self.grupo_radio = QGroupBox("Opciones exclusivas con RadioButton")
        radio_layout = QVBoxLayout(self.grupo_radio)

        self.radio1 = QRadioButton("A")
        self.radio2 = QRadioButton("B")
        self.radio3 = QRadioButton("C")

        radio_layout.addWidget(self.radio1)
        radio_layout.addWidget(self.radio2)
        radio_layout.addWidget(self.radio3)

        main_layout.addWidget(self.grupo_radio)

        # -----------------------------
        # GRUPO DE CHECKBOXES
        # -----------------------------
        self.grupo_check = QGroupBox("Opciones múltiples con CheckBox")
        check_layout = QVBoxLayout(self.grupo_check)

        self.texto = QLabel("Elige lo que quieras, brou:")

        self.check1 = QCheckBox("Patatas")
        self.check2 = QCheckBox("Hamburguesa")
        self.check3 = QCheckBox("Sí")
        self.check4 = QCheckBox("Bomba")

        check_layout.addWidget(self.texto)
        check_layout.addWidget(self.check1)
        check_layout.addWidget(self.check2)
        check_layout.addWidget(self.check3)
        check_layout.addWidget(self.check4)

        main_layout.addWidget(self.grupo_check)

        # -----------------------------
        # ETIQUETA + BOTÓN
        # -----------------------------
        self.label_estado = QLabel("Selecciona algo y pulsa el botón.")
        self.btn_check = QPushButton("VERIFICAR")

        main_layout.addWidget(self.label_estado)
        main_layout.addWidget(self.btn_check)

        # Conexión
        self.btn_check.clicked.connect(self.vericar_opciones)

    # -----------------------------
    # SLOT
    # -----------------------------
    def vericar_opciones(self):
        # A. Verificar RadioButtons
        if self.radio1.isChecked():
            opcion_radio = self.radio1.text()
        elif self.radio2.isChecked():
            opcion_radio = self.radio2.text()
        elif self.radio3.isChecked():
            opcion_radio = self.radio3.text()
        else:
            opcion_radio = "Ninguna"

        # B. Verificar CheckBoxes
        uno = "Sí" if self.check1.isChecked() else "No"
        dos = "Sí" if self.check2.isChecked() else "No"
        tres = "Sí" if self.check3.isChecked() else "No"
        cuatro = "Sí" if self.check4.isChecked() else "No"

        self.label_estado.setText(
            f"RadioButton: {opcion_radio} | CheckBoxes: {uno}, {dos}, {tres}, {cuatro}"
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SelectoresApp()
    window.show()
    sys.exit(app.exec())
