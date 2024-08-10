from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from generative_ai_python import YourGenerativeAIClient

# إعداد عميل الذكاء الاصطناعي
api_key = 'AIzaSyBtv6W1BL7GrcQD14P07nKdG50vHucNouU'  # استبدل بـ API Key الخاص بك
client = YourGenerativeAIClient(api_key)

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('مرحبًا! أنا بوت الذكاء الاصطناعي الخاص بك.')

def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('أرسل لي رسالة وسأرد عليك.')

def handle_message(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text
    response = client.generate_response(user_message)  # استخدم الطريقة المناسبة من مكتبة الذكاء الاصطناعي
    update.message.reply_text(response)

def main() -> None:
    # إعداد البوت
    updater = Updater("7218686976:AAF9sDAr5tz8Nt_eMBoOl9-2RR6QsH5onTo")  # استبدل بـ توكن البوت الخاص بك

    dispatcher = updater.dispatcher

    # تعيين معالجات الأوامر والرسائل
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('help', help_command))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # بدء البوت
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
