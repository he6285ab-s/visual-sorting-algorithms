from drawing import window
import colors as c
import random
import time


class sorting:
    """Handles the sorting and calls on drawing methods."""

    def __init__(self, title):
        # Set up the window and the list
        self.win = window(title)
        self.numbers = list(range(1, 101))

    def loop(self, sorting_type):
        # Shuffle list and draw to screen
        random.shuffle(self.numbers)
        self.win.draw_list(self.numbers)

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
        n = len(self.numbers) - 1
        for i in range(n, 0, -1):
            for j in range(i):
                self.win.redraw_line(
                    j + 1, self.numbers[j + 1],
                )
                if self.numbers[j] > self.numbers[j + 1]:
                    # Swap if left one is bigger
                    self.numbers[j], self.numbers[j + 1] = (
                        self.numbers[j + 1],
                        self.numbers[j],
                    )

                    self.win.redraw_line(j, self.numbers[j], c.CHECK_LINE_COLOR)
                    self.win.redraw_line(j + 1, self.numbers[j + 1], c.CHECK_LINE_COLOR)
                n -= 1
                time.sleep(0.075)
                self.win.redraw_line(j, self.numbers[j])
            self.win.redraw_line(i, self.numbers[i], c.SORTED_LINE_COLOR)

    def _insertion_sort(self):
        """Performs an insertion sort and redraws window for each step."""
        for i in range(1, len(self.numbers)):
            j = i
            next_element = self.numbers[i]

            # Find in currently sorted part where next_element fits
            while self.numbers[j - 1] > next_element and j > 0:
                self.numbers[j] = self.numbers[j - 1]
                self.win.redraw_line(j, self.numbers[j])
                self.win.redraw_line(j - 1, next_element, c.CHECK_LINE_COLOR)
                time.sleep(0.05)
                self.win.redraw_line(j - 1, next_element)
                j -= 1

            self.numbers[j] = next_element
            self.win.redraw_line(j, self.numbers[j])

    def _selection_sort(self):
        """Performs a selection sort and redraws window for each step."""
        # Loop over every element and set the sorted ones to color green.
        for i in range(len(self.numbers)):
            self.win.redraw_line(i, self.numbers[i], c.SORTED_LINE_COLOR)
            min_index = i
            self.win.redraw_line(
                min_index, self.numbers[min_index], c.SEL_SORT_MIN_COLOR
            )

            # Look for minimum value and set it to red
            # and set value that's currently being checked to yellow
            for j in range(i + 1, len(self.numbers)):
                self.win.redraw_line(j, self.numbers[j], c.CHECK_LINE_COLOR)
                time.sleep(0.05)

                # Recolor and reset minimum if value being checked is smaller,
                # otherwise move on to the next one
                if self.numbers[min_index] > self.numbers[j]:
                    self.win.redraw_line(min_index, self.numbers[min_index])
                    min_index = j
                    self.win.redraw_line(j, self.numbers[j], c.SEL_SORT_MIN_COLOR)
                else:
                    self.win.redraw_line(j, self.numbers[j])

            # Swap and redraw if smaller value than current value
            # for current i has been found
            if i != min_index:
                self.numbers[i], self.numbers[min_index] = (
                    self.numbers[min_index],
                    self.numbers[i],
                )
                self.win.redraw_line(i, self.numbers[i], c.SORTED_LINE_COLOR)
                self.win.redraw_line(min_index, self.numbers[min_index])
            else:
                self.win.redraw_line(i, self.numbers[i], c.SORTED_LINE_COLOR)
            time.sleep(0.075)
