from .fetcher import fetch_page

def get_job_site3(card):
    atag = card.div.a
    title = card.find('h5', itemprop='title').text.strip()
    employer = card.find('span', itemprop='name').text.strip()

    try:
        salary = card.find('div', 'JCContentMiddle__Salary').text.strip()
    except AttributeError:
        salary = ''


    job_url ='hipo.ro' + atag.get('href')
    job = (title, employer, salary, job_url)

    # job -> variabila tupple care va contine titlul, companie, url-ul pentru job
    return job