import sys
from pathlib import Path

from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import (
    QApplication,
    QFileDialog,
    QLineEdit,
    QToolButton,
    QGridLayout,
    QWidget,
)

FOLDER_ICON = QIcon.fromTheme(QIcon.ThemeIcon.FolderOpen)

stylesheet = """
QWidget {
    background-color: #eee;
}
QLineEdit,
QToolButton {
    border: 2px solid cyan;
    background-color: white;
}
"""


class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle('LineEdit With Dialog Button')
        self.setStyleSheet(stylesheet)
        layout = QGridLayout(self)

        lineedit1 = QLineEdit(self)
        lineedit1.setPlaceholderText('ファイルを選択してください')
        button = QToolButton(self)
        button.setIcon(FOLDER_ICON)
        self.lineedit2 = QLineEdit(self)
        self.lineedit2.setPlaceholderText('ファイルを選択してください')

        dialog_act = QAction(FOLDER_ICON, 'Open Dialog', self)
        self.lineedit2.addAction(dialog_act, QLineEdit.ActionPosition.TrailingPosition)
        dialog_act.triggered.connect(self.get_open_file)

        layout.addWidget(lineedit1, 0, 0)
        layout.addWidget(button, 0, 1)
        layout.addWidget(self.lineedit2, 1, 0, 1, 2)

    def get_open_file(self) -> None:
        file, _ = QFileDialog.getOpenFileName(self, 'Select File')
        if file and Path(file).exists():
            self.lineedit2.setText(file)


if __name__ == '__main__':
    app = QApplication()
    win = Window()
    win.show()
    sys.exit(app.exec())
