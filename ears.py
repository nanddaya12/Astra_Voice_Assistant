import speech_recognition as sr
import sounddevice as sd


def listen():
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Listening...")
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source, timeout=8)
        return r.recognize_google(audio)
    except sr.UnknownValueError:
        return ""
    except sr.RequestError:
        return "Connection Error"
    except Exception as e:
        print(f"Listening error: {e}")
        return ""