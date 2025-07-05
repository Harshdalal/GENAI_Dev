import mlflow
import mlflow.keras
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.datasets import mnist
from sklearn.metrics import accuracy_score
import numpy as np

# Load and preprocess data
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train[..., np.newaxis]/255.0, x_test[..., np.newaxis]/255.0

# Build CNN model
model = models.Sequential([
    layers.Conv2D(32, 3, activation='relu', input_shape=(28, 28, 1)),
    layers.MaxPooling2D(),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# MLflow autologging
mlflow.keras.autolog()

with mlflow.start_run() as run:
    model.fit(x_train, y_train, epochs=2, validation_split=0.1)
    val_preds = np.argmax(model.predict(x_test), axis=1)
    acc = accuracy_score(y_test, val_preds)
    print("✅ Accuracy:", acc)
    print("📁 Run ID:", run.info.run_id)
