from drawing import window
import random
import time


class sorting:
    """Handles the sorting and calls on drawing methods."""

    def __init__(self, title):
        # Set up the window and the list
        self.win = window(title)
        self.number_list = list(range(1,101))

    def loop(self, sorting_type):
        # Shuffle list and draw to screen
        random.shuffle(self.number_list)
        self.win.draw_list(self.number_list)

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
                    self.win.redraw_bubble(j, j + 1, self.number_list)
                n -= 1
                time.sleep(0.075)

    def _insertion_sort(self):
        """Performs an insertion sort and redraws window for each step."""
        for i in range(1, len(self.number_list)):
            j = i
            next_element = self.number_list[i]
            
            # Find in currently sorted part where next_element fits
            while self.number_list[j - 1] > next_element and j > 0:
                self.number_list[j] = self.number_list[j - 1]
                self.win.redraw_line_completely(j, self.number_list[j])
                self.win.redraw_line_completely(j - 1, next_element)
                time.sleep(0.05)
                j -= 1

            self.number_list[j] = next_element
            self.win.redraw_line_completely(j, self.number_list[j])

    def _selection_sort(self):
        """Performs a selection sort and redraws window for each step."""
        # Loop over every element and set the sorted ones to color green.
        for i in range(len(self.number_list)):
            self.win.redraw_line_completely(i, self.number_list[i], 'green')
            min_index = i
            self.win.redraw_line_completely(min_index, self.number_list[min_index], 'red')

            # Look for minimum value and set it to red
            # and set value that's currently being checked to yellow
            for j in range(i+1, len(self.number_list)):
                self.win.redraw_line_completely(j, self.number_list[j], 'yellow')
                time.sleep(0.05)

                # Recolor and reset minimum if value being checked is smaller, 
                # otherwise move on to the next one
                if self.number_list[min_index] > self.number_list[j]:
                    self.win.redraw_line_completely(min_index, self.number_list[min_index])
                    min_index = j
                    self.win.redraw_line_completely(j, self.number_list[j], 'red')
                else:
                    self.win.redraw_line_completely(j, self.number_list[j])

            # Swap and redraw if smaller value than current value
            # for current i has been found
            if i != min_index:
                self.number_list[i], self.number_list[min_index] = self.number_list[min_index], self.number_list[i]
                self.win.redraw_line_completely(i, self.number_list[i], 'green')
                self.win.redraw_line_completely(min_index, self.number_list[min_index])
            else:
                self.win.redraw_line_completely(i, self.number_list[i], 'green')
            time.sleep(0.075)


    