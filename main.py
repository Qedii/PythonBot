from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes


TOKEN: Final = '7319576557:AAF03X5jheN6n3JHdT0nx8YjhGX4Uk3dE3Y'
BOT_USERNAME: Final = '@python078_bot'

#Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! Its nice to see you! I am a programming language bot named as python!")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("I am a python bot! Please type something so I can respond to you!")

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("This is a custom command!")

#Responses

def handle_response(text: str) ->  str:
    processed: str = text.lower()

    if 'hello' or 'hi' or 'hey' in processed:
        return 'Hey there!'


    if 'how are you' in processed:
        return 'Im good! Thanks for asking! What about you?'


    if 'im good aswell' or 'im good too' in processed:
        return 'Im glad to hear that!'


    if 'i wanna learn python' in processed:
        return 'Then you can visit this youtube channels for better experience! ( freeCodeCamp.org ; Programming with Mosh ; Ishan Sharma etc.) '

    return 'I do not understand what you wrote...'

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)


    print('Bot:', response)
    await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}' )

if __name__ == '__main__':
    print('Starting bot...')
    app = Application.builder().token(TOKEN).build()

    #Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

    #Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    #Errors
    app.add_error_handler(error)

    #Polls the bot
    print('Polling...')
    app.run_polling(poll_interval=3)