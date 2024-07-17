import pygame


def _display(self, events):
    """Game Screen Assets"""
    # Clamp Upper Limit (Limit FPS)
    update = False
    for event in events:
        if event.type == self._display_cycle:
            update = True
    if not update: return

    # Update Clock
    self._display_clock.tick()

    # Display FPS in Window Title
    fps = round(self._display_clock.get_fps())
    caption = self.window_title + f' [{fps}]'
    pygame.display.set_caption(caption)

    self._screen.fill("gray")
    self.snake.draw()

    pygame.display.flip()
