from interface import Interface


class Clock:

    @staticmethod
    def start(minutes, total_sessions, clock_window):
            current_session = 1

            while current_session <= total_sessions:
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
                current_session += 1
