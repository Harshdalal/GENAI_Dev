import mlflow
import mlflow.keras
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load dataset
max_features = 10000
(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=max_features)

x_train = pad_sequences(x_train, maxlen=200)
x_test = pad_sequences(x_test, maxlen=200)

# Build RNN model
model = models.Sequential([
    layers.Embedding(max_features, 128),
    layers.SimpleRNN(64),
    layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

mlflow.keras.autolog()

with mlflow.start_run() as run:
    model.fit(x_train, y_train, epochs=2, validation_split=0.1)
    print("📁 Run ID:", run.info.run_id)
