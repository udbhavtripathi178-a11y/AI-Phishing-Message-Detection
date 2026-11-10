# 🛡️ AI Phishing Message Detection

An AI-powered machine learning application that classifies text messages into three categories: **Ham, Spam, and Smishing**.

## 📌 Project Overview

Phishing and fraudulent messages are a growing cybersecurity threat. This project uses Natural Language Processing (NLP) and Machine Learning to identify potentially harmful messages and help users recognise suspicious communication.

## ✨ Features

- Text message classification into Ham, Spam, and Smishing
- Text preprocessing and TF-IDF feature extraction
- Machine Learning using Multinomial Naive Bayes and Logistic Regression
- Model evaluation and comparison
- Interactive Streamlit web interface
- Recent prediction history

## 🧰 Technologies Used

- Python
- Pandas and NumPy
- NLTK
- Scikit-learn
- Matplotlib
- Joblib
- Streamlit

## 🤖 Machine Learning Models

Two models were trained and evaluated:

| Model | Accuracy |
|---|---:|
| Multinomial Naive Bayes | 94.54% |
| Logistic Regression | 96.81% |

Logistic Regression was selected as the preferred model for V1.0 based on the evaluation results.

*Note: These results are from the project's current train/test split and do not guarantee performance on unseen real-world messages.*

## 📂 Project Structure

```text
SIC_Phishing_detection/
├── app/
├── data/
├── models/
├── notebooks/
├── src/
├── tests/
├── .gitignore
├── requirements.txt
└── README.md
```

## ⚙️ Installation and Setup

1. Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

2. Move into the project directory:

```bash
cd SIC_Phishing_detection
```

3. Create and activate a virtual environment:

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

4. Install dependencies:

```bash
pip install -r requirements.txt
```

## ▶️ Run the Application

```bash
python -m streamlit run app/app.py
```

Open the local URL displayed in your terminal.

## ⚠️ Disclaimer

This application is an educational machine learning prototype. Predictions may be incorrect. Do not rely on it as the sole method of identifying phishing or fraudulent messages. Never share passwords, OTPs, or sensitive information based only on its prediction.

## 🚀 Future Improvements

- Support for Hindi and Hinglish messages
- URL and link analysis
- Improved dataset quality and class balance
- Explainable predictions and risk scoring
- Mobile application integration

## 👨‍💻 Project Status

**Version:** 1.0  
**Status:** Initial prototype completed

Developed as part of the Samsung Innovation Campus AI learning journey.