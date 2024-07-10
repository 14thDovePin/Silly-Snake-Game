from pygame import *


class Snake:
    """The snake of the game!"""

    def __init__(self, screen):
        self.screen = screen
        self.dt = 0
        self.tps = 1.2 # tiles per second
        self.pos = Vector2(
            self.screen.get_width()/2,
            self.screen.get_height()/2
        )
        self.rect = Rect(
            (0, 0),  # Left Top
            (45, 45)  # Width Height
        )

        # Center object to screen.
        self.rect.centerx = self.pos.x
        self.rect.centery = self.pos.y

    def input(self, key):
        """input updates"""
        # basi movments
        if key == K_w or key == K_UP:
            self.pos.y -= 45
        if key == K_s or key == K_DOWN:
            self.pos.y += 45
        if key == K_a or key == K_LEFT:
            self.pos.x -= 45
        if key == K_d or key == K_RIGHT:
            self.pos.x += 45


    def update(self, dt):
        """objet updates"""
        # Automatic Movement
        self.dt += dt
        if self.dt > 1:
            self.pos.x += 45
            self.dt -= 1
        self.rect.center = (self.pos.x, self.pos.y)

    def draw(self):
        """"""
        draw.rect(
            self.screen,
            (100, 100, 100),
            self.rect,
        )
