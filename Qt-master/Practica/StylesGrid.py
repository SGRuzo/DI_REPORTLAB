import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QMainWindow, QPushButton, QHBoxLayout, QWidget, QApplication,
    QLabel, QComboBox, QCheckBox, QRadioButton, QGroupBox, QVBoxLayout,
    QTabWidget, QTextEdit, QButtonGroup, QDateTimeEdit, QSlider, QDial, QLineEdit,
    QGridLayout
)


class Styles(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Styles (Grid Version)")

        # -------------------------
        #   FILA 0 - STYLE OPTIONS
        # -------------------------
        lbl_style = QLabel("Style:")
        cmbComboBox = QComboBox()
        cmbComboBox.addItems(["Fusion", "Windows", "Macintosh"])
        checkBox1 = QCheckBox("Use style's standard palette")
        checkBox2 = QCheckBox("Disable widgets")

        # -------------------------
        #   GROUP 1
        # -------------------------
        rboton1 = QRadioButton("Radio button 1")
        rboton2 = QRadioButton("Radio button 2")
        rboton3 = QRadioButton("Radio button 3")
        tri_check = QCheckBox("Tri-state check box")
        tri_check.setTristate(True)

        grupoBotones1 = QButtonGroup(self)
        grupoBotones1.addButton(rboton1)
        grupoBotones1.addButton(rboton2)
        grupoBotones1.addButton(rboton3)
        grupoBotones1.addButton(tri_check)
        grupoBotones1.setExclusive(True)

        group1 = QGroupBox("Group 1")
        group1_layout = QVBoxLayout()
        group1_layout.addWidget(rboton1)
        group1_layout.addWidget(rboton2)
        group1_layout.addWidget(rboton3)
        group1_layout.addWidget(tri_check)
        group1.setLayout(group1_layout)

        # -------------------------
        #   GROUP 2
        # -------------------------
        group2 = QGroupBox("Group 2")
        group2_layout = QVBoxLayout()
        btnon1_normal = QPushButton("Default Push Button")
        btnon2_toggle = QPushButton("Toggle Push Button")
        btnon2_toggle.setCheckable(True)
        btnon3_flat = QPushButton("Flat Push Button")
        btnon3_flat.setFlat(True)

        group2_layout.addWidget(btnon1_normal)
        group2_layout.addWidget(btnon2_toggle)
        group2_layout.addWidget(btnon3_flat)
        group2.setLayout(group2_layout)

        # -------------------------
        #   TABS + GROUP 3
        # -------------------------
        tabbed_stack = QTabWidget()
        txtAreaTexto = QTextEdit()
        tabbed_stack.addTab(QWidget(), "Table")
        tabbed_stack.addTab(txtAreaTexto, "Text Edit")

        text7 = QLineEdit()
        text7.setEchoMode(QLineEdit.EchoMode.Password)

        datatimer = QDateTimeEdit()
        slider = QSlider(Qt.Orientation.Horizontal)
        dial = QDial()

        group3 = QGroupBox("Group 3")
        group3_layout = QVBoxLayout()
        group3_layout.addWidget(text7)
        group3_layout.addWidget(datatimer)
        group3_layout.addWidget(slider)
        group3_layout.addWidget(dial)
        group3.setLayout(group3_layout)

        # -------------------------
        #   GRID PRINCIPAL
        # -------------------------

        grid = QGridLayout()
        grid.setSpacing(15)

        # Fila 0 - Opciones de estilo
        grid.addWidget(lbl_style,      0, 0)
        grid.addWidget(cmbComboBox,    0, 1)
        grid.addWidget(checkBox1,      0, 2)
        grid.addWidget(checkBox2,      0, 3)

        # Fila 1 - Group 1 y Group 2
        grid.addWidget(group1, 1, 0, 1, 2)
        grid.addWidget(group2, 1, 2, 1, 2)

        # Fila 2 - Tabs y Group 3
        grid.addWidget(tabbed_stack, 2, 0, 1, 3)
        grid.addWidget(group3,       2, 3)

        container = QWidget()
        container.setLayout(grid)
        self.setCentralWidget(container)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Styles()
    ventana.show()
    sys.exit(app.exec())
