import subprocess
import datetime
import webbrowser

def open_notepad():
    subprocess.Popen("notepad.exe")

def open_calculator():
    subprocess.Popen("calc.exe")

def get_time():
    return datetime.datetime.now().strftime("%I:%M %p")

def get_date():
    return datetime.datetime.now().strftime("%d %B %Y")

def open_youtube():
    webbrowser.open("https://www.youtube.com")

def open_google():
    webbrowser.open("https://www.google.com")

def open_github():
    webbrowser.open("https://github.com")

def open_chatgpt():
    webbrowser.open("https://chat.openai.com")

def search_google(query):

    url = "https://www.google.com/search?q=" + query

    webbrowser.open(url)