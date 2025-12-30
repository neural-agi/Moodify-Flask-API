# Moodify – Sentiment-Based Mood Prediction API

Moodify is a lightweight **Flask-based REST API** that predicts the **emotional mood** of a given text input using a **pre-trained NLP sentiment analysis model**.  
It demonstrates how to expose a machine learning model as an API for real-time inference.

---

## 🚀 Features

- REST API built with Flask
- Uses a pre-trained Transformer model for sentiment analysis
- Predicts mood from raw text input
- Returns structured JSON responses
- Simple, clean, and deployment-ready project structure

---

## 🧠 How It Works

1. The API receives text input via an HTTP POST request.
2. A pre-trained sentiment analysis model processes the text.
3. The predicted sentiment is mapped to a mood label.
4. The API returns the mood and confidence score as JSON.

---

## 🛠️ Tech Stack

- **Python 3.10**
- **Flask**
- **Hugging Face Transformers**
- **PyTorch (CPU)**

---

## 📦 Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/neural-agi/moodify-flask-api.git
cd moodify-flask-api
```
### 2. Create and activate a virtual environment
```bash
python -m venv venv
venv\Scripts\activate
```
### 3. Install dependencies
```bash
3. Install dependencies
```
### 4. ▶️ Running the API
```bash
python app.py
```
### The Server will start at 
```cpp
http://127.0.0.1:5000/
```
### 🔗 API Endpoints
### Health Check
### GET /
### Response
```json
{
  "message": "Moodify API is running 🚀"
}
```
### Predict Mood
### POST /predict
### Request Body:
```json
{
  "text": "I finally built my first ML API"
}
```
### Response:
```json
{
  "text": "I finally built my first ML API",
  "predicted_mood": "Happy",
  "confidence": 0.98
}
```
---
## 🎯 Use Cases

1. Sentiment analysis demonstrations
2. NLP inference services
3. Backend + ML integration practice
4. Machine Learning internship portfolio project

---

## 🔮 Future Improvements

1. Batch text prediction support
2. Additional mood categories
3. Confidence-based neutral classification
4. Public API deployment (Render / Railway / AWS)
5. Logging and monitoring

---

## 👤 Author

Paranjay Das
BTech CSE (AI/ML)
Aspiring Machine Learning Engineer
