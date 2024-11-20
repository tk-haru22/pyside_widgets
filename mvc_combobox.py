from PySide6.QtGui import (
    QStandardItemModel,
    QStandardItem,
)
from PySide6.QtWidgets import (
    QMainWindow,
    QComboBox,
    QTreeView,
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
        self.model = QStandardItemModel(self)
        self.view = QTreeView(self)

        self.setup_model()
        self.view.setModel(self.model)
        self.combo1.setModel(self.model)
        self.combo1.setRootModelIndex(self.root_index)

    def setup_model(self):
        root_item = QStandardItem('root')
        parents = [
            QStandardItem('parent-item1'),
            QStandardItem('parent-item2'),
            QStandardItem('parent-item3'),
        ]
        root_item.appendRow(parents)
        child1 = [
            QStandardItem('child-item1'),
            QStandardItem('child-item2'),
            QStandardItem('child-item3'),
            QStandardItem('child-item4'),
            QStandardItem('child-item5'),
        ]
        parents[0].appendRow(child1)
        child2 = [
            QStandardItem('child-item6'),
            QStandardItem('child-item7'),
            QStandardItem('child-item8'),
            QStandardItem('child-item9'),
            QStandardItem('child-item10'),
        ]
        parents[1].appendRow(child2)
        child3 = [
            QStandardItem('child-item11'),
            QStandardItem('child-item12'),
            QStandardItem('child-item13'),
        ]
        parents[2].appendRow(child3)
        self.model.appendRow(root_item)
        
        self.root_index = root_item.index()
