let recognition;
let transcription = '';
let sentimentModel;

async function loadSentimentModel() {
    sentimentModel = await sentiment.load();
}

function startRecording() {
    transcription = '';
    recognition = new webkitSpeechRecognition();
    recognition.continuous = true;
    recognition.interimResults = true;

    recognition.onresult = function(event) {
        const result = event.results[event.results.length - 1];
        transcription += result[0].transcript;
        document.getElementById('transcription').innerText = transcription;
    };

    recognition.onend = function() {
        analyzeSentiment();
    };

    recognition.start();
}

function stopRecording() {
    recognition.stop();
}

async function analyzeSentiment() {
    if (sentimentModel) {
        const result = await sentimentModel.predict(transcription);
        const sentimentLabel = result[0].label;
        const sentimentScore = result[0].confidence;

        document.getElementById('sentiment').innerText = `Sentiment: ${sentimentLabel} (${sentimentScore.toFixed(2)})`;
    } else {
        console.error('Sentiment model not loaded.');
    }
}

document.addEventListener('DOMContentLoaded', () => {
    loadSentimentModel();
});
