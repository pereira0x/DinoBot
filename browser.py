from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service('./chromedriver')
driver = webdriver.Chrome(service=s)
driver.maximize_window()
driver.get("https://offline-dino-game.firebaseapp.com/")
