import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout
""" The same as without_layout.py but with a smart arrangement. """


# here we inherit from QWidget instead of QMainWindow because
# I didn't want to look for a way of manipulating QMainWindow's layout
class MyWindowWithLayout(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("крутой пацанский лейаут")
        self.setGeometry(500, 500, 400, 100)
        self.widget1 = QWidget()
        self.widget2 = QWidget()
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(self.widget1)
        self.layout().addWidget(self.widget2)
        self.widget1.setLayout(QHBoxLayout())
        self.widget2.setLayout(QHBoxLayout())


# the same, but without manual arrangement of the buttons
class CoolLayoutApp(QApplication):
    def __init__(self):
        super().__init__([])
        self.window = MyWindowWithLayout()
        # create three buttons
        self.button1 = QPushButton("1", parent=self.window)
        self.button2 = QPushButton("2", parent=self.window)
        self.button3 = QPushButton("3", parent=self.window)
        self.button4 = QPushButton("4", parent=self.window)
        # add buttons to window's layout so the geometry is set automatically
        self.window.widget1.layout().addWidget(self.button1)
        self.window.widget1.layout().addWidget(self.button2)
        self.window.widget2.layout().addWidget(self.button3)
        self.window.widget2.layout().addWidget(self.button4)

        self.window.show()


if __name__ == "__main__":
    app = CoolLayoutApp()
    sys.exit(app.exec())
