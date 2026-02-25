import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (QApplication, QMainWindow, QGridLayout, QVBoxLayout, QHBoxLayout, QWidget,
                             QLabel, QListWidget, QPushButton, QComboBox, QLineEdit,
                             QRadioButton, QGroupBox, QTableView, QAbstractItemView, QTabWidget, QCheckBox, QSlider)

class InterfazAvanzada(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tabs y Splitters")
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        #QSplitter, divisor principal horizontal
        self.main_splitter = QSlider(Qt.Horizontal)

        #Panel izquierdo, control
        control_panel = QGroupBox("Panel de control")
        control_layout = QVBoxLayout(control_panel)

        control_layout.addWidget(QLabel("Lista de opciones:"))
        control_layout.addWidget(QListWidget())
        control_layout.addWidget(QPushButton("Aplicar cambios"))
        control_layout.addStretch()

        self.main_splitter.addWidget(control_panel)


        #Panel derecho QTabWidget

        self.tab_contenedor = QTabWidget()

        #Pestaña 1:
        vista_general = QWidget()
        layout_general = QVBoxLayout(vista_general)
        layout_general.addWidget(QLabel("Contenido de viste general"))


        # Pestaña 2
        consola_panel = QWidget()
        layout_consola = QVBoxLayout(consola_panel)
        layout_consola.addWidget(QLabel("Consola de mensajes:"))
        layout_consola.addWidget(QListWidget())

        # Añadir las pestañas al QTabWidget
        self.tab_contenedor.addTab(vista_general, "General")
        self.tab_contenedor.addTab(consola_panel, "Consola")

        self.main_splitter.addWidget(self.tab_contenedor)

        # Configurar tamaños iniciales del Splitter
        self.main_splitter.setSizes([200, 600])

        main_layout.addWidget(self.main_splitter)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InterfazAvanzada()
    window.show()
    sys.exit(app.exec())