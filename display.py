import pygame


def _display(self):
    """Update screen related assets."""
    self.screen.fill("gray")

    pygame.display.flip()
