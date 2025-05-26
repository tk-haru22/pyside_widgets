from __future__ import annotations

from PySide6.QtCore import (
    QModelIndex,
    Qt,
    QObject,
    QItemSelectionModel,
    Slot,
    QAbstractItemModel,
)
from PySide6.QtWidgets import (
    QListView,
    QMainWindow,
)



class Item:
    def __init__(self, name: str, id_: int | None = None) -> None:
        self.name = name
        self.parent: Item | None = None
        self.children: list[Item] = []
        self.id = id_

    def add_child(self, child: Item) -> None:
        """ 子アイテムを追加し、親子関係を持たせる """
        self.children.append(child)
        child.parent = self

    def num_children(self) -> None:
        """ 子アイテムの数を得る """
        return len(self.children)

    def child(self, index: int) -> Item | None:
        """
        indexに対応する子アイテムを得る
        index が範囲内であれば self.children[index] と等価
        範囲外なら None
        """
        if 0 <= index < self.num_children():
            return self.children[index]
        return None

    def index(self) -> int:
        """ 親アイテムからみたインデックスを得る """
        if self.parent is None:
            return -1
        return self.parent.index(self)

    def __repr__(self) -> str:
        return f"Item('{self.name}', {self.id})"


class ListModel(QAbstractItemModel):
    def __init__(self, items: list[Item], parent: QObject) -> None:
        super().__init__(parent)
        self.items = items

    def index(self, row: int, column: int, /, parent: QModelIndex = ...) -> QModelIndex:
        # createIndexの第三引数で渡したオブジェクトが internalPointer でとれるオブジェクトになる
        # 例えば self.createIndex(row, column, self.None) にすると
        # Noneが帰ってくる。
        return self.createIndex(row, column, self.items[row])

    def parent(self, index: QModelIndex = ...) -> QModelIndex:
        # ツリーモデルではないので常にルートインデックス
        # 再実装で必ず必要
        return QModelIndex()

    def rowCount(self, /, parent: QModelIndex = ...) ->     int:
        return len(self.items)

    def columnCount(self, /, parent: QModelIndex = ...) -> int:
        # ListViewは 1列しか表示しない
        return 1

    def hasChildren(self, /, parent: QModelIndex = ...) -> bool:
        # ツリーモデルではなく、子は表示しないので
        # ルートインデックスではTrue、有効なインデックスではFalseを返す
        return not self.checkIndex(parent)

    def data(self, index: QModelIndex, /, role: Qt.ItemDataRole = Qt.ItemDataRole.DisplayRole) -> None:
        if not index.isValid():
            return None

        row = index.row()
        item: Item = self.items[row]
        match role:
            case Qt.ItemDataRole.DisplayRole:
                data = item.name
            case Qt.ItemDataRole.ToolTipRole:
                data = str(item.id)
            case _:
                data = None
        return data


class Window(QMainWindow):
    def __init__(self) -> None:
        super().__init__(None)
        self.model = ListModel(create_items(), self)
        self.selmodel = QItemSelectionModel(self.model, self)
        self.list_view = QListView(self)
        self.list_view.setModel(self.model)
        self.list_view.setSelectionModel(self.selmodel)
        self.setCentralWidget(self.list_view)

        self.selmodel.currentChanged.connect(self.on_selection_changed)

    @Slot(QModelIndex, QModelIndex)
    def on_selection_changed(self, current: QModelIndex, previous: QModelIndex) -> None:
        print(current.internalPointer())



def create_items() -> ListModel:
    names = [
        '北海道',
        '青森県',
        '岩手県',
        '宮城県',
        '秋田県',
        '山形県',
        '福島県',
        '茨城県',
        '栃木県',
        '群馬県',
        '埼玉県',
        '千葉県',
        '東京都',
        '神奈川県',
        '山梨県',
        '長野県',
        '新潟県',
        '富山県',
        '石川県',
        '福井県',
        '岐阜県',
        '静岡県',
        '愛知県',
        '三重県',
        '滋賀県',
        '京都府',
        '大阪府',
        '兵庫県',
        '奈良県',
        '和歌山県',
        '鳥取県',
        '島根県',
        '岡山県',
        '広島県',
        '山口県',
        '徳島県',
        '香川県',
        '愛媛県',
        '高知県',
        '福岡県',
        '佐賀県',
        '長崎県',
        '熊本県',
        '大分県',
        '宮崎県',
        '鹿児島県',
        '沖縄県',
    ]

    return [Item(name, i) for i, name in enumerate(names)]



if __name__ == '__main__':
    import sys

    from PySide6.QtWidgets import QApplication

    app = QApplication()
    win = Window()
    win.show()
    sys.exit(app.exec())
