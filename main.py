from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import requests

# استبدل بالرمز السري الخاص بالبوت من BotFather
TELEGRAM_TOKEN = '7218686976:AAF9sDAr5tz8Nt_eMBoOl9-2RR6QsH5onTo'
# استبدل بمفتاح API الخاص بـ Google Generative Language
GOOGLE_API_KEY = 'AIzaSyBytHaZDwFzOhtsvDXJOOX7p2WCs7-jWC0'
GOOGLE_API_URL = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent'

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! Send me a text and I will explain how AI works using Google Generative Language API.')

def explain(update: Update, context: CallbackContext) -> None:
    user_input = ' '.join(context.args)
    if not user_input:
        update.message.reply_text('Please provide a text to explain.')
        return

    # إرسال الطلب إلى API
    response = requests.post(
        GOOGLE_API_URL,
        headers={'Content-Type': 'application/json'},
        json={'contents': [{'parts': [{'text': user_input}]}]},
        params={'key': GOOGLE_API_KEY}
    )

    if response.status_code == 200:
        result = response.json()
        explanation = result['contents'][0]['parts'][0]['text']
        update.message.reply_text(explanation)
    else:
        update.message.reply_text('Failed to get a response from the API.')

def main() -> None:
    updater = Updater(TELEGRAM_TOKEN)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('explain', explain))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
