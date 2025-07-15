# -*- coding: utf-8 -*-
"""
Created on Tue Jul 15 18:05:19 2025

@author: User
"""

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes
import random

# Foydalanuvchining holatini saqlash uchun:
user_data = {}

# 🔐 Obuna tekshiruvi funksiyasi
async def check_subscription(bot, user_id):
    try:
        member = await bot.get_chat_member(chat_id='@SIZNING_KANAL_USERNAME', user_id=user_id)
        return member.status in ['member', 'administrator', 'creator']
    except:
        return False

# Boshlang'ich /start komandasi (obuna tekshiruvi bilan)
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id

    # Obuna tekshirish
    is_subscribed = await check_subscription(context.bot, user_id)
    if not is_subscribed:
        await update.message.reply_text(
            "👋 Botdan foydalanish uchun avval kanalimizga obuna bo‘ling:\n"
            "👉 https://t.me/KANAL_NOMI\n\n"
            "Obuna bo‘lgach, /start buyrug‘ini qayta yuboring."
        )
        return

    # Asosiy tugmalar
    keyboard = [
        [InlineKeyboardButton("📝 So'z topish", callback_data='soz')],
        [InlineKeyboardButton("🔢 Son topish", callback_data='son')],
        [InlineKeyboardButton("🧮 Matematik o'yin", callback_data='math')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Xush kelibsiz Hasanning telegram botiga! 👋\n\nQuyidagi o'yinlardan birini tanlang:",
        reply_markup=reply_markup
    )

# Tugma bosilganda nima bo'ladi
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    user_id = query.from_user.id

    if query.data == 'soz':
        await start_soz_topish(query, context)
    elif query.data == 'son':
        random_number = random.randint(1, 10)
        user_data[user_id] = {
            'game': 'son',
            'step': 1,
            'number': random_number,
            'tries': 1
        }
        await query.edit_message_text("🎲 Men 1 dan 10 gacha son o'yladim. Topishga urinib ko'ring!")
    elif query.data == 'math':
        sir = random.randint(100, 200)
        user_data[user_id] = {
            'game': 'math',
            'secret': sir,
            'original': sir,
            'buzilgan': 0,
            'tanlovlar': [1],
            'first': True
        }
        await query.edit_message_text(
            "🧮 Matematik o'yin boshlandi!\n\nKompyuter 100 va 200 oralig'ida sirli sonni tanladi.\n"
            "Siz uning bo'luvchisini topishingiz kerak.Agar siz aytgan son sirli sonning bo'luvchisi bo'lmasa bu son sirli sondan ayiriladi va sirli son kamayadi.Keyingi navbatda siz endi kamaygan sirli sonni bo'luvchisini topishingiz kerak! \n⚠️ Eslatma!\n Agar sizning bir necha muaffaqqiyatsiz yurishlaringgizdan keyin sirli son manfiy qiymatga erishsa siz yutqazasiz!\n"
            "⚠️ Diqqat:\n - 1 ni yozish mumkin emas.\n - Bir xil sonni ikki marta yuborish ham mumkin emas.\n ⚠️Qoidalarni 3 marta buzgan yutqazadi!"
            "Sirli son: ???\n\nIltimos, bo'luvchi sifatida bitta son yuboring:"
        )

# So'z topish o'yini boshlanishi
async def start_soz_topish(query, context):
    sozlar = ['kitob', 'daftar', 'ruchka', 'oyna', 'deraza', 'maktab', 'sinf', 'dars', 'qalam', 'telefon',
             'non', 'suv', 'choy', 'lagan', 'soat', 'oy', 'quyosh', 'tong', 'kecha', 'bahor', 'kuz', 'yoz',
             'qish', 'bola', 'qiz', 'ona', 'ota', 'buvi', 'bobo', 'mashina', 'velosiped', 'alam', 'daraxt',
             'gul', 'gilam', 'tokcha', 'devor', 'eshik', 'kalit', 'piyola', 'qoshiq', 'pichoq', 'idish',
             'peshtaxta', 'uy', 'xona', 'qozon', 'chinni', 'tarozi', 'gazeta', 'avtobus', 'tramvay',
             'zinalar', 'pol', 'stul', 'stol', 'karavot', 'supurgi', 'mashq', 'sport', 'futbol', 'basketbol',
             'voleybol', 'piyoda', 'yugurish', 'toqqa', 'suzish', 'baliqchi', 'baliq', 'ariq', 'suvlik',
             'shakar', 'guruch', 'un', 'laganda', 'qoshiqcha', 'likopcha', 'osh', 'oshpaz', 'mehmon',
             'xonanda', 'chiroq', 'tok', 'kompyuter', 'sichqoncha', 'ekran', 'klaviatura', 'daftarlar',
             'doska', 'tayoq', 'parda', 'politsa', 'militsiya', 'askar', 'zobit', 'rahbar', 'ustoz',
             'hamkasb', 'kotib', 'qalamdon', 'sumka', 'sochiq', 'sovun', 'taroq', 'oynak', 'narsa', 'kiyim',
             'futbolka', 'shim', 'poyabzal', 'etik', 'botinka', 'paypoq', 'shlyapa', 'zanjir', 'uzuk',
             'taqinchoq', 'qumsoat', 'yostiq', 'zukkochabot', 'choynak', 'stakan', 'nonvoy', 'novvoy', 'rastaxona',
             'uddalamoq', 'vaqt', 'vaqtinchalik', 'kechikish', 'tezlik', 'sekinlik', 'telefonlar', 'hamyon',
             'avtoulov', 'moy', 'gaz', 'shisha', 'oyna', 'sochiqlar', 'tugma','Olim', 'Asilbek', 'Jahongir', 'Doston',
             'Sardor', 'Shaxzod', 'Bobur', 'Ulug‘bek', 'Sherzod', 'Azizbek', 'Farrux', 'Islombek', 'Jasur', 'Oybek', 
             'Zafar', 'Rustam', 'Behruz', 'Anvar', 'Shavkat', 'Kamoliddin', 'Umid', 'Shuhrat', 'Erkin', 'Habibulloh', 
             'Muhammadali', 'Mirjalol', 'Sirojiddin', 'Doniyor', 'Dilshod', 'Saidbek', 'Lazizbek', 'Baxtiyor', 'Shohruh', 
             'Zohidbek', 'Sarvar', 'Alisher', 'Komil', 'Ravshan', 'Murod', 'Abduvali', 'Shohjahon', 'Sherali', 'Tohir', 
             'Alimardon', 'Salohiddin', 'Temur', 'Nodirbek', 'Ilhom', 'Muso', 'Rauf','oybek','hasan','husan','abbos','Gulnora',
             'Dilnoza', 'Zilola', 'Malika', 'Sitora', 'Nodira', 'Shahzoda', 'Zarnigor', 'Rayhona', 'Feruza', 'Yulduz', 'Nigora',
             'Lola', 'Asal', 'Mehribon', 'Gulbahor', 'Durdona', 'Mohira', 'Madinabonu', 'Muxlisa', 'Zuxra', 'Diyora', 'Shahlo', 
             'Nasiba', 'Robiya', 'Ziyoda', 'Mushtariy', 'Rano', 'Ozoda', 'Shirin', 'Dilafruz', 'Shahrizoda', 'Madina', 'Kamola', 
             'Nozima', 'Bibisora', 'Ruxshona', 'Guli', 'Saodat', 'Marhabo', 'Gulchehra', 'Nilufar', 'Sevara', 'Ozodaxon', 'Umida',
             'Orzigul', 'nigina', 'Zebuniso', 'Gulruh', 'Tozagul','Fazila']
    soz = random.choice(sozlar).upper()
    qolib = ['_'] * len(soz)
    user_id = query.from_user.id

    user_data[user_id] = {
        'game': 'soz',
        'word': soz,
        'display': qolib,
        'attempts': []
    }

    await query.edit_message_text(
        f"📝 So'z topish o'yini boshlandi!\n\n{len(soz)} harfdan iborat so'zni toping:\n{' '.join(qolib)}\n\nHarf yuboring:"
    )

# Harf yoki son yuborilganda ishlovchi funksiya
async def handle_guess(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.message.from_user.id
    if user_id not in user_data:
        return

    msg = update.message.text.strip()
    data = user_data[user_id]

    # So'z topish
    if data['game'] == 'soz':
        tahmin = msg.upper()
        if len(tahmin) != 1 or not tahmin.isalpha():
            await update.message.reply_text("Faqat bitta harf yuboring.\n(sh,ch,ng va (') lar aholida alohida harf!)\n Yana urining!")
            return

        data['attempts'].append(tahmin)
        if tahmin in data['word']:
            for i, harf in enumerate(data['word']):
                if harf == tahmin:
                    data['display'][i] = tahmin
            if '_' not in data['display']:
                await update.message.reply_text(f"🎉 Tabriklaymiz! Topdinggiz!🏆\n So'z {data['word']} edi!\n/start bilan qayta boshlang.")
                del user_data[user_id]
            else:
                await update.message.reply_text(f"✅ Bor!\n{' '.join(data['display'])} \n Urinishlar=>{''.join(data['attempts'])}")

        else:
            await update.message.reply_text(f"❌ Yo'q.\n{' '.join(data['display'])} \n Urinishlar=>{''.join(data['attempts'])}")

    # Son topish (ikki bosqichli)
    elif data['game'] == 'son':
        if data['step'] == 1:
            if not msg.isdigit():
                await update.message.reply_text("Iltimos, 1 dan 10 gacha son yuboring.")
                return

            guess = int(msg)
            if guess == data['number']:
                await update.message.reply_text(
                    f"✅ Siz men o'ylagan {data['number']} sonini topdingiz!\n"
                    f"Urinishlar: {data['tries']} marta \n\n"
                    "Endi siz son o'ylang, men topishga harakat qilaman.\n"
                    "OK deb yozing tayyor bo'lsangiz."
                )
                data['step'] = 2
                data['comp_range'] = list(range(1, 11))
                data['comp_tries'] = 1
                data['game_ready'] = False
            elif guess < data['number']:
                data['tries'] += 1
                await update.message.reply_text("⬆ Men o'ylagan son bundan katta.\n Yana urining!")
            else:
                data['tries'] += 1
                await update.message.reply_text("⬇ Men o'ylagan son bundan kichik.\n Yana urining")

        elif data['step'] == 2:
            if not data.get('game_ready'):
                if msg.lower() == "ok":
                    data['game_ready'] = True
                    comp_guess = random.choice(data['comp_range'])
                    data['comp_guess'] = comp_guess
                    await update.message.reply_text(
                        f"🤔 Siz o'ylagan son {comp_guess} edi deb o'ylayman.\n"
                        f"To'g'ri bo'lsa: `T`, soninggiz bundan kichik bo'lsa: `-`, agar katta bo'lsa: `+` yozing."
                    )
                else:
                    await update.message.reply_text("OK deb yozing tayyor bo'lsangiz.")
            else:
                javob = msg.strip().lower()
                comp_guess = data['comp_guess']
                if javob == 't':
                    foydalanuvchi = data['tries']
                    kompyuter = data['comp_tries']
                    if foydalanuvchi > kompyuter:
                        text = f"💻 Kompyuter yutdi!\nSiz {foydalanuvchi} urinishda topdingiz, men esa {kompyuter} urinishda ."
                    elif foydalanuvchi < kompyuter:
                        text = f"😎 Siz yutdingiz!\nSiz {foydalanuvchi} urinishda topdingiz, men esa {kompyuter} urinishda."
                    else:
                        text = f"🤝 Do'stlik g'alaba qildi!\nIkkovimiz ham {foydalanuvchi} urinishda topdik!"
                    await update.message.reply_text(text + "\n\n/start bilan boshqa o'yin boshlang.")
                    del user_data[user_id]
                elif javob == '+':
                    data['comp_range'] = [n for n in data['comp_range'] if n > comp_guess]
                    data['comp_tries'] += 1
                elif javob == '-':
                    data['comp_range'] = [n for n in data['comp_range'] if n < comp_guess]
                    data['comp_tries'] += 1
                else:
                    await update.message.reply_text("Faqat `T`, `+` yoki `-` deb javob bering.")
                    return

                if javob in ['+', '-'] and data['game_ready']:
                    if not data['comp_range']:
                        await update.message.reply_text("🤖 Xatolik! siz botni aldadinggiz😒. Sonlar oralig'i bo'sh bo'lib qoldi.\n/start bilan qayta boshlang.")
                        del user_data[user_id]
                        return
                    data['comp_guess'] = random.choice(data['comp_range'])
                    await update.message.reply_text(
                        f"🤔 Balki siz {data['comp_guess']} ni o'ylagandirsiz?\n"
                        f"To'g'ri bo'lsa: `T`,soninggiz bundan kichik bo'lsa: `-`, agar katta bo'lsa: `+` yozing."
                    )

    # Matematik o'yin
    elif data['game'] == 'math':
        if not msg.isdigit():
            await update.message.reply_text("Faqat son yuboring.")
            return

        tanlov = int(msg)
        if tanlov == 1 or tanlov in data['tanlovlar']:
            data['buzilgan'] += 1
            sabab = "1 ni yozish taqiqlangan!" if tanlov == 1 else "Bir xil sonni ikkinchi marta yubordingiz!"
            await update.message.reply_text(f"⛔ Qoidani buzdingiz! ({data['buzilgan']}/3)\nSabab: {sabab}")
            if data['buzilgan'] >= 3:
                await update.message.reply_text(f"❌ Siz qoidalarni 3marta buzganingiz uchun mag'lub bo'ldingiz. Sirli son dastlab {data['original']} edi.\n/start bilan qayta boshlang.")
                del user_data[user_id]
            return

        data['tanlovlar'].append(tanlov)
        if data['secret'] % tanlov == 0:
            await update.message.reply_text(
                f"🎉 Tabriklaymiz! Siz {tanlov} sonini tanladingiz va bu sirli sonning bo'luvchisi edi!\n"
                f"Sirli son dastlab {data['original']} edi, siz sirli son {data['secret']} bo'lganda uning bo'luvchisi {tanlov} ni topdinggiz! \n/start bilan yana o'ynang."
            )
            del user_data[user_id]
        else:
            data['secret'] -= tanlov
            if data['secret'] < 0:
                await update.message.reply_text(
                    f"💥 Siz yutqazdingiz. Sirli son dastlab {data['original']} edi,\n"
                    f"Sizning xato bo'lgan javoblaringgizni sirli sondan ayirish natijasida u manfiy({data['secret']}) bo'lib qoldi.\n/start bilan qayta o'ynang."
                )
                del user_data[user_id]
            else:
                await update.message.reply_text(
                    f"❌ {tanlov} bo'luvchi emas. Bu son endi sirli sondan ayirildi.\n⚠️Sirli son endi o'zgardi!\nYana son yuboring:"
                )

# Botni ishga tushirish
if __name__ == '__main__':
    app = ApplicationBuilder().token("TOKEN KIRIT").build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_guess))
    print("Bot ishga tushdi!")
    app.run_polling()