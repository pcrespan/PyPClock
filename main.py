import sys


def main():
    arguments = sys.argv[1:]
    minutes = int(arguments[0])
    break_duration = arguments[1]
    total = arguments[2]

        
def print_timer(minutes, seconds):
        print("{}:{}".format(minutes, seconds))

if __name__ == "__main__":
    main()
