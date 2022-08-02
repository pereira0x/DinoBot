import argparse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

parser = argparse.ArgumentParser()

# Flag to start program on bot mode
parser.add_argument("-b", "--bot", action='store_true',
                    help="play using a bot")
# Flag to start program on video capture mode
parser.add_argument("-v", "--video", action='store_true',
                    help="play using video capture")

args = parser.parse_args()

# If both flags are set, raise error
if args.bot == args.video == True:
    print("Both flags -b and -v are set. Please use only one.")
    exit()

# Open Chrome browser on the game URL
s = Service('./chromedriver')
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://offline-dino-game.firebaseapp.com/")
