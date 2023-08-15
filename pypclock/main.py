import helpers
import curses
import interface
from clock import Clock
from curses.textpad import rectangle
import time


args = helpers.arg_checker()

# Curses setup
screen = curses.initscr()
curses.curs_set(0)

def main(screen):
    screen.clear()

    #rectangle(screen, curses.LINES // 3, 3 * curses.COLS // 8, 3 * curses.LINES // 4, 3 * curses.COLS // 5)
    #screen.refresh()
    win = interface.Interface.get_clock_window()
    win.clear()

    sessions_window = interface.Interface.get_sessions_window()
    sessions_window.clear()

    minutes = args.minutes[0]
    break_duration = args.break_duration[0]
    total_sessions = args.sessions[0]
    current_session = 1

    while current_session <= total_sessions:
        interface.Interface.print_session(current_session, total_sessions, sessions_window)
        Clock.start(minutes, win)
        if current_session != total_sessions:
            Clock.break_time(break_duration, win)
        current_session += 1

        
curses.wrapper(main)
