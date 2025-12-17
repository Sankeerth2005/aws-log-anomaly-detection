import pickle
from preprocess import load_logs, window_logs, extract_features
from sklearn.ensemble import IsolationForest
import os

DATA_PATH = "../data/raw/app.log"
MODEL_PATH = "../models/isolation_forest.pkl"

def main():
    logs = load_logs(DATA_PATH)
    windows = window_logs(logs)

    X = []
    for _, log_window in windows.items():
        features = extract_features(log_window)
        X.append(features)

    print(f"Training on {len(X)} windows")

    model = IsolationForest(
        n_estimators=100,
        contamination=0.2,
        random_state=42
    )
    model.fit(X)

    os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
    with open(MODEL_PATH, "wb") as f:
        pickle.dump(model, f)

    print(f"Model saved to {MODEL_PATH}")

if __name__ == "__main__":
    main()
