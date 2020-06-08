from graphics import *
import random
import time

class sorting_window:
    
    def __init__(self):
        # Set up the window
        self.win = GraphWin(width = 800, height = 800)
        self.win.setCoords(0, 0, 100, 100) # bottom left is (0, 0); top right is (200, 200)
        # Set up the list
        self.number_list = list(range(100))

    def loop(self, sorting_type):
        # Shuffle list and draw to screen
        random.shuffle(self.number_list)
        self._draw_list()

        if sorting_type == "bubble":
            self._bubble_sort()

        time.sleep(2.0)
        self.win.close()

    def _bubble_sort(self):    
        n = len(self.number_list) - 1
        for i in range(n, 0, -1):
            for j in range(i):
                if self.number_list[j] > self.number_list[j + 1]:
                    self.number_list[j], self.number_list[j + 1] = self.number_list[j + 1], self.number_list[j]
                    self._redraw(j, j+1)
                n-=1
                time.sleep(0.00)

    # ------- HELP METHODS -------

    # Draw current state of the list
    def _draw_list(self):
        for i, number in enumerate(self.number_list, 0):
            temp_line = Line(Point(i, 0), Point(i, number))
            temp_line.setWidth(5)
            temp_line.draw(self.win)

    # Redraw two lines when they have been swapped
    def _redraw(self, first, second): 

        # Second line is bigger:
        # -> only extending the current second
        temp_line = Line(Point(second, self.number_list[first] - 1), Point(second, self.number_list[second]))
        temp_line.setWidth(5)
        temp_line.draw(self.win) 

        # -> only shortening current first
        temp_white_line = Line(Point(first, self.number_list[first]), Point(first, self.number_list[second] + 1))
        temp_white_line.setWidth(5)
        temp_white_line.setOutline('white')
        temp_white_line.draw(self.win)
