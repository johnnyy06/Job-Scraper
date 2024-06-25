import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def get_url(template, location, position):
    url = template.format(location, position)
    return url


def fetch_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        return BeautifulSoup(response.text, 'html.parser')
    else:
        raise Exception(f"Failed to fetch page: {response.status_code}")
    
    
    
def fetch_all_cards(url):
    # setari pentru a rula selenium fara a deschide browserul
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    # deschide browserul
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    #asteapta pana se incarca pagina
    last_height = driver.execute_script("return document.body.scrollHeight")
    
    #bucla while pentru a face scroll pana la finalul paginii
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    #parseaza pagina cu BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    #inchide browserul
    driver.quit()
    
    #returneaza pagina parsata
    return soup
