def get_job_site3(card):
    # extrage titlul
    job_title_element = card.find('h5', itemprop='title')
    title = job_title_element.text.strip() if job_title_element else 'N/A'
    
    if title == 'N/A':
        return
    
    # extrage angajatorul
    company_name_element = card.find('span', itemprop='name')
    employer = company_name_element.text.strip() if company_name_element else 'N/A'
    
    # extrage link-ul catre pagina job-ului
    job_url_element = card.find('a', class_='job-title')
    job_url = 'https://www.hipo.ro/' + job_url_element['href'] if job_url_element else 'N/A'
    
    # extrage salariul, daca exista
    try:
        salary = card.find('div', 'JCContentMiddle__Salary').text.strip()
    except AttributeError:
        salary = ''
        
    location = ''

    # creeaza variabila job care va contine titlul, compania, salariul, url-ul pentru job si locatia
    job = (title, employer, salary, job_url, location)

    return job