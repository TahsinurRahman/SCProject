import speech_recognition as sr
import playsound
import os
from gtts import gTTS

r = sr.Recognizer()

with sr.Microphone() as source:
    print("say something")
    audio = r.listen(source)
    print("time over")  


foo = r.recognize_google(audio, language="bn-BD")
print("text: " + foo)

qs = "আমার নাম কি"
if foo == qs:
    ans = "তোমার নাম প্রান্ত"
else:
    ans = "😂😂😂😂😂😂"

print(ans)

tts = gTTS(text=ans, lang='bn')
tts.save("good.mp3")
os.system("mpg321 good.mp3")
playsound.playsound('good.mp3', True)