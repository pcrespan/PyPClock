import subprocess


def play_alarm():
    subprocess.call(["ffplay", "-nodisp", "-autoexit", "-loglevel", "8", "./analog_watch.wav"])
