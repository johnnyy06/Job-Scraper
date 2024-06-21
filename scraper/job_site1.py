from .fetcher import fetch_page

def get_job_site1(card):
    atag = card.div.a
    title = card.get('data-title')
    employer = card.get('data-employer-name')

    try:
        salary = card.find('div', 'text-nowrap').text.strip()
    except AttributeError:
        salary = ''


    job_url = atag.get('href')
    job = (title, employer, salary, job_url)

    # job -> variabila tupple care va contine titlul, companie, url-ul pentru job
    return job