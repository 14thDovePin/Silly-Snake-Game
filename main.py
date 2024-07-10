import pygame

from snake import Snake


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
    from update import _update
    from display import _display

    def __init__(self):
        """Initialize Pygame"""
        pygame.init()
        pygame.display.set_caption(WINDOW_TITLE)
        self.screen = pygame.display.set_mode(RESOLUTION)
        self.clock = pygame.time.Clock()
        self.dt = 0
        self.cycle = True

        # Initialize objects.
        self.snake = Snake(self.screen)

    def start(self):
        """Run the game's life cycle."""
        while self.cycle:
            # Limit Updates per Second
            self.dt = self.clock.tick(UPS)/1000

            # Display FPS in window title.
            pygame.display.set_caption(
                WINDOW_TITLE + f' [{round(self.clock.get_fps())}]'
            )

            # Check Events
            self._check_events()

            # Update Objects
            self._update()

            # Update Display
            self._display()


if __name__ == '__main__':
    Game().start()
