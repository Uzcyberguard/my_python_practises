from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes import random

user_data = {}

/start komandasi

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE): keyboard = [ [InlineKeyboardButton("🌝 So‘z topish", callback_data='soz')], [InlineKeyboardButton("🌢 Son topish", callback_data='son')], [InlineKeyboardButton("🧮 Matematik o‘yin", callback_data='math')] ] reply_markup = InlineKeyboardMarkup(keyboard) await update.message.reply_text( "Xush kelibsiz Hasanning telegram botiga! \U0001f44b\n\nQuyidagi o‘yinlardan birini tanlang:", reply_markup=reply_markup )

Tugma bosilganda nima bo‘ladi

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE): query = update.callback_query await query.answer() user_id = query.from_user.id

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
    await query.edit_message_text("\U0001f3b2 Men 1 dan 10 gacha son o‘yladim. Topishga urinib ko‘ring!")
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
        "🧮 Matematik o‘yin boshlandi!\n\nKompyuter 100 va 200 oralig‘ida sirli sonni tanladi.\n"
        "Siz uning bo‘luvchisini topishingiz kerak.\n"
        "⚠️ Diqqat:\n - 1 ni yozish mumkin emas.\n - Bir xil sonni ikki marta yuborish ham mumkin emas.\n"
        "Sirli son: ???\n\nIltimos, bo‘luvchi sifatida bitta son yuboring:"
    )

So‘z topish o‘yini

async def start_soz_topish(query, context): sozlar = ['kitob', 'daftar', 'ruchka', 'oyna', 'maktab'] soz = random.choice(sozlar).upper() qolib = ['_'] * len(soz) user_id = query.from_user.id

user_data[user_id] = {
    'game': 'soz',
    'word': soz,
    'display': qolib,
    'attempts': []
}

await query.edit_message_text(
    f"🆝 So‘z topish o‘yini boshlandi!\n\n{len(soz)} harfdan iborat so‘zni toping:\n{' '.join(qolib)}\n\nHarf yuboring:"
)

Harf yoki son yuborilganda ishlovchi funksiya

async def handle_guess(update: Update, context: ContextTypes.DEFAULT_TYPE): user_id = update.message.from_user.id if user_id not in user_data: return

msg = update.message.text.strip()
data = user_data[user_id]

# So‘z topish
if data['game'] == 'soz':
    tahmin = msg.upper()
    if len(tahmin) != 1 or not tahmin.isalpha():
        await update.message.reply_text("Faqat bitta harf yuboring.")
        return

    data['attempts'].append(tahmin)
    if tahmin in data['word']:
        for i, harf in enumerate(data['word']):
            if harf == tahmin:
                data['display'][i] = tahmin
        if '_' not in data['display']:
            await update.message.reply_text(f"🎉 Tabriklaymiz! So‘z: {data['word']}\n/start bilan qayta boshlang.")
            del user_data[user_id]
        else:
            await update.message.reply_text(f"✅ Bor!\n{' '.join(data['display'])}")
    else:
        await update.message.reply_text(f"❌ Yo‘q.\n{' '.join(data['display'])}")

# Son topish (ikki bosqichli)
elif data['game'] == 'son':
    if data['step'] == 1:
        if not msg.isdigit():
            await update.message.reply_text("Iltimos, 1 dan 10 gacha son yuboring.")
            return

        guess = int(msg)
        if guess == data['number']:
            await update.message.reply_text(
                f"✅ Siz men o‘ylagan {data['number']} sonini topdingiz!\n"
                f"Urinishlar: {data['tries']}\n\n"
                "Endi siz son o‘ylang, men topishga harakat qilaman.\n"
                "OK deb yozing tayyor bo‘lsangiz."
            )
            data['step'] = 2
            data['comp_range'] = list(range(1, 11))
            data['comp_tries'] = 1
            data['game_ready'] = False
        elif guess < data['number']:
            data['tries'] += 1
            await update.message.reply_text("⬆ Men o‘ylagan son bundan katta.")
        else:
            data['tries'] += 1
            await update.message.reply_text("⬇ Men o‘ylagan son bundan kichik.")

    elif data['step'] == 2:
        if not data.get('game_ready'):
            if msg.lower() == "ok":
                data['game_ready'] = True
                comp_guess = random.choice(data['comp_range'])
                data['comp_guess'] = comp_guess
                await update.message.reply_text(
                    f"🤔 Siz o‘ylagan son {comp_guess} edi deb o‘ylayman.\n"
                    f"To‘g‘ri bo‘lsa: `T`, kichik bo‘lsa: `-`, katta bo‘lsa: `+` yozing."
                )
            else:
                await update.message.reply_text("OK deb yozing tayyor bo‘lsangiz.")
        else:
            javob = msg.strip().lower()
            comp_guess = data['comp_guess']
            if javob == 't':
                foydalanuvchi = data['tries']
                kompyuter = data['comp_tries']
                if foydalanuvchi > kompyuter:
                    text = f"💻 Kompyuter yutdi!\nSiz {foydalanuvchi} urinishda topdingiz, men esa {kompyuter} da."
                elif foydalanuvchi < kompyuter:
                    text = f"😎 Siz yutdingiz!\nSiz {foydalanuvchi} da topdingiz, men esa {kompyuter} da."
                else:
                    text = f"🤝 Do‘stlik g‘alaba qildi!\nIkkovimiz ham {foydalanuvchi} urinishda topdik!"
                await update.message.reply_text(text + "\n\n/start bilan boshqa o‘yin boshlang.")
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

            if data['game_ready']:
                if not data['comp_range']:
                    await update.message.reply_text("🤖 Xatolik! Sonlar oraliq bo‘sh.\n/start bilan qayta boshlang.")
                    del user_data[user_id]
                    return
                data['comp_guess'] = random.choice(data['comp_range'])
                await update.message.reply_text(
                    f"🤔 Balki siz {data['comp_guess']} ni o‘ylagandirsiz?\n"
                    f"To‘g‘ri bo‘lsa: `T`, kichik bo‘lsa: `-`, katta bo‘lsa: `+` yozing."
                )

# Matematik o‘yin
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
            await update.message.reply_text(f"❌ Siz mag‘lub bo‘ldingiz. Sirli son {data['original']} edi.\n/start bilan qayta boshlang.")
            del user_data[user_id]
        return

    data['tanlovlar'].append(tanlov)
    if data['secret'] % tanlov == 0:
        await update.message.reply_text(
            f"🎉 Tabriklaymiz! Siz {tanlov} sonini tanladingiz va bu sirli sonning bo‘luvchisi edi!\n"
            f"Sirli son: {data['original']}\n/start bilan yana o‘ynang."
        )
        del user_data[user_id]
    else:
        data['secret'] -= tanlov
        if data['secret'] < 0:
            await update.message.reply_text(
                f"💥 Siz yutqazdingiz. Sirli son {data['original']} edi,\n"
                f"u {tanlov} ni ayirish natijasida manfiy bo‘lib qoldi.\n/start bilan qayta o‘ynang."
            )
            del user_data[user_id]
        else:
            await update.message.reply_text(
                f"❌ {tanlov} bo‘luvchi emas. Sirli son hozir: {data['secret']}.\nYana son yuboring:"
            )

Botni ishga tushirish

if name == 'main': app = ApplicationBuilder().token("BU_YERGA_BOT_TOKENINGNI_QO'Y").build() app.add_handler(CommandHandler("start", start)) app.add_handler(CallbackQueryHandler(button_handler)) app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_guess)) print("Bot ishga tushdi!") app.run_polling()

