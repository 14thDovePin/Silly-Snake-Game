import pygame


RESOLUTION = (1280, 720)
UPS = 60


class Game:
    def __init__(self):
        """Initialize Pygame"""
        pygame.init()
        self.screen = pygame.display.set_mode(RESOLUTION)
        self.clock = pygame.time.Clock()
        self.cycle = True

    def start(self):
        # Limit Updates per Second
        self.clock.tick(UPS)
        while self.cycle:
            pass


if __name__ == '__main__':
    Game().start()
