import sys
from random import choice
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QLabel
from styles import WINDOW_STYLE, HIDE_BUTTON_STYLE, MY_BUTTON_STYLE
OBSCENE_WORDS = "Говно, залупа, пенис, хер, давалка, хуй, блядина, \
Головка, шлюха, жопа, член, еблан, петух, Мудила, \
Рукоблуд, ссанина, очко, блядун, вагина, \
Сука, ебланище, влагалище, пердун, дрочила, \
Пидор, пизда, туз, малафья, \
Гомик, мудила, пилотка, манда, \
Анус, вагина, путана, педрила, \
Шалава, хуило, мошонка, елдa".upper().split(", ")

""" Our cool button app, but with style. """


# the same
class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("приложение с прикольной кнопкой")
        self.setGeometry(750, 500, 400, 100)


class PopupWidget(QWidget):
    def __init__(self):
        super().__init__(parent=None)
        self.hide_button = QPushButton("X", parent=self)
        self.label = QLabel(parent=self)
        self.hide_button.clicked.connect(self.hide)
        self.set_all_geometry()
        self.set_all_styles()

    def set_text_and_show(self):  # this will set the label text and show the widget
        word = choice(OBSCENE_WORDS)
        self.label.setText(f"кто на меня нажал, тот {word}")
        self.show()

    def set_all_geometry(self):
        self.setGeometry(780, 400, 300, 80)
        self.hide_button.setGeometry(10, 25, 30, 30)
        self.label.setGeometry(50, 5, 250, 70)

    # here we use style sheets defined in styles.py and apply them
    def set_all_styles(self):
        self.hide_button.setStyleSheet(HIDE_BUTTON_STYLE)
        self.setStyleSheet(WINDOW_STYLE)


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
        self.set_all_styles()
        self.window.show()

    # here we use style sheets defined in styles.py and apply them
    def set_all_styles(self):
        self.button.setStyleSheet(MY_BUTTON_STYLE)
        self.window.setStyleSheet(WINDOW_STYLE)


if __name__ == "__main__":
    app = SimpleButtonApp()
    sys.exit(app.exec())
