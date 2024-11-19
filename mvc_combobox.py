from PySide6.QtGui import (
    QStandardItemModel,
)
from PySide6.QtWidgets import (
    QMainWindow,
    QComboBox,
)


items = [
    'root/parent-item1/child-item1',
    'root/parnet-item1/child-item2',
    'root/parnet-item1/child-item3',
    'root/parnet-item1/child-item4',
    'root/parnet-item1/child-item5',
    'root/parnet-item2/child-item6',
    'root/parnet-item2/child-item7',
    'root/parnet-item2/child-item8',
    'root/parnet-item2/child-item9',
    'root/parnet-item2/child-item10',
    'root/parnet-item3/child-item11',
    'root/parnet-item3/child-item12',
    'root/parnet-item3/child-item13',
]


class Window(QMainWindow):

    def __init__(self, parent = ..., flags = ...):
        super().__init__(parent, flags)
        self.combo1 = QComboBox(self)
        self.combo2 = QComboBox(self)
