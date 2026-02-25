import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout,
    QStackedLayout, QRadioButton, QCheckBox, QLabel, QLineEdit, QMainWindow
)
from PyQt6.QtGui import QColor, QPalette
""""
Deseña unha interface que permita ao usuario introducir o seu ano de nacemento nun cadro de texto e,
ao premer un botón “Calcular idade”, amose a súa idade nunha etiqueta. Validar que a entrada sexa un número.
Se o usuario introduce un ano non válido (ex: 3000), amosar unha mensaxe de erro nunha etiqueta en vermello.
Engade un botón “Limpar” que borre o cadro de texto e a etiqueta de resultado.as
"""
#Funcion que calcule la edad
# que valide si es un año valido
#boton de borrar

class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ej4 Boletin2")

        # --- Layout principal ---
        layout_principal = QVBoxLayout()

        self.cadro_texto = QLineEdit()
        #cadro_texto.setText("Introduce o teu ano de nacemento")
        lbl_contraseña = QLabel("Introduce tu año de nacimiento:")
        self.lbl_resultado = QLabel("Resultado:" )
        self.btn_calcular = QPushButton("Calcular idade")
        self.btn_borrar = QPushButton("Limpar")

        self.btn_calcular.clicked.connect(self.on_btn_clicked_calcular_idade)
        self.btn_borrar.clicked.connect(self.on_btn_clicked_limpiar)

        layout_principal.addWidget(lbl_contraseña)
        layout_principal.addWidget(self.cadro_texto)
        layout_principal.addWidget(self.btn_calcular)
        layout_principal.addWidget(self.btn_borrar)
        layout_principal.addWidget(self.lbl_resultado)



        container = QWidget()
        container.setLayout(layout_principal)
        self.setCentralWidget(container)

    def on_btn_clicked_calcular_idade(self):
        ano_nacemento = int(self.cadro_texto.text())
        print(type(ano_nacemento))
        if ano_nacemento < 1900 or ano_nacemento > 2025:
            self.lbl_resultado.setStyleSheet("color: red")
            self.lbl_resultado.setText("Introduce un año válido (1900-2025)")

        else:
            self.lbl_resultado.setText(f"Tienes: {2025 - ano_nacemento}")

    def on_btn_clicked_limpiar(self):
        self.cadro_texto.clear()
        self.lbl_resultado.clear()








if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())