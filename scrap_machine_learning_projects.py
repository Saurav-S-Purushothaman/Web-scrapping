"""
Scrapping interesting machine learning projects 
owner - saurav.purushothaman@gmail.com
"""

#imports 
from selenium import webdriver 
from selenium.webdriver.common.by import By 
import pandas as pd 


# prepare for easy opening new browser 
driver_option = webdriver.ChromeOptions()
driver_option.add_argument("--incognito") 

# chrome driver path configured by default. So removing this.
# chromedriver_path = "chrome_driver"

def create_webdriver():
    driver = webdriver.Chrome(options=driver_option)
    return driver


browser = create_webdriver()
browser.get("https://github.com/collections/machine-learning")

# using this to persist the browser session to get the xpath 
# input("Press any key to exit...")
# browser.quit()

projects = browser.find_elements(By.XPATH,"//h1[@class='h3 lh-condensed']")

prj_list = {}
for prj in projects : 
    prj_name = prj.text
    prj_url = prj.find_element(By.XPATH, "a").get_attribute("href")
    prj_list[prj_name] = prj_url



prj_df = pd.DataFrame.from_dict(prj_list,orient = "index")
prj_df["project_name"] = prj_df.index
prj_df.columns = ['project_url', 'project_name'] 

prj_df = prj_df.reset_index(drop = True )
prj_df.to_csv("machine_learning_open_source_projects.csv", index = False)
