import sys

from PyQt6.QtWidgets import (
    QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QMainWindow, QLineEdit, QTextEdit
)


class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ej5 Boletín2")

        # --- Layout principal ---
        layout_principal = QVBoxLayout()

        self.cuadro_none = QLineEdit()
        self.cuadro_none.setPlaceholderText("Introduce tu nombre")
        self.cadro_email = QLineEdit()
        self.cadro_email.setPlaceholderText("Introduce tu email")
        self.cuadroMultilinea_mensaxe = QTextEdit()
        self.cuadroMultilinea_mensaxe.setPlaceholderText("Escribe tu mensaje aquí...")
        btn_enviar = QPushButton("Enviar")
        self.lbl_resultado = QLabel()

        btn_enviar.clicked.connect(self.on_btn_clicked_enviar)

        layout_principal.addWidget(self.cuadro_none)
        layout_principal.addWidget(self.cadro_email)
        layout_principal.addWidget(self.cuadroMultilinea_mensaxe)
        layout_principal.addWidget(btn_enviar)
        layout_principal.addWidget(self.lbl_resultado)





        container = QWidget()
        container.setLayout(layout_principal)
        self.setCentralWidget(container)


    def on_btn_clicked_enviar(self):
        if self.cuadro_none.text() == "" or self.cuadro_email.text() == "" or self.cuadroMultilinea_mensaxe.toPlainText() == "":
            self.lbl_resultado.setStyleSheet("color: red")
            self.lbl_resultado.setText("Faltan datos. Completa todos os campos.")
        else:
            self.lbl_resultado.setText("Formulario enviado correctamente.")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())
