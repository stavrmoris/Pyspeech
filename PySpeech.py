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
	x = 0
	for i in range(len(hello)):
		if(hello[i] in task):
			engine.say(random.choice(hello_answer))
			x = 1
	
	for i in range(len(How_are_you)):
		if(How_are_you[i] in task):
			engine.say(random.choice(How_are_you_answer))
			x = 1

	for i in range(len(date_now)):
		if(date_now[i] in task):
			engine.say(random.choice(hello_answer))
			x = 1


	if(x == 0):
		engine.say('I hate people')
	engine.runAndWait()

while True:
	command()
