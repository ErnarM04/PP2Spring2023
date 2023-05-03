import telegram, psycopg2
from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

conn = psycopg2.connect(
    host='localhost',
    dbname='KBTU',
    user='postgres',
    password='20112004erkow',
    port = '6566'
)

TOKEN: Final = "5920440522:AAGldHJcHfFi_ct8y1T3ywZLTkQA9MkjiZQ"
BOT_USERNAME: Final = '@kbtuhelper_bot'

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! Here you can find the cabinet you need. Write only in English.')
async def credit_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This bot can hep you find room you want in KBTU. In the future, I will add some features. Creator is Mukhtaruly Ernar (@er_m2004).')
async def map_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('You can get map of the floor you want by typing "map {floor}".')

def handle_response(text):
    processed = text.lower()
    if 'hello' in processed:
        return 'Hey there!'
    if 'kbtu' in processed:
        return 'I do not like it'
    return 'I do not understand what you wrote'

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type = update.message.chat.type
    text = update.message.text
    cur = conn.cursor()

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')
    response = ''
    text = text.lower()

    if 'map' in text:
        if text == 'map 1':
            await update.message.reply_photo('1st floor.jpg')
        elif text == 'map 2':
            await update.message.reply_photo('2nd floor.jpg')
        elif text == 'map 3':
            await update.message.reply_photo('3rd floor.jpg')
        elif text == 'map 4':
            await update.message.reply_photo('4th floor.jpg')
        elif text == 'map 5':
            await update.message.reply_photo('5th floor.jpg')
    elif 'map' not in text:
        cur.execute("SELECT * FROM rooms WHERE name = %s", (text,))
        room = cur.fetchall()
        if room != []:
            place = room[0][1]
            await update.message.reply_text(place)
        else:
            text = text[0:-1]
            cur.execute("SELECT * FROM rooms WHERE name ILIKE %s", (text,))
            room = cur.fetchall()
            if room == []:
                cur.execute("SELECT * FROM rooms WHERE name ILIKE %s", ('%' + text + '%',))
                room = cur.fetchall()
                place = room[0][1]
                await update.message.reply_text(place)
            else:
                place = room[0][1]
                await update.message.reply_text(place)
    elif message_type == 'group':
        if BOT_USERNAME in text:
            new_text = text.replace(BOT_USERNAME, '').strip()
            response = handle_response(new_text)
        else:
            return
    else:
        response = handle_response(text)

    if response != '':
        print('Bot:', response)
        await update.message.reply_text(response)

    cur.close()
    
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')
    
if __name__ == '__main__':
    print('Starting bot...')
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('credits', credit_command))
    app.add_handler(CommandHandler('map', map_command))

    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    
    app.add_error_handler(error)
    
    print('Polling...')
    app.run_polling(poll_interval=3)