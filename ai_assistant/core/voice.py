import os
from gtts import gTTS
from playsound import playsound
import speech_recognition as sr
import whisper

recognizer = sr.Recognizer()
model = whisper.load_model("base")


def speak(text):

    try:
        tts = gTTS(text=text, lang="en")
        tts.save("voice.mp3")
        playsound("voice.mp3")
        os.remove("voice.mp3")

    except Exception as e:
        print("Speech Error:", e)


def listen():

    try:

        with sr.Microphone() as source:

            recognizer.adjust_for_ambient_noise(source, duration=1)

            audio = recognizer.listen(
                source,
                timeout=10,
                phrase_time_limit=10
            )

        with open("voice.wav", "wb") as f:
            f.write(audio.get_wav_data())

        result = model.transcribe("voice.wav")

        os.remove("voice.wav")

        return result["text"]

    except sr.WaitTimeoutError:
        return None

    except Exception as e:
        print(e)
        return None