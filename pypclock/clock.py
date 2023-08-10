import time

class Clock:

    @staticmethod
    def start(minutes):
            first_minute = True
            i = minutes
            j = 60

            while i >= 0:
                while j >= 0:
                    if first_minute:
                        j = 0
                        Clock.print_timer(i, j)
                        i -= 1
                        j = 60
                        first_minute = False
                    else:
                        Clock.print_timer(i, j)
                    j -= 1
                i -= 1
                j = 59


    @staticmethod
    def print_timer(minutes, seconds):
        print("{}:{}".format(minutes, seconds))
