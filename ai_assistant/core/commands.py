import subprocess
import datetime


def open_notepad():
    subprocess.Popen("notepad.exe")


def open_calculator():
    subprocess.Popen("calc.exe")


def get_time():
    return datetime.datetime.now().strftime("%I:%M %p")


def get_date():
    return datetime.datetime.now().strftime("%d %B %Y")