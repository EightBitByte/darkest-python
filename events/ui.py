# events\ui.py
#
# The module for events pertaining to user interface interaction
from events.event import Event
from enum import Enum

class SendTextEvent(Event):
    def __init__(self, txt):
        self._text = txt

    @property
    def text(self):
        return self._text

    def __repr__(self):
        return f'SendTextEvent       : text = \'{self._text}\''

class ToggleDebugEvent(Event):
    def __repr__(self):
        return f'ToggleDebugEvent    :'

class ViewButton(Enum):
    STATS = 0
    RELATIONSHIP = 1
    INVENTORY = 2

class RightViewChangeEvent(Event):
    def __init__(self, button: ViewButton):
        self._button = button

    def __repr__(self):
        return f'RightViewChangeEvent: button = {self._button.name}'