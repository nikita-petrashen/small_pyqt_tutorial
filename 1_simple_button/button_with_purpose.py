import sys
from random import choice
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QStyle
from utils import OBSCENE_WORDS
""" Application with a funny little button. When clicked, it emits a message to the console. """


# the same
class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("приложение с прикольной кнопкой")
        self.setGeometry(500, 500, 400, 100)


def print_msg():
    word = choice(OBSCENE_WORDS)
    print(f"кто на меня нажал, тот {word}")


class MyButton(QPushButton):
    def __init__(self, parent):
        super().__init__("екарный бабай жми", parent=parent)
        self.setGeometry(100, 10, 200, 70)
        self.clicked.connect(print_msg) # here we connect the "button clicked" event to the "print_msg" function


# the same
class SimpleButtonApp(QApplication):
    def __init__(self):
        super().__init__([])
        self.window = MyMainWindow()
        self.button = MyButton(parent=self.window)
        self.window.show()


if __name__ == "__main__":
    app = SimpleButtonApp()
    sys.exit(app.exec())
