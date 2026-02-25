import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QVBoxLayout, QLineEdit, QListView
)
from PyQt6.QtCore import QStringListModel, QSortFilterProxyModel, Qt


class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Filtro de nomes con QSortFilterProxyModel")

        layout = QVBoxLayout()

        # --- Cadro de busca ---
        self.cadro_busca = QLineEdit()
        self.cadro_busca.setPlaceholderText("Busca un nome…")
        self.cadro_busca.textChanged.connect(self.actualizar_filtro)

        # --- Modelo base con nomes ---
        nomes = [
            "Ana", "Brais", "Carlos", "Diana", "Elena",
            "Fernando", "Gabriel", "Helena", "Iria", "Javier",
            "Karla", "Lucas", "Miriam", "Noa", "Oscar",
            "Paula", "Quintín", "Raquel", "Sergio", "Tamara"
        ]

        self.modelo = QStringListModel(nomes)

        # --- Proxy para filtrar ---
        self.proxy = QSortFilterProxyModel()
        self.proxy.setSourceModel(self.modelo)
        self.proxy.setFilterCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive) # sen distinguir maiúsculas
        self.proxy.setFilterKeyColumn(0)  # única columna

        # --- Lista visual ---
        self.lista_view = QListView()
        self.lista_view.setModel(self.proxy)

        # Engadir ao layout
        layout.addWidget(self.cadro_busca)
        layout.addWidget(self.lista_view)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def actualizar_filtro(self, texto):
        """Actualiza o filtro en tempo real."""
        self.proxy.setFilterFixedString(texto)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())
