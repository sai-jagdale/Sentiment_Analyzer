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

##🛠️ Technologies Used
Python – Programming language used for backend and model training
Flask – Lightweight web framework for building the application interface
NLTK – Natural Language Toolkit for text preprocessing and cleaning
Scikit-learn – For building and training the sentiment classification model
Pandas – Handling and processing dataset (CSV files)
Joblib – Saving and loading trained ML models and vectorizers
Tailwind CSS – For modern, responsive frontend styling (via CDN)
HTML5 – Markup language for frontend UI
Jupyter Notebook – For training and experimenting with the model

## 🚀 How to Run the Project
# 1. Clone the repository
```bash
git clone https://github.com/your-username/sentiment-analyzer.git
cd sentiment-analyzer
```
# 2. Install dependencies
```bash
pip install -r requirements.txt
```
# 3. (Optional) Train the model if not already done
```bash
# Open Jupyter Notebook and run all cells to train the model
jupyter notebook model/train_model.ipynb
```
# 4. Start the Flask app
```bash
python app.py
```
> ✅ Go to your browser and open: http://127.0.0.1:5000/

## 📦 Dependencies
Flask
scikit-learn
pandas
joblib
nltk
notebook

## 📚 Dataset Used
Twitter sentiment dataset (twitter_training.csv and twitter_validation.csv) - From Kaggle
