from PyQt6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, QWidget, QPlainTextEdit,
                             QComboBox, QSpinBox, QPushButton, QCheckBox, QLineEdit)
import sys

class Fiestra(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exemplo con QSS")

        caixaV = QVBoxLayout()

        self.pteEditor = QPlainTextEdit()
        self.pteEditor.textChanged.connect(self.on_pteEditor_textChanged)
        caixaV.addWidget(self.pteEditor)

        """
        QLineEdit{background-color:yellow;
border: 10px solid red;
border-color: red;
}"""

        chkOpcion = QCheckBox("Opcions")
        caixaV.addWidget(chkOpcion)

        cmbcombo = QComboBox()
        cmbcombo.setObjectName("oCombo")
        cmbcombo.addItems(["Un", "Dous", "Tres", "Catro"])
        caixaV.addWidget(cmbcombo)

        sbpSpin = QSpinBox()
        sbpSpin.setRange(0, 9999)
        caixaV.addWidget(sbpSpin)

        self.txtTexto = QLineEdit()
        self.txtTexto.setObjectName("editorTxt")
        self.txtTexto.textChanged.connect(self.on_txtTexto_textChanged)

        caixaV.addWidget(self.txtTexto)

        btnBoton = QPushButton("Pulsa")
        caixaV.addWidget(btnBoton)

        container = QWidget()
        container.setLayout(caixaV)
        self.setCentralWidget(container)

        self.show()

    def on_pteEditor_textChanged(self):
        qss = self.pteEditor.toPlainText()
        self.setStyleSheet(qss)

    def on_txtTexto_textChanged(self):
        longitud = len(self.txtTexto.text())
        if longitud <= 6:
            self.txtTexto.setStyleSheet("QLineEdit {background-color: rgb(120, 0, 0);}")
        elif longitud > 6 and longitud <= 10:
            self.txtTexto.setStyleSheet("QLineEdit {background-color: rgb(255, 191, 0);}")
        elif longitud > 10:
            self.txtTexto.setStyleSheet("QLineEdit {background-color: rgb(0, 120, 0);}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    fiestra = Fiestra()
    app.exec()