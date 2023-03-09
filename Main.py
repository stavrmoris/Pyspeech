import random
from Answers import *
from Sounding_the_answer import text_in_audio

def command():
	task = input()
	x = 0
	for i in range(len(hello)):
		if(hello[i] in task):
			text_in_audio(random.choice(hello_answer))
			x = 1
	
	for i in range(len(How_are_you)):
		if(How_are_you[i] in task):
			text_in_audio(random.choice(How_are_you_answer))
			x = 1

	for i in range(len(date_now)):
		if(date_now[i] in task):
			text_in_audio(random.choice(hello_answer))
			x = 1


	if(x == 0):
		text_in_audio('I hate people')

while True:
	command()
