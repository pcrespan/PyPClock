import curses
import pyfiglet
import time


class Interface:


    @staticmethod
    def get_clock_window():
        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)
        win = curses.newwin(curses.LINES // 4, 9 * curses.COLS // 40, 3 * curses.LINES // 8, 31 * curses.COLS // 80)
        win.bkgd(' ', curses.color_pair(1) | curses.A_BOLD | curses.A_REVERSE)
        return win

    @staticmethod
    def print_time(minutes, seconds, clock_window):
        WINDOW_LINES = curses.LINES // 2
        WINDOW_COLUMNS = curses.LINES // 2

        moment = pyfiglet.figlet_format("{}:{}".format(minutes, seconds))

        for index, line in enumerate(moment.split("\n")):
            clock_window.addstr(WINDOW_LINES + index, WINDOW_COLUMNS - len(line) // 2, line)
            clock_window.refresh()
        time.sleep(1)
        clock_window.clear()
