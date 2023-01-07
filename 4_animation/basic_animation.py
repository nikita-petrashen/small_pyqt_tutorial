import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt6.QtCore import QPropertyAnimation, QSize
""" This code shows an example of a basic animation. """


class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("анимация")
        self.setGeometry(900, 500, 500, 500)
        self.widget = QWidget(self)
        self.widget.resize(100, 100)
        self.widget.setStyleSheet("background-color:red;border-radius:15px")
        # say that we want to animate a widget's size
        self.anim = QPropertyAnimation(self.widget, b"size")
        # set the parameters of the animation
        self.anim.setEndValue(QSize(500, 500))
        self.anim.setDuration(1500)
        self.anim.start()


class HelloWorldApp(QApplication):
    def __init__(self):
        super().__init__([])
        self.window = MyMainWindow()
        self.window.show()


if __name__ == "__main__":
    app = HelloWorldApp()
    sys.exit(app.exec())
