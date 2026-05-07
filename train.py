# Import libraries
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

from utils import load_data
from preprocess import preprocess

# Load dataset
texts, labels = load_data("data/train.ft.txt")

# Clean text
texts = [preprocess(t) for t in texts]

# Convert text into numbers using TF-IDF it gives score to word like imp work much score
vectorizer = TfidfVectorizer(max_features=5000)
X = vectorizer.fit_transform(texts)

# Split data into training & testing
X_train, X_test, y_train, y_test = train_test_split(
    X, labels, test_size=0.2, random_state=42
)

# Create model
model = LogisticRegression(max_iter=200)

# Train model
model.fit(X_train, y_train)

# Test model
y_pred = model.predict(X_test)

# Print performance
print(classification_report(y_test, y_pred))

# Save trained model
with open("model/model.pkl", "wb") as f:
    pickle.dump(model, f)

# Save vectorizer
with open("model/vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

print("✅ Model trained and saved!")