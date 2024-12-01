import sys

from PySide6.QtCore import (
    Slot,
    Qt,
)
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QSizePolicy,
    QToolButton,
    QVBoxLayout,
    QWidget,
)


class Window(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Collaplible widget')
        self.setCentralWidget(QWidget(self))

        self.create_widget()
        self.create_layout()
        self.create_connections()

        self.header.setChecked(True)
        self.header.clicked.emit()

    def create_widget(self):
        self.header = QToolButton(self)
        self.header.setText('Collasible widget')
        self.header.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.header.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.header.setCheckable(True)
        self.body = QWidget(self)
        self.contents = QPushButton('Button')

    def create_layout(self):
        layout = QVBoxLayout(self.centralWidget())
        layout.addWidget(self.header)
        layout.addWidget(self.body)
        content_layout = QVBoxLayout(self.body)
        content_layout.setContentsMargins(0, 0, 0, 0)
        content_layout.addWidget(self.contents)
        layout.addStretch()

    def create_connections(self):
        self.header.clicked.connect(self.on_header_clicked)

    @Slot()
    def on_header_clicked(self):
        state = self.header.isChecked()
        if state:
            self.header.setArrowType(Qt.DownArrow)
        else:
            self.header.setArrowType(Qt.RightArrow)
        self.body.setVisible(state)

if __name__ == '__main__':
    app = QApplication()
    win = Window()
    win.show()
    sys.exit(app.exec())
