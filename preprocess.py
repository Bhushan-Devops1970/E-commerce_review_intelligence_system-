import re                           # Import regular expressions (for cleaning text)
import nltk                         # Import nltk stopwords (common words like "the", "is")
from nltk.corpus import stopwords

nltk.download('stopwords')

# Store stopwords in a set for fast lookup (it help to featch it fast)
stop_words = set(stopwords.words('english'))

# Function to clean text
def preprocess(text):
    text = text.lower()                                     # Convert text to lowercase
    text = re.sub(r'[^a-zA-Z]', ' ', text)                  # Remove numbers and special characters
    words = text.split()                                    # Split sentence into words
    words = [w for w in words if w not in stop_words]       # Remove common useless words (stopwords)
    return " ".join(words)                                  # Join words back into sentence