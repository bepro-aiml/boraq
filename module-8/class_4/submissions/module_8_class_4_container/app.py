from datetime import datetime, timezone
import joblib
import numpy as np
from flask import Flask, jsonify, request

app = Flask(__name__)
model = joblib.load("model.pkl")
EXPECTED_FEATURES = int(model.n_features_in_)

@app.get("/health")
def health():
    return jsonify({"status": "healthy", "model_version": "v1.0"})

@app.post("/predict")
def predict():
    body = request.get_json(silent=True)
    if not isinstance(body, dict) or "features" not in body:
        return jsonify({"error": "JSON object with a features list is required"}), 400
    try:
        values = np.asarray(body["features"], dtype=float).reshape(1, -1)
    except (TypeError, ValueError):
        return jsonify({"error": "features must be numeric"}), 400
    if values.shape[1] != EXPECTED_FEATURES or not np.isfinite(values).all():
        return jsonify({"error": f"provide {EXPECTED_FEATURES} finite numeric features"}), 400
    probabilities = model.predict_proba(values)[0]
    return jsonify({"prediction": int(model.predict(values)[0]), "confidence": float(probabilities.max()), "model_version": "v1.0", "timestamp": datetime.now(timezone.utc).isoformat()})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
