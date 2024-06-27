# Job-Scraper
A Python application which will help you with job searching.

# 17.06.2024

    - am ales ca tema "Aplicatie Python - Web Scraping"
    - aplicatia pe care vreau sa o creez este un "Job Finder" -> aceasta va ajuta la gasirea unui job dupa anumite criterii introduse de utilizator

    - astazi am studiat mai avansat conceptul de web scraping si URL-urile (majoritatea proprietatilor URL-urilor)
    - de asemenea, am cautat informatii despre cateva tool-uri folosite in Python pentru acest procedeu
    - mi-am facut o idee despre cum ar trebui sa arate proiectul si despre cerintele pe care o astfel de aplicatie le presupune

# 18.06.2024
    
    - am creat un mediu virtual pentru a crea proiectul in acesta
    - am construit si configurat modul de lucru
    - am construit un sistem de fisiere -> scheletul proiectului
    - am inceput scrierea codului pentru scraper

# 19.06.2024

    - am reusit sa scriu codul pentru scraping
    - am observat ca pentru fiecare site se aplica un pattern diferit pentru colectarea datelor
    - am incercat cu cateva site-uri din tara si din strainatate si am fost destul de "norocos" ca primele mele incercari sa fie pe site-uri care imi detectau si respingeau activitatea (primeam eroare 403 => nu puteam sa iau datele)
    - in cele din urma am reusit cu cateva site-uri, iar acum va urma etapa de procesare a datelor

# 20.06.2024

    - am reusit sa parsez datele necesare pentru un site
    - in continuare (la urmatorul commit) vreau sa fac procesul pentru mai multe site-uri si sa-l generalizez pentru toate job-urile de un anumit fel de pe un site
    - urmeaza sa salvez datele gasite intr-un fisier de tip foaie de calcul

# 25.06.2024

    - am marit aplicatia pentru a face scraping la mai multe site-uri
    - rezultatele le-am salvat intr-un fisier tip baza de date
    - urmeaza sa fac o interfata grafica pentru a chestiona baza de date si a intoarce rezultatele dorite

# 26.06.2024

    - am realizat interfata grafica
    - aceasta ia rezultatele din baza de date si le afiseaza
    - am rezolvat un bug pentru parsarea informatiilor de pe site-ul 3

# 27.06.2024

    - proiectul este finalizat
    - am facut 2 variante
    - prima presupune cautarea unui job dupa nume si locatie -> cand se apasa butonul "Cauta" va incepe cautarea pe internet si extragerea informatiilor de pe site-uri -> dupa un scurt timp (aproximativ 3 secunde) cautarea va intoarce rezultatele care vor fi afisate intr-o lista pentru utilizator
    - a doua varianta presupune rularea script-ului de scraping pentru a extrage job-uri dintr-o lista de job-uri din diferite locatii (gasite tot intr-o lista) de pe diferite site-uri si salvarea acestora intr-o baza de date
    - aceasta cautare va lua mai mult timp, motiv pentru care am decis ca aceasta componenta sa fie singulara (doar sa faca scraping-ul, sa caute job-urile si sa le salveze in baza de date)
    - cea de-a doua componenta va fi un "motor de cautare" prin baza de date (va cauta un job dupa titlu, angajator, salariu si locatie)




## Sfat: va trebui crea inca un folder numit "data" in care vor fi 2 fisiere: "jobs.csv" si "jobs.db"