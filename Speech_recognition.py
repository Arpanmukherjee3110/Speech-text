import speech_recognition as sr
file=("Text_to_Speech.wav")
r=sr.Recognizer()
print("--------------------------------")
print("--------------------------------")
with sr.AudioFile("Text_to_Speech.wav") as source:
    audio=sr.Recognizer().record(source)
    try:
        print(r.recognize_google(audio))
    except sr.UnknownValueError:
        print("Speech recognition could not understand the data")
    except sr.RequestError:
        print("Request error")