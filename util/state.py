from pyglet.sprite import Sprite
from pyglet.text import Label
from util import log

import signals

class State:
    '''
    State defines a screen of Game (Menu, Credits, Level_1 etc.)
    '''

    def __init__(self, name=None):
        self._name = name
        self._batch = None
        self.slots = {}

    def register_slot(self, signal, slot):
        self.slots[signal] = slot

    def emit(self, signal, **kwargs):
        log('Emitting "{}"'.format(signal))

        self.slots[signal](**kwargs)

    @property
    def batch(self):
        return self._batch

    @batch.setter
    def batch(self, new_val):
        self._batch = new_val

    # Helper functions

    def go_to_next_state(self):
        self.emit(signal=signals.GO_TO_NEXT_STATE)

    def go_to_previous_state(self):
        self.emit(signal=signals.GO_TO_PREVIOUS_STATE)

    def go_to_state(self, state_id):
        self.emit(signal=signals.GO_TO_STATE, state_id=state_id)

    # Factories

    def make_label(self, *args, **kwargs):
        return Label(*args, **kwargs)

    def make_sprite(self, *args, **kwargs):
        return Sprite(*args, **kwargs)
