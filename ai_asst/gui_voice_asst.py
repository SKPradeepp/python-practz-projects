import tkinter as tk
from tkinter import scrolledtext
import speech_recognition as sr
import whisper
from gtts import gTTS
from playsound import playsound
import os
from datetime import datetime
import webbrowser

# Load Whisper model
model = whisper.load_model("base")

recognizer = sr.Recognizer()

# ---------------- SPEAK ----------------
def speak(text):
    chat_area.insert(tk.END, "Bot: " + text + "\n")
    chat_area.yview(tk.END)

    try:
        tts = gTTS(text=text, lang="en")
        tts.save("voice.mp3")
        playsound("voice.mp3")
        os.remove("voice.mp3")
    except:
        chat_area.insert(tk.END, "Bot: Speech error\n")


# ---------------- COMMAND PROCESS ----------------
def process(command):
    command = command.lower().strip()

    if "hello" in command:
        speak("Hello Pradeep!")

    elif "time" in command:
        time = datetime.now().strftime("%H:%M")
        speak("Current time is " + time)

    elif "date" in command:
        date = datetime.now().strftime("%d %B %Y")
        speak("Today's date is " + date)

    elif "youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://youtube.com")

    elif "google" in command:
        speak("Opening Google")
        webbrowser.open("https://google.com")

    elif "instagram" in command:
        speak("Opening Instagram")
        webbrowser.open("https://instagram.com")

    elif "joke" in command:
        speak("Why did the computer go to therapy? Because it had too many bugs!")

    elif "bye" in command or "exit" in command:
        speak("Goodbye Pradeep!")
        root.destroy()

    else:
        speak("I did not understand")


# ---------------- TEXT INPUT ----------------
def send():
    text = entry.get()
    entry.delete(0, tk.END)

    chat_area.insert(tk.END, "You: " + text + "\n")
    process(text)


# ---------------- VOICE INPUT (FIXED) ----------------
def voice_input():
    try:
        with sr.Microphone() as source:
            chat_area.insert(tk.END, "Listening...\n")
            chat_area.yview(tk.END)

            recognizer.adjust_for_ambient_noise(source, duration=1)

            # SAFE LISTEN (no crash)
            audio = recognizer.listen(source, timeout=10, phrase_time_limit=10)

        chat_area.insert(tk.END, "Recognizing...\n")

        with open("voice.wav", "wb") as f:
            f.write(audio.get_wav_data())

        result = model.transcribe("voice.wav")
        command = result["text"]

        os.remove("voice.wav")

        chat_area.insert(tk.END, "You (voice): " + command + "\n")
        process(command)

    except sr.WaitTimeoutError:
        chat_area.insert(tk.END, "Bot: No speech detected. Try again.\n")

    except Exception as e:
        chat_area.insert(tk.END, "Error: " + str(e) + "\n")


# ---------------- GUI ----------------
root = tk.Tk()
root.title("Pradeep AI Assistant")
root.geometry("520x620")
root.config(bg="black")

chat_area = scrolledtext.ScrolledText(
    root, wrap=tk.WORD, bg="black", fg="lime", font=("Arial", 12)
)
chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(padx=10, pady=5, fill=tk.X)

send_btn = tk.Button(root, text="Send", command=send, bg="green", fg="white")
send_btn.pack(pady=5)

voice_btn = tk.Button(root, text="🎤 Speak", command=voice_input, bg="blue", fg="white")
voice_btn.pack(pady=5)

exit_btn = tk.Button(root, text="Exit", command=root.destroy, bg="red", fg="white")
exit_btn.pack(pady=5)

root.mainloop()