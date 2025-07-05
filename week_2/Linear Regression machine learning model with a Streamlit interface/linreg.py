import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Sample dataset
data = {
    'Area (sqft)': [1000, 1500, 2000, 2500, 3000],
    'Price (in Lakhs)': [50, 75, 100, 125, 150]
}
df = pd.DataFrame(data)

# Train model
X = df[['Area (sqft)']]
y = df['Price (in Lakhs)']
model = LinearRegression()
model.fit(X, y)

# Streamlit UI
st.set_page_config(page_title="Linear Regression App", page_icon="📈")
st.title("📈 House Price Predictor")
st.write("Enter area to predict house price using Linear Regression.")

# User input
area_input = st.number_input("Enter Area (in sqft):", min_value=100, max_value=5000, step=100)
if area_input:
    prediction = model.predict([[area_input]])
    st.success(f"Predicted Price: ₹ {prediction[0]:.2f} Lakhs")

# Plotting
st.subheader("Regression Fit")
x_vals = np.array(X).reshape(-1)
y_vals = model.predict(X)

plt.figure(figsize=(8, 4))
plt.scatter(X, y, color='blue', label='Data Points')
plt.plot(X, y_vals, color='red', label='Regression Line')
plt.xlabel("Area (sqft)")
plt.ylabel("Price (in Lakhs)")
plt.title("Linear Regression")
plt.legend()
st.pyplot(plt)
