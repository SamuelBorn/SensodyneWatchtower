import os
import time
from datetime import datetime

import dotenv
import requests
from bs4 import BeautifulSoup

# Download the Pushover app from the App Store or Google Play Store
# Load Pushover API keys from .env file
dotenv.load_dotenv()
PUSHOVER_TOKEN = os.getenv("PUSHOVER_TOKEN")
PUSHOVER_USER_KEY = os.getenv("PUSHOVER_USER_KEY")

# Content to monitor
url = "https://www.erlebe-haleon.de/deals/sensodyne-clinical-repair"
div_id = "restZahlAnzeige"


def get_content():
    response = requests.get(url)
    if response.status_code != 200:
        return None
    soup = BeautifulSoup(response.text, "html.parser")
    return soup.find("div", id=div_id)


def send_notification(message):
    data = {"token": PUSHOVER_TOKEN, "user": PUSHOVER_USER_KEY, "message": message}
    requests.post("https://api.pushover.net/1/messages.json", data=data)


def monitor_website():
    inital_content = get_content()

    while True:
        current_content = get_content()

        if current_content and current_content != inital_content:
            send_notification("The webpage content has changed!")
            return

        print(f"{datetime.now()} - No change detected.")
        time.sleep(3)


if __name__ == "__main__":
    monitor_website()
