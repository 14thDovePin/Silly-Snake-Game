import sys

import pygame


def _check_events(self):
    """Checks user related events."""
    # Grab and check events and its type.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            self._check_keydown_events(event)
        if event.type == pygame.KEYUP:
            self._check_keyup_events(event)

def _check_keydown_events(self, event):
    # Basic movement.
    if event.key == pygame.K_w or event.key == pygame.K_UP:
        print('up')
    elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
        print('down')
    elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
        print('left')
    elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
        print('right')

def _check_keyup_events(self, event):
    pass
