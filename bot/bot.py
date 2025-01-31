import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from config.config import TELEGRAM_API_KEY  # Ensure the correct path is used  # Import the bot token from config.py
from scraper.crunchyroll_scraper import get_video_url
from downloader import download_video
from decryption import decrypt_video
from media.muxer import mux_video

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Start command to send welcome message
def start(update: Update, context: CallbackContext):
    try:
        update.message.reply_text('Welcome to the Crunchyroll Downloader Bot! Use /download <URL> to download videos.')
    except Exception as e:
        logger.error(f"Error in start command: {e}")
        update.message.reply_text("An error occurred while processing your request.")

# Download command to initiate video download process
def download(update: Update, context: CallbackContext):
    try:
        # Check if the user provided a URL
        if not context.args:
            update.message.reply_text("Please provide a Crunchyroll URL with the /download command.")
            return
        
        video_url = context.args[0]
        update.message.reply_text(f"Downloading video from: {video_url}")
        
        # Scrape video information from Crunchyroll
        video_info = get_video_url(video_url)
        if not video_info:
            update.message.reply_text("Failed to retrieve video info.")
            return
        
        # Download the video
        downloaded_video = download_video(video_info['video_url'])
        
        # Decrypt the video
        decrypted_video = decrypt_video(downloaded_video)
        
        # Mux video and audio into final format
        final_video = mux_video(decrypted_video)
        
        update.message.reply_text(f"Download and processing complete! Here is your video: {final_video}")
    except Exception as e:
        logger.error(f"Error in download command: {e}")
        update.message.reply_text("An error occurred while processing your request.")

# Main function to start the bot
def main():
    try:
        # Import the bot token from config.py
        updater = Updater(TELEGRAM_API_KEY, use_context=True)  # Use token from config.py
        dispatcher = updater.dispatcher

        dispatcher.add_handler(CommandHandler("start", start))
        dispatcher.add_handler(CommandHandler("download", download))

        # Start the bot
        updater.start_polling()
        updater.idle()
    except Exception as e:
        logger.error(f"Error starting the bot: {e}")

if __name__ == '__main__':
    main()
