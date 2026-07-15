import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import joblib
import os

print("=== Student Feedback Model Training ===")

df = pd.read_csv("sentiment_results.csv")

df = df.dropna(subset=["cleaned_teaching", "sentiment"])

X = df["cleaned_teaching"]
y = df["sentiment"]

print(f"Dataset loaded: {len(df)} rows")

print("\nSentiment Distribution:")
print(y.value_counts())

print("\nApplying TF-IDF...")
vectorizer = TfidfVectorizer(max_features=5000)

X_vectorized = vectorizer.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
X_vectorized,
y,
test_size=0.2,
random_state=42
)

print(f"\nTraining samples: {X_train.shape[0]}")
print(f"Testing samples: {X_test.shape[0]}")

print("\nTraining Model...")
model = LogisticRegression(max_iter=500)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print(f"\nAccuracy: {accuracy*100:.2f}%")

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

os.makedirs("model", exist_ok=True)

joblib.dump(model, "model/student_feedback_model.pkl")
joblib.dump(vectorizer, "model/tfidf_vectorizer.pkl")

print("\nModel Saved Successfully!")