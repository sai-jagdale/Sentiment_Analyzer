from flask import Flask, render_template, request
import joblib
import re

# === Initialize Flask App ===
app = Flask(__name__)

# === Load Pre-trained Artifacts ===
model = joblib.load("model/sentiment_model.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")
label_encoder = joblib.load("model/label_encoder.pkl")


# === Text Preprocessing Function ===
def clean_text(text):
    """
    Cleans the input text by:
    - Converting to lowercase
    - Removing URLs, special characters, and extra whitespace
    """
    text = text.lower()
    text = re.sub(r"http\S+", "", text)  # Remove URLs
    text = re.sub(r"[^a-zA-Z\s]", "", text)  # Remove special characters and digits
    text = re.sub(r"\s+", " ", text).strip()  # Remove extra whitespace
    return text


# === Home Route ===
@app.route("/", methods=["GET", "POST"])
def index():
    # Default values
    sentiment = None
    score = None
    explanation = None
    error_message = None

    # Handle POST request
    if request.method == "POST":
        user_input = request.form.get("user_input", "").strip()

        # === Input Validation ===
        if not user_input:
            error_message = "⚠️ Please enter some text."
        elif len(user_input) > 500:
            error_message = "⚠️ Input too long. Please limit to 500 characters."
        else:
            try:
                # === Preprocess and Vectorize Text ===
                cleaned_text = clean_text(user_input)
                vectorized = vectorizer.transform([cleaned_text])

                # Check if vector is empty (no known words)
                if vectorized.nnz == 0:
                    error_message = (
                        "⚠️ Not enough recognizable words to classify sentiment."
                    )
                else:
                    # === Predict Sentiment ===
                    prediction = model.predict(vectorized)[0]
                    sentiment = label_encoder.inverse_transform([prediction])[0]
                    score = round(model.predict_proba(vectorized).max(), 2)

                    # === Sentiment Explanation ===
                    explanation_map = {
                        "positive": "The text expresses a positive sentiment, indicating a favorable or optimistic tone.",
                        "negative": "The text expresses a negative sentiment, indicating criticism, dissatisfaction, or concern.",
                        "neutral": "The text appears neutral without strong emotion or bias.",
                    }
                    explanation = explanation_map.get(
                        sentiment.lower(),
                        "The text was classified, but no explanation is available.",
                    )

                    # Capitalize first letter
                    sentiment = sentiment.capitalize()

            except Exception as e:
                error_message = f"⚠️ An error occurred: {str(e)}"

    # === Render Frontend ===
    return render_template(
        "index.html",
        sentiment=sentiment,
        score=score,
        explanation=explanation,
        error=error_message,
    )


# === Run Flask App ===
if __name__ == "__main__":
    app.run(debug=True)
