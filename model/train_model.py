import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle
import os

def train_and_save_model(data_path, model_path):
    df = pd.read_csv(data_path)
    X = df[['sessions_played', 'avg_session_length', 'purchases', 'level']]
    y = df['churned']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LogisticRegression()
    model.fit(X_train, y_train)

    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    with open(model_path, 'wb') as f:
        pickle.dump(model, f)
    print(f"✅ Model trained and saved to {model_path}")

if __name__ == "__main__":
    train_and_save_model("data/gallery_churn.csv", "model/churn_model.pkl")
