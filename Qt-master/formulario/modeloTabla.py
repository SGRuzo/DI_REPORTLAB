from PyQt6 import QtGui
from PyQt6.QtCore import Qt, QAbstractTableModel

class ModeloTabla(QAbstractTableModel):
    def __init__(self, taboa):
        super().__init__()
        self. taboa = taboa


    def rowCount(self, indice):
        return len(self.taboa)

    def columnCount(self, indice):
        return len(self.taboa[0]) if len(self.taboa) !=0 else 0

    def data(self, indice, rol):
        if rol == Qt.ItemDataRole.DisplayRole:
            return str(self.taboa[indice.row()][indice.column()])
        if rol == Qt.ItemDataRole.BackgroundRole:
            if self.taboa[indice.row()][2] == "Masculino":
                return QtGui.QColor ("lightblue")
            elif self.taboa[indice.row()][2] == "Feminino":
                return QtGui.QColor ("lightpink")

