import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtGui import QColor
from PyQt6.QtCore import QPropertyAnimation, Qt
from PyQt6.QtCore import pyqtProperty
""" This code shows how to create a custom animation. """


class MyLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__("<h2>здарова придурки</h2>", parent=parent)
        self.move(50, 50)
        self.resize(400, 400)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._color = QColor("blue")

    @pyqtProperty(QColor)
    def color(self):
        return self._color

    @color.setter
    def color(self, _color):
        self._color = _color

    def redraw(self, _color):
        self.setStyleSheet(f"background-color:{_color.name()};border-radius:15px")


class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("анимация")
        self.setGeometry(900, 500, 500, 500)
        self.widget = MyLabel(self)
        self.anim = None
        self.set_animations()

    def set_animations(self):
        self.anim = QPropertyAnimation(self.widget, b"color")
        self.anim.setStartValue(QColor("blue"))
        self.anim.setEndValue(QColor("red"))
        self.anim.setDuration(1500)
        self.anim.setLoopCount(10)
        self.anim.valueChanged.connect(self.widget.redraw)
        self.anim.start()


class HelloWorldApp(QApplication):
    def __init__(self):
        super().__init__([])
        self.window = MyMainWindow()
        self.window.show()


if __name__ == "__main__":
    app = HelloWorldApp()
    sys.exit(app.exec())
