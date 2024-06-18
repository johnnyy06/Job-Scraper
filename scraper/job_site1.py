from scraper.fetcher import fetch_page

def parse_job_site1(soup):
    jobs = []
    for job in soup.find_all('div', class_='job-listing'):
        title = job.find('h2').text
        company = job.find('div', class_='company').text
        location = job.find('div', class_='location').text
        jobs.append({
            'title': title,
            'company': company,
            'location': location
        })
    return jobs