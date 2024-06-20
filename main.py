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
        data_ini TEXT NOT NULL,
        data_fin TEXT NOT NULL,
        danni TEXT,
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
                   rip_spray, rotelle, note):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO dati (nominativo, num_bici, data_ini, data_fin, danni, luce_ant, luce_post, casco, '
                   'lucch, seggio, rip_spray, rotelle, note) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                   (nominativo, num_bici, data_ini, data_fin, danni, luce_ant, luce_post, casco, lucch, seggio,
                    rip_spray, rotelle, note))
    conn.commit()
    conn.close()
    messagebox.showinfo("Successo", "Dati inseriti con successo!")


def aggiorna_dati(id, nominativo, num_bici, data_ini, data_fin, danni, luce_ant, luce_post, casco, lucch, seggio,
                  rip_spray, rotelle, note):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('UPDATE dati SET nominativo=?, num_bici=?, data_ini=?, data_fin=?, danni=?, luce_ant=?, luce_post=?,'
                   ' casco=?, lucch=?, seggio=?, rip_spray=?, rotelle=?, note=? WHERE id=?',
                   (nominativo, num_bici, data_ini, data_fin, danni, luce_ant, luce_post, casco, lucch, seggio,
                    rip_spray, rotelle, note, id))
    conn.commit()
    conn.close()
    messagebox.showinfo("Successo", "Dati aggiornati con successo!")


def elimina_dati(id):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM dati WHERE id=?', (id,))
    conn.commit()
    conn.close()
    messagebox.showinfo("Successo", "Dati eliminati con successo!")


def ottieni_dati():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM dati')
    rows = cursor.fetchall()
    conn.close()
    return rows


def mostra_finestra_inserimento(id=None, dati=None):
    def submit_data():
        nominativo = entry_nomi.get()
        num_bici = entry_num_bici.get()
        data_ini = entry_data_ini.get_date().strftime('%d-%m-%Y')
        data_fin = entry_data_fin.get_date().strftime('%d-%m-%Y')
        danni = entry_danni.get("1.0", tk.END).strip()
        luce_ant = entry_luce_ant.get()
        luce_post = entry_luce_post.get()
        casco = entry_casco.get()
        lucch = entry_lucch.get()
        seggio = entry_seggio.get()
        rip_spray = entry_rip_spray.get()
        rotelle = entry_rotelle.get()
        note = entry_note.get("1.0", tk.END).strip()

        if nominativo and num_bici and data_ini and data_fin:
            if id:
                aggiorna_dati(id, nominativo, num_bici, data_ini, data_fin, danni, luce_ant, luce_post, casco, lucch,
                              seggio, rip_spray, rotelle, note)
            else:
                inserisci_dati(nominativo, num_bici, data_ini, data_fin, danni, luce_ant, luce_post, casco, lucch,
                               seggio, rip_spray, rotelle, note)

            window.destroy()
            mostra_finestra_lista()
        else:
            messagebox.showwarning("Attenzione", "I campi non sono stati tutti compilati")

    window = tk.Tk()
    window.title("Inserisci Noleggio" if not id else "Modifica Noleggio")

    # Stile minimalista e color scuri
    style = ttk.Style(window)
    style.configure("TLabel", font=("Helvetica", 12), background="#2e2e2e", foreground="#ffffff")
    style.configure("TButton", font=("Helvetica", 12), background="#4a4a4a", foreground="#ffffff")
    style.configure("TEntry", font=("Helvetica", 12), background="#3e3e3e", foreground="#ffffff")
    style.configure("TText", font=("Helvetica", 12), background="#3e3e3e", foreground="#ffffff")
    style.configure("TFrame", background="#2e2e2e")

    window.configure(bg="#2e2e2e")

    frame = ttk.Frame(window)
    frame.grid(row=0, column=0, padx=20, pady=20)

    ttk.Label(window, text="Nominativo:").grid(row=0, column=0, padx=10, pady=5)
    entry_nomi = ttk.Entry(window)
    entry_nomi.grid(row=0, column=1, padx=10, pady=5)
    if dati:
        entry_nomi.insert(0, dati[1])

    ttk.Label(window, text="N Bici:").grid(row=0, column=2, padx=10, pady=5)
    entry_num_bici = ttk.Entry(window)
    entry_num_bici.grid(row=0, column=3, padx=10, pady=5)
    if dati:
        entry_num_bici.insert(0, dati[2])

    ttk.Label(window, text="Da:").grid(row=1, column=0, padx=10, pady=5)
    entry_data_ini = DateEntry(window, date_pattern='dd-mm-yyyy')
    entry_data_ini.grid(row=1, column=1, padx=10, pady=5)
    if dati:
        entry_data_ini.set_date(dati[3])

    ttk.Label(window, text="A:").grid(row=1, column=2, padx=10, pady=5)
    entry_data_fin = DateEntry(window, date_pattern='dd-mm-yyyy')
    entry_data_fin.grid(row=1, column=3, padx=10, pady=5)
    if dati:
        entry_data_fin.set_date(dati[4])

    ttk.Label(window, text="Danni:").grid(row=2, column=0, padx=10, pady=5)
    entry_danni = tk.Text(window, height=3, width=30, font=("Helvetica", 12), bg="#ffffff")
    entry_danni.grid(row=2, column=1, columnspan=3, padx=10, pady=5)
    if dati:
        entry_danni.insert(1.0, dati[5])

    ttk.Label(window, text="Luce Anteriore:").grid(row=3, column=0, padx=10, pady=5)
    entry_luce_ant = ttk.Entry(window)
    entry_luce_ant.grid(row=3, column=1, padx=10, pady=5)
    if dati:
        entry_luce_ant.insert(0, dati[6])

    ttk.Label(window, text="Luce Posteriore:").grid(row=3, column=2, padx=10, pady=5)
    entry_luce_post = ttk.Entry(window)
    entry_luce_post.grid(row=3, column=3, padx=10, pady=5)
    if dati:
        entry_luce_post.insert(0, dati[7])

    ttk.Label(window, text="Casco:").grid(row=4, column=0, padx=10, pady=5)
    entry_casco = ttk.Entry(window)
    entry_casco.grid(row=4, column=1, padx=10, pady=5)
    if dati:
        entry_casco.insert(0, dati[8])

    ttk.Label(window, text="Lucchetto:").grid(row=4, column=2, padx=10, pady=5)
    entry_lucch = ttk.Entry(window)
    entry_lucch.grid(row=4, column=3, padx=10, pady=5)
    if dati:
        entry_lucch.insert(0, dati[9])

    ttk.Label(window, text="Seggiolino:").grid(row=5, column=0, padx=10, pady=5)
    entry_seggio = ttk.Entry(window)
    entry_seggio.grid(row=5, column=1, padx=10, pady=5)
    if dati:
        entry_seggio.insert(0, dati[10])

    ttk.Label(window, text="Spray Riparatore:").grid(row=5, column=2, padx=10, pady=5)
    entry_rip_spray = ttk.Entry(window)
    entry_rip_spray.grid(row=5, column=3, padx=10, pady=5)
    if dati:
        entry_rip_spray.insert(0, dati[11])

    ttk.Label(window, text="Rotelle:").grid(row=6, column=0, padx=10, pady=5)
    entry_rotelle = ttk.Entry(window)
    entry_rotelle.grid(row=6, column=1, padx=10, pady=5)
    if dati:
        entry_rotelle.insert(0, dati[12])

    ttk.Label(window, text="Note:").grid(row=6, column=2, padx=10, pady=5)
    entry_note = tk.Text(window, height=3, width=30, font=("Helvetica", 12), bg="#ffffff")
    entry_note.grid(row=6, column=3, padx=10, pady=5)
    if dati:
        entry_note.insert(1.0, dati[13])

    ttk.Button(window, text="Inserisci" if not id else "Modifica", command=submit_data).grid(row=7, column=0,
                                                                                             columnspan=4, pady=10)

    window.mainloop()


def mostra_finestra_lista():
    def modifica_selezione():
        selezione = tree.selection()
        if selezione:
            item = tree.item(selezione)
            valori = item['values']
            mostra_finestra_inserimento(id=valori[0], dati=valori)

    def elimina_selezione():
        selezione = tree.selection()
        if selezione:
            item = tree.item(selezione)
            valori = item['values']
            elimina_dati(valori[0])
            mostra_finestra_lista()

    window = tk.Tk()
    window.title("Lista Noleggi")
    window.configure(bg="#f0f0f0")  # Colore di sfondo grigio chiaro

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

    tk.Button(window, text="Modifica", command=modifica_selezione).pack(side=tk.LEFT, padx=10, pady=10)
    tk.Button(window, text="Elimina", command=elimina_selezione).pack(side=tk.RIGHT, padx=10, pady=10)

    window.mainloop()


def main():
    crea_db()

    root = tk.Tk()
    root.title("Nole4Mori")
    root.configure(bg="#202020")  # Colore di fonds scour

    tk.Label(root, text="Benvenuto su Nole4Mori", font=("Helvetica", 20), fg="white", bg="#202020").pack(pady=20)

    tk.Button(root, text="Inserisci Noleggio", command=mostra_finestra_inserimento, width=20).pack(pady=10)
    tk.Button(root, text="Lista Noleggi", command=mostra_finestra_lista, width=20).pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    main()
