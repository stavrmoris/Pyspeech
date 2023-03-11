import random

from datetime import datetime
from Answers import *
from Sounding_the_answer import text_in_audio
from Speech_recognition import *

now = datetime.now() 
current_time = now.strftime("%H:%M:%S:%x")

def command(task):
	#task = input()
	x = 0
	for i in range(len(hello)): #Перебираем все элементы списка hello
		if(hello[i] in task): #И если элемент из списка hello попадется
			text_in_audio(random.choice(hello_answer)) #И озвучиваем рандомный ответ из списка hello_answer
			x = 1
	
	for i in range(len(How_are_you)):
		if(How_are_you[i] in task):
			text_in_audio(random.choice(How_are_you_answer))
			x = 1

	for i in range(len(date_now)):
		if(date_now[i] in task):
			text_in_audio("Сейчас: ")
			text_in_audio(current_time)
			x = 1


	if(x == 0):
		text_in_audio('Я пока что не понимаю, что вы мне говорите.')

while True:
	command(recognition())
