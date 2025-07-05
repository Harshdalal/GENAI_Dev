# train_model.py
from sklearn.datasets import load_wine
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
import joblib
import os

# Load dataset
wine = load_wine()
X, y = wine.data, wine.target

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train SVM model
svm_model = SVC(probability=True)
svm_model.fit(X_train, y_train)

# Save model
os.makedirs("model", exist_ok=True)
joblib.dump(svm_model, "model/wine_svm_model.pkl")

print("✅ SVM model trained and saved at model/wine_svm_model.pkl")
