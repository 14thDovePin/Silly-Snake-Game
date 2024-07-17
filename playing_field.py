from pygame import Rect, draw


class PlayingField:

    def __init__(
            self,
            window_size,
            cell_size,
            cell_margin=2,
            top_margin=1.5,
            side_margin=1,
            bottom_margin=1,
        ):
        """initialize object"""
        self.window_size = window_size
        self.cell_size = cell_size
        self.cell_margin = cell_margin
        self.top_margin = top_margin
        self.side_margin = side_margin
        self.bottom_margin = bottom_margin
        self.cells = []

        # create and calculate field
        self._calc_field()

        # create cells & set their rectangles
        self._create_rects()

        self.starting_rect = self.cells[0].center
        print(self.starting_rect)

    def _calc_field(self):
        """calculate the location of each rectangle"""
        # calculate the top-left as well as rows and cols
        win_x, win_y = self.window_size[0], self.window_size[1]
        x_result = win_x/self.cell_size
        y_result = win_y/self.cell_size
        self.rows = int(y_result-(self.top_margin+self.bottom_margin))
        self.cols = int(x_result-(self.side_margin*2))
        self._left_edge = round(
            ( (x_result - self.cols) / 2 ) * self.cell_size
        )
        self._top_edge = round(
            ( self.top_margin + ( y_result - self.rows \
            - self.top_margin - self.bottom_margin ) \
            / 2 ) * self.cell_size
        )

    def _create_rects(self):
        """create cells and set their rects"""
        l_val = self._left_edge
        for x in range(self.cols):
            t_val = self._top_edge
            for y in range(self.rows):
                cell = Rect(
                    (l_val, t_val),
                    (
                        self.cell_size-self.cell_margin,
                        self.cell_size-self.cell_margin
                    )
                )
                t_val += self.cell_size
                self.cells.append(cell)
            l_val += self.cell_size


    def draw(self, surface):
        """draw the field"""
        for x, rect in enumerate(self.cells):
            color = "#ff33cc"  # pink
            if x % 2 == 0:
                color = "#ff99e6"  # lighter pink
            draw.rect(surface, color, rect) #Rect(100, 135, 45, 45))



    def test(self):
        """TODO: Remove after use."""
        print(self.rows, self.cols)
        print(self._top_edge)
        print(self._left_edge)



