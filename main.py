from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from config import *

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://www.python.org/")

event_titles = driver.find_elements(By.CSS_SELECTOR, ".event-widget .menu a")
event_dates = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")

py_events = {}
for i in range(0, len(event_titles)):
    py_events[i] = {
        "time": event_dates[i].text,
        "name": event_titles[i].text,
    }

print(py_events)

# driver.close()
driver.quit()
