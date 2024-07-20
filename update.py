import pygame


def _update(self):
    """Game Updates"""
    self.snake.update(self._dt)

    # Check if snake bites itself.
    spawn_location = self.playing_field.random_start()
    if self.snake.bite_self():
        self.snake.respawn(spawn_location)

    # Check if snake is outside the boarder.
