"""
Crea unha táboa que amose os seguintes datos (simulados):

Ana López     Vigo       ✅
Carlos R.     Santiago   ❌
María G.      A Coruña   ✅

Usa QStandardItemModel para poboar a táboa.
Os campos “Activo” deben ser QCheckBox (setCheckable(True)).
Engade un botón “Mostrar só activos”.
"""

import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QPushButton, QTableView
)
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtCore import Qt



class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Táboa de usuarios")

        layout = QVBoxLayout()

        # --- TÁBOA ---
        self.tabla = QTableView()
        layout.addWidget(self.tabla)

        # --- BOTÓN ---
        btn_filtrar = QPushButton("Mostrar só activos")
        btn_filtrar.clicked.connect(self.filtrar_activos)
        layout.addWidget(btn_filtrar)

        # Modelo de datos
        self.modelo = QStandardItemModel()
        self.modelo.setHorizontalHeaderLabels(["Nome", "Cidade", "Activo"])

        # Datos simulados
        datos = [
            ("Ana López", "Vigo", True),
            ("Carlos R.", "Santiago", False),
            ("María G.", "A Coruña", True)
        ]

        # Engadir filas ao modelo
        for nome, cidade, activo in datos:
            item_nome = QStandardItem(nome)
            item_cidade = QStandardItem(cidade)

            item_activo = QStandardItem()
            item_activo.setCheckable(True)
            # Marcamos o checkbox según o valor
            if activo:
                item_activo.setCheckState(Qt.CheckState.Checked)
            else:
                item_activo.setCheckState(Qt.CheckState.Unchecked)

            self.modelo.appendRow([item_nome, item_cidade, item_activo])

        self.tabla.setModel(self.modelo)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def filtrar_activos(self):
        """Mostrar só filas onde o checkbox está marcado"""
        for fila in range(self.modelo.rowCount()):
            activo_item = self.modelo.item(fila, 2)
            activo = activo_item.checkState() == Qt.CheckState.Checked

            # Amosar/ocultar fila
            self.tabla.setRowHidden(fila, not activo)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())
