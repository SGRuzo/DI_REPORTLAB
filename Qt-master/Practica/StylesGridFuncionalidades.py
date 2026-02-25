import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QMainWindow, QPushButton, QWidget, QApplication,
    QLabel, QComboBox, QCheckBox, QRadioButton, QGroupBox, QVBoxLayout,
    QTabWidget, QTextEdit, QButtonGroup, QDateTimeEdit, QSlider, QDial, QLineEdit,
    QGridLayout, QStyleFactory
)


class Styles(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Styles (Grid Version)")

        # -------------------------
        #   FILA 0 - STYLE OPTIONS
        # -------------------------
        self.lbl_style = QLabel("Style:")
        self.cmbComboBox = QComboBox()
        self.cmbComboBox.addItems(["Fusion", "Windows", "Macintosh"])
        self.checkBox1 = QCheckBox("Use style's standard palette")
        self.checkBox2 = QCheckBox("Disable widgets")

        # -------------------------
        #   GROUP 1
        # -------------------------
        self.rboton1 = QRadioButton("Radio button 1")
        self.rboton2 = QRadioButton("Radio button 2")
        self.rboton3 = QRadioButton("Radio button 3")
        self.tri_check = QCheckBox("Tri-state check box")
        self.tri_check.setTristate(True)

        self.grupoBotones1 = QButtonGroup(self)
        self.grupoBotones1.addButton(self.rboton1)
        self.grupoBotones1.addButton(self.rboton2)
        self.grupoBotones1.addButton(self.rboton3)
        self.grupoBotones1.addButton(self.tri_check)
        self.grupoBotones1.setExclusive(True)

        group1 = QGroupBox("Group 1")
        group1_layout = QVBoxLayout()
        group1_layout.addWidget(self.rboton1)
        group1_layout.addWidget(self.rboton2)
        group1_layout.addWidget(self.rboton3)
        group1_layout.addWidget(self.tri_check)
        group1.setLayout(group1_layout)

        # -------------------------
        #   GROUP 2
        # -------------------------
        group2 = QGroupBox("Group 2")
        group2_layout = QVBoxLayout()
        self.btnon1_normal = QPushButton("Default Push Button")
        self.btnon2_toggle = QPushButton("Toggle Push Button")
        self.btnon2_toggle.setCheckable(True)
        self.btnon3_flat = QPushButton("Flat Push Button")
        self.btnon3_flat.setFlat(True)

        group2_layout.addWidget(self.btnon1_normal)
        group2_layout.addWidget(self.btnon2_toggle)
        group2_layout.addWidget(self.btnon3_flat)
        group2.setLayout(group2_layout)

        # -------------------------
        #   TABS + GROUP 3
        # -------------------------
        self.tabbed_stack = QTabWidget()
        self.txtAreaTexto = QTextEdit()
        self.tabbed_stack.addTab(QWidget(), "Table")
        self.tabbed_stack.addTab(self.txtAreaTexto, "Text Edit")

        # TAB EXTRA
        self.tab_info = QTextEdit()
        self.tab_info.setReadOnly(True)
        self.tabbed_stack.addTab(self.tab_info, "Info")

        self.text7 = QLineEdit()
        self.text7.setEchoMode(QLineEdit.EchoMode.Password)

        self.datatimer = QDateTimeEdit()
        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.dial = QDial()

        group3 = QGroupBox("Group 3")
        group3_layout = QVBoxLayout()
        group3_layout.addWidget(self.text7)
        group3_layout.addWidget(self.datatimer)
        group3_layout.addWidget(self.slider)
        group3_layout.addWidget(self.dial)
        group3.setLayout(group3_layout)

        # -------------------------
        #   GRID PRINCIPAL
        # -------------------------
        grid = QGridLayout()
        grid.setSpacing(15)

        grid.addWidget(self.lbl_style, 0, 0)
        grid.addWidget(self.cmbComboBox, 0, 1)
        grid.addWidget(self.checkBox1, 0, 2)
        grid.addWidget(self.checkBox2, 0, 3)

        grid.addWidget(group1, 1, 0, 1, 2)
        grid.addWidget(group2, 1, 2, 1, 2)

        grid.addWidget(self.tabbed_stack, 2, 0, 1, 3)
        grid.addWidget(group3, 2, 3)

        container = QWidget()
        container.setLayout(grid)
        self.setCentralWidget(container)
        self.container = container

        # ============================
        #   SEÑALES SIN LAMBDA
        # ============================

        self.btnon2_toggle.toggled.connect(self.toggle_button_text)
        self.slider.valueChanged.connect(self.sync_slider_to_dial)
        self.dial.valueChanged.connect(self.sync_dial_to_slider)
        self.tri_check.stateChanged.connect(self.update_tristate_info)

        self.slider.valueChanged.connect(self.update_tab_info)
        self.dial.valueChanged.connect(self.update_tab_info)
        self.datatimer.dateTimeChanged.connect(self.update_tab_info)

        self.cmbComboBox.currentTextChanged.connect(self.change_style)
        self.checkBox1.toggled.connect(self.toggle_palette)
        self.checkBox2.toggled.connect(self.disable_widgets)

    # -------------------------
    # FUNCIONALIDADES NUEVAS
    # -------------------------

    def toggle_button_text(self, estado):
        """Cambia el texto del botón Toggle"""
        if estado:
            self.btnon2_toggle.setText("ON")
        else:
            self.btnon2_toggle.setText("OFF")

    def sync_slider_to_dial(self, valor):
        """Slider actualiza el dial"""
        self.dial.setValue(valor)

    def sync_dial_to_slider(self, valor):
        """Dial actualiza el slider"""
        self.slider.setValue(valor)

    def update_tristate_info(self, estado):
        """Muestra el estado del tri-check en el TextEdit"""
        self.txtAreaTexto.setPlainText(f"Tri-State actual: {estado.name}")

    def update_tab_info(self):
        """Actualiza la pestaña 'Info'"""
        self.tab_info.setPlainText(
            f"Password: {self.text7.text()}\n"
            f"Fecha/hora: {self.datatimer.dateTime().toString()}\n"
            f"Slider: {self.slider.value()}\n"
            f"Dial: {self.dial.value()}"
        )

    def change_style(self, estilo):
        """Cambia el estilo visual"""
        QApplication.setStyle(QStyleFactory.create(estilo))

    def toggle_palette(self, usar):
        """Activa/desactiva la paleta del estilo"""
        if usar:
            QApplication.setPalette(QApplication.style().standardPalette())
        else:
            QApplication.setPalette(QApplication.palette())

    def disable_widgets(self, estado):
        """Deshabilita todos los widgets excepto el checkbox"""
        self.container.setEnabled(not estado)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Styles()
    ventana.show()
    sys.exit(app.exec())
