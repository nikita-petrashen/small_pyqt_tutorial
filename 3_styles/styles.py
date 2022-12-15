MY_BUTTON_STYLE = """MyButton {
    background-color: yellow;
    border-style: outset;
    border-width: 2px;
    border-radius: 10px;
    border-color: beige;
    font: italic;
    min-width: 10em;
    padding: 6px;
}
MyButton:pressed {
    background-color: violet;
    border-style: inset;
}
"""

HIDE_BUTTON_STYLE = """QPushButton {
    background-color: rgb(100, 200, 100);
    border-style: outset;
    border-radius: 3px;
    font: italic;
}
MyButton:pressed {
    background-color: violet;
    border-style: inset;
}
"""

WINDOW_STYLE = """MyMainWindow, PopupWidget{
    border-style: outset;
    border-width: 2px;
    border-radius: 10px;
    border-color: beige;
    font: italic;
    min-width: 10em;
    padding: 6px;
}
MyMainWindow { background-color: blue; }
PopupWidget { background-color: cyan;}
"""
