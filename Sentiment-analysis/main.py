# Importation des modules nécessaires
from flask import Flask, render_template, request, jsonify
from transformers import pipeline

# Initialisation de l'application Flask
app = Flask(__name__)

# Initialisation du pipeline pour l'analyse de sentiments
sentiment_analysis = pipeline("sentiment-analysis")

# Route pour la page test
@app.route('/')
def test():
    return render_template('test.html')

# Route pour la page accueil (anciennement /)
@app.route('/accueil')
def accueil():
    return render_template('Accueil.html')

# Route pour la prédiction depuis le formulaire texte
@app.route('/accueil', methods=['POST'])
def predict_text():
    # Récupération du texte depuis le formulaire
    text = request.form['text']

    # Analyse de sentiments avec le modèle pré-entraîné
    result = sentiment_analysis(text)
    sentiment = result[0]['label']
    
    # Renvoie du résultat à la page Accueil
    return render_template('Accueil.html', sentiment=sentiment)

# Route pour la page audio
@app.route('/audio')
def audio():
    return render_template('audio.html')

# Route pour la prédiction depuis l'audio (cette route est appelée via JavaScript)
@app.route('/predict_audio', methods=['POST'])
def predict_audio():
    # Récupération de la transcription audio depuis la requête JSON
    audio_transcription = request.json['audio_transcription']

    # Analyse de sentiments avec le modèle pré-entraîné
    result = sentiment_analysis(audio_transcription)
    sentiment = result[0]['label']

    # Renvoie du résultat sous forme de réponse JSON
    return jsonify({'sentiment': sentiment  })

# Point d'entrée principal
if __name__ == '__main__':
    # Lancement de l'application Flask en mode débogage
    app.run(debug=True)
