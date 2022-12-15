import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
""" Applicaton with three dummy buttons arranged manually. """


# the same
class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("кривой лейаут")
        self.setGeometry(500, 500, 400, 100)


# here we add three buttons and manually arrange them in the window
class NoLayoutApp(QApplication):
    def __init__(self):
        super().__init__([])
        self.window = MyMainWindow()
        # create three buttons
        self.button1 = QPushButton("1", parent=self.window)
        self.button2 = QPushButton("2", parent=self.window)
        self.button3 = QPushButton("3", parent=self.window)
        # manually set their geometry (boooring)
        self.button1.setGeometry(10, 10, 30, 30)
        self.button2.setGeometry(10, 40, 30, 30)
        self.button3.setGeometry(10, 70, 30, 30)

        self.window.show()


if __name__ == "__main__":
    app = NoLayoutApp()
    sys.exit(app.exec())
