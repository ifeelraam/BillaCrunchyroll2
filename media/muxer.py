import ffmpeg
import logging

# Set up logging
logger = logging.getLogger(__name__)

def mux_video(decrypted_video_path):
    try:
        output_file = decrypted_video_path.replace('_decrypted', '_final')
        # Mux video and audio
        ffmpeg.input(decrypted_video_path).output(output_file).run()
        
        logger.info(f"Video muxed and saved to {output_file}")
        return output_file
    except ffmpeg.Error as e:
        logger.error(f"Error during muxing: {e}")
        return None
