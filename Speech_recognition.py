import speech_recognition as sr
from Sounding_the_answer import text_in_audio

def recognition():
	r = sr.Recognizer()

	# Начинаем прослушивать микрофон и записываем данные в source
	with sr.Microphone() as source:
		# Просто вывод, чтобы мы знали когда говорить
		print("Говорите")
		# Устанавливаем паузу, чтобы прослушивание началось лишь по прошествию 1 секунды
		r.pause_threshold = 1
		# используем adjust_for_ambient_noise для удаления посторонних шумов из аудио дорожки
		r.adjust_for_ambient_noise(source, duration=1)
		# Полученные данные записываем в переменную audio пока мы получили лишь mp3 звук
		audio = r.listen(source)

	try: 
		task = r.recognize_google(audio, language="ru-RU").lower()
		# Отображаем, что сказал пользователь
		print("Вы сказали: " + task)
	# Если не смогли распознать текст, то будет вызвана эта ошибка
	except sr.UnknownValueError:
		# Здесь просто проговариваем слова
		text_in_audio("Я вас не расслышала")
		task = recognition()
	return task
