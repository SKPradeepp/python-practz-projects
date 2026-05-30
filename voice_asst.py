import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import whisper
import os
from datetime import datetime
import webbrowser
import subprocess

# Load Whisper model
model = whisper.load_model("base")

# Speech recognizer
recognizer = sr.Recognizer()


def speak(text):

    print("Bot:", text)

    tts = gTTS(text=text, lang="en")

    tts.save("voice.mp3")

    playsound("voice.mp3")

    os.remove("voice.mp3")


print("===== Pradeep Voice Assistant Started =====")

while True:

    try:

        with sr.Microphone() as source:

            print("\nListening...")

            recognizer.adjust_for_ambient_noise(source, duration=1)

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

        command = command.replace(".", "").replace("!", "")

        print("You said:", command)

        # Greetings
        if "hello" in command or "hi" in command:

            speak("Hello Pradeep")

        elif "how are you" in command:

            speak("I am doing great")

        # Time
        elif "time" in command:

            current_time = datetime.now().strftime("%H:%M")

            speak("Current time is " + current_time)

        # Date
        elif "date" in command:

            current_date = datetime.now().strftime("%d %B %Y")

            speak("Today's date is " + current_date)

        # Memory Read
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

        # Memory Save
        elif "remember" in command:

            data = command.replace("remember", "").strip()

            if data == "":

                speak("Please tell me what to remember")

            else:

                with open("memory.txt", "a") as f:

                    f.write(data + "\n")

                speak("I will remember that")

        # Notes Save
        elif "take note" in command or "take a note" in command:

            note = command.replace("take note", "")
            note = note.replace("take a note", "")
            note = note.strip()

            if note == "":

                speak("Please tell me what note to save")

            else:

                with open("notes.txt", "a") as f:

                    f.write(note + "\n")

                speak("Note saved")

        # Notes Show
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

        # Apps
        elif "open calculator" in command:

            subprocess.Popen("calc.exe")

            speak("Opening Calculator")

        elif "open notepad" in command:

            subprocess.Popen("notepad.exe")

            speak("Opening Notepad")

        elif "open paint" in command:

            subprocess.Popen("mspaint.exe")

            speak("Opening Paint")

        # Websites
        elif "open youtube" in command:

            webbrowser.open("https://www.youtube.com")

            speak("Opening YouTube")

        elif "open google" in command:

            webbrowser.open("https://www.google.com")

            speak("Opening Google")

        elif "open chat g p t" in command or "open chatgpt" in command:

            webbrowser.open("https://chatgpt.com")

            speak("Opening Chat GPT")

        # Exit
        elif (
            "bye" in command
            or "goodbye" in command
            or "exit" in command
            or "stop" in command
        ):

            speak("Goodbye Pradeep")

            print("Assistant stopped.")

            if os.path.exists("voice.wav"):

                os.remove("voice.wav")

            break

        else:

            print("Unknown command")

        # Cleanup
        if os.path.exists("voice.wav"):

            os.remove("voice.wav")

    except sr.WaitTimeoutError:

        print("No speech detected")

    except KeyboardInterrupt:

        print("\nAssistant closed manually")

        break

    except Exception as e:

        print("Error:", e)