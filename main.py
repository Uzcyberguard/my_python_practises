
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes
import random

user_data = {}

# /start komandasi
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📝 So'z topish", callback_data='soz')],
        [InlineKeyboardButton("🔢 Son topish", callback_data='son')],
        [InlineKeyboardButton("➕ Matematik o'yin", callback_data='math')]
    ]
    markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Xush kelibsiz Hasanning telegram botiga! 👋", reply_markup=markup)

# Tugmalarni boshqarish
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    if query.data == "soz":
        await start_soz(query)
    elif query.data == "son":
        user_data[user_id] = {"game": "son", "step": 1, "number": random.randint(1, 10), "tries": 1}
        await query.edit_message_text("1dan 10 gacha son o'yladim, topishga urinib ko'ring:")
    elif query.data == "math":
        rules = (
            "Bu o'yin sonlar asosida tuzilgan. Kompyuter 100–200 oralig‘ida sirli son o‘ylaydi."

            "Siz shu sonning bo‘luvchisini topishingiz kerak."

            "Agar topolmasangiz, siz tanlagan son sirli sondan ayriladi."

            "⚠️ Qoidalar:"

            "- 1 ni kiritish mumkin emas"

            "- Takroriy son yuborish taqiqlanadi"

            "- 3 ta qoidabuzarlikdan keyin o‘yin tugaydi"

        )
        await query.edit_message_text("Matematik o'yin boshlandi!"

 + rules)
        sir = random.randint(100, 200)
        user_data[user_id] = {"game": "math", "secret": sir, "original": sir, "violations": 0, "used": [1]}

async def start_soz(query):
    user_id = query.from_user.id
    words = ['kitob', 'daftar', 'ruchka', 'oyna', 'deraza', 'maktab', 'sinf', 'dars', 'qalam', 'telefon',
             'non', 'suv', 'choy', 'lagan', 'soat', 'oy', 'quyosh', 'tong', 'kecha', 'bahor', 'kuz', 'yoz',
             'qish', 'bola', 'qiz', 'ona', 'ota', 'buvi', 'bobo', 'mashina', 'velosiped', 'alam', 'daraxt',
             'gul', 'gilam', 'tokcha', 'devor', 'eshik', 'kalit', 'piyola', 'qoshiq', 'pichoq', 'idish',
             'peshtaxta', 'uy', 'xona', 'qozon', 'chinni', 'tarozi', 'gazeta', 'avtobus', 'tramvay',
             'zinalar', 'pol', 'stul', 'stol', 'karavot', 'supurgi', 'mashq', 'sport', 'futbol', 'basketbol',
             'voleybol', 'piyoda', 'yugurish', 'toqqa', 'suzish', 'baliqchi', 'baliq', 'ariq', 'suvlik',
             'shakar', 'guruch', 'un', 'laganda', 'qoshiqcha', 'likopcha', 'osh', 'oshpaz', 'mehmon',
             'xonaqadam', 'chiroq', 'tok', 'kompyuter', 'sichqoncha', 'ekran', 'klaviatura', 'daftarlar',
             'doska', 'tayoq', 'parda', 'politsa', 'militsiya', 'askar', 'zobit', 'rahbar', 'ustoz',
             'hamkasb', 'kotib', 'qalamdon', 'sumka', 'sochiq', 'sovun', 'taroq', 'oynak', 'narsa', 'kiyim',
             'futbolka', 'shim', 'poyabzal', 'etik', 'botinka', 'paypoq', 'shlyapa', 'zanjir', 'uzuk',
             'taqinchoq', 'soatbop', 'yostiq', 'adyol', 'choynak', 'stakan', 'nonvoy', 'novvoy', 'rastaxona',
             'eplaydi', 'vaqt', 'vaqtinchalik', 'kechikish', 'tezlik', 'sekinlik', 'telefonlar', 'hamyon',
             'avtoulov', 'moy', 'gaz', 'shisha', 'oyna', 'sochiqlar', 'tugma']
    word = random.choice(words).upper()
    user_data[user_id] = {"game": "soz", "word": word, "display": ["_"] * len(word), "tries": []}
    await query.edit_message_text(f"So'z topish boshlandi:{' '.join(user_data[user_id]['display'])}")

# Matnli javoblarni qayta ishlash
async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    if user_id not in user_data:
        return
    data = user_data[user_id]
    msg = update.message.text.strip().upper()

    if data["game"] == "soz":
        if len(msg) != 1 or not msg.isalpha():
            await update.message.reply_text("Faqat 1 dona harf yuboring.")
            return
        data["tries"].append(msg)
        if msg in data["word"]:
            for i, harf in enumerate(data["word"]):
                if harf == msg:
                    data["display"][i] = msg
            if "_" not in data["display"]:
                await update.message.reply_text(f"🎉 Tabriklaymiz! So'z: {data['word']}")
                del user_data[user_id]
            else:
                await update.message.reply_text(f"Bor!{' '.join(data['display'])}  Urinishlar: {''.join(data['tries'])}")
        else:
            await update.message.reply_text(f"Yo‘q. {' '.join(data['display'])}  Urinishlar: {''.join(data['tries'])}")

    elif data["game"] == "son":
        if data["step"] == 1:
            if not msg.isdigit():
                await update.message.reply_text("Son yuboring.")
                return
            guess = int(msg)
            if guess == data["number"]:
                await update.message.reply_text(f"Siz topdingiz! Men o‘ylagan son {guess} edi.Endi siz son o‘ylang va 'ok' deb yozing.")
                data["step"] = 2
                data["comp_range"] = list(range(1, 11))
                data["comp_tries"] = 1
                data["ready"] = False
            elif guess < data["number"]:
                data["tries"] += 1
                await update.message.reply_text("Men o‘ylagan son bundan katta.")
            else:
                data["tries"] += 1
                await update.message.reply_text("Men o‘ylagan son bundan kichik.")
        elif data["step"] == 2:
            if not data.get("ready") and msg.lower() == "ok":
                data["ready"] = True
                data["guess"] = random.choice(data["comp_range"])
                await update.message.reply_text(f"Siz o‘ylagan son {data['guess']} edi? T (to‘g‘ri), + (katta), - (kichik)")
            elif data.get("ready"):
                javob = msg
                if javob == "T":
                    text = f"Men {data['comp_tries']} ta urinishda topdim, siz esa {data['tries']} ta."
                    await update.message.reply_text(text)
                    del user_data[user_id]
                elif javob == "+":
                    data["comp_range"] = [n for n in data["comp_range"] if n > data["guess"]]
                elif javob == "-":
                    data["comp_range"] = [n for n in data["comp_range"] if n < data["guess"]]
                if data["comp_range"]:
                    data["guess"] = random.choice(data["comp_range"])
                    data["comp_tries"] += 1
                    await update.message.reply_text(f"Balki siz {data['guess']} ni o‘ylagandirsiz? T, +, -")
                else:
                    await update.message.reply_text("Xatolik! /start bilan qayta boshlang.")
                    del user_data[user_id]

    elif data["game"] == "math":
        if not msg.isdigit():
            await update.message.reply_text("Faqat son yuboring.")
            return
        tanlov = int(msg)
        if tanlov == 1 or tanlov in data["used"]:
            data["violations"] += 1
            if data["violations"] >= 3:
                await update.message.reply_text(f"❌ Siz yutqazdingiz. Sirli son: {data['original']}")
                del user_data[user_id]
                return
            else:
                await update.message.reply_text(f"⛔ Qoidani buzdingiz! ({data['violations']}/3)")
                return
        data["used"].append(tanlov)
        if data["secret"] % tanlov == 0:
            await update.message.reply_text(f"✅ Tabriklaymiz! {tanlov} bo‘luvchi edi. Sirli son: {data['original']}")
            del user_data[user_id]
        else:
            data["secret"] -= tanlov
            if data["secret"] < 0:
                await update.message.reply_text(f"💥 Siz yutqazdingiz. Sirli son manfiy bo‘ldi. {data['original']}")
                del user_data[user_id]
            else:
                await update.message.reply_text("❌ Bo‘luvchi emas. Yana urinib ko‘ring.")

# Botni ishga tushirish
if __name__ == '__main__':
    app = ApplicationBuilder().token("7682630882:AAGoQcnmTBD3YjBi2MxJrlqKdjjkPbraGaI").build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
    print("Bot ishga tushdi!")
    app.run_polling()
# hasan_bot_main.py fayl oxirida
import time

while True:
    try:
        app.run_polling()
    except Exception as e:
        print("Xatolik:", e)
    time.sleep(5)    
    
    
    
    
    
    
    
