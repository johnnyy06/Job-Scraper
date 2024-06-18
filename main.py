from scraper.job_site1 import fetch_page, parse_job_site1
from scraper.utils import save_to_csv, save_to_db

def main():
    url = 'https://www.ejobs.ro/locuri-de-munca/it-software'
    soup = fetch_page(url)
    jobs = parse_job_site1(soup)
    save_to_csv(jobs)
    save_to_db(jobs)

if __name__ == '__main__':
    main()