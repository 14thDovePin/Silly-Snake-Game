import pygame


def _display(self):
    """Game Screen Assets"""
    self.screen.fill("gray")
    self.snake.draw()

    pygame.display.flip()
