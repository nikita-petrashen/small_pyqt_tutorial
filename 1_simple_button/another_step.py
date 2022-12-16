import sys
from random import choice
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QLabel
from utils import OBSCENE_WORDS
""" The same as button_with_purpose, but the message now is shown in a popup window. """


# the same
class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("приложение с прикольной кнопкой")
        self.setGeometry(750, 500, 400, 100)


# instead of print_msg we now show a widget with the message and a close button
class PopupWidget(QWidget):
    def __init__(self):
        # here we set the parent as None so the widget is shown separately from the app window
        super().__init__(parent=None)
        self.hide_button = QPushButton("X", parent=self)
        self.label = QLabel(parent=self)
        self.hide_button.clicked.connect(self.hide)  # now when we press the button the popup will call self.hide()
        self.set_all_geometry()  # use a separate method to set the geometry for cleaner code

    def set_text_and_show(self):  # this will set the label text and show the widget
        self.hide()  # hide the popup if it's already shown
        self.setGeometry(780, 400, 300, 80)  # without this the widget drifts upwards when called consecutively
        word = choice(OBSCENE_WORDS)
        self.label.setText(f"кто на меня нажал, тот {word}")
        self.show()

    def set_all_geometry(self):
        self.setGeometry(780, 400, 300, 80)
        self.hide_button.setGeometry(10, 25, 30, 30)
        self.label.setGeometry(50, 5, 250, 70)


# the same
class MyButton(QPushButton):
    def __init__(self, parent):
        super().__init__("екарный бабай жми", parent=parent)
        self.setGeometry(100, 10, 200, 70)


# the same
class SimpleButtonApp(QApplication):
    def __init__(self):
        super().__init__([])
        self.window = MyMainWindow()
        self.button = MyButton(parent=self.window)
        self.popup = PopupWidget()
        self.button.clicked.connect(self.popup.set_text_and_show)
        self.window.show()


if __name__ == "__main__":
    app = SimpleButtonApp()
    sys.exit(app.exec())
