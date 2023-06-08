"""
Scrapping interesting machine learning projects 
owner - saurav.purushothaman@gmail.com
"""

#imports 
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions 
from selenium.common.exceptions import TimeoutException

# prepare for easy opening new browser 
driver_option = webdriver.ChromeOptions
driver_option.add_argument(" - incognito") 
chromedriver_path = "./chrome_driver"
def create_webdriver():
    return webdriver.Chrome(executable_path = chromedriver_path, chrome_option = driver_option)


