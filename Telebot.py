import telebot
import requests
import COVID19Py
from bs4 import BeautifulSoup

bot = telebot.TeleBot("1802314363:AAGQB6rvf09M7SMVkj4--aOLPEft1wdeqTI")

@bot.message_handler(commands=["start", "help", "menu"])
def send_welcome(message):
	markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 2)
	btnWeather = telebot.types.KeyboardButton("Погода")
	btnCovid = telebot.types.KeyboardButton("Статистика Ковид")
	btnDol = telebot.types.KeyboardButton("Курс")
	markup.add(btnWeather, btnCovid, btnDol)
	bot.send_message(message.chat.id, f"Ассаламу алейкум, {message.from_user.first_name}! Выберите какую новость хотите посмотреть.", reply_markup = markup)

@bot.message_handler(content_types = ["text"])
def answer(message):
	covid19 = COVID19Py.COVID19()
	get_message = message.text.lower()
	if get_message == "погода":
		markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 2)
		btnTash = telebot.types.KeyboardButton("Ташкент")
		btnMos = telebot.types.KeyboardButton("Москва")
		btn = telebot.types.KeyboardButton("Меню")
		markup.add(btnMos, btnTash, btn)
		bot.send_message(message.chat.id, "Выберите город.", reply_markup = markup)
	elif get_message == "ташкент":
		weatherTash = "https://rp5.ru/Погода_в_Ташкенте"
		headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15"}
		full_pageTash = requests.get(weatherTash, headers = headers)
		soupTash = BeautifulSoup(full_pageTash.content, "html.parser")
		inf = str(soupTash.findAll("meta", {"name" : "description"}))
		infTash = inf[inf.find('"')+1:inf.find("РП5")]
		bot.send_message(message.chat.id, infTash)
	elif get_message == "москва":
		weatherMos = "https://rp5.ru/Погода_в_Москве_(ВДНХ)"
		headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15"}
		full_pageMos = requests.get(weatherMos, headers = headers)
		soupMos = BeautifulSoup(full_pageMos.content, "html.parser")
		inf = str(soupMos.findAll("meta", {"name" : "description"}))
		infMos = inf[inf.find('"')+1:inf.find("РП5")]
		bot.send_message(message.chat.id, infMos)
	elif get_message == "курс":
		markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 2)
		btnDol = telebot.types.KeyboardButton("Доллар")
		btnEvro = telebot.types.KeyboardButton("Евро")
		btn = telebot.types.KeyboardButton("Меню")
		markup.add(btnDol, btnEvro, btn)
		bot.send_message(message.chat.id, "Выберите валюту.", reply_markup = markup)
	elif get_message == "доллар":
		headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15"}
		courseDol = "https://ru.investing.com/currencies/usd-rub"
		full_pageCourse = requests.get(courseDol, headers = headers)
		soupDol = BeautifulSoup(full_pageCourse.content, "html.parser")
		inf = soupDol.findAll("span", {"class": "arial_26 inlineblock pid-2186-last", "id": "last_last"})
		infDol = inf[0].text
		bot.send_message(message.chat.id, f"1$ = {infDol} рублей")
	elif get_message == "евро":
		headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15"}
		courseEvro = "https://ru.investing.com/currencies/eur-rub"
		full_pageCourse = requests.get(courseEvro, headers = headers)
		soupEvro = BeautifulSoup(full_pageCourse.content, "html.parser")
		inf = soupEvro.findAll("span", {"id": "last_last"})
		infEvro = inf[0].text
		bot.send_message(message.chat.id, f"1€ = {infEvro} рублей")
	elif get_message == "меню":
		markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 2)
		btnWeather = telebot.types.KeyboardButton("Погода")
		btnCovid = telebot.types.KeyboardButton("Статистика Ковид")
		btnDol = telebot.types.KeyboardButton("Курс")
		markup.add(btnWeather, btnCovid, btnDol)
		bot.send_message(message.chat.id, f"Выберите какую новость хотите посмотреть.", reply_markup = markup)
	elif "ковид" in get_message or "статистика" in get_message:
		markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
		btn1 = telebot.types.KeyboardButton('Во всём мире')
		btn2 = telebot.types.KeyboardButton('Украина')
		btn3 = telebot.types.KeyboardButton('Россия')
		btn4 = telebot.types.KeyboardButton('Беларусь')
		btn5 = telebot.types.KeyboardButton('Казакхстан')
		btn6 = telebot.types.KeyboardButton('Италия')
		btn7 = telebot.types.KeyboardButton('Франция')
		btn8 = telebot.types.KeyboardButton('Германия')
		btn9 = telebot.types.KeyboardButton('Япония')
		btn10 = telebot.types.KeyboardButton('США')
		btn11 = telebot.types.KeyboardButton('Узбекистан')
		btn12 = telebot.types.KeyboardButton('Меню')
		markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12)
		bot.send_message(message.chat.id, "Выберите статистику какой страны вы хотите увидеть.", reply_markup = markup)
	elif get_message == "сша":
		location = covid19.getLocationByCountryCode("US")
		date = location[0]['last_updated'].split("T")
		time = date[1].split(".")
		final_message = f"<u>Данные по стране:</u>\nНаселение: {location[0]['country_population']:,}\n" \
				f"Последнее обновление: {date[0]} {time[0]}\nПоследние данные:\n<b>" \
				f"Заболевших: </b>{location[0]['latest']['confirmed']:,}\n<b>Сметрей: </b>" \
				f"{location[0]['latest']['deaths']:,}"
		bot.send_message(message.chat.id, final_message, parse_mode = "html")
	elif get_message == "украина":
		location = covid19.getLocationByCountryCode("UA")
		date = location[0]['last_updated'].split("T")
		time = date[1].split(".")
		final_message = f"<u>Данные по стране:</u>\nНаселение: {location[0]['country_population']:,}\n" \
				f"Последнее обновление: {date[0]} {time[0]}\nПоследние данные:\n<b>" \
				f"Заболевших: </b>{location[0]['latest']['confirmed']:,}\n<b>Сметрей: </b>" \
				f"{location[0]['latest']['deaths']:,}"
		bot.send_message(message.chat.id, final_message, parse_mode = "html")
	elif get_message == "россия":
		location = covid19.getLocationByCountryCode("RU")
		date = location[0]['last_updated'].split("T")
		time = date[1].split(".")
		final_message = f"<u>Данные по стране:</u>\nНаселение: {location[0]['country_population']:,}\n" \
				f"Последнее обновление: {date[0]} {time[0]}\nПоследние данные:\n<b>" \
				f"Заболевших: </b>{location[0]['latest']['confirmed']:,}\n<b>Сметрей: </b>" \
				f"{location[0]['latest']['deaths']:,}"
		bot.send_message(message.chat.id, final_message, parse_mode = "html")
	elif get_message == "беларусь":
		location = covid19.getLocationByCountryCode("BY")
		date = location[0]['last_updated'].split("T")
		time = date[1].split(".")
		final_message = f"<u>Данные по стране:</u>\nНаселение: {location[0]['country_population']:,}\n" \
				f"Последнее обновление: {date[0]} {time[0]}\nПоследние данные:\n<b>" \
				f"Заболевших: </b>{location[0]['latest']['confirmed']:,}\n<b>Сметрей: </b>" \
				f"{location[0]['latest']['deaths']:,}"
		bot.send_message(message.chat.id, final_message, parse_mode = "html")
	elif get_message == "казакхстан":
		location = covid19.getLocationByCountryCode("KZ")
		date = location[0]['last_updated'].split("T")
		time = date[1].split(".")
		final_message = f"<u>Данные по стране:</u>\nНаселение: {location[0]['country_population']:,}\n" \
				f"Последнее обновление: {date[0]} {time[0]}\nПоследние данные:\n<b>" \
				f"Заболевших: </b>{location[0]['latest']['confirmed']:,}\n<b>Сметрей: </b>" \
				f"{location[0]['latest']['deaths']:,}"
		bot.send_message(message.chat.id, final_message, parse_mode = "html")
	elif get_message == "италия":
		location = covid19.getLocationByCountryCode("IT")
		date = location[0]['last_updated'].split("T")
		time = date[1].split(".")
		final_message = f"<u>Данные по стране:</u>\nНаселение: {location[0]['country_population']:,}\n" \
				f"Последнее обновление: {date[0]} {time[0]}\nПоследние данные:\n<b>" \
				f"Заболевших: </b>{location[0]['latest']['confirmed']:,}\n<b>Сметрей: </b>" \
				f"{location[0]['latest']['deaths']:,}"
		bot.send_message(message.chat.id, final_message, parse_mode = "html")
	elif get_message == "франция":
		location = covid19.getLocationByCountryCode("FR")
		date = location[0]['last_updated'].split("T")
		time = date[1].split(".")
		final_message = f"<u>Данные по стране:</u>\nНаселение: {location[0]['country_population']:,}\n" \
				f"Последнее обновление: {date[0]} {time[0]}\nПоследние данные:\n<b>" \
				f"Заболевших: </b>{location[0]['latest']['confirmed']:,}\n<b>Сметрей: </b>" \
				f"{location[0]['latest']['deaths']:,}"
		bot.send_message(message.chat.id, final_message, parse_mode = "html")
	elif get_message == "германия":
		location = covid19.getLocationByCountryCode("DE")
		date = location[0]['last_updated'].split("T")
		time = date[1].split(".")
		final_message = f"<u>Данные по стране:</u>\nНаселение: {location[0]['country_population']:,}\n" \
				f"Последнее обновление: {date[0]} {time[0]}\nПоследние данные:\n<b>" \
				f"Заболевших: </b>{location[0]['latest']['confirmed']:,}\n<b>Сметрей: </b>" \
				f"{location[0]['latest']['deaths']:,}"
		bot.send_message(message.chat.id, final_message, parse_mode = "html")
	elif get_message == "япония":
		location = covid19.getLocationByCountryCode("JP")
		date = location[0]['last_updated'].split("T")
		time = date[1].split(".")
		final_message = f"<u>Данные по стране:</u>\nНаселение: {location[0]['country_population']:,}\n" \
				f"Последнее обновление: {date[0]} {time[0]}\nПоследние данные:\n<b>" \
				f"Заболевших: </b>{location[0]['latest']['confirmed']:,}\n<b>Сметрей: </b>" \
				f"{location[0]['latest']['deaths']:,}"
		bot.send_message(message.chat.id, final_message, parse_mode = "html")
	elif get_message == "узбекистан":
		location = covid19.getLocationByCountryCode("UZ")
		date = location[0]['last_updated'].split("T")
		time = date[1].split(".")
		final_message = f"<u>Данные по стране:</u>\nНаселение: {location[0]['country_population']:,}\n" \
				f"Последнее обновление: {date[0]} {time[0]}\nПоследние данные:\n<b>" \
				f"Заболевших: </b>{location[0]['latest']['confirmed']:,}\n<b>Сметрей: </b>" \
				f"{location[0]['latest']['deaths']:,}"
		bot.send_message(message.chat.id, final_message, parse_mode = "html")
	elif "во всём мире":
		location = covid19.getLatest()
		final_message = f"<u>Данные по всему миру:</u>\n<b>Заболевших: </b>{location['confirmed']:,}\n<b>Смертей: </b>{location['deaths']:,}"
		bot.send_message(message.chat.id, final_message, parse_mode = "html")
	else:
		markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard = True, row_width = 2)
		btnWeather = telebot.types.KeyboardButton("Погода")
		btnCovid = telebot.types.KeyboardButton("Статистика Ковид")
		btnDol = telebot.types.KeyboardButton("Курс")
		markup.add(btnWeather, btnCovid, btnDol)
		bot.send_message(message.chat.id, f"Я вас не понимаю. Выберите какую новость хотите посмотреть.", reply_markup = markup, parse_mode = "html")

bot.polling(none_stop = True, interval = 1)