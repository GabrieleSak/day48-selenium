from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from config import *

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options, service=Service(executable_path=chrome_driver_path))

driver.get("https://www.google.com")

