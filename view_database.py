# view_database.py
import sqlite3
import json
from tabulate import tabulate

# Installer tabulate si nécessaire: pip install tabulate
conn = sqlite3.connect('karaoke.db')
cursor = conn.cursor()

# Récupération des données
cursor.execute("SELECT * FROM playlists")
rows = cursor.fetchall()

# Formatage des données
formatted_data = []
for row in rows:
    formatted_data.append([
        row[0],  # ID
        row[1],  # Téléphone
        row[2],  # Song ID
        row[3],  # Titre
        json.loads(row[4])  # Settings convertis de JSON à dict
    ])

# Affichage avec mise en forme
print(tabulate(
    formatted_data,
    headers=["ID", "Téléphone", "Song ID", "Titre", "Paramètres"],
    tablefmt="fancy_grid"
))

conn.close()