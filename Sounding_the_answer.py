import gtts
from playsound import playsound

def text_in_audio(text):
    print(text)
    tts = gtts.gTTS(text, lang="ru", slow=False) #Синтезируем речь
    tts.save("Answer.mp3") #Сохраняем речь как Answer.mp3
    playsound("Answer.mp3") #Запускаем Answer.mp3