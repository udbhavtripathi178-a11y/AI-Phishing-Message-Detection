
import joblib
import re
from pathlib import Path

# Find the main project directory
BASE_DIR = Path(__file__).resolve().parents[2]

# Load saved model and TF-IDF vectorizer
model = joblib.load(BASE_DIR / "models" / "logistic_regression_model.pkl")
tfidf = joblib.load(BASE_DIR / "models" / "tfidf_vectorizer.pkl")


# Clean input message
def clean_text(text):
    text = text.lower()
    text = re.sub(r"\s+", " ", text).strip()
    return text


# Predict message category
def predict_message(message):
    cleaned_message = clean_text(message)

    message_vector = tfidf.transform([cleaned_message])

    prediction = model.predict(message_vector)

    return prediction[0]
