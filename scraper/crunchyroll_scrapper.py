import sys
import os
import requests
from bs4 import BeautifulSoup
import logging
from config.config import CRUNCHYROLL_EMAIL, CRUNCHYROLL_PASSWORD

# Set up logging
logger = logging.getLogger(__name__)

def login_to_crunchyroll(session):
    try:
        # Set up login URL and credentials
        login_url = "https://www.crunchyroll.com/login"
        payload = {
            'email': CRUNCHYROLL_EMAIL,
            'password': CRUNCHYROLL_PASSWORD
        }

        # Send POST request to log in
        response = session.post(login_url, data=payload)

        # Check if login was successful
        if response.status_code != 200 or "incorrect login" in response.text.lower():
            logger.error("Login failed. Please check your credentials.")
            return False
        
        logger.info("Login successful.")
        return True
    except Exception as e:
        logger.error(f"Error logging in: {e}")
        return False

def get_video_url(cr_url):
    try:
        # Initialize a session to handle cookies and login
        session = requests.Session()

        # Log in to Crunchyroll with premium credentials
        if not login_to_crunchyroll(session):
            return None

        # Fetch page content
        response = session.get(cr_url)
        if response.status_code != 200:
            logger.error(f"Failed to fetch video page: {cr_url}")
            return None

        page_content = response.text
        
        # Parse page content with BeautifulSoup
        soup = BeautifulSoup(page_content, 'html.parser')

        # Extract video URL
        video_url = soup.find('video')['src']
        
        # Extract additional metadata such as title
        title = soup.find('title').text.strip()
        
        logger.info(f"Video URL extracted: {video_url}")
        return {'video_url': video_url, 'title': title}
    
    except Exception as e:
        logger.error(f"Error in get_video_url: {e}")
        return None
