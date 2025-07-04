# train_model.py

import pandas as pd
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
import pickle

# Load dataset
iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = iris.target

# Train model
model = DecisionTreeClassifier()
model.fit(X, y)

# Save model to file using pickle
with open("decision_tree_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model saved as decision_tree_model.pkl")
