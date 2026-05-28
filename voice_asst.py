import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import whisper
import os
from datetime import datetime

# Load Whisper model
model = whisper.load_model("base")

# Speech recognizer
recognizer = sr.Recognizer()


# Speak function
def speak(text):

    print("Bot:", text)

    tts = gTTS(text=text, lang="en")

    tts.save("voice.mp3")

    playsound("voice.mp3")

    os.remove("voice.mp3")


print("===== Pradeep Voice Assistant Started =====")

while True:

    try:

        # Use microphone
        with sr.Microphone() as source:

            print("\nListening...")

            recognizer.adjust_for_ambient_noise(source, duration=1)

            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=5
            )

            print("Recognizing...")

            # Save temporary audio
            with open("voice.wav", "wb") as f:

                f.write(audio.get_wav_data())

        # Whisper recognition
        result = model.transcribe("voice.wav")

        command = result["text"].lower().strip()

        command = command.replace(".", "").replace("!", "")

        print("You said:", command)

        # Commands
        if "hello" in command:

            speak("Hello Pradeep")

        elif "how are you" in command:

            speak("I am doing great")

        elif "time" in command:

            current_time = datetime.now().strftime("%H:%M")

            speak("Current time is " + current_time)

        elif "date" in command:

            current_date = datetime.now().strftime("%d %B %Y")

            speak("Today's date is " + current_date)

        elif "bye" in command or "exit" in command or "stop" in command:

            speak("Goodbye Pradeep")

            print("Assistant stopped.")

            if os.path.exists("voice.wav"):

                os.remove("voice.wav")

            break

        else:

            print("Unknown command")

        # Remove temp file
        if os.path.exists("voice.wav"):

            os.remove("voice.wav")

    except sr.WaitTimeoutError:

        print("No speech detected")

    except KeyboardInterrupt:

        print("\nAssistant closed manually")

        break

    except Exception as e:

        print("Error:", e)