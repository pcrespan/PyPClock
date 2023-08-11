import curses
import math
import pyfiglet
import time


class Interface:

    @staticmethod
    def print_time(minutes, seconds, clock_window):
        WINDOW_LINES = math.floor(curses.LINES / 2)
        WINDOW_COLUMNS = math.floor(curses.COLS / 2.3)

        moment = pyfiglet.figlet_format("{}:{}".format(minutes, seconds))

        for index, line in enumerate(moment.split("\n")):
            clock_window.addstr(WINDOW_LINES + index, WINDOW_COLUMNS, line)
            clock_window.refresh()
        time.sleep(1)
        clock_window.clear()
