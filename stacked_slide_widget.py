import sys

from PySide6.QtCore import (
    QPoint,
    Qt,
    QEasingCurve,
    QParallelAnimationGroup,
    QPropertyAnimation,
)
from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton,
    QSizePolicy,
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
        self.in_animation = False

    def create_widgets(self) -> None:
        self.stacked_widget = QStackedWidget(self)
        self.buttons: list[QPushButton] = []
        for i in range(4):
            label = QLabel(f'Page {i}', self)
            label.setAlignment(
                Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignHCenter,
            )
            label.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
            label.setObjectName(f'pageLabel{i}')
            button = QPushButton(str(i), self)
            button.setObjectName('pageButton')
            # self.pages.append(label)
            self.buttons.append(button)
            self.stacked_widget.addWidget(label)

    def create_layout(self) -> None:
        main_layout = QVBoxLayout(self.centralWidget())
        main_layout.addWidget(self.stacked_widget)
        btn_layout = QHBoxLayout()
        [btn_layout.addWidget(btn) for btn in self.buttons]
        main_layout.addLayout(btn_layout)

    def create_connections(self) -> None:
        for i, button in enumerate(self.buttons):
            button.clicked.connect(lambda _, i=i: self.slide_animation(i))

    def slide_animation(self, next_index: int) -> None:
        current_index = self.stacked_widget.currentIndex()
        if current_index == next_index or self.in_animation:
            return
        self.in_animation = True
        frame_rect = self.stacked_widget.frameRect()
        width = frame_rect.width()
        height = frame_rect.height()
        orig_widget = self.stacked_widget.widget(current_index)
        next_widget = self.stacked_widget.widget(next_index)
        offset_width = width if current_index < next_index else -width

        next_widget.setGeometry(0, 0, width, height)
        next_pos = next_widget.pos()
        next_widget.move(next_pos.x() + offset_width, next_pos.y())
        next_widget.show()
        next_widget.raise_()

        orig_pos = orig_widget.pos()

        animgroup = QParallelAnimationGroup(self)
        # next widget animation
        anim = QPropertyAnimation(next_widget, b'pos')
        anim.setDuration(self.SPEED)
        anim.setStartValue(next_widget.pos())
        anim.setEndValue(orig_pos)
        anim.setEasingCurve(self.ANIMTYPE)
        animgroup.addAnimation(anim)

        # orig widget animation
        anim = QPropertyAnimation(orig_widget, b'pos')
        anim.setDuration(self.SPEED)
        anim.setStartValue(orig_pos)
        anim.setEndValue(orig_pos - QPoint(offset_width, 0))
        anim.setEasingCurve(self.ANIMTYPE)
        animgroup.addAnimation(anim)

        def when_animation_done():
            self.stacked_widget.setCurrentIndex(next_index)
            orig_widget.hide()
            orig_widget.move(orig_pos)
            orig_widget.update()
            self.in_animation = False
        animgroup.finished.connect(when_animation_done)
        animgroup.start()


if __name__ == '__main__':
    app = QApplication()
    win = StackedSlideWidget()
    win.show()
    sys.exit(app.exec())
