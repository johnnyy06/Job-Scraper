from scraper import fetch_page, get_url, get_job_site1, get_job_site2, save_to_csv, save_to_db

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

def fetch_all_cards(url):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = webdriver.Chrome(options=options)
    driver.get(url)

    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()
    return soup

def main():
    location = "brasov"
    position = "software-developer"
    template = "https://www.ejobs.ro/locuri-de-munca/{}/{}"
    url = template.format(location, position)

    soup = fetch_all_cards(url)
    # pentru verificare
    print(soup) # -> aici am tot codul html de pe site
    
    # aici ia doar 3 job cards
    for i in soup.find_all('div', {'class': 'JobCard'}):
        print(i)

    cards = soup.find_all('div', 'JobCard')
    jobs = []
    for card in cards:
        job = get_job_site2(card)
        jobs.append(job)

    for i in jobs:
        print(i)

if __name__ == '__main__':
    main()