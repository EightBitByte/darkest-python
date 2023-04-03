# main.py
#
# The main module. Run from here to run the application.
from PySide6 import QtWidgets
from events.handler import EventHandler
from interface.main import MainWindow
import sys
import ctypes

MYAPPID = 'jam.darkest-python.mainapp.v1'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(MYAPPID)


if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    e_handler = EventHandler()
    window = MainWindow(e_handler)

    window.show()
    sys.exit(app.exec())