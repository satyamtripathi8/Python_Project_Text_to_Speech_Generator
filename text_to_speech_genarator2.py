from gtts import gTTS
x=input("Enter text you want to give voice:")
Language = 'en'
obj = gTTS(text=x,lang=Language,slow=False)
obj.save(f"{x[:2]}.mp3")