from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import logging

# Enable logging to see what's happening
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Function to handle the /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Hello! I am your bot.')

# Function to echo back any other text messages
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(update.message.text)

# Main function to set up and run the bot
def main() -> None:
    # Create the application and set the bot token
    application = ApplicationBuilder().token('7438915846:AAG28ItjuC63bdSDC9fb6ALOvmp3T3aK6tQ').build()

    # Add command and message handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Start the bot and keep it running
    application.run_polling()

# Run the bot if this script is executed
if __name__ == '__main__':
    main()
