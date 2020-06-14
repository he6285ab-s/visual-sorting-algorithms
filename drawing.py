from graphics import *
import colors as c


class window:
    """Handles the window and the drawing/redrawing of the lines representing numbers."""

    def __init__(self, title):
        self.win = GraphWin(title=title, width=816, height=816)
        self.win.setCoords(
            -1, -1, 101, 101
        )  # bottom left is (-1, -1); top right is (100, 100)
        self.win.setBackground(c.BKG_COLOR)

    def close(self):
        self.win.close()

    def draw_list(self, list):
        """Draw's the entire list to the window."""
        for i, number in enumerate(list, 0):
            temp_line = Line(Point(i, 0), Point(i, number))
            temp_line.setWidth(5)
            temp_line.setOutline(c.BASE_LINE_COLOR)
            temp_line.draw(self.win)

    def redraw_line(self, index, value, color=c.BASE_LINE_COLOR):
        """Completely erases and redraws a line to the value."""
        temp_white_line = Line(Point(index, 0), Point(index, 200))
        temp_white_line.setOutline(c.BKG_COLOR)
        temp_white_line.setWidth(5)
        temp_white_line.draw(self.win)

        temp_line = Line(Point(index, 0), Point(index, value))
        temp_line.setOutline(color)
        temp_line.setWidth(5)
        temp_line.draw(self.win)
