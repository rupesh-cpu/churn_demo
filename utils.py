import pickle
import numpy as np

def load_model(model_path="model/churn_model.pkl"):
    with open(model_path, 'rb') as f:
        return pickle.load(f)

def predict_churn(model, sessions, session_length, purchases, level):
    input_data = np.array([[sessions, session_length, purchases, level]])
    return model.predict(input_data)[0]
