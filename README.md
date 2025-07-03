# 🧠 Sentiment Analyzer Web App

A simple NLP project that uses a trained machine learning model to predict the **sentiment** of user input text (positive, negative, neutral) using **Flask** and **Tailwind CSS**.

## 💡 Features

- Takes user input in a web form
- Predicts sentiment using a trained ML model
- Shows emoji-based feedback and explanation
- Clean Tailwind CSS interface
- Works with browser favicon using emoji 🧠

## 📦 Project Structure
Sentiment_Analyzer/
│
├── data/
│ ├── twitter_training.csv
│ └── twitter_validation.csv
│
├── model/
│ ├── label_encoder.pkl
│ ├── sentiment_model.pkl
│ ├── vectorizer.pkl
│ └── train_model.ipynb
│
├── templates/
│ └── index.html # Frontend UI
│
├── Screenshots/
│ ├── Preview1.png
│ ├── Preview2.png
│ ├── Preview3.png
│ └── Preview4.png
│
├── app.py # Flask backend
├── requirements.txt
└── README.md

## 🧠 Model Info
The model was trained on a Twitter sentiment dataset using TF-IDF vectorization + Logistic Regression classifier.
