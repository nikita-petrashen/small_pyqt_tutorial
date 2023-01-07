import random
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QHBoxLayout
from PyQt6.QtGui import QColor, QPainter, QPen
from PyQt6.QtCore import QPropertyAnimation, Qt, QParallelAnimationGroup
from PyQt6.QtCore import pyqtProperty
""" This code shows how to create a custom animation. """


OBSCENE_WORDS = "Говно, залупа, пенис, хер, давалка, хуй, блядина, \
Головка, шлюха, жопа, член, еблан, петух, Мудила, \
Рукоблуд, ссанина, очко, блядун, вагина, \
Сука, ебланище, влагалище, пердун, дрочила, \
Пидор, пизда, туз, малафья, \
Гомик, мудила, пилотка, манда, \
Анус, вагина, путана, педрила, \
Шалава, хуило, мошонка, елдa".upper().split(", ")


class MyLabel(QLabel):
    def __init__(self, text, parent=None):
        super().__init__(text, parent=parent)
        self.resize(100, 30)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setStyleSheet(f"border-style: inset; border-width: 1px; border-color: black;border-radius:5px")
        self._color = QColor("blue")

    @pyqtProperty(QColor)
    def color(self):
        return self._color

    @color.setter
    def color(self, _color):
        self._color = _color

    def redraw(self, _color):
        self.setStyleSheet(f"background-color:{_color.name()};border-radius:15px")


class SlotMachineWidget(QWidget):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.resize(200, 94)
        self.move(200, 200)
        self.widgets = [MyLabel(random.choice(OBSCENE_WORDS), self) for _ in range(4)]
        self.widgets[0].move(0, -32)
        self.widgets[1].move(0, 0)
        self.widgets[2].move(0, 32)
        self.widgets[3].move(0, 64)

        self._offset = 0
        self.set_animations()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(QColor("green"), 3))
        painter.drawRect(0, 31, 100, 32)

    def set_animations(self):
        anims = [QPropertyAnimation(widget, b"color") for widget in self.widgets]
        colors = ["red", "yellow", "cyan", "orange", "violet"]
        self.anim_group = QParallelAnimationGroup()
        for anim, widget in zip(anims, self.widgets):
            anim.setStartValue(QColor(random.choice(colors)))
            anim.setEndValue(QColor("green"))
            anim.setDuration(1500)
            anim.setLoopCount(10)
            anim.valueChanged.connect(widget.redraw)
            self.anim_group.addAnimation(anim)

        self.anim_group.start()

    @pyqtProperty(int)
    def offset(self):
        return self._offset

    @offset.setter
    def offset(self, _offset):
        self._offset = _offset

    def redraw(self, _offset):
        for i, widget in enumerate(self.widgets):
            widget.move(0, (_offset + i * 32) % 128 - 32)
            if widget.pos().y() >= 96:
                widget.setText(random.choice(OBSCENE_WORDS))
                widget.move(0, -32)


class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("анимация")
        self.setGeometry(900, 500, 500, 500)
        self.widget = SlotMachineWidget(self)
        self.label = QLabel("<h3>Сегодня ты </h3>", parent=self)
        self.label.move(90, 230)
        self.anim = None
        self.set_animations()

    def set_animations(self):
        self.anim = QPropertyAnimation(self.widget, b"offset")
        self.anim.setStartValue(0)
        self.anim.setEndValue(32*10)
        self.anim.setDuration(1500)
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
