import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
""" This code is exactly the same as basic.py but more cleanly written. """


# here we use class inheritance to create our custom window
class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("дерзкое приложение")
        self.setGeometry(900, 500, 280, 80)


class MyLabel(QLabel):
    def __init__(self, parent):
        super().__init__("<h2>здарова придурки</h2>", parent=parent)
        self.setGeometry(45, 10, 200, 70)


class HelloWorldApp(QApplication):
    def __init__(self):
        super().__init__([])
        self.window = MyMainWindow()
        self.label = MyLabel(parent=self.window)
        self.window.show()


# this will run only when you launch this script directly
# will not run if you import this file as a library
# __name__ is this file's attribute
# it's set to __main__ when you execute the file
if __name__ == "__main__":
    app = HelloWorldApp()
    sys.exit(app.exec())
