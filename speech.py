from gtts import gTTS
import playsound

mytext = 'আমার নাম তাহসিন'

language = 'bn'
output = gTTS(text=mytext, lang='bn', slow=False, lang_check=True)

output.save('output.mp3')
playsound.playsound('output.mp3', True)