import os
from datetime import datetime
from PIL import ImageGrab

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCREENSHOT_DIR = os.path.join(BASE_DIR, "data", "screenshots")

os.makedirs(SCREENSHOT_DIR, exist_ok=True)


def take_screenshot():

    filename = datetime.now().strftime("screenshot_%Y%m%d_%H%M%S.png")

    path = os.path.join(SCREENSHOT_DIR, filename)

    screenshot = ImageGrab.grab()

    screenshot.save(path)

    return path


def open_screenshot_folder():

    os.startfile(SCREENSHOT_DIR)