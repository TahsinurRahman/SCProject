import speech_recognition as sr
import playsound
import os
from gtts import gTTS

r = sr.Recognizer()

with sr.Microphone() as source:
    print("say something")
    audio = r.listen(source)
    print("time over")  


collected_audio = r.recognize_google(audio, language="bn-BD")
print("text: " + collected_audio)

qs = "আমার নাম কি"
if qs in collected_audio:
    ans = "তোমার নাম তাহসিন"
elif collected_audio == "তোমার নাম কি":
    ans = "আমার নাম তুফান"
else:
    ans = "আমি কিছু বুঝিনি"

print(ans)

tts = gTTS(text=ans, lang='bn')
tts.save("good.mp3")
os.system("mpg321 good.mp3")
playsound.playsound('good.mp3', True)