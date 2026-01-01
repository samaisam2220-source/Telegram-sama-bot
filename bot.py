
from telegram.ext import Updater, MessageHandler, Filters

KEYWORDS = [
    "احتاج معلمة انجليزي",
    "معلمة انجليزي",
    "معلمة اونلاين",
    "أبغى معلمة انجليزي",
    "أبغى معلمة"
]

def monitor(update, context):
    text = update.message.text.lower()
    for word in KEYWORDS:
        if word in text:
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text="🔔 تم العثور على شخص يبحث عن معلمة إنجليزي"
            )
            break

TOKEN = "8389507406:AAGc1oJP8-wZfdksT8GOGEitF1_V7SPEIBA"

updater = Updater(TOKEN, use_context=True)
dp = updater.dispatcher
dp.add_handler(MessageHandler(Filters.text & ~Filters.command, monitor))

updater.start_polling()
print("✅ البوت يعمل الآن على الخاص والجروبات")
updater.idle()

