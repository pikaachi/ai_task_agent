import spacy
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

# Load spaCy NLP model
nlp = spacy.load("en_core_web_sm")

# Training data: (Text, Category, Priority)
training_data = [
    ("Finish the financial report", "Work", "High"),
    ("Schedule a meeting with the team", "Work", "Medium"),
    ("Buy groceries for the week", "Personal", "Low"),
    ("Call mom and check in", "Personal", "Medium"),
    ("Pick up dry cleaning", "Errands", "Low"),
    ("Submit the project proposal", "Work", "High"),
    ("Go to the gym", "Personal", "Medium"),
]

# Extract text and labels
texts, categories, priorities = zip(*training_data)

# Convert text to numerical format
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

# Train category classification model
category_model = MultinomialNB()
category_model.fit(X, categories)

# Train priority classification model
priority_model = MultinomialNB()
priority_model.fit(X, priorities)

# Save models for later use
with open("app/category_model.pkl", "wb") as f:
    pickle.dump(category_model, f)

with open("app/priority_model.pkl", "wb") as f:
    pickle.dump(priority_model, f)

with open("app/vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

def classify_task(task_text):
    """Predicts category and priority for a given task text"""
    with open("app/category_model.pkl", "rb") as f:
        category_model = pickle.load(f)

    with open("app/priority_model.pkl", "rb") as f:
        priority_model = pickle.load(f)

    with open("app/vectorizer.pkl", "rb") as f:
        vectorizer = pickle.load(f)

    X_input = vectorizer.transform([task_text])

    predicted_category = category_model.predict(X_input)[0]
    predicted_priority = priority_model.predict(X_input)[0]

    return predicted_category, predicted_priority
