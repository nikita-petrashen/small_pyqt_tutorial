import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
""" The same as hello_world but with a button instead of label. """


# the same
class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("приложение с дурацкой кнопкой")
        self.setGeometry(500, 500, 400, 100)


# button!
class MyButton(QPushButton):
    def __init__(self, parent):
        super().__init__("бесполезная кнопка", parent=parent)
        self.setGeometry(100, 10, 200, 70)


# the same but with a button
class SimpleButtonApp(QApplication):
    def __init__(self):
        super().__init__([])
        self.window = MyMainWindow()
        self.button = MyButton(parent=self.window)
        self.window.show()


if __name__ == "__main__":
    app = SimpleButtonApp()
    sys.exit(app.exec())
