# test_import.py
try:
    from scraper.crunchyroll_scraper import get_video_url
    print("Import Successful")
except ImportError as e:
    print(f"ImportError: {e}")