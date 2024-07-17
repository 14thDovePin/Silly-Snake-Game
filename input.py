import pygame

from pygame import *
from pygame.time import set_timer


def _process_events(self, events):
    """Checks user related events."""
    for event in events:
        # process keydown events
        if event.type == pygame.KEYDOWN:
            self._keydown_triggers(event)

def _keydown_triggers(self, event):
    key = event.key

    # print movements
    if check_key(key, K_w, K_UP):
        print('up')
    if check_key(key, K_s, K_DOWN):
        print('down')
    if check_key(key, K_a, K_LEFT):
        print('left')
    if check_key(key, K_d, K_RIGHT):
        print('right')

    self.snake.input(event)

def check_key(key, *match):
    if key in match : return True
