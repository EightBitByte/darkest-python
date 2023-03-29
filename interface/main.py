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

        # Set-up widgets and layouts
        self.main_widget = QtWidgets.QWidget(self)
        main_layout = QtWidgets.QVBoxLayout(self.main_widget)
        main_layout.setDirection(QtWidgets.QVBoxLayout.LeftToRight)

        left_widget = self._setup_left()

        # Create menu
        self._add_menu()

        # Add widgets to layout
        main_layout.addWidget(left_widget, stretch = 80)
        main_layout.addStretch(20)

        # Finally, set the layout
        self.setCentralWidget(self.main_widget)
        self.resize(800, 600)
        self.show()


    @QtCore.Slot()
    def toggle_debug_action(self):
        self.send_event(ToggleDebugEvent())


    def send_event(self, event: Event):
        self.event_handler.handle(event)


    def _add_menu(self):
        self.toggle_debug = QtGui.QAction('Toggle Debug', self)
        self.toggle_debug.setCheckable(True)
        self.toggle_debug.triggered.connect(self.toggle_debug_action)

        debug_menu = QtWidgets.QMenu('&Debug', self)
        debug_menu.addAction(self.toggle_debug)

        toolbar = QtWidgets.QMenuBar(self)
        toolbar.setStyleSheet('background-color: #d6d4d4')
        toolbar.addMenu(debug_menu)
        self.setMenuBar(toolbar)

    def _setup_left(self):
        left_widget = QtWidgets.QWidget(self.main_widget)
        left_layout = QtWidgets.QVBoxLayout(left_widget)

        dialog = DialogBox(left_widget)
        left_view = View(left_widget)

        left_layout.setSpacing(0)
        left_layout.addStretch(1)
        left_layout.addWidget(left_view, stretch = 900)
        left_layout.addWidget(dialog, stretch = 10, alignment = QtCore.Qt.AlignBottom)
        left_widget.setLayout(left_layout)

        return left_widget


if __name__ == '__main__':
    app = QtWidgets.QApplication([])

    e_handler = EventHandler()

    window = MainWindow(e_handler)

    window.show()

    sys.exit(app.exec())

__all__ = [MainWindow.__name__]