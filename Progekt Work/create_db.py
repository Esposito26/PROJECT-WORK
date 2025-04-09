import sqlite3

# Connessione al database (verrà creato automaticamente se non esiste)
conn = sqlite3.connect('feedback.db')
cursor = conn.cursor()

# Creazione della tabella per il feedback
cursor.execute('''
    CREATE TABLE IF NOT EXISTS feedback (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        pdf_utility TEXT,
        liked_part TEXT,
        improvement TEXT,
        pdf_errors TEXT,
        error_details TEXT,
        web_navigation TEXT,
        info_found TEXT,
        info_searched TEXT,
        web_design TEXT,
        web_suggestions TEXT
    )
''')

# Commit delle modifiche e chiusura della connessione
conn.commit()
conn.close()

print("Database 'feedback.db' e tabella 'feedback' creati con successo.")
