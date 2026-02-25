# python
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QMainWindow, QPushButton, QHBoxLayout, QWidget, QApplication,
    QLabel, QComboBox, QCheckBox, QRadioButton, QGroupBox, QVBoxLayout,
    QTabWidget, QTextEdit, QButtonGroup, QDateTimeEdit, QSlider, QDial, QLineEdit
)


class Styles(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Styles")

        lbl_style = QLabel("Style:")
        cmbComboBox = QComboBox()
        cmbComboBox.addItems(["Fusion", "Windows", "Macintosh"])
        checkBox1 = QCheckBox("Use style's standard palette")
        checkBox2 = QCheckBox("Disable widgets")

        h1layout = QHBoxLayout()
        h1layout.addWidget(lbl_style)
        h1layout.addWidget(cmbComboBox)
        h1layout.addWidget(checkBox1)
        h1layout.addWidget(checkBox2)

        rboton1 = QRadioButton("Radio button 1")
        rboton2 = QRadioButton("Radio button 2")
        rboton3 = QRadioButton("Radio button 3")
        tri_check = QCheckBox("Tri-state check box")
        tri_check.setTristate(True)  # Set the checkbox to be tri-state

        group1 = QGroupBox("Group 1")
        grupoBotones1 = QButtonGroup(self)
        # Only add radio buttons to the exclusive group
        grupoBotones1.addButton(rboton1)
        grupoBotones1.addButton(rboton2)
        grupoBotones1.addButton(rboton3)
        grupoBotones1.setExclusive(True)

        group1_layout = QVBoxLayout()
        group1_layout.addWidget(rboton1)
        group1_layout.addWidget(rboton2)
        group1_layout.addWidget(rboton3)
        # tri_check is kept in the group layout but not in the exclusive button group
        group1_layout.addWidget(tri_check)
        group1.setLayout(group1_layout)

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

        # Horizontal layout for group1 and group2
        h_groups = QHBoxLayout()
        h_groups.addWidget(group1)
        h_groups.addWidget(group2)

        tabbed_stack = QTabWidget()
        txtAreaTexto = QTextEdit()
        tabbed_stack.addTab(QWidget(), "Table")
        tabbed_stack.addTab(txtAreaTexto, "Text Edit")

        text7 = QLineEdit()
        text7.setEchoMode(QLineEdit.EchoMode.Password)  # PasswordEchoOnEdit

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

        h2_layout = QHBoxLayout()
        h2_layout.addWidget(tabbed_stack)
        h2_layout.addWidget(group3)

        layout_vertical = QVBoxLayout()
        layout_vertical.addLayout(h1layout)
        layout_vertical.addLayout(h_groups)
        # cmbComboBox is already in h1layout; do not add it again here
        layout_vertical.addLayout(h2_layout)

        container = QWidget()
        container.setLayout(layout_vertical)
        self.setCentralWidget(container)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Styles()
    ventana.show()
    sys.exit(app.exec())