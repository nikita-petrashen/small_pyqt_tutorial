import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
""" The same as without_layout.py but with a smart arrangement. """


# here we inherit from QWidget instead of QMainWindow because
# I didn't want to look for a way of manipulating QMainWindow's layout
class MyWindowWithLayout(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("крутой пацанский лейаут")
        self.setGeometry(500, 500, 400, 100)
        self.setLayout(QVBoxLayout())


# the same, but without manual arrangement of the buttons
class CoolLayoutApp(QApplication):
    def __init__(self):
        super().__init__([])
        self.window = MyWindowWithLayout()
        # create three buttons
        self.button1 = QPushButton("1", parent=self.window)
        self.button2 = QPushButton("2", parent=self.window)
        self.button3 = QPushButton("3", parent=self.window)
        # add buttons to window's layout so the geometry is set automatically
        self.window.layout().addWidget(self.button1)
        self.window.layout().addWidget(self.button2)
        self.window.layout().addWidget(self.button3)

        self.window.show()


if __name__ == "__main__":
    app = CoolLayoutApp()
    sys.exit(app.exec())
