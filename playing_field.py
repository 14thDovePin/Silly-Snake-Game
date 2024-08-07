from random import randint

from pygame import Rect, draw


class PlayingField:
    """
    A dynamic grid playing field.

    Parameters
    ----------
    window_size : tuple
        The width and height of the window in pixels.
    cell_size : int
        The size of each cell in pixels.
    cell_margin : int
        Applies for all sides in pixels.
    top_margin : int
        Set top margin in cells. Includes remainder from calculation.
    side_margin : int
        Set side margin in cells. Includes remainder from calculation.
    bottom_margin : int
        Set bottom margin in cells. Includes remainder from calculation.

    Attributes TODO: Update Accordingly
    ----------
    field : list of list of any
        Represents the playing field where:
        - Each element of the parent list represents a column.
        - Each element of the nested list represents a row.

    Notes
    -----
        Margins includes the remeinder left over from
        calculating the rows and columns of the field.
    """

    def __init__(self, window_size, cell_size, cell_margin=2,
                top_margin=1.5, side_margin=1, bottom_margin=1,):

        self.window_size = window_size
        self.cell_size = cell_size
        self.cell_margin = cell_margin
        self.top_margin = top_margin
        self.side_margin = side_margin
        self.bottom_margin = bottom_margin
        self.cells = list
        self._left_edge = int
        self._top_edge = int

        # build and setup the field
        self.build_field()
        self._set_rects()

        self.starting_rect = (self._left_edge, self._top_edge)
        self.starting_rect = self.random_start()

    def build_field(self):
        """calculate initial cell location and build data strcuture"""
        win_x, win_y = self.window_size[0], self.window_size[1]

        # divide window size by cell size
        x_result = win_x/self.cell_size
        y_result = win_y/self.cell_size

        # calculate rows and columns subtracting the margins
        self.rows = int(y_result-(self.top_margin+self.bottom_margin))
        self.cols = int(x_result-(self.side_margin*2))

        # calculate top-left value, including
        # remainder from previous calculation
        self._left_edge = round(
            ( (x_result - self.cols) / 2 ) * self.cell_size
        )
        self._top_edge = round(
            ( self.top_margin + ( y_result - self.rows \
            - self.top_margin - self.bottom_margin ) \
            / 2 ) * self.cell_size
        )

        # build the data structure
        self.cells = [
            [None for _ in range(self.rows)] for _ in range(self.cols)
            ]

    def _set_rects(self):
        """calculate and set rectangles of all cells"""
        # loop through cells structure
        l_val = self._left_edge  # Left Edge of Cell
        for c, col in enumerate(self.cells[:]):
            t_val = self._top_edge  # Top Edge of Cell
            for r, row in enumerate(col):
                # remove element from structure
                self.cells[c].pop(r)

                # construct rect
                cell = Rect(
                    (l_val, t_val),
                    (
                        self.cell_size-self.cell_margin,
                        self.cell_size-self.cell_margin
                    )
                )

                # properly align rect
                cell.center = Rect(
                    (l_val, t_val),
                    (
                        self.cell_size,
                        self.cell_size
                    )
                ).center

                # insert rect
                self.cells[c].insert(r, cell)
                t_val += self.cell_size
            l_val += self.cell_size

    def random_start(self, margins=4):
        """
        Return a random top-left from the grid.

        Paremeters
        ----------
        margins : int
            Sets the margins for selecting a
            random cell within the grid.
        """
        # double check if margins*2 exceed playing field
        msg = "PlayingFieldError! Margins cannot " \
              "exceed playing field size."
        if margins*2 >= self.rows or margins*2 >= self.cols:
            raise Exception(msg)

        cells_tl = []

        # pull cells inside margins
        for x, col in enumerate(self.cells):
            if x+1 > margins and x < len(self.cells) - margins:
                for y, cell in enumerate(col):
                    if y+1 > margins and y < len(col) - margins:
                        cells_tl.append(cell)

        # choose and return a random top-left value.
        n = randint(1, len(cells_tl))-1
        random_rect = cells_tl[n]

        tl_rect = Rect(
            (0, 0),
            (self.cell_size, self.cell_size)
        )
        tl_rect.center = random_rect.center
        return tl_rect

    def draw(self, surface):
        """draw the field"""
        # loop through cells
        for n, col in enumerate(self.cells):
            if n % 2 == 0: x = 1
            else: x = 0
            for rect in col:
                x += 1

                # alternate color
                color = "#ff33cc"  # pink
                if x % 2 == 0:
                    color = "#ff99e6"  # lighter pink

                # draw cell
                draw.rect(surface, color, rect)

    def outside_perimeter(self, cords):
        """returns true if coordinates is outside perimeter"""
        # get all edge coordinates
        bottom_right = self.cells[-1][-1].bottomright
        b, r = bottom_right[1], bottom_right[0]
        l, t = self._left_edge, self._top_edge
        # print(b, r)

        x, y = cords[0], cords[1]

        # check if coordinates is outside of perimeter
        if x > r or x < l:
            return True
        if y > b or y < t:
            return True
        return False
