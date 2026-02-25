# python
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction, QKeySequence
from PyQt6.QtWidgets import (
    QMainWindow, QPushButton, QHBoxLayout, QWidget, QApplication,
    QLabel, QComboBox, QCheckBox, QRadioButton, QGroupBox, QVBoxLayout,
    QTabWidget, QTextEdit, QButtonGroup, QDateTimeEdit, QSlider, QDial,
    QLineEdit, QFileDialog
)


class Styles(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Styles")

        # --- Top row: style selector and toggles ---
        lbl_style = QLabel("Style:")
        self.cmbComboBox = QComboBox()  # NEW: made attribute to connect signals
        self.cmbComboBox.addItems(["Fusion", "Windows", "Macintosh"])
        self.checkBox1 = QCheckBox("Use style's standard palette")  # NEW: attribute
        self.checkBox2 = QCheckBox("Disable widgets")  # NEW: attribute

        h1layout = QHBoxLayout()
        h1layout.addWidget(lbl_style)
        h1layout.addWidget(self.cmbComboBox)
        h1layout.addWidget(self.checkBox1)
        h1layout.addWidget(self.checkBox2)

        # --- Group 1: radios and tri-state checkbox ---
        rboton1 = QRadioButton("Radio button 1")
        rboton2 = QRadioButton("Radio button 2")
        rboton3 = QRadioButton("Radio button 3")
        tri_check = QCheckBox("Tri-state check box")
        tri_check.setTristate(True)

        group1 = QGroupBox("Group 1")
        self.group1 = group1  # NEW: attribute to enable/disable from other widgets
        grupoBotones1 = QButtonGroup(self)
        grupoBotones1.addButton(rboton1)
        grupoBotones1.addButton(rboton2)
        grupoBotones1.addButton(rboton3)
        grupoBotones1.setExclusive(True)

        group1_layout = QVBoxLayout()
        group1_layout.addWidget(rboton1)
        group1_layout.addWidget(rboton2)
        group1_layout.addWidget(rboton3)
        group1_layout.addWidget(tri_check)
        group1.setLayout(group1_layout)

        # --- Group 2: some buttons and reset button ---
        group2 = QGroupBox("Group 2")
        self.group2 = group2  # NEW: attribute
        group2_layout = QVBoxLayout()
        btnon1_normal = QPushButton("Default Push Button")
        btnon2_toggle = QPushButton("Toggle Push Button")
        btnon2_toggle.setCheckable(True)
        btnon3_flat = QPushButton("Flat Push Button")
        btnon3_flat.setFlat(True)
        # NEW: Reset defaults button
        btn_reset = QPushButton("Reset Defaults")
        btn_reset.clicked.connect(self.reset_defaults)  # NEW: connect to reset
        group2_layout.addWidget(btnon1_normal)
        group2_layout.addWidget(btnon2_toggle)
        group2_layout.addWidget(btnon3_flat)
        group2_layout.addWidget(btn_reset)  # NEW
        group2.setLayout(group2_layout)

        # Horizontal layout for group1 and group2
        h_groups = QHBoxLayout()
        h_groups.addWidget(group1)
        h_groups.addWidget(group2)

        # --- Tabbed area: table placeholder and text edit with save/load ---
        tabbed_stack = QTabWidget()
        tabbed_stack.addTab(QWidget(), "Table")

        # NEW: make txtAreaTexto an attribute and add Save/Load controls in its tab
        self.txtAreaTexto = QTextEdit()
        text_tab = QWidget()  # NEW
        text_tab_layout = QVBoxLayout()  # NEW
        text_tab_layout.addWidget(self.txtAreaTexto)  # NEW

        # NEW: Save and Load buttons for text tab
        h_text_buttons = QHBoxLayout()  # NEW
        btn_save = QPushButton("Save Text")  # NEW
        btn_save.clicked.connect(self.save_text)  # NEW
        btn_load = QPushButton("Load Text")  # NEW
        btn_load.clicked.connect(self.load_text)  # NEW
        h_text_buttons.addWidget(btn_save)  # NEW
        h_text_buttons.addWidget(btn_load)  # NEW
        text_tab_layout.addLayout(h_text_buttons)  # NEW

        text_tab.setLayout(text_tab_layout)  # NEW
        tabbed_stack.addTab(text_tab, "Text Edit")  # replace the previous QTextEdit tab with the composed tab

        # --- Group 3: password field, datetime, slider and dial ---
        self.text7 = QLineEdit()  # NEW: attribute
        self.text7.setEchoMode(QLineEdit.EchoMode.Password)  # password hidden by default

        # NEW: checkbox to toggle password visibility
        chk_show_pass = QCheckBox("Show password")  # NEW
        chk_show_pass.toggled.connect(self.toggle_password_visibility)  # NEW

        datatimer = QDateTimeEdit()
        self.slider = QSlider(Qt.Orientation.Horizontal)  # NEW: attribute
        self.dial = QDial()  # NEW: attribute

        # NEW: connect slider and dial to status updates
        self.slider.valueChanged.connect(self.update_slider_status)  # NEW
        self.dial.valueChanged.connect(self.update_dial_status)  # NEW

        group3 = QGroupBox("Group 3")
        group3_layout = QVBoxLayout()
        group3_layout.addWidget(self.text7)
        group3_layout.addWidget(chk_show_pass)  # NEW
        group3_layout.addWidget(datatimer)
        group3_layout.addWidget(self.slider)
        group3_layout.addWidget(self.dial)
        group3.setLayout(group3_layout)

        h2_layout = QHBoxLayout()
        h2_layout.addWidget(tabbed_stack)
        h2_layout.addWidget(group3)

        layout_vertical = QVBoxLayout()
        layout_vertical.addLayout(h1layout)
        layout_vertical.addLayout(h_groups)
        layout_vertical.addLayout(h2_layout)

        container = QWidget()
        container.setLayout(layout_vertical)
        self.setCentralWidget(container)

        # --- NEW: Status bar and initial message ---
        self.statusBar().showMessage("Ready")  # NEW

        # --- NEW: Signal connections for top controls ---
        self.cmbComboBox.currentTextChanged.connect(self.change_style)  # NEW
        self.checkBox1.toggled.connect(self.toggle_standard_palette)  # NEW
        self.checkBox2.toggled.connect(self.toggle_disable_groups)  # NEW

        # --- NEW: Shortcut for reset (Ctrl+R) ---
        reset_action = QAction(self)
        reset_action.setShortcut(QKeySequence("Ctrl+R"))
        reset_action.triggered.connect(self.reset_defaults)
        self.addAction(reset_action)

    # --- NEW: Methods added below ---

    def change_style(self, style_name: str):
        """Change application style and update status bar."""
        app = QApplication.instance()
        style = None
        if app:
            from PyQt6.QtWidgets import QStyleFactory
            style = QStyleFactory.create(style_name)
        if style and app:
            app.setStyle(style)
            # If standard palette checkbox is checked, apply it after style change
            if getattr(self, "checkBox1", None) and self.checkBox1.isChecked():
                app.setPalette(app.style().standardPalette())
            self.statusBar().showMessage(f"Style: {style_name}")  # NEW

    def toggle_standard_palette(self, checked: bool):
        """Apply or clear the style's standard palette."""
        app = QApplication.instance()
        if not app:
            return
        if checked:
            app.setPalette(app.style().standardPalette())
            self.statusBar().showMessage("Standard palette applied")  # NEW
        else:
            app.setPalette(QApplication.palette(self))  # restore to default-ish
            self.statusBar().showMessage("Custom palette (cleared)")  # NEW

    def toggle_disable_groups(self, disabled: bool):
        """Disable/enable the main groups but keep top controls active."""
        # Keep combo and checkboxes enabled so user can change them
        # Disable the group widgets themselves
        if getattr(self, "group1", None):
            self.group1.setDisabled(disabled)
        if getattr(self, "group2", None):
            self.group2.setDisabled(disabled)
        self.statusBar().showMessage("Widgets disabled" if disabled else "Widgets enabled")  # NEW

    def toggle_password_visibility(self, visible: bool):
        """Toggle password echo mode for text7."""
        if visible:
            self.text7.setEchoMode(QLineEdit.EchoMode.Normal)
            self.statusBar().showMessage("Password visible")  # NEW
        else:
            self.text7.setEchoMode(QLineEdit.EchoMode.Password)
            self.statusBar().showMessage("Password hidden")  # NEW

    def update_slider_status(self, value: int):
        """Update status bar with slider value."""
        self.statusBar().showMessage(f"Slider: {value}")  # NEW

    def update_dial_status(self, value: int):
        """Update status bar with dial value."""
        self.statusBar().showMessage(f"Dial: {value}")  # NEW

    def reset_defaults(self):
        """Restore sensible defaults for the UI (connected to Reset button and Ctrl+R)."""
        # Reset style to Fusion (common default)
        self.cmbComboBox.setCurrentText("Fusion")
        # Uncheck palette checkbox
        self.checkBox1.setChecked(False)
        # Enable groups
        self.checkBox2.setChecked(False)
        # Hide password
        self.text7.setEchoMode(QLineEdit.EchoMode.Password)
        # Reset slider and dial to 0
        self.slider.setValue(0)
        self.dial.setValue(0)
        # Clear text area
        self.txtAreaTexto.clear()
        self.statusBar().showMessage("Defaults restored")  # NEW

    def save_text(self):
        """Save text from the text edit to a file (file dialog)."""
        fname, _ = QFileDialog.getSaveFileName(self, "Save Text", "", "Text Files (*.txt);;All Files (*)")
        if fname:
            try:
                with open(fname, "w", encoding="utf-8") as f:
                    f.write(self.txtAreaTexto.toPlainText())
                self.statusBar().showMessage(f"Saved to {fname}")
            except Exception as e:
                self.statusBar().showMessage(f"Save failed: {e}")

    def load_text(self):
        """Load text into the text edit from a file (file dialog)."""
        fname, _ = QFileDialog.getOpenFileName(self, "Open Text", "", "Text Files (*.txt);;All Files (*)")
        if fname:
            try:
                with open(fname, "r", encoding="utf-8") as f:
                    self.txtAreaTexto.setPlainText(f.read())
                self.statusBar().showMessage(f"Loaded from {fname}")
            except Exception as e:
                self.statusBar().showMessage(f"Load failed: {e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Styles()
    ventana.show()
    sys.exit(app.exec())