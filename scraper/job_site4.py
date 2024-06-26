from .fetcher import fetch_page

def get_job_site4(card):
    atag = card.div.a
    title = card.find('h2', 'job-title').text.strip()
    employer = card.find('p', 'company-name').text.strip()

    salary = ''

    job_url =atag.get('href')
    job = (title, employer, salary, job_url)

    # job -> variabila tupple care va contine titlul, companie, url-ul pentru job
    return job