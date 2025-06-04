import os

def cancella_file(nome_file):
    comando = f"rm {nome_file}"
    os.system(comando)

# Esempio di uso
nome = input("Inserisci il nome del file da cancellare: ")
cancella_file(nome)
