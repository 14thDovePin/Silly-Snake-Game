from pygame import *

from input import check_key


class Snake:
    """The snake of the game!"""

    def __init__(self, screen, starting_rect, cell_size=45):
        self._dt = 0
        self._screen = screen

        self.tile_size = cell_size  # in pixels
        self.move_speed = 6  # tiles per second
        self.direction = 'e'  # north south east west
        self._tps = 1000/self.move_speed  # ms/tps
        self.segments = []
        self.length = 1  # TODO: Remove after use.

        # Input Buffer
        self._ib_halt = False
        self._ib_dt = 0
        self._ib_ft = self._tps*0.75  # fizzle time
        self._ib_stack = []
        self._ib_max = 3  # max no. of elements in stack

        # Starting Rect & Pos
        self._rect = Rect(
            starting_rect,  # Left Top
            (cell_size, cell_size)  # Width Height
        )
        self.pos = Vector2(  # set position to center of rect
            self._rect.centerx,
            self._rect.centery
        )

    def input(self, event):
        """input updates"""
        # insert event to buffer stack
        if len(self._ib_stack) <= self._ib_max:
            self._ib_stack.append([event, self._ib_ft])

    def change_direction(self):
        """change snake direction"""
        self._ib_halt = True

        # extract key from stack
        key = self._ib_stack.pop(0)[0].key

        # change direction
        if check_key(key, K_w, K_UP) \
        and not self.direction == 's':
            self.direction = 'n'

        if check_key(key, K_s, K_DOWN) \
        and not self.direction == 'n':
            self.direction = 's'

        if check_key(key, K_a, K_LEFT) \
        and not self.direction == 'e':
            self.direction = 'w'

        if check_key(key, K_d, K_RIGHT) \
        and not self.direction == 'w':
            self.direction = 'e'

    def update(self, dt):
        """objet updates"""
        # Manage Input Buffer
        self._input_buffer(dt)

        # Change Direction
        if self._ib_stack and not self._ib_halt:
            self.change_direction()

        # Move. If time > set_time then move
        # and update rectangle and position
        self._dt += dt
        if self._dt > self._tps:
            self._dt -= self._tps
            self._move()
        self._rect.center = (self.pos.x, self.pos.y)

    def _input_buffer(self, dt):
        """input buffer"""
        # if event in stack > fizzle time, remove it
        if self._ib_stack:
            for x, item in enumerate(self._ib_stack[:]):
                event, event_dt = item[0], item[1]
                if event_dt > 0:
                    new_item = [event, event_dt-dt]
                    self._ib_stack.remove(item)
                    self._ib_stack.insert(x, new_item)
                else:
                    self._ib_stack.remove(item)

    def _move(self):
        """move forward in current direction"""
        self._ib_halt = False

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
            "#669900",
            self._rect,
        )
