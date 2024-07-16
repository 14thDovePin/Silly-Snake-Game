import pygame


WINDOW_TITLE = 'A Silly Snake Game'


def _display(self, events):
    """Game Screen Assets"""
    # Clamp Upper Limit (Limit FPS)
    update = False
    for event in events:
        if event.type == self._display_cycle:
            update = True
    if not update: return

    # Display FPS in Window Title
    self.clock.tick()
    caption = WINDOW_TITLE + f' [{round(self.clock.get_fps())}]'
    pygame.display.set_caption(caption)

    self.screen.fill("gray")
    self.snake.draw()

    pygame.display.flip()
