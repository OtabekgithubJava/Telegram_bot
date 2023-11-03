from typing import Final
from telegram import Update
from telegram.ext  import *

TOKEN: Final = '6552844300:AAF7JqkllGSTFO8Keo5RG3ggNZBK7GzPKP8'
BOT_USERNAME: Final = '@Hello_The_Worldbot'

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("HEllo, Thanks for chatting with me! I'm a chatting buddy!")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("I'm a chatting buddy! Please type something, so I can respond")

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("This is a custom command!")

def handle_responses(text):

    processed: str = text.lower()

    if 'hello' in processed:
        return 'Hey there!'
    if 'Are you chatGPT?' or "are you GPT" in processed:
        return "No! I'm just a chatting buddy bot"
    return "I don't understand what you wrote..."

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_responses(new_text)
        else:
            return
    else:
        response: str = handle_responses(text)

    print('BOT:', response)
    await update.message.reply_text(response)



async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()


    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('start', custom_command))


    app.add_handler(MessageHandler(filter.TEXT, handle_message))


    app.add_error_handler(error)

    print("polling ...")



    app.run_polling(poll_interval=3)
