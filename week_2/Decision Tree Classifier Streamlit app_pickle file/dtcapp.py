# app.py

import streamlit as st
import pickle
import numpy as np
from sklearn.datasets import load_iris

# Load model from pickle
with open("decision_tree_model.pkl", "rb") as f:
    model = pickle.load(f)

# Load Iris feature names
iris = load_iris()
feature_names = iris.feature_names
target_names = iris.target_names

# Streamlit UI
st.set_page_config(page_title="Decision Tree Classifier", page_icon="🌸")
st.title("🌸 Iris Species Predictor")
st.write("This app predicts the species of Iris flowers using a Decision Tree model.")

# Input sliders for features
sepal_length = st.slider("Sepal Length (cm)", 4.0, 8.0, 5.1)
sepal_width = st.slider("Sepal Width (cm)", 2.0, 4.5, 3.5)
petal_length = st.slider("Petal Length (cm)", 1.0, 7.0, 1.4)
petal_width = st.slider("Petal Width (cm)", 0.1, 2.5, 0.2)

# Prepare input
features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])

# Predict
prediction = model.predict(features)[0]
predicted_species = target_names[prediction]

# Display result
st.success(f"🌼 Predicted Species: **{predicted_species.capitalize()}**")
