from scraper import fetch_page, get_url, get_job_site1, get_job_site2, save_to_csv, save_to_db

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time

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

def main():
    #setare locatie si pozitie cautate pentru teste
    location = "brasov"
    position = "software-developer"
    
    #setare url template (site-ul pentru job-uri ejobs.ro cu pozitie si locatie ca parametri)
    template = "https://www.ejobs.ro/locuri-de-munca/{}/{}"
    
    #setare url final (adauga pozitia si locatia pe care le-am dat mai sus ca parametri)
    url = template.format(location, position)

    #parseaza pagina cu BeautifulSoup
    soup = fetch_all_cards(url)
    
    #------
    # pentru verificare
    print(soup) # -> aici am tot codul html de pe site
    # aici ia doar 3 job cards
    for i in soup.find_all('div', {'class': 'JobCard'}):
        print(i)
    #-------

    #cauta toate job cards (dintr-un motiv necunoscut, nu imi ia toate job cards, ci doar 3)
    cards = soup.find_all('div', 'JobCard')
    
    jobs = []
    for card in cards:
        job = get_job_site2(card)
        jobs.append(job)

    #afiseaza job-urile (titlu job, companie, salariu si link catre job)
    for i in jobs:
        print(i)

if __name__ == '__main__':
    main()