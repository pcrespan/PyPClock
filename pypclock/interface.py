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
    def get_sessions_window():
        curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)
        sessions_win = curses.newwin(2, 40)
        sessions_win.bkgd(' ', curses.color_pair(1) | curses.A_BOLD | curses.A_REVERSE)
        return sessions_win

    @staticmethod
    def print_session(current_session, total_sessions, session_win):
        session_win.addstr(1, 1, "Session {}/{}".format(current_session, total_sessions))
        session_win.refresh()


    @staticmethod
    def print_time(minutes, seconds, clock_window):

        BEGIN_COLUMN = 7
        moment = pyfiglet.figlet_format(Interface.format_time(minutes, seconds))

        for index, line in enumerate(moment.split("\n")):
            clock_window.addstr(index + 2, BEGIN_COLUMN, line)
            clock_window.refresh()
        time.sleep(1)
        clock_window.clear()

    @staticmethod
    def format_time(minutes, seconds):
        if minutes < 10:
            minutes = str("0" + str(minutes))
        if seconds < 10:
            seconds = str("0" + str(seconds))
        return str(minutes) + ":" + str(seconds)
