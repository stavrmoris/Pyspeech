import random
import runpy
import sys

from Sounding_the_answer import text_in_audio
from Speech_recognition import *

cityes_old = []
symbols_bad = {"ь","ъ","ы","ц","й"}
  
  
text1 = open("/home/stavr/Рабочий стол/Pyspeech/Pyspeech/cities.txt")
cityes = []
for i in text1:
    cityes.append(i)
  
for i in range(len(cityes)):
    if cityes[i][-1] == "\n":
        cityes[i]=cityes[i][:-1]
  
cityes_all = cityes.copy()
  
game_over = False
text_in_audio("Игра в города. Что бы закончить игру введите слово стоп")
  
city = random.choice(cityes)
print(city)
s_end = city[-1]
step = 'human'
cityes_old.append(city)
s_end = city[-1]
  
while game_over == False:
    if step == 'human':
  
        correct = False
        while correct == False:
            print("Введите ваш город: на букву: ", s_end)
            task = recognition()
            city = task.capitalize()
            print(city)
            if city == "стоп":
                game_over = True
                correct = True
                runpy.run_module(mod_name='main.py')
                sys.exit()
            else:
                correct = True
                #Проверить что город на нужную букву
                if city[0].lower () != s_end:
                    correct = False
                    print("Не верно. Назовите город на букву", s_end)
  
                #Проверить что такой город существует
                if city in set(cityes_all):
                    pass
                else:
                    correct = False
                    text_in_audio("Не верно. Такого города не существует")                
  
                #Проверить что ранее этот город не называли
                if city in set(cityes_old):
                    correct = False
                    text_in_audio("Не верно. Такой город уже называли")    
  
        step = 'AI'
    else:
          
        city = ''
        for city_next in cityes:            
            if city_next[0].lower() == s_end:
                city = city_next
  
        if city == '':
            text_in_audio('Вы победили')
            print('Не найден город на букву', s_end)
            game_over = True
        else:
            print(city)
              
              
        step = 'human'
  
    if game_over == False:
        cityes.remove(city)
        cityes_old.append(city)
  
        s_end = city[-1]
        if s_end in symbols_bad:
            s_end = city[-2]
  
        if s_end in symbols_bad:
            s_end = city[-3]
    else:
        pass
          



text_in_audio('Игра окончена')
print('Назвали ' + len(cityes_old) + " городов из " + len(cityes_all))