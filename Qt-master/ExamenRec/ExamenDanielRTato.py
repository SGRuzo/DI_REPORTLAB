import sys
from selectors import SelectSelector

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (QApplication, QMainWindow, QGridLayout, QVBoxLayout, QHBoxLayout, QWidget,
                             QLabel, QListWidget, QPushButton, QComboBox, QLineEdit,
                             QRadioButton, QGroupBox, QTableView, QAbstractItemView, QTabWidget, QCheckBox, QSlider,
                             QTextEdit)


class FiestraPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exame 24-11-2025")

        layout_principal = QHBoxLayout()
        grid = QGridLayout()

        self.lista = ["Semanal", "Diario"]

        #tabs = QTabWidget()
        #tabs.addTab("Configuración Zoa 1")
        #tabs.addTab("Configuración Zoa 2")
        #tabs.addTab("Consola")
        #layout_principal.addWidget(tabs)

         # Elementos da pestana de configuración

        lblZoaActivada = QLabel("Zoa activada")
        self.tx_consola = QTextEdit()


        self.chkZoaActivada = QCheckBox()
        self.chkZoaActivada.stateChanged.connect(self.zonaActiva_toggled)

        lblHoraComezoRego = QLabel("Hora de comezo de rego")

        self.txtHoraComezoRego = QLineEdit()
        self.txtHoraComezoRego.textChanged.connect(self.valdiarHora)


        lblDuracionRego = QLabel("Duración rego")

        self.sldDuracionRego = QSlider(Qt.Orientation.Horizontal)
        self.sldDuracionRego.setRange(0, 600)
        self.sldDuracionRego.valueChanged.connect(self.mover_barra)


        self.cmbDiario = QComboBox()
        self.cmbDiario.addItems(self.lista)
        self.cmbDiario.currentIndexChanged.connect(self.mostrarSemanalmensal)

        chkAntixiada = QCheckBox("Antixiada")
        chkChuvia = QCheckBox("Chuvia")

        chkLuns = QCheckBox("Luns")
        chkMartes = QCheckBox("Martes")
        chkMercores = QCheckBox("Mércores")
        chkXoves = QCheckBox("Xoves")
        chkVenres = QCheckBox("Venres")
        chkSabado = QCheckBox("Sábado")
        chkDomingo = QCheckBox("Domingo")

        btnAceptar = QPushButton("Aceptar")


        grid.addWidget(lblZoaActivada,0,0)
        grid.addWidget(self.chkZoaActivada, 0, 1)
        grid.addWidget(lblHoraComezoRego, 1, 0)
        grid.addWidget(self.txtHoraComezoRego, 1, 1)
        grid.addWidget(lblDuracionRego, 2, 0)
        grid.addWidget(self.sldDuracionRego, 2, 1)

        gpbOpcions = QGroupBox("Opcións")
        layout_opcions = QHBoxLayout()
        layout_opcions.addWidget(self.cmbDiario)
        layout_opcions.addWidget(chkAntixiada)
        layout_opcions.addWidget(chkChuvia)
        gpbOpcions.setLayout(layout_opcions)


        layout_zonaIz = QVBoxLayout()
        layout_zonaIz.addLayout(grid)
        layout_zonaIz.addWidget(gpbOpcions)

        layout_principal.addLayout(layout_zonaIz)

        gpbDias = QGroupBox("Días")
        grid_dias = QGridLayout()
        grid_dias.addWidget(chkLuns, 0, 0)
        grid_dias.addWidget(chkMartes, 0, 1)
        grid_dias.addWidget(chkMercores, 1, 0)
        grid_dias.addWidget(chkXoves, 1, 1)
        grid_dias.addWidget(chkVenres, 2, 0)
        grid_dias.addWidget(chkSabado, 2, 1)
        grid_dias.addWidget(chkDomingo, 3, 0)
        gpbDias.setLayout(grid_dias)
        layout_principal.addWidget(gpbDias)

        layout_principal.addWidget(self.tx_consola)


        laya = QVBoxLayout()
        tabs = QTabWidget()
        tab1 = QTabWidget()
        tab2 = QTabWidget()
        tab3 = QTabWidget()
        tabs.addTab(tab1,"Configuracion Zoa1")
        tabs.addTab(tab2,"Configuracion Zoa 2")
        tabs.addTab(tab3,"Consola")
        tab3.setLayout(laya)

        layout_principal.addWidget(tabs)



        container = QWidget()
        container.setLayout(layout_principal)
        self.setCentralWidget(container)


    def zonaActiva_toggled(self, estado):
        text = "Zoa activada"
        if  self.chkZoaActivada.stateChanged:
            self.tx_consola.append(text)

        else:
            self.tx_consola.setText("Zoa desactivada")

    def mover_barra(self, valor):
        self.tx_consola.setText(f"Duración rego {valor} minutos")

    def mostrarSemanalmensal(self):
        if self.cmbDiario.currentIndex() < 0:
            return

        text = self.cmbDiario.currentText()
        mensaje = f"Estado cambiado a: {text}"
        self.tx_consola.append(mensaje)

    def valdiarHora(self):
        hora = self.txtHoraComezoRego.text()

        self.tx_consola.append(hora)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = FiestraPrincipal()
    ventana.show()
    sys.exit(app.exec())