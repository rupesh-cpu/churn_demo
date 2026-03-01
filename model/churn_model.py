import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle
import os

# Load dataset
df = pd.read_csv('data/gallery_churn.csv')

# Features and target
X = df[['sessions_played', 'avg_session_length', 'purchases', 'level']]
y = df['churned']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save model
os.makedirs('model', exist_ok=True)
with open('model/churn_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("✅ Model trained and saved as churn_model.pkl")
