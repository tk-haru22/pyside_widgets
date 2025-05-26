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


class TreeModel(QAbstractItemModel):
    def __init__(self, root_item: Item, parent: QObject) -> None:
        super().__init__(parent)
        self.root_item = root_item

    def index(self, row: int, column: int, /, parent: QModelIndex = ...) -> QModelIndex:
        parent_item = self.root_item
        if not parent.isValid():
            parent_item = self.root_item
        if parent.isValid():
            indices: list[QModelIndex] = []
            current = parent
            while current.isValid():
                indices.append(current)
                current = current.parent()
            while indices:
                parent_item = parent_item.child(indices.pop().row())
        return self.createIndex(row, column, parent_item.child(row))
