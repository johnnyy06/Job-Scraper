from scraper import fetch_page, get_url, get_job_site1, get_job_site2, save_to_csv, save_to_db

def main():
    #location = input("Format locatie: <oras>\nIntrodu locatia job-ului: ")
    #position = input("\n\nFormat pozitie: <nume1>-<nume2>- ...\nIntrodu pozitia pentru care vrei sa aplici: ")

    # doar pentru teste
    location = "brasov"
    position = "software-developer"

    # template = "https://www.bestjobs.eu/ro/locuri-de-munca-in-{}/{}"
    # url = get_url(template, location, position)
    # soup = fetch_page(url)

    # cards = soup.find_all('div', 'col mb-5 js-card-item card-item job-card')

    # jobs = []
    # for card in cards:
    #     job = get_job_site1(card)
    #     jobs.append(job)
    
    # save_to_csv(jobs)
    # save_to_db(jobs)

    template = "https://www.ejobs.ro/locuri-de-munca/{}/{}"
    url = get_url(template, location, position)
    soup = fetch_page(url)

    cards = soup.find_all('div', 'JobCard')

    jobs = []
    for card in cards:
        job = get_job_site2(card)
        jobs.append(job)
        
    for i in jobs:
        print(i)

    # save_to_csv(jobs)
    # save_to_db(jobs)

if __name__ == '__main__':
    main()
