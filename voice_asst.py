import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import whisper
import wikipedia
import webbrowser
import os
from datetime import datetime

# Load Whisper model
model = whisper.load_model("tiny")

# Speech recognizer
recognizer = sr.Recognizer()


def speak(text):
    print("Bot:", text)

    tts = gTTS(text=text, lang="en")
    tts.save("voice.mp3")

    playsound("voice.mp3")

    if os.path.exists("voice.mp3"):
        os.remove("voice.mp3")


print("===== Pradeep Voice Assistant Started =====")

while True:

    try:

        with sr.Microphone() as source:

            print("\nListening...")

            recognizer.adjust_for_ambient_noise(
                source,
                duration=1
            )

            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=5
            )

            print("Recognizing...")

            with open("voice.wav", "wb") as f:
                f.write(audio.get_wav_data())

        result = model.transcribe("voice.wav")

        command = result["text"].lower().strip()

        command = command.replace(".", "")
        command = command.replace("!", "")

        print("You said:", command)

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

                with open("memory.txt", "a") as f:
                    f.write(data + "\n")

                speak("I will remember that")

            else:

                speak("Tell me what to remember")

        # MEMORY SHOW
        elif "what do you remember" in command:

            try:

                with open("memory.txt", "r") as f:
                    data = f.read()

                if data.strip():

                    speak(data)

                else:

                    speak("I do not remember anything yet")

            except:

                speak("Memory file not found")

        # NOTE SAVE
        elif command.startswith("take note"):

            note = command.replace(
                "take note",
                ""
            ).strip()

            if note:

                with open("notes.txt", "a") as f:
                    f.write(note + "\n")

                speak("Note saved")

            else:

                speak("Please tell me what note to save")

        # SHOW NOTES
        elif "show notes" in command:

            try:

                with open("notes.txt", "r") as f:
                    notes = f.read()

                if notes.strip():

                    speak(notes)

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

                speak(
                    "Searching Google for " + query
                )

            else:

                speak(
                    "Please tell me what to search"
                )

        # WIKIPEDIA
        elif command.startswith("who is"):

            person = command.replace(
                "who is",
                ""
            ).strip()

            try:

                result = wikipedia.summary(
                    person,
                    sentences=2
                )

                speak(result)

            except:

                speak(
                    "Could not find information"
                )

        # OPEN YOUTUBE
        elif "youtube" in command:

            webbrowser.open(
                "https://www.youtube.com"
            )

            speak("Opening YouTube")

        # OPEN GOOGLE
        elif "google" in command:

            webbrowser.open(
                "https://www.google.com"
            )

            speak("Opening Google")

        # HELP
        elif "help" in command:

            speak(
                "Available commands are hello, time, date, remember, take note, show notes, search, who is, google, youtube and bye"
            )

        # EXIT
        elif (
            "bye" in command
            or "exit" in command
            or "stop" in command
        ):

            speak("Goodbye Pradeepp")

            print("Assistant stopped.")

            if os.path.exists("voice.wav"):
                os.remove("voice.wav")

            break

        else:

            speak("I did not understand that")

        if os.path.exists("voice.wav"):
            os.remove("voice.wav")

    except sr.WaitTimeoutError:

        print("No speech detected")

    except KeyboardInterrupt:

        print("\nAssistant closed manually")

        break

    except Exception as e:

        print("Error:", e)