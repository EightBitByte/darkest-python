# interface/main.py
#
# The main module for the interface package. This is where the main
# user interface is drawn with the help of Qt.
import sys
from PySide6 import QtWidgets, QtCore, QtGui
from interface.dialog import DialogBox
from interface.view import View
from events.handler import EventHandler
from events.event import Event
from events.ui import ToggleDebugEvent

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, event_handler, parent = None):
        super(MainWindow, self).__init__(parent)
        self.event_handler = event_handler
        self.setWindowTitle('DarkestPython')

        # Initialize elements
        main_widget = QtWidgets.QWidget(self)
        diag = DialogBox(parent = self)
        view = View(self)
        layout = QtWidgets.QVBoxLayout(main_widget)

        # Create menu

        self.toggle_debug = QtGui.QAction('Toggle Debug', self)
        self.toggle_debug.setCheckable(True)
        self.toggle_debug.triggered.connect(self.toggle_debug_action)

        debug_menu = QtWidgets.QMenu('&Debug', self)
        debug_menu.addAction(self.toggle_debug)

        toolbar = QtWidgets.QMenuBar(self)
        toolbar.setStyleSheet('background-color: #d6d4d4')
        toolbar.addMenu(debug_menu)
        self.setMenuBar(toolbar)


        # Add widgets to layout
        layout.addWidget(view, stretch = 80)
        layout.addWidget(diag)

        # Finally, set the layout
        self.setCentralWidget(main_widget)
        self.resize(800, 600)
        self.show()

    @QtCore.Slot()
    def toggle_debug_action(self):
        self.send_event(ToggleDebugEvent())

    def send_event(self, event: Event):
        self.event_handler.handle(event)




if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    e_handler = EventHandler()

    window = MainWindow(e_handler)

    window.show()

    sys.exit(app.exec())

__all__ = [MainWindow.__name__]