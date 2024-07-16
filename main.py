import sys

import pygame

from snake import Snake


RESOLUTION = (1280, 720)
FPS = 60


class Game:

    # Import external methods.
    from input import (
        _process_events,
        _keydown_triggers,
    )
    from update import _update
    from display import _display

    def __init__(self):
        """Initialize Pygame"""
        pygame.init()
        self.screen = pygame.display.set_mode(RESOLUTION)
        self.clock = pygame.time.Clock()
        self.dt = 0
        self.cycle = True

        # User Events
        self._display_cycle = pygame.USEREVENT+1

        # Initialize objects.
        self.snake = Snake(self.screen)

    def start(self):
        """Run the game's life cycle."""
        # start display cycle timer
        fps = int(1000/FPS)
        pygame.time.set_timer(self._display_cycle, fps)

        # start program's main cycle
        while self.cycle:
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
