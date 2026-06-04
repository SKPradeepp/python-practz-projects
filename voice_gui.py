import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import whisper
import ollama
import os
import time
from datetime import datetime

# Load Whisper model
model = whisper.load_model("medium")

# Speech recognizer
recognizer = sr.Recognizer()

# Chat memory
chat_history = [
    {
        "role": "system",
        "content": "You are Pradeepp's friendly AI voice assistant. Give concise and helpful answers."
    }
]


def speak(text):

    print("Bot:", text)

    try:

        filename = f"voice_{int(time.time())}.mp3"

        tts = gTTS(text=text, lang="en")

        tts.save(filename)

        playsound(filename)

        time.sleep(0.5)

        if os.path.exists(filename):
            os.remove(filename)

    except Exception as e:

        print("Speech Error:", e)


def ask_ai(prompt):

    try:

        chat_history.append(
            {
                "role": "user",
                "content": prompt
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

        # Keep only recent conversation
        if len(chat_history) > 12:
            del chat_history[1:3]

        return answer

    except Exception as e:

        print("Ollama Error:", e)

        return "Sorry, I cannot connect to Ollama."


print("===== Pradeepp AI Assistant Started =====")

speak("Assistant started")

while True:

    try:

        with sr.Microphone() as source:

            print("\nListening...")

            recognizer.adjust_for_ambient_noise(
                source,
                duration=0.5
            )

            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=10
            )

        print("Recognizing...")

        with open("voice.wav", "wb") as f:
            f.write(audio.get_wav_data())

        result = model.transcribe("voice.wav")

        command = result["text"].lower().strip()

        command = (
            command.replace(".", "")
                   .replace("!", "")
                   .replace("?", "")
                   .strip()
        )

        print("You said:", command)

        if not command:

            continue

        # EXIT
        if (
            "bye" in command
            or "goodbye" in command
            or "exit" in command
            or "stop" in command
        ):

            speak("Goodbye Pradeepp")

            break

        # HELLO
        elif "hello" in command or "hi" in command:

            speak("Hello Pradeepp. How can I help you?")

        # TIME
        elif "time" in command:

            current_time = datetime.now().strftime("%H:%M")

            speak(f"The current time is {current_time}")

        # DATE
        elif "date" in command:

            current_date = datetime.now().strftime("%d %B %Y")

            speak(f"Today's date is {current_date}")

        # EVERYTHING ELSE → OLLAMA
        else:

            answer = ask_ai(command)

            print("\nAI Response:\n")

            print(answer)

            speak(answer[:500])

        if os.path.exists("voice.wav"):

            os.remove("voice.wav")

    except sr.WaitTimeoutError:

        print("No speech detected")

    except KeyboardInterrupt:

        print("\nAssistant closed manually")

        break

    except Exception as e:

        print("Error:", e)

        if os.path.exists("voice.wav"):

            os.remove("voice.wav")