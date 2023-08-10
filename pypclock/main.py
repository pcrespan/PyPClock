import sys
import helpers
from clock import Clock


def main():
    args = helpers.arg_checker()
    Clock.start(args.minutes[0])
        
def print_timer(minutes, seconds):
        print("{}:{}".format(minutes, seconds))

if __name__ == "__main__":
    main()
