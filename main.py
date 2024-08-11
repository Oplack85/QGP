import telethon
from telethon import TelegramClient, events
import openai  # تحتاج لتثبيت هذه المكتبة بكتابة: pip install openai

# قم بوضع بيانات API الخاصة بك هنا من موقع Telegram و OpenAI
api_id = "23970174"
api_hash = "f1db2e38b2c73448ef09c504187e888d"
bot_token = "7218686976:AAF9sDAr5tz8Nt_eMBoOl9-2RR6QsH5onTo"
openai.api_key = "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"


client = TelegramClient('your_bot', api_id, api_hash).start(bot_token=bot_token)

@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    """يرسل رسالة ترحيب عند بدء التشغيل."""
    await event.respond("مرحبًا بك في بوت الذكاء الاصطناعي! 👋 \n اكتب أي شيء لأبدأ المحادثة.")


@client.on(events.NewMessage)
async def handle_message(event):
    """يتعامل مع جميع الرسائل الواردة من المستخدمين."""
    if event.message.message.startswith('/'):
        # تجاهل الأوامر التي تبدأ بـ '/'
        return

    # الحصول على نص رسالة المستخدم
    user_message = event.message.message

    # استخدام نموذج GPT-3 من OpenAI لتوليد رد
    response = openai.Completion.create(
        engine="text-davinci-003",  # يمكنك تجربة نماذج أخرى هنا
        prompt=user_message,
        max_tokens=150,  # يمكنك ضبط طول الرد
        temperature=0.7,  # يمكنك ضبط درجة عشوائية الرد
    )

    # إرسال رد GPT-3 إلى المستخدم
    await event.respond(response['choices'][0]['text'])


client.run_until_disconnected()
