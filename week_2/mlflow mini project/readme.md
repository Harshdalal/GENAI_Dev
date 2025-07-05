mlops_mlflow_iris/

│

├── train_mlflow.py        # Train and log model to MLflow

├── predict_mlflow.py      # Predict using a logged model

├── requirements.txt

└── mlruns/                # MLflow tracking directory (auto-created)


#bash > python train_mlflow.py
#bash > mlflow ui

Then open in browser:
👉 http://127.0.0.1:5000

#bash > python predict_mlflow.py

✅ Summary Table

| Step                      | Command                    |

| ------------------------- | -------------------------- |

| Train and log model       | `python train_mlflow.py`   |

| Start MLflow UI           | `mlflow ui`                |

| Open MLflow UI            | `http://127.0.0.1:5000`    |

| Predict from logged model | `python predict_mlflow.py` |
