from interface import Interface
from sound import play_alarm


class Clock:

    @staticmethod
    def start(minutes, clock_window):
            first_minute = True
            i = minutes
            j = 60

            while i >= 0:
                while j >= 0:
                    if first_minute:
                        j = 0
                        Interface.print_time(i, j, clock_window)
                        i -= 1
                        j = 60
                        first_minute = False
                    else:
                        Interface.print_time(i, j, clock_window)
                    j -= 1
                i -= 1
                j = 59
            play_alarm()


    @staticmethod
    def break_time(break_duration, clock_window):
        Clock.start(break_duration, clock_window)
