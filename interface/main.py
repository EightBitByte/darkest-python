# interface/main.py
#
# The main module for the interface package. This is where the main
# user interface is drawn with the help of Qt.
from PySide6 import QtWidgets, QtCore, QtGui
from interface.menu_buttons import MenuButtons
from interface.dialog import DialogBox
from interface.view import View
from events.event import Event
from events.ui import ToggleDebugEvent
from pathlib import Path

RIGHT_HAND_STRETCH = 20
LEFT_HAND_STRETCH = 75
ICO_PATH = Path(__file__).parent.parent / '_icons' / 'glimmerofhope.png'

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, event_handler, parent = None):
        super(MainWindow, self).__init__(parent)
        self.event_handler = event_handler
        self.setWindowTitle('DarkestPython')
        self.setWindowIcon(QtGui.QIcon(str(ICO_PATH)))


        # Set-up widgets and layouts
        self.main_widget = QtWidgets.QWidget(self)
        main_layout = QtWidgets.QVBoxLayout(self.main_widget)

        top_widget = self._setup_top()
        bottom_widget = self._setup_bottom()

        # Create menu
        self._add_menu()

        # Add widgets to layout
        main_layout.setSpacing(0)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.addWidget(top_widget, stretch = 900)
        main_layout.addWidget(bottom_widget, stretch = 10)


        # Finally, set the layout
        self.setCentralWidget(self.main_widget)
        self.resize(800, 600)
        self.show()


    @QtCore.Slot()
    def toggle_debug_action(self):
        """Toggles the debug output to console"""
        self.send_event(ToggleDebugEvent())


    def send_event(self, event: Event):
        """Sends an event to the EventHandler"""
        self.event_handler.handle(event)


    def _add_menu(self):
        """Adds the toolbar to the window."""
        self.toggle_debug = QtGui.QAction('Toggle Debug', self)
        self.toggle_debug.setCheckable(True)
        self.toggle_debug.triggered.connect(self.toggle_debug_action)

        debug_menu = QtWidgets.QMenu('&Debug', self)
        debug_menu.addAction(self.toggle_debug)

        toolbar = QtWidgets.QMenuBar(self)
        toolbar.setStyleSheet('background-color: #d6d4d4')
        toolbar.addMenu(debug_menu)
        self.setMenuBar(toolbar)


    def _setup_top(self):
        """Sets up the top widget (the two views)"""
        top_widget = QtWidgets.QWidget(self.main_widget)
        top_layout = QtWidgets.QVBoxLayout(top_widget)
        top_layout.setDirection(QtWidgets.QVBoxLayout.LeftToRight)

        self.left_view = View(top_widget)
        self.right_view = View(top_widget)

        top_layout.setSpacing(0)
        top_layout.setContentsMargins(9, 9, 9, 0)
        top_layout.addWidget(self.left_view, stretch = LEFT_HAND_STRETCH)
        top_layout.addWidget(self.right_view, stretch = RIGHT_HAND_STRETCH)
        top_widget.setLayout(top_layout)

        return top_widget


    def _setup_bottom(self):
        """Sets up the bottom widget (the input line and buttons)"""
        bottom_widget = QtWidgets.QWidget(self.main_widget)
        bottom_layout = QtWidgets.QVBoxLayout(bottom_widget)
        bottom_layout.setDirection(QtWidgets.QVBoxLayout.LeftToRight)

        dialog = DialogBox(bottom_widget)
        menu_buttons = MenuButtons(bottom_widget)

        bottom_layout.setSpacing(0)
        bottom_layout.setContentsMargins(9, 0, 9, 9)
        bottom_layout.addWidget(dialog, stretch = LEFT_HAND_STRETCH)
        bottom_layout.addWidget(menu_buttons, stretch = RIGHT_HAND_STRETCH)
        bottom_widget.setLayout(bottom_layout)

        return bottom_widget


__all__ = [MainWindow.__name__]