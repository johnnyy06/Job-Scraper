import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
import sqlite3
import webbrowser

def open_url(url):
    webbrowser.open(url)

def search_jobs(): 
    # asigneaza valorile din campurile de cautare (fiecare unei variabile)
    title = title_entry.get()
    employer = employer_entry.get()
    salary = salary_entry.get()
    city = city_combobox.get()
    
    # realizeaza conexiunea la baza de date
    conn = sqlite3.connect('data/jobs.db')
    
    # realizeaza cursorul
    cursor = conn.cursor()
    
    # combina cautarile dupa titlu, angajator, salariu si oras intr-o singura interogare si sorteaza rezultatele dupa titlu si oras
    query = """
    SELECT * FROM jobs 
    WHERE "0" LIKE ? AND "1" LIKE ? AND "2" LIKE ? AND "4" LIKE ? 
    ORDER BY "0", "4"
    """
    parameters = ('%' + title + '%', '%' + employer + '%', '%' + salary + '%', '%' + city + '%',)
    cursor.execute(query, parameters)
    
    records = cursor.fetchall()
    
    results_text.config(state=tk.NORMAL)
    results_text.delete('1.0', tk.END)
    
    for record in records:
        rezultat = 'Titlu: ' + record[0] + '|\tAngajator: ' + record[1] + '|\tSalariu: ' + record[2] + '|\tLocatie: ' + record[4]
        url = record[3]
        results_text.insert(tk.END, rezultat + "\n")
        results_text.insert(tk.END, url + "\n", "hyperlink")
        results_text.tag_add("hyperlink", "end-1c linestart", "end-1c")
        results_text.tag_config("hyperlink", foreground="blue", underline=1)
        results_text.tag_bind("hyperlink", "<Button-1>", lambda e, url=url: open_url(url))
    
    results_text.config(state=tk.DISABLED)
    conn.close()



# creaza fereasta
root = tk.Tk()
root.title("Gaseste un job care ti se potriveste!")

# creaza bara de cautare pentru titlul job-ului
tk.Label(root, text="Job").pack(side=tk.TOP, fill=tk.X)
title_entry = tk.Entry(root, width=50)
title_entry.pack(pady=20)

# creaza bara de cautare pentru angajatorul job-ului
tk.Label(root, text="Angajator").pack(side=tk.TOP, fill=tk.X)
employer_entry = tk.Entry(root, width=50)
employer_entry.pack(pady=20)

# creaza bara de cautare pentru salariul job-ului
tk.Label(root, text="Salariu").pack(side=tk.TOP, fill=tk.X)
salary_entry = tk.Entry(root, width=50)
salary_entry.pack(pady=20)

# creaza bara de cautare pentru orasul job-ului
tk.Label(root, text="Locatie").pack(side=tk.TOP, fill=tk.X)
cities = ["Bucuresti", "Cluj-Napoca", "Iasi", "Timisoara", "Constanta", "Brasov", "Sibiu", "Arad", "Oradea", "Galati", "Craiova", "Baia-Mare", "Targu-Mures", "Alba-Iulia", "Deva", "Targu-Jiu"]
city_combobox = ttk.Combobox(root, width=49, values=cities)
city_combobox.pack()

# creaza butonul de cautare
search_button = tk.Button(root, text="Cauta", command=search_jobs)
search_button.pack()

# arata rezultatele in lista
results_text = scrolledtext.ScrolledText(root, width=100, height=20, wrap=tk.WORD)
results_text.pack(pady=20)
results_text.config(state=tk.DISABLED)

# porneste fereastra
root.mainloop()