# events\ui.py
#
# The module for events pertaining to user interface interaction
from events.event import Event

class SendTextEvent(Event):
    def __init__(self, txt):
        self._text = txt

    @property
    def text(self):
        return self._text

    def __repr__(self):
        return f'SendTextEvent   : text = \'{self._text}\''

class ToggleDebugEvent(Event):
    def __repr__(self):
        return f'ToggleDebugEvent: state = OFF'