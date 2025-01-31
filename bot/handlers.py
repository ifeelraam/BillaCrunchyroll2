from telegram import Update
from telegram.ext import CallbackContext
from bot.commands import download_video_command
import logging

# Set up logging
logger = logging.getLogger(__name__)

# Handler for /start command
def start_handler(update: Update, context: CallbackContext):
    try:
        update.message.reply_text('Welcome to the Crunchyroll Downloader Bot! Use /download <URL> to download videos.')
    except Exception as e:
        logger.error(f"Error in start_handler: {e}")
        update.message.reply_text("An error occurred while processing your request.")

# Handler for /download command
def download_handler(update: Update, context: CallbackContext):
    try:
        # Ensure the user provided a URL
        if not context.args:
            update.message.reply_text("Please provide a Crunchyroll URL with the /download command.")
            return

        video_url = context.args[0]
        update.message.reply_text(f"Downloading video from: {video_url}")
        
        # Call the download function (defined in bot.commands)
        download_video_command(update, video_url)
    except Exception as e:
        logger.error(f"Error in download_handler: {e}")
        update.message.reply_text("An error occurred while processing your request.")