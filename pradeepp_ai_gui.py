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

# =========================
# AI RESPONSE
# =========================

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

# =========================
# SEND MESSAGE
# =========================

def send_message():

    user_message = entry.get().strip()

    if not user_message:
        return

    chat_box.insert(
        tk.END,
        f"You: {user_message}\n\n"
    )

    chat_box.see(tk.END)

    entry.delete(0, tk.END)

    answer = ask_ai(user_message)

    chat_box.insert(
        tk.END,
        f"Bot: {answer}\n\n"
    )

    chat_box.see(tk.END)

    threading.Thread(
        target=speak,
        args=(answer,),
        daemon=True
    ).start()

# =========================
# VOICE INPUT
# =========================

def listen_voice():

    try:

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

        if os.path.exists("voice.wav"):

            os.remove("voice.wav")

        chat_box.insert(
            tk.END,
            f"You 🎤: {command}\n\n"
        )

        chat_box.see(tk.END)

        answer = ask_ai(command)

        chat_box.insert(
            tk.END,
            f"Bot: {answer}\n\n"
        )

        chat_box.see(tk.END)

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

chat_box.insert(
    tk.END,
    "System: Assistant Ready\n\n"
)

root.mainloop()