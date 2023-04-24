# This program works according to the user's input where the user chooses either
# 1-->to change speech to text or
# 2-->to change text to speech


import speech_recognition as sr
from gtts import gTTS
import pyaudio
print("Press 1 for Speech to Text")
print("Press 2 for Text to Speech")
txt="Hello, world!"
n=int(input())
if n==1:
    with sr.Microphone() as source:
        print("Please Speak ----------")
        file=sr.Recognizer().listen(source)
        print(sr.Recognizer().recognize_google(file))
if n==2:
    print("Type the text that you want to change to audio")
    txt=input()
    try:
        file=gTTS(text=txt, lang="en", slow=False)
        file.save("Text_to_audio.mp3")
    except:
        print("Since you did not enter any text the default text will be --- Hello, world!")
        txt="Hello, world"
        file=gTTS(text=txt, lang="en", slow=False)
        file.save("Text_to_audio.mp3")