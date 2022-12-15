import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel

# init QApplication object
# this is the main app object that we will run later in the script
# it has no GUI itself
app = QApplication([])

# initialize the app's main window
window = QMainWindow()
window.setWindowTitle("дерзкое приложение")   # set title
window.setGeometry(900, 500, 280, 80)   # set position and size
# initialize text label
label = QLabel("<h2>здарова придурки</h2>", parent=window)  # parent means that this label is inside the main window
label.setGeometry(45, 10, 200, 70)
# show window and start the app
# the window will not show unless the app is started
# window.show() here only declares to the app that it should be shown
window.show()
sys.exit(app.exec())
