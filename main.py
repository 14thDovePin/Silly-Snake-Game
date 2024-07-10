import pygame


WINDOW_TITLE = 'A Silly Snake Game'
RESOLUTION = (1280, 720)
UPS = 60


class Game:

    # Import external methods.
    from input import (
        _check_events,
        _check_keydown_events,
        _check_keyup_events
    )
    from display import _display

    def __init__(self):
        """Initialize Pygame"""
        pygame.init()
        pygame.display.set_caption(WINDOW_TITLE)
        self.screen = pygame.display.set_mode(RESOLUTION)
        self.clock = pygame.time.Clock()
        self.cycle = True

    def start(self):
        """Run the game's life cycle."""
        while self.cycle:
            # Limit Updates per Second
            self.clock.tick(UPS)

            # Check Events
            self._check_events()

            # Update Display
            self._display()


if __name__ == '__main__':
    Game().start()
