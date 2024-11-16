# Importing necessary modules
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from seleniumbase import Driver



#driver = webdriver.Chrome()
#driver.get("http://google.com")

driver = Driver(uc=True)
driver.get("https://www.1tamilmv.app")
time.sleep(3)

links = driver.find_elements(By.PARTIAL_LINK_TEXT,"Tamil")

for i in links:
    print(i.get_attribute("href"))
time.sleep(5)

driver.quit()


