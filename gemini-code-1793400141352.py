import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

# Берешь токен у @BotFather
TOKEN = 'ТВОЙ_ТОКЕН_ОТ_БОТА'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    # Создаем кнопку, которая открывает игру
    markup = InlineKeyboardMarkup()
    # Сюда вставляешь ссылку, которую получишь на Vercel
    web_app_url = "https://твоя-ссылка-на-игру.vercel.app" 
    
    markup.add(InlineKeyboardButton(
        text="🕹 Запустить кубики", 
        web_app=WebAppInfo(url=web_app_url)
    ))
    
    bot.send_message(message.chat.id, "Залетай, расставляй блоки и бей рекорды!", reply_markup=markup)

print("Бот запущен и готов рубить кэш...")
bot.infinity_polling()