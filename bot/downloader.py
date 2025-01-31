import requests
import sys
import os
import logging

# Set up logging
logger = logging.getLogger(__name__)

def download_video(video_url):
    try:
        response = requests.get(video_url, stream=True)
        if response.status_code != 200:
            logger.error(f"Failed to download video: {video_url}")
            return None

        video_path = f"downloads/{os.path.basename(video_url)}"
        
        # Write video content to file
        with open(video_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=1024):
                if chunk:
                    file.write(chunk)
        
        logger.info(f"Video downloaded: {video_path}")
        return video_path
    except requests.exceptions.RequestException as e:
        logger.error(f"Network error while downloading: {e}")
        return None
    except Exception as e:
        logger.error(f"Error downloading video: {e}")
        return None
