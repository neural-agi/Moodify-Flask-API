from flask import Flask, request, jsonify
from transformers import pipeline

print("Starting Moodify app...")

app = Flask(__name__)

print("Loading sentiment model (first run may take time)...")
classifier = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)
print("Model loaded successfully.")

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Moodify API is running 🚀"})

@app.route("/predict", methods=["POST"])
def predict_mood():
    data = request.get_json()

    if not data or "text" not in data:
        return jsonify({"error": "No text provided"}), 400

    text = data["text"]
    result = classifier(text)[0]

    label = result["label"]
    score = result["score"]

    mood = "Happy" if label == "POSITIVE" else "Sad"

    return jsonify({
        "text": text,
        "predicted_mood": mood,
        "confidence": round(score, 3)
    })

if __name__ == "__main__":
    print("Starting Flask server...")
    app.run(debug=True, use_reloader=False)
