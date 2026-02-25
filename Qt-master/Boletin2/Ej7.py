import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QVBoxLayout, QLineEdit, QTextEdit, QLabel
)


class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Filtro de nomes")

        layout = QVBoxLayout()

        # --- Cadro de busca ---
        self.cadro_busca = QLineEdit()
        self.cadro_busca.setPlaceholderText("Busca un nome…")
        self.cadro_busca.textChanged.connect(self.filtrar)

        # --- Lista multiliña ---
        self.lista_nomes_widget = QTextEdit()
        self.lista_nomes_widget.setReadOnly(True)

        # Modelo base (20 nomes)
        self.lista_nomes = [
            "Ana", "Brais", "Carlos", "Diana", "Elena",
            "Fernando", "Gabriel", "Helena", "Iria", "Javier",
            "Karla", "Lucas", "Miriam", "Noa", "Oscar",
            "Paula", "Quintín", "Raquel", "Sergio", "Tamara"
        ]

        # Amosar todo ao comezo
        self.mostrar_todo()

        layout.addWidget(self.cadro_busca)
        layout.addWidget(self.lista_nomes_widget)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def mostrar_todo(self):
        """Mostra a lista completa no QTextEdit."""
        texto = "\n".join(self.lista_nomes)
        self.lista_nomes_widget.setPlainText(texto)

    def filtrar(self):
        """Filtra os nomes en tempo real (case-insensitive)."""
        termo = self.cadro_busca.text().lower()

        if termo == "":
            self.mostrar_todo()
            return

        nomes_filtrados = [
            nome for nome in self.lista_nomes
            if termo in nome.lower()
        ]

        self.lista_nomes_widget.setPlainText("\n".join(nomes_filtrados))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())
