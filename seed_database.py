# seed_database.py
import sqlite3
import json

# Connexion à la base
conn = sqlite3.connect('karaoke.db')
cursor = conn.cursor()

# Créer la table si elle n'existe pas
cursor.execute('''
CREATE TABLE IF NOT EXISTS playlists (
    id INTEGER PRIMARY KEY,
    phone TEXT NOT NULL,
    song_id TEXT NOT NULL,
    title TEXT NOT NULL,
    custom_settings TEXT
)
''')
conn.commit()
# -----------

# Création d'utilisateurs avec leurs playlists
users_data = [
    {
        "phone": "+33123456789",
        "playlist": [
            {"song_id": "dQw4w9WgXcQ", "title": "Never Gonna Give You Up", "settings": {"key": "+2", "rap": False}},
            {"song_id": "9bZkp7q19f0", "title": "Gangnam Style", "settings": {"key": "0", "rap": True}}
        ]
    },
    {
        "phone": "+33987654321",
        "playlist": [
            {"song_id": "kJQP7kiw5Fk", "title": "Despacito", "settings": {"key": "-1", "rap": False}}
        ]
    }
]

# Insertion des données
for user in users_data:
    for song in user["playlist"]:
        cursor.execute('''
            INSERT INTO playlists (phone, song_id, title, custom_settings)
            VALUES (?, ?, ?, ?)
        ''', (
            user["phone"],
            song["song_id"],
            song["title"],
            json.dumps(song["settings"])  # Convertit le dict en JSON
        ))

conn.commit()
conn.close()
print("Base de données remplie avec succès!")