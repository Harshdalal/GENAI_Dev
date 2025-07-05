import mlflow.keras
import numpy as np
from tensorflow.keras.datasets import mnist

RUN_ID = "1e56a9f4d9c446ed9d39d2e75b91979f"

# Load model
model_uri = f"runs:/{RUN_ID}/model"
model = mlflow.keras.load_model(model_uri)

# Sample input
(_, _), (x_test, y_test) = mnist.load_data()
x_sample = x_test[0][np.newaxis, ..., np.newaxis] / 255.0
pred = model.predict(x_sample)
print("🔮 Predicted class:", np.argmax(pred))
