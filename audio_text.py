import speech_recognition as sr
import pyaudio
with sr.Microphone() as source:
    file=sr.Recognizer().listen(source)
    print(sr.Recognizer().recognize_google(file))