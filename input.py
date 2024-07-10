import sys

import pygame


def _check_events(self):
    """Checks user related events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
