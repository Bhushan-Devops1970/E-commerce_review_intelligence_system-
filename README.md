# 🛒 E-commerce Review Intelligence System

An AI-powered NLP application that analyzes customer reviews and provides:

- ✅ Sentiment Analysis (Positive / Negative / Neutral)
- ⭐ Rating Prediction (1–5 stars)
- 📦 Category Detection
- 🚨 Fake Review Detection
- 📊 Analytics Dashboard
- 🗄️ Database Storage using SQLite

---

# 🚀 Features

## 🔹 Sentiment Analysis
Predicts whether a review is:
- Positive
- Negative
- Neutral

---

## 🔹 Rating Prediction
Automatically predicts:
- ⭐ 1–5 Star Rating

---

## 🔹 Category Detection
Detects categories such as:
- Delivery
- Quality
- Pricing
- Customer Service
- Packaging

---

## 🔹 Fake Review Detection
Detects suspicious reviews using:
- Repetitive words
- Very short reviews

---

## 🔹 Database Storage
All analyzed reviews are stored permanently using SQLite database.

The database:
- Creates automatically
- Does NOT duplicate
- Stores previous reviews permanently

---

## 🔹 Analytics Dashboard
Provides:
- Sentiment distribution
- Rating distribution
- Category filtering
- Sentiment filtering

---

# 🧠 Project Workflow

```text
User Input
    ↓
Preprocessing
    ↓
TF-IDF Vectorization
    ↓
Machine Learning Model
    ↓
Predictions
    ↓
Store in Database
    ↓
Analytics Dashboard
```

---

# 📁 Project Structure

```text
project/
│── data/
│   ├── train.ft.txt
│   ├── test.ft.txt
│
│── model/
│   ├── model.pkl
│   ├── vectorizer.pkl
│
│── assets/
│   ├── bg.jpg
│
│── database.py
│── app.py
│── preprocess.py
│── train.py
│── utils.py
│── requirements.txt
│── README.md
```

---

# ⚙️ Installation Guide

## Step 1: Clone or Download Project

```bash
git clone <your-repository-link>
cd project
```

OR simply download ZIP and extract.

---

## Step 2: Install Required Libraries

Run:

```bash
pip install -r requirements.txt
```

---

# 🧠 Train the Model

IMPORTANT:
You must train the model before running the application.

Run:

```bash
python train.py
```

This will:
- Load dataset
- Clean text
- Train ML model
- Save:
  - model/model.pkl
  - model/vectorizer.pkl

---

# ▶️ Run the Application

After training is completed:

```bash
streamlit run app.py
```

---

# 🌐 Open in Browser

Streamlit will automatically open:

```text
http://localhost:8501
```

---

# 📊 Example Inputs

## Example 1
```text
Amazing quality and fast delivery
```

Output:
- Positive
- ⭐⭐⭐⭐⭐
- Delivery / Quality

---

## Example 2
```text
Worst product ever waste of money
```

Output:
- Negative
- ⭐
- Pricing

---

## Example 3
```text
bad bad bad bad
```

Output:
- Fake Review Detected

---

# 🧠 Technologies Used

- Python
- Streamlit
- Scikit-learn
- TF-IDF
- Logistic Regression
- SQLite
- Pandas
- NLTK

---

# 📈 Model Performance

Approximate Results:
- Accuracy: ~89%
- Precision: ~89%
- Recall: ~89%
- F1-score: ~89%

---

# 🗄️ Database

Database file:
```text
reviews.db
```

The database stores:
- Review text
- Sentiment
- Category
- Rating
- Confidence
- Fake detection result

---

# 🔥 Future Improvements

Possible future upgrades:
- BERT Model
- Real-time charts
- Cloud deployment
- Emotion detection
- Search functionality

---

# 👨‍💻 Author

Your Name

---

# 📌 Dataset Format

Dataset uses FastText format:

```text
__label__1 → Negative
__label__2 → Positive
```

Example:

```text
__label__2 Amazing product quality
__label__1 Worst product ever
```

---

# 🏆 Conclusion

This project demonstrates how Natural Language Processing (NLP), Machine Learning, Database Systems, and Web Applications can be combined to build an intelligent E-commerce Review Analysis System.


