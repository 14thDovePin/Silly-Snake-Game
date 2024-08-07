from random import randint

from pygame import *

from input import check_key


class Snake:
    """
    A dynamic segmented snake!

    Parameters
    ----------
    screen : display
        The display on which the snake will be drawn/blipped.
    starting_rect : tuple
        The (left, top) edge integers of the starting rectangle.
    cell_size : int
        Used to calculate the movement and sizizng of the snake.

    Attributes
    ----------
    segments : dictionary of list of Rect and Vector2
        Represents each segment of the snake where:
        - The key is the identifier for each segment.
        - The value is a list containing the
          segment's rectangle, and position.
    """

    def __init__(self, screen, starting_rect, cell_size=45,
                 move_speed=6):
        self._dt = 0
        self._screen = screen

        self.cell_size = cell_size
        self.tile_size = cell_size  # in pixels
        self.move_speed = move_speed  # tiles per second
        self.direction = self._set_direction(starting_rect)
        self._tps = 1000/self.move_speed  # ms/tps
        self.segments = {}
        self.starting_length = 3

        # Input Buffer
        self._ib_halt = False
        self._ib_dt = 0
        self._ib_ft = self._tps*0.75  # fizzle time
        self._ib_stack = []
        self._ib_max = 3  # max no. of elements in stack

        # create initial segments
        for i in range(self.starting_length):
            self.add_segment(starting_rect)

    def _set_direction(self, starting_pos):
        """returns a direction based on starting position"""
        wsize = self._screen.get_size()
        screen_x, screen_y = wsize[0], wsize[1]
        x, y = starting_pos[0], starting_pos[1]

        # calculate left and right ranges
        right = screen_x - x
        left = screen_x - right
        # calculate top and bottom ranges
        top = screen_y - y
        bottom = screen_y - top

        # set initial direction
        dir = 'nesw'

        # set direction to opposite of the
        # nearest border of the coordinate
        if left <= right: dir = dir.replace('w', '')
        else: dir = dir.replace('e', '')
        if bottom <= top: dir = dir.replace('n', '')
        else: dir = dir.replace('s', '')
        if x <= y:
            dir = dir.replace('e', '')
            dir = dir.replace('w', '')
        else:
            dir = dir.replace('n', '')
            dir = dir.replace('s', '')

        return dir

    def add_segment(self, starting_rect):
        """add a segment to the snake"""
        # set identifier and modifier
        id = len(self.segments)+1
        mod = self.cell_size*id

        # segment position modifier based on direction
        x, y = starting_rect[0], starting_rect[1]
        if self.direction == 'n':
            mod_rect = (x, y+mod)
        if self.direction == 's':
            mod_rect = (x, y-mod)
        if self.direction == 'e':
            mod_rect = (x-mod, y)
        if self.direction == 'w':
            mod_rect = (x+mod, y)

        # construct rectangle and position
        rect = Rect(
            mod_rect,  # Left Top
            (self.cell_size, self.cell_size)  # Width Height
        )
        pos = Vector2(rect.center)

        # insert segment
        self.segments[str(id)] = [rect, pos]

    def input(self, event):
        """input updates"""
        # insert event to buffer stack
        if len(self._ib_stack) <= self._ib_max:
            self._ib_stack.append([event, self._ib_ft])

    def update(self, dt):
        """objet updates"""
        # Manage Input Buffer
        self._input_buffer(dt)

        # Change Direction
        if self._ib_stack and not self._ib_halt:
            self.change_direction()

        # Move. If time > set_time then move
        # and update rectangle and position
        # TODO: Change to a `pygame.time` timer?
        self._dt += dt
        if self._dt > self._tps:
            self._dt -= self._tps
            self._move()

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

    def _move(self):
        """move forward in current direction"""
        self._ib_halt = False

        # loop through segments
        segments = list(self.segments.keys())
        previous_position = []
        for x, key in enumerate(segments):
            rect, pos = self.segments[key]

            # store previous position
            previous_position.append(Vector2(pos.x, pos.y))

            if not x:
                # update head segment position
                if self.direction == 'n':
                    pos.y -= self.tile_size
                if self.direction == 's':
                    pos.y += self.tile_size
                if self.direction == 'e':
                    pos.x += self.tile_size
                if self.direction == 'w':
                    pos.x -= self.tile_size
            else:
                # update segment position
                prev_pos = previous_position.pop(0)
                pos.x = prev_pos[0]
                pos.y = prev_pos[1]

            # update segment rect
            rect.center = (pos.x, pos.y)

    def draw(self):
        """"""
        # loop through segments
        for key in list(self.segments.keys()):
            # pull rect from dict
            rect = self.segments[key][0]

            # draw segment
            draw.rect(
                self._screen,
                "#669900",
                rect,
            )

    def respawn(self, starting_rect):
        """reset snake on playing field"""
        # reset dt
        self._dt = 0

        # remove all segments.
        self.segments.clear()

        # set random spawn and direction
        self.direction = self._set_direction(starting_rect)

        # create starting segments
        for i in range(self.starting_length):
            self.add_segment(starting_rect)

    def bite_self(self):
        """check if the snake bit itself"""
        # extract segment positions
        positions = []
        for key in list(self.segments.keys()):
            positions.append(self.segments[key][1])

        # check for duplicates
        for pos in positions:
            if positions.count(pos) != 1:
                return True
        return False

    def get_head_cords(self):
        """returns the center coordinate of the head"""
        key = list(self.segments.keys())[0]
        head_cords = self.segments[key][0].center
        return head_cords
