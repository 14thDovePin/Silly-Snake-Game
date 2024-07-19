import sys

import pygame

from playing_field import PlayingField
from snake import Snake


WINDOW_TITLE = 'A Silly Snake Game'
RESOLUTION = (1600, 900)
FPS = 60
CELL_SIZE = 45


class Game:

    # Import External Methods
    from input import (
        _process_events,
        _keydown_triggers,
    )
    from update import _update
    from display import _display

    def __init__(self):
        """Initialize Pygame"""
        pygame.init()
        self.window_title = WINDOW_TITLE
        self._screen = pygame.display.set_mode(RESOLUTION)
        self._clock = pygame.time.Clock()
        self._display_clock = pygame.time.Clock()
        self._dt = 0
        self.cycle = True

        # User Events
        self._display_cycle = pygame.USEREVENT+1

        # Initialize Objects
        self.playing_field = PlayingField(
            RESOLUTION,
            CELL_SIZE,
            10
        )
        self.snake = Snake(
            self._screen,
            self.playing_field.starting_rect,
            CELL_SIZE
        )

    def start(self):
        """Run the game's life cycle."""
        # start display cycle timer
        fps = int(1000/FPS)
        pygame.time.set_timer(self._display_cycle, fps)

        # start program's main cycle
        while self.cycle:
            # Update Clock
            self._dt = self._clock.tick()

            # Pull & Process Events
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    sys.exit()

            # Process Events
            self._process_events(events)

            # Update Objects
            self._update()

            # Update Display
            self._display(events)


if __name__ == '__main__':
    Game().start()
