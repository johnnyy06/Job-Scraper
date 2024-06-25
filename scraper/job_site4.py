from .fetcher import fetch_page

def get_job_site4(card):
    atag = card.article.a
    title = card.find('a', 'u-text-double-line').text.strip()
    employer = card.find('dic', 'c-job-item__info-item').text.strip()

    salary = ''

    job_url =atag.get('href')
    job = (title, employer, salary, job_url)

    # job -> variabila tupple care va contine titlul, companie, url-ul pentru job
    return job