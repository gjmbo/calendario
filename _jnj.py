import sqlite3

def login(username, password):
    conn = sqlite3.connect("utenti.db")
    cursor = conn.cursor()

    # VULNERABILE a SQL Injection
    query = f"SELECT * FROM utenti WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)

    result = cursor.fetchone()
    if result:
        print("Accesso riuscito!")
    else:
        print("Accesso negato.")

# Esempio di input malevolo
login("admin", "' OR '1'='1")
