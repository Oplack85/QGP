from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
import requests

# استبدل بالرمز السري الخاص بالبوت من BotFather
TELEGRAM_TOKEN = '7218686976:AAF9sDAr5tz8Nt_eMBoOl9-2RR6QsH5onTo'
# استبدل بمفتاح API الخاص بـ Google Generative Language
GOOGLE_API_KEY = 'AIzaSyBytHaZDwFzOhtsvDXJOOX7p2WCs7-jWC0'
GOOGLE_API_URL = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent'

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Hello! Send me a text and I will explain how AI works using Google Generative Language API.')

async def explain(update: Update, context: CallbackContext) -> None:
    user_input = ' '.join(context.args)
    if not user_input:
        await update.message.reply_text('Please provide a text to explain.')
        return

    # إرسال الطلب إلى API
    response = requests.post(
        GOOGLE_API_URL,
        headers={'Content-Type': 'application/json'},
        json={
            'prompt': {
                'text': user_input
            }
        },
        params={'key': GOOGLE_API_KEY}
    )

    if response.status_code == 200:
        result = response.json()
        explanation = result.get('result', {}).get('output', 'No explanation found.')
        await update.message.reply_text(explanation)
    else:
        await update.message.reply_text('Failed to get a response from the API.')

def main() -> None:
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('explain', explain))

    application.run_polling()

if __name__ == '__main__':
    main()
