import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtCore import QPropertyAnimation, QParallelAnimationGroup, QSize, QPoint, Qt
""" This code shows how to group different animations together. """


class MyLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__("<h2>здарова придурки</h2>", parent=parent)
        self.resize(100, 100)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setStyleSheet("background-color:red;border-radius:15px")


class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("анимация")
        self.setGeometry(900, 500, 500, 500)
        self.widget = MyLabel(self)
        self.anim = None
        self.set_animations()

    def set_animations(self):
        pos_anim = QPropertyAnimation(self.widget, b"pos")
        pos_anim.setEndValue(QPoint(200, 200))
        pos_anim.setDuration(1500)
        pos_anim.setLoopCount(3)
        size_anim = QPropertyAnimation(self.widget, b"size")
        size_anim.setEndValue(QSize(250, 250))
        size_anim.setDuration(1500)
        size_anim.setLoopCount(3)
        self.anim = QParallelAnimationGroup()
        self.anim.addAnimation(pos_anim)
        self.anim.addAnimation(size_anim)
        self.anim.start()


class HelloWorldApp(QApplication):
    def __init__(self):
        super().__init__([])
        self.window = MyMainWindow()
        self.window.show()


if __name__ == "__main__":
    app = HelloWorldApp()
    sys.exit(app.exec())
