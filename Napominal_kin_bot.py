#Ass We Can



import datetime as dt
import telebot # Библиотека для создания Telegram-бота
from telebot import types # Библиотека для создания inline кнопок

answer = '' # Переменная для ответов
name = ''

bot = telebot.TeleBot('5690547992:AAEwbmMfngk0IpHUaeZWuIGAtPrel305U5s') # API ключ бота 
keyboard = types.InlineKeyboardMarkup() # Переменная для inline кнопок



@bot.message_handler(commands=["start"]) # Команда для запуска бота 
def start(m, res=False): # Функция срабатывающая при старт
        bot.send_message(m.chat.id, 'Напиши фамилию как в образце("Иванов"), чтобы продолжить работу.')
        
        bot.register_next_step_handler(m, priv)



@bot.message_handler(content_types=["text"]) # Команда для получения текста   
def menu(message): # Функция для обработки основных кнопок 
    global answer
    
    name = message.text.strip()
    
    answer = "Приветствую вас, " + name # Определение переменной для ответа (встречается везде, где нужен ответ)
    
    bot.send_message(message.chat.id, answer) # Отправка переменной answer, в которой находиться ответ (встречается везде, где нужен ответ)



bot.polling(none_stop=True, interval=0) # Запуск бота 