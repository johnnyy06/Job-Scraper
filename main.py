from scraper import fetch_page, get_url, get_job_site1, get_job_site2, get_job_site3, get_job_site4, save_to_csv, save_to_db

def main():
    #location = input("Format locatie: <oras>\nIntrodu locatia job-ului: ")
    #position = input("\n\nFormat pozitie: <nume1>-<nume2>- ...\nIntrodu pozitia pentru care vrei sa aplici: ")

    #lista cu job-uri
    jobs = []
    
    # doar pentru teste
    location = "brasov"
    position = "software-developer"

    # site 1
    template = "https://www.bestjobs.eu/ro/locuri-de-munca-in-{}/{}"
    url = get_url(template, location, position)
    soup = fetch_page(url)

    cards = soup.find_all('div', 'col mb-5 js-card-item card-item job-card')
    
    for card in cards:
        job = get_job_site1(card)
        jobs.append(job)
    
    save_to_csv(jobs)
    save_to_db(jobs)
    
    
    # site 2
    template = "https://www.ejobs.ro/locuri-de-munca/{}/{}"
    url = get_url(template, location, position)
    soup = fetch_page(url)

    cards = soup.find_all('div', 'JobCard')

    for card in cards:
        job = get_job_site2(card)
        jobs.append(job)

    save_to_csv(jobs)
    save_to_db(jobs)
    
    
    # site 3
    template = "https://www.hipo.ro/locuri-de-munca/cautajob/Toate-Domeniile/{}/{}/"
    url = get_url(template, location, position)
    soup = fetch_page(url)
    
    job_title_element = soup.find('h5', itemprop='title').text.strip()
    print(job_title_element)
    
    cards = soup.find_all('div', 'job-item p-3 mb-4') # -> 10 carduri
    
    for card in cards:
        job = get_job_site3(card)
        jobs.append(job)
     
    save_to_csv(jobs)
    save_to_db(jobs)

if __name__ == '__main__':
    main()
