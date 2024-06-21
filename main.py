from scraper import fetch_page, get_url, get_job_site1, parse_job_site2, save_to_csv, save_to_db

def main():
    location = input("Format locatie: <oras>\nIntrodu locatia job-ului: ")
    position = input("\n\nFormat pozitie: <nume1>-<nume2>- ...\nIntrodu pozitia pentru care vrei sa aplici: ")

    template = "https://www.bestjobs.eu/ro/locuri-de-munca-in-{}/{}"
    url = get_url(template, location, position)
    soup = fetch_page(url)

    cards = soup.find_all('div', 'col mb-5 js-card-item card-item job-card')
    #cards = soup.find_all('div', 'card-51')
    print(cards[0])
    print(len(cards))

    # PENTRU VERIFICARE
    #soup = fetch_page(url)
    #cards = soup.find_all('div', 'col mb-5 js-card-item card-item job-card')
    #print(len(cards))

    card=cards[0]
    job = get_job_site1(card)
    print(job)

    print(cards[1])

    card=cards[1]
    job = get_job_site1(card)
    print(job)
    
    #save_to_csv(jobs)
    #save_to_db(jobs)

    #template = "https://www.ejobs.ro/locuri-de-munca/{}/{}"
    #url = get_url(template, location, position)
    

    # PENTRU VERIFICARE
    #soup = fetch_page(url)
    #cards = soup.find_all('div', 'JobCard')
    #print(len(cards))

    #jobs = parse_job_site2(url)
    #save_to_csv(jobs)
    #save_to_db(jobs)

if __name__ == '__main__':
    main()