import subprocess
import logging
from config import secrets

# Set up logging
logger = logging.getLogger(__name__)

def decrypt_video(encrypted_video_path):
    try:
        decrypted_video_path = encrypted_video_path.replace('.mp4', '_decrypted.mp4')
        # Run mp4decrypt command (ensure mp4decrypt is installed and available in the PATH)
        command = f"mp4decrypt --key '{secrets.MP4DECRYPT_KEY}' {encrypted_video_path} {decrypted_video_path}"
        subprocess.run(command, shell=True, check=True)
        
        logger.info(f"Video decrypted: {decrypted_video_path}")
        return decrypted_video_path
    except subprocess.CalledProcessError as e:
        logger.error(f"Decryption error: {e}")
        return None
    except Exception as e:
        logger.error(f"Error decrypting video: {e}")
        return None
