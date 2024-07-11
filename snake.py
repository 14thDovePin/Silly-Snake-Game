from pygame import *


class Snake:
    """The snake of the game!"""

    def __init__(self, screen):
        self._screen = screen
        self._dt = 0
        self.tile_size = 45  # in pixels
        self.move_speed = 6  # tiles per second
        self._tps = 1/self.move_speed
        self.direction = 'n'  # north south east west
        self._lock_direction = False

        self._rect = Rect(
            (0, 0),  # Left Top
            (45, 45)  # Width Height
        )

        self.pos = Vector2(
            self._screen.get_width()/2,
            self._screen.get_height()/2
        )

        # Center object to screen.
        self._rect.centerx = self.pos.x
        self._rect.centery = self.pos.y

    def input(self, key):
        """input updates"""
        # basic movments
        if not self._lock_direction \
        and (key == K_w or key == K_UP) \
        and not self.direction == 's':
            self._lock_direction = True
            self.direction = 'n'

        if not self._lock_direction \
        and (key == K_s or key == K_DOWN) \
        and not self.direction == 'n':
            self._lock_direction = True
            self.direction = 's'

        if not self._lock_direction \
        and (key == K_a or key == K_LEFT) \
        and not self.direction == 'e':
            self._lock_direction = True
            self.direction = 'w'

        if not self._lock_direction \
        and (key == K_d or key == K_RIGHT) \
        and not self.direction == 'w':
            self._lock_direction = True
            self.direction = 'e'


    def update(self, dt):
        """objet updates"""
        # Automatic Movement
        self._dt += dt
        if self._dt > self._tps:
            self._move()
            self._dt -= self._tps
        self._rect.center = (self.pos.x, self.pos.y)

    def _move(self):
        """move forward in current direction"""
        self._lock_direction = False
        if self.direction == 'n':
            self.pos.y -= self.tile_size
        if self.direction == 's':
            self.pos.y += self.tile_size
        if self.direction == 'e':
            self.pos.x += self.tile_size
        if self.direction == 'w':
            self.pos.x -= self.tile_size

    def draw(self):
        """"""
        draw.rect(
            self._screen,
            (100, 100, 100),
            self._rect,
        )
