import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler

# Load dataset
df = pd.read_csv("diabetes.csv")  # Ensure diabetes.csv exists in the same folder

# Split data into features and labels
X = df.drop(columns=["Outcome"])  # Adjust this if your dataset has a different target column
y = df["Outcome"]

# Split into training/testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the trained model
with open("diabetes.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model saved successfully as 'diabetes.pkl'")
