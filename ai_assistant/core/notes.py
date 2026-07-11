import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NOTES_FILE = os.path.join(BASE_DIR, "data", "notes.txt")


def save_note(note):

    with open(NOTES_FILE, "a", encoding="utf-8") as f:
        f.write(note + "\n")


def read_notes():

    if not os.path.exists(NOTES_FILE):
        return []

    with open(NOTES_FILE, "r", encoding="utf-8") as f:
        return f.readlines()