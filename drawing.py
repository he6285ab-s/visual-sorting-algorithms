from graphics import *

class window:
    """Handles the window and the drawing/redrawing of the lines representing numbers."""

    def __init__(self, title):
        self.win = GraphWin(title=title, width=800, height=800)
        self.win.setCoords(
            -1, -1, 100, 100
        )  # bottom left is (-1, -1); top right is (100, 100)

    def close(self):
        self.win.close()

    def draw_list(self, list):
        """Draw's the entire list to the window."""
        for i, number in enumerate(list, 0):
            temp_line = Line(Point(i, 0), Point(i, number))
            temp_line.setWidth(5)
            temp_line.draw(self.win)

    def redraw_bubble(self, first, second, list):
        """Does efficient redrawing swap for bubble sort."""
        # Second line is always bigger after a swap in bubble sort:

        # -> only extending the current second
        self.redraw_line_partly(
            second, list[first] - 1, list[second]
        )

        # -> only shortening current first
        self.redraw_line_partly(
            first, list[first], list[second] + 1, "white"
        )

    def redraw_line_partly(self, index, lowest, highest, color="black"):
        """Redraws a line partly between two values."""
        temp_line = Line(Point(index, lowest), Point(index, highest))
        temp_line.setOutline(color)
        temp_line.setWidth(5)
        temp_line.draw(self.win)
        del(temp_line)

    def redraw_line_completely(self, index, value, color="black"):
        """Completely erases and redraws a line to the value."""
        temp_white_line = Line(Point(index, 0), Point(index, 200))
        temp_white_line.setOutline("white")
        temp_white_line.setWidth(5)
        temp_white_line.draw(self.win)
        del(temp_white_line)

        temp_line = Line(Point(index, 0), Point(index, value))
        temp_line.setOutline(color)
        temp_line.setWidth(5)
        temp_line.draw(self.win)
        del(temp_line)

