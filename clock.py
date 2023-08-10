import time

class Clock:

    @staticmethod
    def start(self, minutes, total):
        seconds = 60
        first_minute = True

        for i in range(minutes, 0, -1):
            for j in range (seconds, 0, -1):
                if first_minute:
                    seconds = 0
                    self.print_timer(i, j)
                    time.sleep(1000)
                    seconds = 60
                    first_minute = False
                else:
                    self.print_timer(i, j)
                    time.sleep(1000)


    @staticmethod
    def print_timer(minutes, seconds):
        print("{}:{}".format(minutes, seconds))
