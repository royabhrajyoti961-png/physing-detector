import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from utils import clean_text

# Load dataset
data = pd.read_csv("dataset.csv")

# Clean text
data["text"] = data["text"].apply(clean_text)

# Features & labels
X = data["text"]
y = data["label"]

# Convert text → vectors
vectorizer = TfidfVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# Train model
model = MultinomialNB()
model.fit(X_vectorized, y)

def predict_email(email):
    email = clean_text(email)
    email_vec = vectorizer.transform([email])
    
    prediction = model.predict(email_vec)[0]
    probability = model.predict_proba(email_vec)[0]
    
    confidence = max(probability)
    
    return prediction, confidence
