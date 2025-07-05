# predict_mlflow.py
import mlflow.sklearn
import numpy as np

# Replace this with the actual run ID from train_mlflow.py
RUN_ID = "76729c89cbc142d7bbd85eb3d297744a"

# Load model from MLflow run
logged_model_uri = f"runs:/{RUN_ID}/model"
model = mlflow.sklearn.load_model(logged_model_uri)

# Sample input (Iris-setosa like)
sample_input = np.array([[5.1, 3.5, 1.4, 0.2]])
prediction = model.predict(sample_input)

print("🔮 Predicted class:", prediction[0])
