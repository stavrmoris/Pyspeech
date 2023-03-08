import random
import datetime
import subprocess
import pyttsx3


hello = ['привет',  'здравствуйте',  'добрый день',  'доброе утро',  'добрый вечер' 'хай' 'хэй']
hello_answer = ['Привет',  'Здравствуйте',  'Доброго времени суток']
How_are_you = ['как дела', 'как делишки', 'как делишки ']
How_are_you_answer = ['Нормально', 'Хорошо' 'Лучше всех', 'Отлично' 'Прекрасно']
what_are_you_doing = []
what_are_you_doing_answer = []
date_now = ['какой сегодня день', 'какое число', 'какой сегодня день', 'какой сегодня год', 'какой сейчас день', 'какое сейчас число', 'какой сегодня день', 'какой сейчас год', 'какое сегодня число']

engine = pyttsx3.init()

def command():
	task = input()

	if(task in hello):
		engine.say(random.choice(hello_answer))
	elif(task in How_are_you):
		engine.say(random.choice(How_are_you_answer))
	elif(task in date_now):
		engine.say(datetime.date.today())
	elif(task in what_are_you_doing):
		print(random.choice(what_are_you_doing_answer))
	elif(task == "какой твой любимый цвет?"):
		engine.say('Мне нравятся голубой, как небо!')
	elif(task == "как тебя зовут?"):
		engine.say('Александра')
	elif(task == "какой твой любимый напиток?"):
		engine.say('Мне нравится Фруктовый коктель со льдом')
	elif(task == "Открой firefox"):
		subprocess.Popen('C:/Program Files/Mozilla Firefox/firefox.exe')
	else:
		engine.say('I hate people')
	engine.runAndWait()

while True:
	command()
