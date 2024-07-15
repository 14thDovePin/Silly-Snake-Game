import sys

import pygame

from pygame import *
from pygame.time import set_timer

from random import randint


def _check_events(self):
    """Checks user related events."""
    # grab events
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            self._keydown_triggers(event)

def _keydown_triggers(self, event):
    key = event.key

    # Print basic movements.
    if check_key(key, K_w, K_UP):
        print('up')
    if check_key(key, K_s, K_DOWN):
        print('down')
    if check_key(key, K_a, K_LEFT):
        print('left')
    if check_key(key, K_d, K_RIGHT):
        print('right')

    # Pass event to player object
    self.snake.input(event)

def check_key(key, *match):
    if key in match : return True
