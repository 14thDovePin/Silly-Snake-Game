from pygame import *

from input import check_key


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

        # input buffer
        self._ib_state = True
        self._ib_dt = 50  # miliseconds
        self._ib_timer = USEREVENT+1
        self._ib_stack = []
        self._ib_max = 5  # max no. of elements in stack

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

    def input(self, event):
        """input updates"""
        # buffer input
        self._ib_stack.append(event)
        if self._ib_state:
            self._ib_state = False
        else: return

        key = self._ib_stack.pop(0).key

        # direction control
        if check_key(key, K_w, K_UP) \
        and self._change_direction() \
        and not self.direction == 's':
            self.direction = 'n'

        if check_key(key, K_s, K_DOWN) \
        and self._change_direction() \
        and not self.direction == 'n':
            self.direction = 's'

        if check_key(key, K_a, K_LEFT) \
        and self._change_direction() \
        and not self.direction == 'e':
            self.direction = 'w'

        if check_key(key, K_d, K_RIGHT) \
        and self._change_direction() \
        and not self.direction == 'w':
            self.direction = 'e'

    def _change_direction(self):
        if not self._lock_direction:
            self._lock_direction = True
            return True
        return False

    def update(self, dt):
        """objet updates"""
        # input buffer


        # Automatic Movement
        self._dt += dt
        if self._dt > self._tps:
            self._move()
            self._dt -= self._tps
        self._rect.center = (self.pos.x, self.pos.y)

    def _move(self):
        """move forward in current direction"""
        self._ib_state = True
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
