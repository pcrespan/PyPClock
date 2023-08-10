import argparse

def arg_checker():
    parser = argparse.ArgumentParser(
            prog='PyPClock',
            description='Pomodoro clock with curses interface'
            )
    parser.add_argument('minutes', type=int, action='store', nargs=1, metavar='m', help='minutes')
    parser.add_argument('break_duration', type=int, action='store', nargs=1, metavar='d', help='break duration')
    parser.add_argument('sessions', type=int, action='store', nargs=1, metavar='s', help='number of sessions')
    args = parser.parse_args()
    return args
