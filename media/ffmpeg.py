import ffmpeg
import logging

# Set up logging
logger = logging.getLogger(__name__)

def process_video(input_video_path, output_video_path):
    try:
        ffmpeg.input(input_video_path).output(output_video_path).run()
        logger.info(f"Video processed: {output_video_path}")
    except ffmpeg.Error as e:
        logger.error(f"FFmpeg error: {e}")
        return None
    return output_video_path
