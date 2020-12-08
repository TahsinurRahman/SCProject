import pandas
from gtts import gTTS
import speech_recognition as sr
import playsound

# read the csv file
df = pandas.read_csv('qa.csv')

questions = df['Questions'].to_list()
answers = df['Answers'].to_list()


def play_audio(text_to_speak):
    tts = gTTS(text=text_to_speak, lang='bn', lang_check=True)
    tts.save("good.mp3")
    playsound.playsound('good.mp3', True)


r = sr.Recognizer()
with sr.Microphone() as source:
    print("আপনাকে কিভাবে সহায়তা করতে পারি স্যার???")
    audio = r.listen(source)
    print("time over")  


collected_audio = r.recognize_google(audio, language="bn-BD")
print("You said:       {}".format(collected_audio))


if collected_audio in questions:
    # get the matched question index
    matched_question_index = questions.index(collected_audio)
    # get the desired answer for the asked question
    desired_answer = answers[matched_question_index]
    play_audio(desired_answer)
    print(desired_answer)