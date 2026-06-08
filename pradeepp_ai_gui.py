import tkinter as tk
from tkinter import scrolledtext
import threading
import speech_recognition as sr
import whisper
import ollama
from gtts import gTTS
from playsound import playsound
import os
import time
import subprocess
import webbrowser
from datetime import datetime
import wikipedia

# =========================
# LOAD MODELS
# =========================

print("Loading Whisper...")

whisper_model = whisper.load_model("medium")

recognizer = sr.Recognizer()

chat_history = [
    {
        "role": "system",
        "content": "You are Pradeepp's personal AI assistant. Be friendly and helpful."
    }
]

# =========================
# SPEAK FUNCTION
# =========================

def speak(text):

    try:

        filename = f"voice_{int(time.time())}.mp3"

        tts = gTTS(
            text=text,
            lang="en"
        )

        tts.save(filename)

        playsound(filename)

        time.sleep(0.5)

        if os.path.exists(filename):
            os.remove(filename)

    except Exception as e:

        print("Speech Error:", e)
def search_wikipedia(query):

    try:

        results = wikipedia.search(
            query,
            results=5
        )

        if not results:

            return None

        summary = wikipedia.summary(
            results[0],
            sentences=3
        )

        return summary

    except Exception:

        return None
def is_fact_question(message):

    message = message.lower()

    fact_starters = [

        "who is",
        "what is",
        "where is",
        "when was",
        "when is",
        "tell me about",
        "define"

    ]

    return any(
        message.startswith(x)
        for x in fact_starters
    )

def ask_ai(message):

    try:

        chat_history.append(
            {
                "role": "user",
                "content": message
            }
        )

        response = ollama.chat(
            model="llama3.2",
            messages=chat_history
        )

        answer = response["message"]["content"]

        chat_history.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

        return answer

    except Exception as e:

        return f"Error: {e}"

def save_chat(sender, message):

    with open(
        "chat_history.txt",
        "a",
        encoding="utf-8"
    ) as f:

        time_now = datetime.now().strftime(
            "%d-%m-%Y %H:%M:%S"
        )

        f.write(
            f"[{time_now}] {sender}: {message}\n"
        )
def execute_command(command):

    command = command.lower()

    # Calculator
    if "open calculator" in command:

        subprocess.Popen("calc.exe")

        return "Opening Calculator"

    # Notepad
    elif "open notepad" in command:

        subprocess.Popen("notepad.exe")

        return "Opening Notepad"

    # Paint
    elif "open paint" in command:

        subprocess.Popen("mspaint.exe")

        return "Opening Paint"

    # CMD
    elif "open cmd" in command:

        subprocess.Popen("cmd.exe")

        return "Opening Command Prompt"

    # VS Code
    elif "open vs code" in command or "open vscode" in command:

        subprocess.Popen("code")

        return "Opening VS Code"

    # Google
    elif "open google" in command:

        webbrowser.open("https://www.google.com")

        return "Opening Google"

    # YouTube
    elif "open youtube" in command:

        webbrowser.open("https://www.youtube.com")

        return "Opening YouTube"

    # GitHub
    elif "open github" in command:

        webbrowser.open("https://github.com")

        return "Opening GitHub"

    # Gmail
    elif "open gmail" in command:

        webbrowser.open("https://mail.google.com")

        return "Opening Gmail"

    # Google Search
    elif command.startswith("search "):

        query = command.replace("search", "").strip()

        webbrowser.open(
            f"https://www.google.com/search?q={query}"
        )

        return f"Searching Google for {query}"

    # YouTube Search
    elif command.startswith("play "):

        song = command.replace("play", "").strip()

        webbrowser.open(
            f"https://www.youtube.com/results?search_query={song}"
        )

        return f"Playing {song}"

    return None
# =========================
# SEND MESSAGE
# =========================

def send_message():

    message = entry.get().strip()

    if message == "":
        return
    save_chat("You", message)
    chat_box.insert(
        tk.END,
        f"You: {message}\n\n"
    )

    chat_box.see(tk.END)

    entry.delete(0, tk.END)

    answer = execute_command(message)

    if answer is None:

        if is_fact_question(message):
            answer = search_wikipedia(message)

        if answer is None:
            answer = ask_ai(message)

    chat_box.insert(
        tk.END,
        f"Bot: {answer}\n\n"
    )

    chat_box.see(tk.END)

    save_chat("Bot", answer)
    threading.Thread(
        target=speak,
        args=(answer,),
        daemon=True
    ).start()
    if message.lower() in ["bye", "exit", "quit"]:
        speak("Goodbye Pradeepp")
        root.destroy()
        return

# =========================
# VOICE INPUT
# =========================

def listen_voice():

    try:

        status_label.config(
            text="Listening..."
        )

        chat_box.insert(
            tk.END,
            "System: Listening...\n\n"
        )

        chat_box.see(tk.END)

        with sr.Microphone() as source:

            recognizer.adjust_for_ambient_noise(
                source,
                duration=0.5
            )

            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=10
            )

        with open("voice.wav", "wb") as f:

            f.write(audio.get_wav_data())

        result = whisper_model.transcribe(
            "voice.wav"
        )

        command = result["text"].strip()
        save_chat("You", command)
        if os.path.exists("voice.wav"):

            os.remove("voice.wav")

        chat_box.insert(
            tk.END,
            f"You 🎤: {command}\n\n"
        )

        chat_box.see(tk.END)

        answer = execute_command(command)

        if answer is None:

            if is_fact_question(command):
                answer = search_wikipedia(command)

            if answer is None:
                answer = ask_ai(command)

        chat_box.insert(
            tk.END,
            f"Bot: {answer}\n\n"
        )

        save_chat("Bot", answer)
        chat_box.see(tk.END)

        if command.lower() in ["bye", "exit", "quit"]:
            speak("Goodbye Pradeepp")
            root.destroy()
            return
        speak(answer)

    except Exception as e:

        chat_box.insert(
            tk.END,
            f"Error: {e}\n\n"
        )

        chat_box.see(tk.END)

# =========================
# THREAD FOR MIC BUTTON
# =========================

def start_voice_thread():

    threading.Thread(
        target=listen_voice,
        daemon=True
    ).start()

# =========================
# GUI
# =========================

root = tk.Tk()

root.title("Pradeepp AI Assistant")

root.geometry("1000x700")

title = tk.Label(
    root,
    text="🤖 Pradeepp AI Assistant",
    font=("Arial", 20, "bold")
)

title.pack(pady=10)

chat_box = scrolledtext.ScrolledText(
    root,
    wrap=tk.WORD,
    font=("Arial", 11)
)

chat_box.pack(
    padx=10,
    pady=10,
    fill="both",
    expand=True
)

bottom_frame = tk.Frame(root)

bottom_frame.pack(
    fill="x",
    padx=10,
    pady=10
)

entry = tk.Entry(
    bottom_frame,
    font=("Arial", 12)
)

entry.pack(
    side="left",
    fill="x",
    expand=True,
    padx=5
)

send_button = tk.Button(
    bottom_frame,
    text="Send",
    command=send_message,
    width=10
)

send_button.pack(
    side="left",
    padx=5
)

mic_button = tk.Button(
    bottom_frame,
    text="🎤 Speak",
    command=start_voice_thread,
    width=12
)

mic_button.pack(
    side="left",
    padx=5
)
clear_button = tk.Button(
    bottom_frame,
    text="Clear",
    command=lambda: chat_box.delete("1.0", tk.END),
    width=10
)

clear_button.pack(
    side="left",
    padx=5
)
chat_box.insert(
    tk.END,
    "System: Assistant Ready\n\n"
)
entry.bind(
    "<Return>",
    lambda event: send_message()
)

root.configure(bg="#1e1e1e")

chat_box.configure(
    bg="#252526",
    fg="white",
    insertbackground="white"
)

entry.configure(
    bg="#3c3c3c",
    fg="white",
    insertbackground="white"
)
status_label = tk.Label(
    root,
    text="Ready",
    bg="#1e1e1e",
    fg="lightgreen",
    font=("Arial", 10)
)
status_label.pack(pady=5)
root.mainloop()