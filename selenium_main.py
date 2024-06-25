from scraper import fetch_page, fetch_all_cards, get_url, get_job_site1, get_job_site2, save_to_csv, save_to_db

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
    print(soup.prettify()) # -> aici am tot codul html de pe site
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