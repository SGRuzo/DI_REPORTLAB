import sys
from PyQt6.QtCore import Qt, QAbstractListModel

class ModeloFollas (QAbstractListModel):
    def __init__(self, follas = None):
        super().__init__()
        self.follas = follas or []


    def data (self, indice, rol):
        if rol == Qt.ItemDataRole.DisplayRole:
            texto = self.follas [indice.row]

    def rowCount(self, indice):
        return len(self.follas)
