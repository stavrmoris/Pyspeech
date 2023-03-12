import random
import webbrowser

from datetime import datetime
from Answers import *
from Sounding_the_answer import text_in_audio
from Speech_recognition import *

now = datetime.now() 
current_time = now.strftime("%H:%M:%S:%x")

def command():
	task = input()
	x = 0
	for i in range(len(hello)): #Перебираем все элементы списка hello
		if(hello[i] in task): #И если элемент из списка hello попадется
			text_in_audio(random.choice(hello_answer)) #И озвучиваем рандомный ответ из списка hello_answer
			x = 1
	
	for i in range(len(How_are_you)):
		if(How_are_you[i] in task):
			text_in_audio(random.choice(How_are_you_answer))
			x = 1

	for i in range(len(what_are_you_doing)):
		if(what_are_you_doing[i] in task):
			text_in_audio(random.choice(what_are_you_doing_answer))
			x = 1

	for i in range(len(date_now)):
		if(date_now[i] in task):
			text_in_audio("Сейчас: ")
			text_in_audio(current_time)
			x = 1

	for i in range(len(search_in_google)):
		search_text = []
		if(search_in_google[i] in task):
			edit_string_as_list = task.split()
			final_list = [word for word in edit_string_as_list if word not in search_in_google]
			final_string = ' '.join(final_list)
			text_in_audio(random.choice(search_in_web_answer))
			url = 'https://www.google.com/search?q=' + final_string
			webbrowser.open(url, new=0, autoraise=True)
			x = 1

	for i in range(len(search_in_yandex)):
		search_text = []
		if(search_in_yandex[i] in task):
			edit_string_as_list = task.split()
			final_list = [word for word in edit_string_as_list if word not in search_in_yandex]
			final_string = ' '.join(final_list)
			text_in_audio(random.choice(search_in_web_answer))
			url = 'https://yandex.ru/search/?text=' + final_string
			webbrowser.open(url, new=0, autoraise=True)
			x = 1

#webbrowser.open(url, new=0, autoraise=True)
	if(x == 0):
		text_in_audio('Я пока что не понимаю, что вы мне говорите.')

while True:
	#command(recognition())
	command()
