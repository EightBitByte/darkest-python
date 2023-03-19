# interface/main.py
#
# The main module for the interface package. This is where the main
# user interface is drawn with the help of Qt.
import sys
from PySide6 import QtWidgets
from interface.dialog import DialogBox


if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    widget = DialogBox()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())

