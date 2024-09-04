import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import pandas as pd
import re
import time
import undetected_chromedriver as uc
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common import TimeoutException
from selenium.common.exceptions import TimeoutException, NoSuchElementException

options = uc.ChromeOptions()
options.add_argument("--lang=en-US")
driver = uc.Chrome(options=options)

#url = "https://www.imdb.com/search/name/?death_date=1985-01-01,2005-12-31"
#url = "https://www.imdb.com/search/name/?death_date=1985-01-01,1992-12-31"

#url = "https://www.imdb.com/search/name/?death_date=1993-01-01,1999-12-31"
#url = "https://www.imdb.com/search/name/?death_date=2000-01-01,2005-12-31"

url = "https://www.imdb.com/search/name/?birth_place=mexico&death_date=1800-01-01,2024-12-31&sort=death_date,asc"
driver.get(url)

time.sleep(20)
ratings=[]
titles= []
ratings_texts=[]
# Function to click the "Load more" button
def click_load_more():
    try:
        # Wait until the "Load more" button is present in the DOM
        load_more_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'button.ipc-btn.ipc-see-more__button'))
        )
        # Scroll the button into view and click it using JavaScript
        driver.execute_script("arguments[0].scrollIntoView();", load_more_button)
        time.sleep(0.5)  # Give it a moment to scroll into view
        driver.execute_script("arguments[0].click();", load_more_button)
        return True
    #except (TimeoutException, NoSuchElementException):
    except Exception as e:
        return False

'''
# Click the "Load more" button until it disappears or is unclickable
while click_load_more():
    time.sleep(5)
    pass
'''
for i in tqdm(range(500)): #1141
    res = click_load_more()
    time.sleep(3)
    if not res:
        break

time.sleep(10)
# After all reviews are loaded, you can scrape the data
ul = driver.find_element(By.CSS_SELECTOR, "ul.ipc-metadata-list.ipc-metadata-list--dividers-between.sc-748571c8-0.jApQAb.detailed-list-view.ipc-metadata-list--base")
lis = ul.find_elements(By.CSS_SELECTOR, "li.ipc-metadata-list-summary-item")

# Open a file to save the extracted data
with open('imdb_mexico_deaths.txt', 'w', encoding='utf-8') as file:
    # Loop through each review
    for li in tqdm(lis):
        # Extract the URL and title
        a_tag = li.find_element(By.CSS_SELECTOR, "a.ipc-title-link-wrapper")
        url = a_tag.get_attribute("href")
        title = a_tag.find_element(By.CSS_SELECTOR, "h3.ipc-title__text").text
        
        # Clean up the title (if needed)
        title = title.lstrip("1234567890. ")  # Remove numbers and periods from the beginning
        
        # Save the formatted data to the file
        file.write(f"{url} | {title}\n")
# Close the WebDriver
driver.quit()

