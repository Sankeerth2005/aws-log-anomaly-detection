import pickle
from sklearn.ensemble import IsolationForest

def train_model(X):
    model = IsolationForest(
        n_estimators=100,
        contamination=0.1,
        random_state=42
    )
    model.fit(X)
    return model

if __name__ == "__main__":
    # Dummy training data for now
    X = [
        [50, 1, 10],
        [52, 0, 9],
        [300, 120, 80]  # anomaly
    ]

    model = train_model(X)

    with open("model.pkl", "wb") as f:
        pickle.dump(model, f)

    print("Model trained and saved")
