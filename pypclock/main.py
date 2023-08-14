import helpers
import curses
import interface
from clock import Clock
from curses.textpad import rectangle
import time


# Curses setup
screen = curses.initscr()
curses.curs_set(0)

def main(screen):
    args = helpers.arg_checker()
    screen.clear()

    #rectangle(screen, curses.LINES // 3, 3 * curses.COLS // 8, 3 * curses.LINES // 4, 3 * curses.COLS // 5)
    #screen.refresh()
    win = interface.Interface.get_clock_window()
    win.clear()
    Clock.start(args.minutes[0], win)
        
curses.wrapper(main)
