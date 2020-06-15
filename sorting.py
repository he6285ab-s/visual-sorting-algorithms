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
        elif sorting_type == "quick":
            self._quick_sort(
                0, len(self.numbers) - 1
            )  # need parameters due to recursive method
            self.win.draw_list(self.numbers, c.SORTED_LINE_COLOR)
        elif sorting_type == "shell":
            self._shell_sort()
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
                min_index, self.numbers[min_index], c.MIN_OR_PIVOT_COLOR
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
                    self.win.redraw_line(j, self.numbers[j], c.MIN_OR_PIVOT_COLOR)
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

    def _quick_sort(self, low, high):
        """Performs a quick sort on the list."""
        # Since method is recursive, need to check this
        # to find when recursion should end.
        if low < high:

            index = self._partition(low, high)

            # Recursively call on both halves
            self._quick_sort(low, index - 1)
            self._quick_sort(index + 1, high)

    def _partition(self, low, high):
        """Partitions the array, using the last value as a pivot."""
        i = low - 1
        pivot = self.numbers[high]

        self.win.redraw_line(high, self.numbers[high], c.MIN_OR_PIVOT_COLOR)

        for j in range(low, high):
            # Increment partition index if value less/equal to pivot
            # and swap the smaller/equal values to the left of partition index
            self.win.redraw_line(j, self.numbers[j], c.CHECK_LINE_COLOR)
            if self.numbers[j] <= pivot:
                i += 1
                self.numbers[i], self.numbers[j] = self.numbers[j], self.numbers[i]
                self.win.redraw_line(i, self.numbers[i])
                self.win.redraw_line(j, self.numbers[j])
                time.sleep(0.05)
            self.win.redraw_line(j, self.numbers[j])

        self.numbers[i + 1], self.numbers[high] = (
            self.numbers[high],
            self.numbers[i + 1],
        )
        self.win.redraw_line(i + 1, self.numbers[i + 1])
        self.win.redraw_line(high, self.numbers[high])
        time.sleep(0.05)

        return i + 1

    def _shell_sort(self):
        n = len(self.numbers)
        gap = n // 2

        while gap > 0:
            for i in range(gap, n):
                temp = self.numbers[i]
                j = i
                while j >= gap and self.numbers[j - gap] > temp:
                    self.numbers[j] = self.numbers[j - gap]
                    self.win.redraw_line(j, self.numbers[j])
                    j -= gap
                self.numbers[j] = temp
                self.win.redraw_line(j, self.numbers[j])
                self.win.redraw_line(i, self.numbers[i])
                time.sleep(0.05)
            gap //= 2
        
        self.win.draw_list(self.numbers, 'green')