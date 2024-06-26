import tkinter as tk
from tkinter import scrolledtext
import sqlite3
import webbrowser

def open_url(url):
    webbrowser.open(url)

def search_jobs():    
    search_term = search_entry.get()
    
    # realizeaza conexiunea la baza de date
    conn = sqlite3.connect('data/jobs.db')
    
    # realizeaza cursorul
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM jobs WHERE \"0\" LIKE ?", ('%' + search_term + '%',))
    
    records = cursor.fetchall()
    
    results_text.config(state=tk.NORMAL)
    results_text.delete('1.0', tk.END)
    
    for record in records:
        job_title = record[0]
        url = record[3]
        results_text.insert(tk.END, job_title + "\n")
        results_text.insert(tk.END, url + "\n", "hyperlink")
        results_text.tag_add("hyperlink", "end-1c linestart", "end-1c")
        results_text.tag_config("hyperlink", foreground="blue", underline=1)
        results_text.tag_bind("hyperlink", "<Button-1>", lambda e, url=url: open_url(url))
    
    results_text.config(state=tk.DISABLED)
    conn.close()



# creaza fereasta
root = tk.Tk()
root.title("Find a job that matches you!")

# creaza bara de cautare
search_entry = tk.Entry(root, width=50)
search_entry.pack(pady=20)

# creaza butonul de cautare
search_button = tk.Button(root, text="Search", command=search_jobs)
search_button.pack()

# arata rezultatele in lista
results_text = scrolledtext.ScrolledText(root, width=100, height=20, wrap=tk.WORD)
results_text.pack(pady=20)
results_text.config(state=tk.DISABLED)

# porneste fereastra
root.mainloop()