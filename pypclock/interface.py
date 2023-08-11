import curses
import math
import pyfiglet


class Interface:

    @staticmethod
    def get_clock_window():
        return curses.newwin(curses.LINES, curses.COLS, 0, 0)

    @staticmethod
    def print_time(minutes, seconds, clock_window):
        WINDOW_LINES = math.floor(curses.LINES / 2)
        WINDOW_COLUMNS = math.floor(curses.COLS / 2)

        time = pyfiglet.figlet_format("{}:{}".format(minutes, seconds))

        for index, line in enumerate(time.split("\n")):
            clock_window.clear()
            clock_window.addstr(WINDOW_LINES + index, WINDOW_COLUMNS, line)
            clock_window.refresh()
