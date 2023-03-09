import gtts
from playsound import playsound

def text_in_audio(text):
    tts = gtts.gTTS(text, lang="ru")
    tts.save("Answer.mp3")
    playsound("Answer.mp3")