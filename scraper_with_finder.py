import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
import webbrowser

from scraper import fetch_page, get_url, get_job_site1, get_job_site2, get_job_site3

def open_url(url):
    webbrowser.open(url)

def scrap_and_display_jobs():    
    title = title_entry.get()
    location = location_entry.get()
    
    jobs = []
    
    # site 1
    template = "https://www.bestjobs.eu/ro/locuri-de-munca-in-{}/{}"
    url = get_url(template, location, title)
    soup = fetch_page(url)
            
    if soup != '':
        cards = soup.find_all('div', 'col mb-5 js-card-item card-item job-card')

        for card in cards:
            job = get_job_site1(card)
            if job is not None:
                job = list(job)
                job[4] = location
                jobs.append(job)
    
    
    
    # site 2
    template = "https://www.ejobs.ro/locuri-de-munca/{}/{}"
    url = get_url(template, location, title)
    soup = fetch_page(url)
            
    if soup != '':
        cards = soup.find_all('div', 'JobCard')

        for card in cards:
            job = get_job_site2(card)
            if job is not None:
                job = list(job)
                job[4] = location
                jobs.append(job)
    
    
    
    # site 3
    template = "https://www.hipo.ro/locuri-de-munca/cautajob/Toate-Domeniile/{}/{}/"
    url = get_url(template, location, title)
    soup = fetch_page(url)
            
    if soup != '':
        cards = soup.find_all('div', class_='job-item p-3 mb-4') # -> 10 carduri
    
        for card in cards:
            job = get_job_site3(card)
            if job is not None:
                job = list(job)
                job[4] = location
                jobs.append(job)


 
    results_text.config(state=tk.NORMAL)
    results_text.delete('1.0', tk.END)

    for record in jobs:
        rezultat = 'Titlu: ' + record[0] + '|\tAngajator: ' + record[1] + '|\tSalariu: ' + record[2] + '|\tLocatie: ' + record[4]
        url = record[3]
        results_text.insert(tk.END, rezultat + "\n")
        results_text.insert(tk.END, url + "\n", "hyperlink")
        results_text.tag_add("hyperlink", "end-1c linestart", "end-1c")
        results_text.tag_config("hyperlink", foreground="blue", underline=1)
        results_text.tag_bind("hyperlink", "<Button-1>", lambda e, url=url: open_url(url))
    
    results_text.config(state=tk.DISABLED)



# creaza fereasta
root = tk.Tk()
root.title("Gaseste un job care ti se potriveste!")

# creaza bara de cautare pentru titlul job-ului
tk.Label(root, text="Job").pack(side=tk.TOP, fill=tk.X)
title_entry = tk.Entry(root, width=50)
title_entry.pack(pady=20)

# creaza bara de cautare pentru locatia job-ului
tk.Label(root, text="Locatie").pack(side=tk.TOP, fill=tk.X)
location_entry = tk.Entry(root, width=50)
location_entry.pack(pady=20)

# creaza butonul de cautare
search_button = tk.Button(root, text="Cauta", command=scrap_and_display_jobs)
search_button.pack()

# arata rezultatele in lista
results_text = scrolledtext.ScrolledText(root, width=100, height=20, wrap=tk.WORD)
results_text.pack(pady=20)
results_text.config(state=tk.DISABLED)

# porneste fereastra
root.mainloop()