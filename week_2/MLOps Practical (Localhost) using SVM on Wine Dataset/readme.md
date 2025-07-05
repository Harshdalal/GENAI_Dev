mlops_svm_wine/

│

├── train_model.py        # Train SVM and save model

├── app.py                # Flask API

├── test_api.py           # Test the API

├── model/

│   └── wine_svm_model.pkl

└── requirements.txt

#bash > python train_svm_mlops_model.py

#bash > python mlops_wineapp.py > http://127.0.0.1:5000/

#bash > python mlops_test_api.py

| Step             | Command                  |
| ---------------- | ------------------------ |
| Train SVM model  | `python train_model.py`  |
| Start API server | `python app.py`          |
| Test prediction  | `python test_api.py`     |
| Open in browser  | `http://127.0.0.1:5000/` |





