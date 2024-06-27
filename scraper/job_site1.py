def get_job_site1(card):
    atag = card.div.a
    
    # extrage titlul
    title = card.get('data-title')
    
    # extrage angajatorul
    employer = card.get('data-employer-name')

    # extrage salariul, daca exista
    try:
        salary = card.find('div', 'text-nowrap').text.strip()
    except AttributeError:
        salary = ''

    # extrage link-ul catre pagina job-ului
    job_url = atag.get('href')
    
    location = ''
    
    # creeaza variabila job care va contine titlul, compania, salariul, url-ul pentru job si locatia
    job = (title, employer, salary, job_url, location)

    return job