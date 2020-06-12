from graphics import *
import random
import time


class sorting_window:
    """Holds the window and performs the sorting algorithms."""

    def __init__(self, title):
        # Set up the window and the list
        self.win = GraphWin(title=title, width=800, height=800)
        self.win.setCoords(
            -1, 0, 100, 100
        )  # bottom left is (-1, 0); top right is (100, 100)
        self.number_list = list(range(100))

    def loop(self, sorting_type):
        # Shuffle list and draw to screen
        random.shuffle(self.number_list)
        self._draw_list()

        if sorting_type == "bubble":
            self._bubble_sort()
        elif sorting_type == "insertion":
            self._insertion_sort()
        elif sorting_type == "selection":
            self._selection_sort()

        time.sleep(2.0)
        self.win.close()

    def _bubble_sort(self):
        """Performs a bubble sort and redraws window for each step."""
        n = len(self.number_list) - 1
        for i in range(n, 0, -1):
            for j in range(i):
                if self.number_list[j] > self.number_list[j + 1]:
                    self.number_list[j], self.number_list[j + 1] = (
                        self.number_list[j + 1],
                        self.number_list[j],
                    )
                    self._redraw_bubble(j, j + 1)
                n -= 1
                time.sleep(0.075)

    def _insertion_sort(self):
        """Performs an insertion sort and redraws window for each step."""
        for i in range(1, len(self.number_list)):
            j = i
            next_element = self.number_list[i]
            while self.number_list[j - 1] > next_element and j > 0:
                self.number_list[j] = self.number_list[j - 1]
                self._redraw_line_completely(j, self.number_list[j])
                self._redraw_line_completely(j - 1, next_element)
                time.sleep(0.05)
                j -= 1

            self.number_list[j] = next_element
            self._redraw_line_completely(j, self.number_list[j])

    def _selection_sort(self):
        """Performs a selection sort and redraws window for each step."""
        # Loop over every element and set the sorted ones to color green.
        for i in range(len(self.number_list)):
            self._redraw_line_completely(i, self.number_list[i], 'green')
            min_index = i
            self._redraw_line_completely(min_index, self.number_list[min_index], 'red')

            # Look for minimum value and set it to red
            # and set value that's currently being checked to yellow
            for j in range(i+1, len(self.number_list)):
                self._redraw_line_completely(j, self.number_list[j], 'yellow')
                time.sleep(0.05)

                # Recolor and reset minimum if value being checked is smaller, 
                # otherwise move on to the next one
                if self.number_list[min_index] > self.number_list[j]:
                    self._redraw_line_completely(min_index, self.number_list[min_index])
                    min_index = j
                    self._redraw_line_completely(j, self.number_list[j], 'red')
                else:
                    self._redraw_line_completely(j, self.number_list[j])

            # Swap and redraw if smaller value than current value
            # for current i has been found
            if i != min_index:
                self.number_list[i], self.number_list[min_index] = self.number_list[min_index], self.number_list[i]
                self._redraw_line_completely(i, self.number_list[i], 'green')
                self._redraw_line_completely(min_index, self.number_list[min_index])
            else:
                self._redraw_line_completely(i, self.number_list[i], 'green')
            time.sleep(0.075)

    # ------- HELP METHODS -------

    def _draw_list(self):
        """Draw's the entire list to the window."""
        for i, number in enumerate(self.number_list, 0):
            temp_line = Line(Point(i, 0), Point(i, number))
            temp_line.setWidth(5)
            temp_line.draw(self.win)

    def _redraw_bubble(self, first, second):
        """Does efficient redrawing swap for bubble sort."""
        # Second line is always bigger after a swap in bubble sort:

        # -> only extending the current second
        self._redraw_line_partly(
            second, self.number_list[first] - 1, self.number_list[second]
        )

        # -> only shortening current first
        self._redraw_line_partly(
            first, self.number_list[first], self.number_list[second] + 1, "white"
        )

    def _redraw_line_partly(self, index, lowest, highest, color="black"):
        """Redraws a line partly between two values."""
        temp_line = Line(Point(index, lowest), Point(index, highest))
        temp_line.setOutline(color)
        temp_line.setWidth(5)
        temp_line.draw(self.win)
        del(temp_line)

    def _redraw_line_completely(self, index, value, color="black"):
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
