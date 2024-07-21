import pygame


def _update(self):
    """Game Updates"""
    self.snake.update(self._dt)

    # Check if snake bites itself.
    respawn = False
    if self.snake.bite_self():
        respawn = True

    # Check if snake is outside the boarder.
    snake_head_cords = self.snake.get_head_cords()
    hit_edge = self.playing_field.outside_perimeter(
        snake_head_cords
    )

    # respawn snake if edge is hit
    if respawn or hit_edge:
        spawn_location = self.playing_field.random_start()
        self.snake.respawn(spawn_location)
