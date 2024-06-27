from scraper import fetch_page, get_url, get_job_site1, get_job_site2, get_job_site3, save_to_csv, save_to_db
import time

def main():
    # lista orase
    cities = ["bucuresti", "brasov", "cluj-napoca", "iasi", "sibiu", "timisoara", "constanta", "arad", "oradea", "galati", "craiova", "baia-mare", "targu-mures", "alba-iulia", "deva", "targu-jiu"]
    
    # lista pozitii
    positions = ["software-developer", "contabil", "medic", "electrician", "sofer", "casier", "inginer", "asistent-medical", "receptioner", "mecanic-auto", "bucatar", "barman", "vanzator", "consultant-vanzari", "asistent-manager", "asistent-social", "asistent-relatii-clienti", "asistent-financiar", "asistent-marketing", "asistent-achizitii", "paznic"]
    
    #lista cu job-uri
    jobs = []

    for position in positions:
        for location in cities:
            
            # site 1
            template = "https://www.bestjobs.eu/ro/locuri-de-munca-in-{}/{}"
            url = get_url(template, location, position)
            soup = fetch_page(url)
            
            if soup != '':
                cards = soup.find_all('div', 'col mb-5 js-card-item card-item job-card')

                for card in cards:
                    job = get_job_site1(card)
                    if job is not None:
                        job = list(job)
                        job[4] = location
                        jobs.append(job)
    
                save_to_csv(jobs)
                save_to_db(jobs)
    
    
            # site 2
            template = "https://www.ejobs.ro/locuri-de-munca/{}/{}"
            url = get_url(template, location, position)
            soup = fetch_page(url)
            
            if soup != '':
                cards = soup.find_all('div', 'JobCard')

                for card in cards:
                    job = get_job_site2(card)
                    if job is not None:
                        job = list(job)
                        job[4] = location
                        jobs.append(job)

                save_to_csv(jobs)
                save_to_db(jobs)
    
    
            # site 3
            template = "https://www.hipo.ro/locuri-de-munca/cautajob/Toate-Domeniile/{}/{}/"
            url = get_url(template, location, position)
            soup = fetch_page(url)
            
            if soup != '':
                cards = soup.find_all('div', class_='job-item p-3 mb-4') # -> 10 carduri
    
                for card in cards:
                    job = get_job_site3(card)
                    if job is not None:
                        job = list(job)
                        job[4] = location
                        jobs.append(job)
     
                save_to_csv(jobs)
                save_to_db(jobs)

            time.sleep(1)
        time.sleep(2)

if __name__ == '__main__':
    main()
