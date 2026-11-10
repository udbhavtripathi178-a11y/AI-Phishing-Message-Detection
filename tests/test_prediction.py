from src.prediction.predict import model, tfidf, clean_text

messages = [
    "Congratulations! You won a free prize.",
    "You have won a lottery. Click here to claim your prize.",
    "Your bank account is blocked. Verify your KYC immediately."
]

for message in messages:
    cleaned = clean_text(message)
    vector = tfidf.transform([cleaned])

    probabilities = model.predict_proba(vector)[0]
    prediction = model.predict(vector)[0]

    print("\nMessage:", message)
    print("Prediction:", prediction)

    for label, probability in zip(model.classes_, probabilities):
        print(f"{label}: {probability:.2%}")