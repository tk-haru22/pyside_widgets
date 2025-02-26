import sys

from PySide6.QtCore import (
    QEasingCurve,
    QParallelAnimationGroup,
    QPauseAnimation,
    QPropertyAnimation,
    QSequentialAnimationGroup,
)
from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QStackedWidget,
    QVBoxLayout,
    QWidget,
)


class StackedSlideWidget(QMainWindow):

    SPEED = 500
    ANIMTYPE = QEasingCurve.Type.OutCubic

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle('Stacked slide widget')
        self.setCentralWidget(QWidget(self))
        self.create_widgets()
        self.create_layout()
        self.create_connections()

    def create_widgets(self) -> None:
        self.stacked_widget = QStackedWidget(self)
        self.pages = []
        self.buttons = []
        for i in range(4):
            label = QLabel(f'Page {i}', self)
            label.setObjectName(f'pageLabel{i}')
            button = QPushButton(str(i), self)
            button.setObjectName('pageButton')
            self.pages.append(label)
            self.buttons.append(button)

    def create_layout(self) -> None:
        main_layout = QVBoxLayout(self.centralWidget())
        main_layout.addWidget(self.stacked_widget)
        btn_layout = QHBoxLayout()
        [btn_layout.addWidget(btn) for btn in self.buttons]

    def create_connections(self) -> None: ...

    def slide_animation(self, next_index: int) -> None:
        current_index = self.stacked_widget.currentIndex()
        if current_index == next_index:
            return
        frame_rect = self.stacked_widget.frameRect()

if __name__ == '__main__':
    app = QApplication()
    win = StackedSlideWidget()
    win.show()
    sys.exit(app.exec())
