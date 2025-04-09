from flask import Flask, jsonify, render_template
import json

app = Flask(__name__)

# Lecture des fichiers JSON
def load_json(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return json.load(file)

# Routes API REST
@app.route('/api/events', methods=['GET'])
def get_events():
    events = load_json('data/events.json')
    return jsonify(events)

@app.route('/api/news', methods=['GET'])
def get_news():
    news = load_json('data/news.json')
    return jsonify(news)

# Interface simple pour afficher les données
@app.route('/')
def index():
    events = load_json('data/events.json')
    news = load_json('data/news.json')
    return render_template('index.html', events=events, news=news)

if __name__ == '__main__':
    app.run(debug=True)
