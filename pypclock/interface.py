import curses
import math


class Interface:

    @staticmethod
    def get_clock_window():
        return curses.newwin(curses.LINES, curses.COLS, 0, 0)

    @staticmethod
    def print_time(minutes, seconds, clock_window):
            clock_window.addstr(math.floor(curses.LINES / 2), math.floor(curses.COLS / 2), "{}:{}".format(minutes, seconds))
            clock_window.refresh()
