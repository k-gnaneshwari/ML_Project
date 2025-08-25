import pandas as pd
import os
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline

def train():
    # Load dataset
    df = pd.read_csv("C:/Users/KALE SHIVARAM/Downloads/data.csv")

    # Create CLV column (target)
    df["CLV"] = df["Quantity"] * df["UnitPrice"]

    # Select features (you can add more later like CustomerID, Country, etc.)
    X = df[["Quantity", "UnitPrice"]]
    y = df["CLV"]

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Build pipeline
    model = Pipeline([
        ("scaler", StandardScaler()),
        ("regressor", LinearRegression())
    ])

    # Train model
    model.fit(X_train, y_train)

    # Save artifacts
    os.makedirs("artifacts", exist_ok=True)
    joblib.dump(model, "artifacts/model.pkl")

    print("✅ Model training complete. Model saved at artifacts/model.pkl")

if __name__ == "__main__":
    train()
