from flask import Flask, render_template, request
import joblib
from database import create_database, save_prediction, get_history

# ======================================================
# Initialize Flask Application
# ======================================================
app = Flask(__name__)

# ======================================================
# Create SQLite Database
# ======================================================
create_database()

# ======================================================
# Load Trained Machine Learning Model
# ======================================================
model = joblib.load("model/spam_model.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")


# ======================================================
# Home Page
# ======================================================
@app.route("/")
def home():
    return render_template("index.html")


# ======================================================
# Prediction Route
# ======================================================
@app.route("/predict", methods=["POST"])
def predict():

    # Get user message
    message = request.form.get("message")

    # Check empty message
    if message.strip() == "":

        return render_template(
            "index.html",
            prediction="Please enter a message.",
            confidence=0,
            color="warning",
            emoji="⚠️",
            user_message=""
        )

    # Convert into TF-IDF
    message_vector = vectorizer.transform([message])

    # Prediction
    prediction = model.predict(message_vector)[0]

    # Probability
    probability = model.predict_proba(message_vector)[0]

    confidence = round(max(probability) * 100, 2)

    # Spam
    if prediction == 1:

        result = "Spam Message"

        color = "danger"

        emoji = "🚨"

    # Ham
    else:

        result = "Not Spam (Ham)"

        color = "success"

        emoji = "✅"

    # Save Prediction
    save_prediction(

        message,

        result,

        confidence

    )

    return render_template(

        "index.html",

        prediction=result,

        confidence=confidence,

        color=color,

        emoji=emoji,

        user_message=message

    )


# ======================================================
# History Page
# ======================================================
@app.route("/history")
def history():

    rows = get_history()

    return render_template(

        "history.html",

        history=rows

    )


# ======================================================
# About Page
# ======================================================
@app.route("/about")
def about():

    return render_template(

        "about.html"

    )


# ======================================================
# Run Application
# ======================================================
if __name__ == "__main__":

    app.run(

        debug=True

    )