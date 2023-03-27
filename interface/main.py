# interface/main.py
#
# The main module for the interface package. This is where the main
# user interface is drawn with the help of Qt.
import sys
from PySide6 import QtWidgets, QtCore
from interface.dialog import DialogBox
from interface.view import View

class MainWindow(QtWidgets.QWidget):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle('DarkestPython')

        diag = DialogBox()
        view = View()
        layout = QtWidgets.QVBoxLayout()

        layout.addWidget(view, stretch = 80)
        layout.addWidget(diag)

        self.setLayout(layout)




if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    window = MainWindow()
    window.resize(800, 600)
    window.show()

    sys.exit(app.exec())

__all__ = [MainWindow.__name__]