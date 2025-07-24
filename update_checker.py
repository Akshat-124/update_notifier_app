import requests
from config import CURRENT_VERSION, VERSION_URL

def is_update_available():
    try:
        response = requests.get(VERSION_URL)
        latest_version = response.text.strip()
        print(f"Latest version: {latest_version} | Current version: {CURRENT_VERSION}")
        return latest_version != CURRENT_VERSION
    except Exception as e:
        print("Error checking update:", e)
        return False


