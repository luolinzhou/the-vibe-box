import sqlite3

# Créer la base de données
conn = sqlite3.connect('karaoke.db')
cursor = conn.cursor()

# Table pour les playlists
cursor.execute('''
CREATE TABLE IF NOT EXISTS playlists (
    id INTEGER PRIMARY KEY,
    phone TEXT NOT NULL,
    song_id TEXT NOT NULL,
    title TEXT NOT NULL,
    custom_settings TEXT  # Stockera du JSON
)
''')
conn.commit()