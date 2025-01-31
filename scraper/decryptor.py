import logging
from config import secrets
import subprocess

# Set up logging
logger = logging.getLogger(__name__)

def decrypt_video_with_key(encrypted_video_path):
    """
    This function handles the decryption of videos using mp4decrypt.
    It uses the decryption key from secrets.py.
    """
    try:
        decrypted_video_path = encrypted_video_path.replace('.mp4', '_decrypted.mp4')
        command = f"mp4decrypt --key {secrets.MP4DECRYPT_KEY} {encrypted_video_path} {decrypted_video_path}"
        
        # Execute decryption command
        subprocess.run(command, shell=True, check=True)
        
        logger.info(f"Video decrypted: {decrypted_video_path}")
        return decrypted_video_path
    except subprocess.CalledProcessError as e:
        logger.error(f"Error during decryption: {e}")
        return None
    except Exception as e:
        logger.error(f"Unexpected error in decryptor.py: {e}")
        return None
