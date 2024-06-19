import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import os

db_path = os.path.join(os.path.dirname(__file__), 'dati.db')


def crea_db():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
    
    CREATE TABLE IF NOT EXISTS dati(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nominativo TEXT NOT NULL,
        num_bici TEXT NOT NULL,
        data_ini DATA NOT NULL,
        data_fin DATA NOT NULL,
        danni TEXT ,
        luce_ant TEXT NOT NULL,
        luce_post TEXT NOT NULL,
        casco TEXT NOT NULL,
        lucch TEXT NOT NULL,
        seggio TEXT NOT NULL,
        rip_spray TEXT NOT NULL,
        rotelle TEXT NOT NULL,
        note TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()


def inserisci_dati(nominativo, num_bici, data_ini, data_fin, danni, luce_ant, luce_post, casco, lucch, seggio,
                   rip_spray,
                   rotelle, note):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO dati (nominativo, num_bici, data_ini, data_fin,'
                   ' danni, luce_ant, luce_post, casco, lucch, seggio, rip_spray, rotelle, note) '
                   'VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)', (nominativo, num_bici, data_ini, data_fin,
                                                                      danni,
                                                                      luce_ant, luce_post, casco, lucch, seggio,
                                                                      rip_spray, rotelle, note))
    conn.commit()
    conn.close()
    messagebox.showinfo("Successo", "Dati Inseriti con successo!")


def ottieni_dati():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM dati')
    rows = cursor.fetchall()
    conn.close()
    return rows


def mostra_finestra_inserimento():
    def submit_data():
        nominativo = entry_nomi.get()
        num_bici = entry_num_bici.get()
        data_ini = entry_data_ini.get_date().strftime('%d-%m-%Y')
        data_fin = entry_data_fin.get_date().strftime('%d-%m-%Y')
        danni = entry_danni.get("1.0", tk.END)
        luce_ant = entry_luce_ant.get()
        luce_post = entry_luce_post.get()
        casco = entry_casco.get()
        lucch = entry_lucch.get()
        seggio = entry_seggio.get()
        rip_spray = entry_rip_spray.get()
        rotelle = entry_rotelle.get()
        note = entry_note.get("1.0", tk.END)

        if nominativo and num_bici and data_ini and data_fin:

            inserisci_dati(nominativo, num_bici, data_ini, data_fin, danni, luce_ant, luce_post, casco,
                           lucch, seggio, rip_spray, rotelle, note)

            entry_nomi.delete(0, tk.END)
            entry_num_bici.delete(0, tk.END)
            entry_data_ini.set_date('')
            entry_data_fin.set_date('')
            entry_danni.delete(1.0, tk.END)
            entry_luce_ant.delete(0, tk.END)
            entry_luce_post.delete(0, tk.END)
            entry_casco.delete(0, tk.END)
            entry_lucch.delete(0, tk.END)
            entry_seggio.delete(0, tk.END)
            entry_rip_spray.delete(0, tk.END)
            entry_rotelle.delete(0, tk.END)
            entry_note.delete(1.0, tk.END)
        else:
            messagebox.showwarning("Attenzione", "I campi non sono stati tutti compilati")

    window = tk.Tk()
    window.title("Inserisci Noleggio")

    tk.Label(window, text="Nominativo:").grid(row=0, column=0)
    entry_nomi = tk.Entry(window)
    entry_nomi.grid(row=0, column=1)

    tk.Label(window, text="N Bici:").grid(row=0, column=2)
    entry_num_bici = tk.Entry(window)
    entry_num_bici.grid(row=0, column=3)

    tk.Label(window, text="Da:").grid(row=1, column=0)
    entry_data_ini = DateEntry(window, date_pattern='dd-mm-yyyy')
    entry_data_ini.grid(row=1, column=2)

    tk.Label(window, text="A:").grid(row=2, column=0)
    entry_data_fin = DateEntry(window, date_pattern='dd-mm-yyyy')
    entry_data_fin.grid(row=2, column=2)

    tk.Label(window, text="Danni:").grid(row=3, column=0)
    entry_danni = tk.Text(window, height=5, width=30)
    entry_danni.grid(row=3, column=2, columnspan=3, padx=5, pady=5)

    tk.Label(window, text="Luce Anteriore:").grid(row=4, column=0)
    entry_luce_ant = tk.Entry(window)
    entry_luce_ant.grid(row=4, column=1)

    tk.Label(window, text="Luce Posteriore:").grid(row=5, column=0)
    entry_luce_post = tk.Entry(window)
    entry_luce_post.grid(row=5, column=1)

    tk.Label(window, text="Casco:").grid(row=6, column=0)
    entry_casco = tk.Entry(window)
    entry_casco.grid(row=6, column=1)

    tk.Label(window, text="Lucchetto:").grid(row=7, column=0)
    entry_lucch = tk.Entry(window)
    entry_lucch.grid(row=7, column=1)

    tk.Label(window, text="Seggiolino:").grid(row=8, column=0)
    entry_seggio = tk.Entry(window)
    entry_seggio.grid(row=8, column=1)

    tk.Label(window, text="Spray Riparatore:").grid(row=9, column=0)
    entry_rip_spray = tk.Entry(window)
    entry_rip_spray.grid(row=9, column=1)

    tk.Label(window, text="Rotelle:").grid(row=10, column=0)
    entry_rotelle = tk.Entry(window)
    entry_rotelle.grid(row=10, column=1)

    tk.Label(window, text="Note:").grid(row=11, column=0)
    entry_note = tk.Text(window, height=5, width=30)
    entry_note.grid(row=11, column=1, columnspan=3, padx=5, pady=5)

    tk.Button(window, text="Inserisci", command=submit_data).grid(row=12, column=0, columnspan=2)

    window.mainloop()


def mostra_finestra_lista():
    window = tk.Tk()
    window.title("Lista Noleggi")

    columns = ("ID", "Nominativo", "N Bici", "Data Inizio", "Data Fine", "Danni", "Luce Anteriore",
               "Luce Posteriore", "Casco", "Lucchetto", "Seggiolino", "Spray Riparatore", "Rotelle", "Note")

    tree = ttk.Treeview(window, columns=columns, show="headings")

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor=tk.CENTER, width=150)

    rows = ottieni_dati()

    for row in rows:
        tree.insert("", tk.END, values=row)

    tree.pack(fill=tk.BOTH, expand=True)

    window.mainloop()


def main():
    # assicurarsi che il database sia creato e popolato con dati
    crea_db()

    root = tk.Tk()
    root.title("Nole4Mori")

    tk.Button(root, text="Inserisci Noleggio", command=mostra_finestra_inserimento).pack(pady=10)
    tk.Button(root, text="Lista Noleggi", command=mostra_finestra_lista).pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()
