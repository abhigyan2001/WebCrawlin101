from selenium import webdriver
import time
class ScraperBot:
    def __init__(self):
        self.driver = webdriver.Chrome() #Note that I am using Chrome Web Driver, you will need to change this line.
        self.driver.get("https://www.google.com")
        time.sleep(10)
new ScraperBot()