import sys

from PySide6.QtCore import Qt, QMimeData
from PySide6.QtGui import (
    QDragEnterEvent,
    QDropEvent,
    QMouseEvent,
    QDrag,
    QPixmap,
)
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QGridLayout,
    QFrame,
    QLabel,
    QLineEdit,
    QVBoxLayout,
)



css = """
QFrame#drag0 {
    background-color: lightpink;
    border: solid;
    border-width: 0px 0px 1px 0px;
}
QFrame#drag1 {
    background-color: palegreen;
    border: solid;
    border-width: 0px 0px 1px 0px;
}
QFrame#drag2 {
    background-color: lightcyan;
    border: solid;
    border-width: 0px 0px 1px 0px;
}
"""


class SortableWidget(QWidget):

    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.setWindowTitle('Sortable widget')
        self.setAcceptDrops(True)
        self.setObjectName('SortableWidget')
        self._layout = QVBoxLayout(self)
        self._layout.addWidget(DraggableWidget(0, self))
        self._layout.addWidget(DraggableWidget(1, self))
        self._layout.addWidget(DraggableWidget(2, self))

    def dragEnterEvent(self, event: QDragEnterEvent) -> None:
        event.accept()

    def dropEvent(self, event: QDropEvent) -> None:
        widget = event.source()

        pos = event.position()
        spacing = self._layout.spacing() / 2
        for n in range(self._layout.count()):
            w = self._layout.itemAt(n).widget()
            if (w.y() - spacing <= pos.y()
                    and pos.y() <= w.y() + w.size().height() +spacing):
                break

        if 0 <= n < self._layout.count():
            self._layout.insertWidget(n, widget)
        event.accept()


class DraggableWidget(QFrame):

    def __init__(self, id_, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.id_ = id_
        self.setObjectName(f'drag{id_}')
        self._create_layout()

    def _create_layout(self):
        layout = QGridLayout(self)
        layout.addWidget(QLabel(f'Draggable widget {self.id_}'), 0, 0)
        layout.addWidget(QLineEdit(self), 0, 1)

    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        if event.buttons() == Qt.LeftButton:
            drag = QDrag(self)
            mime = QMimeData()
            drag.setMimeData(mime)

            pixmap = QPixmap(self.size())
            self.render(pixmap)
            drag.setPixmap(pixmap)

            drag.exec(Qt.MoveAction)
            self.show()



if __name__ == '__main__':
    app = QApplication()
    app.setStyleSheet(css)
    win = SortableWidget()
    win.show()
    sys.exit(app.exec())
