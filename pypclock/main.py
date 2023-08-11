import helpers
import curses
from clock import Clock


# Curses setup
screen = curses.initscr()
curses.curs_set(0)

def main(screen):
    screen.clear()
    screen.refresh()

    args = helpers.arg_checker()
    Clock.start(args.minutes[0], screen)
        
curses.wrapper(main)
