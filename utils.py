def load_data(file_path):

    texts, labels = [], []
    # texts = reviews, labels = numbers (1 = negative, 2 = positive)

    # Open dataset file in read mode 
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            parts = line.split(' ', 1)          # Split label and review text
            label = int(parts[0].replace('__label__', ''))  # Extract label (remove "__label__")
            text = parts[1]     # Extract review text

            texts.append(text)
            labels.append(label)

    return texts, labels

# Convert prediction in sentiment (3-class)
def get_sentiment(prediction, confidence):
    if confidence < 0.60:
        return "Neutral"
    return "Positive" if prediction == 2 else "Negative"

# Convert prediction into rating (1–5 stars)
def predict_rating(prediction, confidence):
    if confidence < 0.60:
        return 3

    if prediction == 2:
        return 5 if confidence > 0.85 else 4
    else:
        return 1 if confidence > 0.85 else 2

# Detect fake reviews using simple rules
def detect_fake_review(text):
    words = text.lower().split()
    # if it is too short
    if len(words) < 4:
        return "Fake (Too Short)"
    # same words again & again
    if len(set(words)) < len(words) / 2:
        return "Fake (Repetitive)"

    return "Likely Genuine"
    
# Detect category using keywords
def detect_category(text):
    text = text.lower()

    categories = {
        "Delivery": ["delivery", "late", "shipping", "arrived"],
        "Quality": ["quality", "broken", "damage", "defect"],
        "Pricing": ["price", "cost", "expensive", "cheap"],
        "Customer Service": ["service", "support", "help"],
        "Packaging": ["package", "packaging", "box"]
    }

    scores = {}
    # Count how many keywords match
    for cat, keywords in categories.items():
        scores[cat] = sum(word in text for word in keywords)

    # Get best category
    best_category = max(scores, key=scores.get)

    # If no match it will say General
    if scores[best_category] == 0:
        return "General"

    return best_category