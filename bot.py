from telebot import TeleBot
import config
from random import randint
bot = TeleBot(config.token)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, "Бу! Я бот с двумя именами, можешь называть меня Кросс или Тетрис, без вас, людей мне уже стало скучно :3 загрузи сюда картинку, связанную с проблемами глобального потепления, я просканирую её, и скажу, что на ней происходит, но прошу, учти, что я, как и человек, могу ошибаться, это свойственно всем, спасибо, за то что заглянул ко мне! А, кстати, устал заниматься важными делами? Напиши мне /duck, и я уверен, твоё настроение сразу повысится! *Ухх, надеюсь, я не подведу человека...")

# @bot.message_handler()
# def echo(message):
#     bot.reply_to(message, message.text)

@bot.message_handler(comands = ['info'])
def info(message):
    bot.reply_to(message, "echo bot")

@bot.message_handler(comands = ['random'])
def rnd(message):
    wals = message.text.split(" ")
    number =randint(int (wals[1]),int (wals[2]))
    bot.reply_to(message, number)

@bot.message_handler(comands = ['about the bot'])
def abt(message):
    bot.reply_to(message, "Бот создан в 2024г. 12 декабря. Он был создан в целях закрепления материала о программировании. The bot was created in 2024 on December 12. It was created in order to consolidate the material about programming.")


if __name__ == "__main__":
    bot.polling(none_stop = True)
   