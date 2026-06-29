import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import whisper
import ollama
import webbrowser
import os
import time
import subprocess
from datetime import datetime

# Load Whisper model
model = whisper.load_model("medium")

# Speech recognizer
recognizer = sr.Recognizer()


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


def ask_ai(question):

    try:

        response = ollama.chat(
            model="llama3.2",
            messages=[
                {
                    "role": "system",
                    "content":
                    "You are Pradeepp's personal voice assistant. Give short and useful spoken answers."
                },
                {
                    "role": "user",
                    "content": question
                }
            ]
        )

        return response["message"]["content"]

    except Exception as e:

        print("AI Error:", e)

        return "Sorry, I cannot connect to the AI model."


print("===== Pradeep Voice Assistant Started =====")

speak("Voice assistant started")

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

        command = command.replace(".", "")
        command = command.replace("!", "")
        command = command.replace("?", "")

        print("You said:", command)

        if command == "":
            continue

        # HELLO
        if "hello" in command or "hi" in command:

            speak("Hello Pradeepp")

        # HOW ARE YOU
        elif "how are you" in command:

            speak("I am doing great")

        # TIME
        elif "time" in command:

            current_time = datetime.now().strftime("%H:%M")

            speak("Current time is " + current_time)

        # DATE
        elif "date" in command:

            current_date = datetime.now().strftime("%d %B %Y")

            speak("Today's date is " + current_date)

        # MEMORY SAVE
        elif command.startswith("remember"):

            data = command.replace(
                "remember",
                ""
            ).strip()

            if data:

                with open("memory.txt", "a", encoding="utf-8") as f:
                    f.write(data + "\n")

                speak("I will remember that")

            else:

                speak("Tell me what to remember")

        # MEMORY SHOW
        elif "what do you remember" in command:

            try:

                with open(
                    "memory.txt",
                    "r",
                    encoding="utf-8"
                ) as f:

                    memory = f.read()

                if memory.strip():

                    speak(memory[:500])

                else:

                    speak("I do not remember anything")

            except:

                speak("Memory file not found")

        # NOTE SAVE
        elif command.startswith("take note"):

            note = command.replace(
                "take note",
                ""
            ).strip()

            if note:

                with open(
                    "notes.txt",
                    "a",
                    encoding="utf-8"
                ) as f:

                    f.write(note + "\n")

                speak("Note saved")

            else:

                speak("Please tell me what note to save")

        # SHOW NOTES
        elif "show notes" in command:

            try:

                with open(
                    "notes.txt",
                    "r",
                    encoding="utf-8"
                ) as f:

                    notes = f.read()

                if notes.strip():

                    speak(notes[:500])

                else:

                    speak("No notes found")

            except:

                speak("Notes file not found")

        # GOOGLE SEARCH
        elif command.startswith("search"):

            query = command.replace(
                "search",
                ""
            ).strip()

            if query:

                webbrowser.open(
                    f"https://www.google.com/search?q={query}"
                )

                speak("Searching Google for " + query)

        # OPEN GOOGLE
        elif "open google" in command:

            webbrowser.open(
                "https://www.google.com"
            )

            speak("Opening Google")

        # OPEN YOUTUBE
        elif "open youtube" in command:

            webbrowser.open(
                "https://www.youtube.com"
            )

            speak("Opening YouTube")

        # PLAY SONG
        elif command.startswith("play"):

            song = command.replace(
                "play",
                ""
            ).strip()

            if song:

                webbrowser.open(
                    f"https://www.youtube.com/results?search_query={song}"
                )

                speak("Playing " + song)

        # OPEN NOTEPAD
        elif "open notepad" in command:

            subprocess.Popen("notepad.exe")

            speak("Opening Notepad")

        # OPEN CALCULATOR
        elif "open calculator" in command:

            subprocess.Popen("calc.exe")

            speak("Opening Calculator")

        # OPEN VS CODE
        elif "open vs code" in command:

            try:

                subprocess.Popen(
                    r"C:\Users\Pradeepp\AppData\Local\Programs\Microsoft VS Code\Code.exe"
                )

                speak("Opening Visual Studio Code")

            except:

                speak("VS Code not found")

        # OPEN WHATSAPP
        elif "open whatsapp" in command:

            webbrowser.open(
                "https://web.whatsapp.com"
            )

            speak("Opening WhatsApp")

        # HELP
        elif "help" in command:

            speak(
                "You can ask me anything, open apps, search Google, save notes, remember things, play songs and more."
            )

        # EXIT
        elif (
            "bye" in command
            or "goodbye" in command
            or "exit" in command
            or "stop" in command
        ):

            speak("Goodbye Pradeepp")

            print("Assistant stopped")

            break

        # AI MODE
        else:

            answer = ask_ai(command)

            print("\nAI:", answer)

            speak(answer[:700])

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