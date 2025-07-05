import mlflow.keras
import numpy as np
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing.sequence import pad_sequences

RUN_ID = "92215b20fa12437ea54294914bf05e55"

model_uri = f"runs:/{RUN_ID}/model"
model = mlflow.keras.load_model(model_uri)

(_, _), (x_test, y_test) = imdb.load_data(num_words=10000)
x_sample = pad_sequences([x_test[0]], maxlen=200)
prediction = model.predict(x_sample)
print("🔮 Sentiment:", "Positive" if prediction[0][0] > 0.5 else "Negative")
