# interface/menu_buttons.py
#
# Implements the MenuButtons class, which is a widget that
# can change the information on the right view
from PySide6 import QtWidgets, QtCore
from events.ui import ViewButton, RightViewChangeEvent

BUTTON_MAP = {
    'St': ViewButton.STATS,
    'Re': ViewButton.RELATIONSHIP,
    'In': ViewButton.INVENTORY
}

MIN_SIZE = QtCore.QSize(40, 10)

class MenuButtons(QtWidgets.QWidget):
    def __init__(self, parent = None):
        super(MenuButtons, self).__init__(parent)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.setDirection(QtWidgets.QVBoxLayout.LeftToRight)

        self._make_buttons()


    def _reenable_all(self):
        all_buttons = [x for x in dir(self) if '_button' in x
                       and '_pressed' not in x and '_make' not in x]

        for button_name in all_buttons:
            b = getattr(self, button_name)
            b.setEnabled(True)


    def _make_pressed_method(self, name, vb):
        button = getattr(self, f'_button_{name.lower()}')
        def pressed_method():
            self._reenable_all()
            self._send(RightViewChangeEvent(vb))
            button.setDisabled(True)

        return pressed_method


    def _make_pressed_methods(self):
        for name, vb in BUTTON_MAP.items():
            new_method = self._make_pressed_method(name, vb)

            setattr(self, f'_button_{name.lower()}_pressed', new_method)


    def _make_buttons(self):
        # Make the buttons
        for name in BUTTON_MAP.keys():
            b = QtWidgets.QPushButton(name, self)
            b.setMinimumSize(MIN_SIZE)

            setattr(self, f'_button_{name.lower()}', b)
            self.layout.addWidget(b)

        # Make their methods
        self._make_pressed_methods()

        # Connect them
        for name in BUTTON_MAP.keys():
            b = getattr(self, f'_button_{name.lower()}')
            m = getattr(self, f'_button_{name.lower()}_pressed')

            b.clicked.connect(m)


    def _send(self, event):
        self.parent().parent().parent().event_handler.handle(event)