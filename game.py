from pyglet.graphics import Batch
from pyglet.clock import schedule_interval, unschedule

from pyglet.window import Window
from pyglet import app

from util import log

import signals

import resources


class Game(Window):
    def __init__(self, resolution, title, states):
        super(Game, self).__init__(*resolution, caption=title)
        log('Initializing Game')

        self.states = states
        self.current_state_index = 0

        self.load_all_states()
        self.update_current_state()

    @property
    def current_state(self):
        return self.states[self.current_state_index]

    def on_draw(self):
        self.clear()
        self.draw_current_state()

    def run(self):
        app.run()

    def load_all_states(self):
        for state in self.states:
            try:
                log('Loading state "{state_name}"'.format(
                    state_name=state.NAME))
            except:
                raise Exception('You must define a NAME for your state.')

            state.batch = Batch()

            # Registering SLOTS

            state.register_slot(signals.GO_TO_STATE, self.go_to_state)

            state.register_slot(signals.GO_TO_NEXT_STATE,
                                self.go_to_next_state)
            state.register_slot(signals.GO_TO_PREVIOUS_STATE,
                                self.go_to_previous_state)

            state.on_load()

    def draw_current_state(self):
        self.current_state.on_draw()
        self.current_state.batch.draw()

    def update_current_state(self):
        schedule_interval(self.current_state.on_update, 1/120.0)

    def go_to_next_state(self):
        self.go_to_state(self.current_state_index + 1)

    def go_to_previous_state(self):
        self.go_to_state(self.current_state_index - 1)

    def go_to_state(self, state_id):
        unschedule(self.current_state.on_update)

        self.current_state_index = state_id
        self.update_current_state()
