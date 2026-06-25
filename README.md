# 📧 Spam Classification System

A Machine Learning and Flask-based web application that detects whether an SMS or Email message is **Spam** or **Ham (Not Spam)** using Natural Language Processing (NLP).

---

## 🚀 Features

* Spam/Ham message prediction
* TF-IDF Vectorization
* Multinomial Naive Bayes Algorithm
* Confidence Score
* SQLite Prediction History
* Responsive Bootstrap UI
* Flask Web Application
* Professional Project Structure

---

## 🛠️ Technologies Used

* Python
* Flask
* Pandas
* NumPy
* Scikit-learn
* TF-IDF Vectorizer
* Multinomial Naive Bayes
* SQLite
* HTML5
* CSS3
* Bootstrap 5
* JavaScript

---

## 📂 Project Structure

```text
Spam_Classification/
│
├── app.py
├── train_model.py
├── database.py
├── history.db
├── requirements.txt
├── README.md
│
├── dataset/
│   └── spam.csv
│
├── model/
│   ├── spam_model.pkl
│   └── vectorizer.pkl
│
├── templates/
│   ├── index.html
│   ├── history.html
│   └── about.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js
│
└── screenshots/
```

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/Spam_Classification.git
```

### Open the Project

```bash
cd Spam_Classification
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Train the Model

```bash
python train_model.py
```

### Run the Application

```bash
python app.py
```

---

## 🌐 Open in Browser

```
http://127.0.0.1:5000
```

---

## 🧠 Machine Learning Workflow

1. Load Dataset
2. Data Preprocessing
3. Convert Labels (Ham = 0, Spam = 1)
4. TF-IDF Feature Extraction
5. Train-Test Split
6. Train Multinomial Naive Bayes Model
7. Evaluate Model
8. Save Model
9. Predict User Input
10. Store Prediction History

---

## 📊 Model Information

* Algorithm: Multinomial Naive Bayes
* Feature Extraction: TF-IDF Vectorizer
* Dataset: SMS Spam Collection
* Accuracy: Approximately 96%

---

## 📸 Screenshots
.
* Home Page
* Prediction Result
* History Page
* About Page

---

## 🔮 Future Enhancements

* User Authentication
* Email Spam Detection
* Model Comparison
* Charts and Analytics
* Export History to CSV
* Dark Mode
* Cloud Deployment

---

## 👨‍💻 Author

**sanjana.M**

BCA Student

Machine Learning & Python Developer

---

## 📜 License

This project is developed for educational and portfolio purposes.
