import telebot
from telebot import types


def main():
    bot = telebot.TeleBot("6504903326:AAGxq8FzMUfn9NRDxOEi4jyZ9RBMY6iRNf8")

    @bot.message_handler(commands=["start"])
    def send_welcome(message):
        bot.send_message(message.chat.id, text="Welcome to the Business Empire")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Инвестиции")
        btn2 = types.KeyboardButton("Бизнесс")
        btn3 = types.KeyboardButton("Заработок")
        btn4 = types.KeyboardButton("Предметы")
        btn5 = types.KeyboardButton("Профиль")
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.chat.id, text="todo: сделать крутое приветствие".format(message.from_user),
                         reply_markup=markup)

    @bot.message_handler(content_types=["text"])
    def main_menu(message):
        if message.text == "Инвестиции":
            pass
    bot.infinity_polling()


if __name__ == '__main__':
    main()
