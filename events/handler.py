# events\handler.py
#
# Implements EventHandler, which, given an event, properly handles and sends events.
from events import Event
from events.ui import ToggleDebugEvent

class EventHandler:
    def __init__(self):
        self._interface = None
        self._engine = None
        self._is_debug_mode = False

    def toggle_debug(self):
        self._is_debug_mode = not self._is_debug_mode
        print('ToggleDebugEvent: state = ON')

    def handle(self, event: Event):
        if self._is_debug_mode:
            print(event)

        if type(event) is ToggleDebugEvent:
            self.toggle_debug()