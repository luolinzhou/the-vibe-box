from flask import Flask, jsonify, request, render_template
import sqlite3
import json

app = Flask(__name__)

@app.route('/playlists', methods=['GET'])
def get_playlists():
    phone = request.args.get('phone')
    conn = sqlite3.connect('karaoke.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM playlists WHERE phone=?", (phone,))
    playlists = cursor.fetchall()
    return jsonify(playlists)

@app.route('/add_song', methods=['POST'])
def add_song():
    data = request.json
    conn = sqlite3.connect('karaoke.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO playlists (phone, song_id, title, custom_settings)
        VALUES (?, ?, ?, ?)
    ''', (data['phone'], data['song_id'], data['title'], json.dumps(data['settings'])))
    conn.commit()
    return jsonify({"status": "success"})

# Nouvelle route pour l'interface admin
@app.route('/admin')
def admin():
    conn = sqlite3.connect('karaoke.db')
    cursor = conn.cursor()
    
    # Récupérer les playlists
    cursor.execute("SELECT * FROM playlists")
    playlists = cursor.fetchall()
    
    # Récupérer les utilisateurs uniques
    cursor.execute("SELECT DISTINCT phone FROM playlists")
    users = [row[0] for row in cursor.fetchall()]
    
    conn.close()
    
    return render_template('admin.html', users=users, playlists=playlists)

if __name__ == '__main__':
    app.run(debug=True)