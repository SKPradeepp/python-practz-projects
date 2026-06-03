import tkinter as tk
from tkinter import scrolledtext
from datetime import datetime
import ollama

def add_message(sender, message):
    chat_box.insert(tk.END, f"{sender}: {message}\n\n")
    chat_box.see(tk.END)


def start_assistant():

    status_label.config(text="Assistant Running")

    add_message("System", "Assistant Started")


def stop_assistant():

    status_label.config(text="Assistant Stopped")

    add_message("System", "Assistant Stopped")

def ask_ai(prompt):

    try:

        response = ollama.chat(
            model="llama3.2",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]

    except Exception as e:

        return "Sorry, I could not connect to Ollama"
    

def send_text():

    user_text = entry.get().strip()

    if not user_text:
        return

    add_message("You", user_text)

    entry.delete(0, tk.END)

    if "hello" in user_text.lower():

        reply = "Hello Pradeepp"

    elif "time" in user_text.lower():

        reply = "Current time is " + datetime.now().strftime("%H:%M")

    elif "date" in user_text.lower():

        reply = "Today's date is " + datetime.now().strftime("%d %B %Y")

    else:

        reply = ask_ai(user_text)

    add_message("Bot", reply)


# Main Window
root = tk.Tk()

root.title("Pradeepp AI Assistant")

root.geometry("800x600")


# Title
title_label = tk.Label(
    root,
    text="Pradeepp AI Assistant",
    font=("Arial", 18, "bold")
)

title_label.pack(pady=10)


# Status
status_label = tk.Label(
    root,
    text="Assistant Stopped",
    font=("Arial", 12)
)

status_label.pack()


# Chat Area
chat_box = scrolledtext.ScrolledText(
    root,
    wrap=tk.WORD,
    width=80,
    height=25
)

chat_box.pack(padx=10, pady=10, fill="both", expand=True)


# Input Frame
input_frame = tk.Frame(root)

input_frame.pack(fill="x", padx=10, pady=5)


entry = tk.Entry(
    input_frame,
    font=("Arial", 12)
)

entry.pack(side="left", fill="x", expand=True)


send_button = tk.Button(
    input_frame,
    text="Send",
    command=send_text
)

send_button.pack(side="left", padx=5)


# Buttons
button_frame = tk.Frame(root)

button_frame.pack(pady=10)


start_button = tk.Button(
    button_frame,
    text="Start Assistant",
    width=20,
    command=start_assistant
)

start_button.pack(side="left", padx=5)


stop_button = tk.Button(
    button_frame,
    text="Stop Assistant",
    width=20,
    command=stop_assistant
)

stop_button.pack(side="left", padx=5)


root.mainloop()