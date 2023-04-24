from gtts import gTTS
txt="Hello, world! Let me know what you are doing"
speech=gTTS(text=txt, lang="en", slow=False)
speech.save("Text_to_Speech.mp3")
print("done")