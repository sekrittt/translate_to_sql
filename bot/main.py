import telebot
from transformers import pipeline

translator = pipeline('translation_ru_to_en', model='Helsinki-NLP/opus-mt-ru-en')

TOKEN = '5667745940:AAEGT9iEDxPZ6llHUqnDAihDQAs8IzqaRLY'

bot = telebot.TeleBot(TOKEN)




@bot.message_handler(commands=['start'])
def start(message: telebot.telebot.types.Message):
    bot.send_message(message.chat.id, 'Здравствуйте! Этот бот предназначен для перевода запросов к базе данных на естественном языке на формальный язык SQL.')

@bot.message_handler(content_types=['text'])
def handler(message: telebot.telebot.types.Message):
    text = translator(message.text)
    bot.send_message(message.chat.id, text[0]['translation_text'])

if __name__ == '__main__':
    print('Start bot...')
    bot.polling(none_stop=True)