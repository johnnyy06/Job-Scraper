def get_job_site2(card):
    atag = card.div.a
    
    # extrage titlul
    title = card.find('span').text.strip()
    
    # extrage angajatorul
    employer = card.find('a').text.strip()

    # extrage salariul, daca exista
    try:
        salary = card.find('div', 'JCContentMiddle__Salary').text.strip()
    except AttributeError:
        salary = ''

    # extrage link-ul catre pagina job-ului
    job_url ='ejobs.ro' + atag.get('href')
    
    location = ''
    
    # creeaza variabila job care va contine titlul, compania, salariul, url-ul pentru job si locatia
    job = (title, employer, salary, job_url, location)

    return job