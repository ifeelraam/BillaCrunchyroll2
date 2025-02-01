from scraper.crunchyroll_scraper import get_video_url
from bot.downloader import download_video
from bot.decryption import decrypt_video
from media.muxer import mux_video
import logging

# Set up logging
logger = logging.getLogger(__name__)

# Download function that is called from the download handler
def download_video_command(update, video_url):
    try:
        # Scrape video info from Crunchyroll
        video_info = get_video_url(video_url)
        if not video_info:
            update.message.reply_text("Failed to retrieve video info.")
            return

        # Download the video
        downloaded_video = download_video(video_info['video_url'])

        # Decrypt the downloaded video
        decrypted_video = decrypt_video(downloaded_video)

        # Mux video and audio into the final output
        final_video = mux_video(decrypted_video)

        # Send the final processed video back to the user
        # Assuming `final_video` is the path to the final video file
        update.message.reply_document(document=open(final_video, 'rb'))  # send the video as a document

        # Alternatively, if you want to send the video directly (without packaging as a document), use:
        # update.message.reply_video(video=open(final_video, 'rb'))

        # Optionally, notify the user the processing is complete
        update.message.reply_text(f"Download and processing complete! Here is your video: {final_video}")
    except Exception as e:
        # Log and notify the user if there was an error
        logger.error(f"Error in download_video_command: {e}")
        update.message.reply_text("An error occurred while processing the video.")