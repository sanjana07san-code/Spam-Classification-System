import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
import joblib
import os

# ==========================
# 1. Load Dataset
# ==========================
data = pd.read_csv("dataset/spam.csv", encoding="latin-1")

# Keep only required columns
data = data[['v1', 'v2']]

# Rename columns
data.columns = ['label', 'message']

# Convert labels into numbers
data['label'] = data['label'].map({'ham': 0, 'spam': 1})

# ==========================
# 2. Features and Labels
# ==========================
X = data['message']
y = data['label']

# ==========================
# 3. Convert Text to Numbers
# ==========================
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(X)

# ==========================
# 4. Split Dataset
# ==========================
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# ==========================
# 5. Train Model
# ==========================
model = MultinomialNB()
model.fit(X_train, y_train)

# ==========================
# 6. Prediction
# ==========================
prediction = model.predict(X_test)

# ==========================
# 7. Evaluation
# ==========================
accuracy = accuracy_score(y_test, prediction)

print("=" * 40)
print("Spam Classification Model")
print("=" * 40)
print(f"Accuracy : {accuracy:.2%}")
print("\nClassification Report\n")
print(classification_report(y_test, prediction))

# ==========================
# 8. Save Model
# ==========================
os.makedirs("model", exist_ok=True)

joblib.dump(model, "model/spam_model.pkl")
joblib.dump(vectorizer, "model/vectorizer.pkl")

print("\nModel Saved Successfully!")