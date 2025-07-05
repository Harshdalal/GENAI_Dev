# train_mlflow.py
import mlflow
import mlflow.sklearn
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Load Iris dataset
iris = datasets.load_iris()
X, y = iris.data, iris.target

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Enable autologging
mlflow.sklearn.autolog()

with mlflow.start_run() as run:
    # Model training
    model = SVC(probability=True, kernel='rbf')
    model.fit(X_train, y_train)

    # Evaluation
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)

    print("✅ Accuracy:", acc)
    print("📁 Run ID:", run.info.run_id)
