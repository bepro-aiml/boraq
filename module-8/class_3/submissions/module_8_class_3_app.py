from datetime import datetime, timezone
from pathlib import Path

import joblib
import numpy as np
from flask import Flask, jsonify, request

app = Flask(__name__)
MODEL_PATH = Path(__file__).with_name("model.pkl")
model = joblib.load(MODEL_PATH)
EXPECTED_FEATURES = int(model.n_features_in_)


@app.get("/health")
def health():
    return jsonify({"status": "healthy", "model_version": "v1.0"})


@app.post("/predict")
def predict():
    data = request.get_json(silent=True)
    if not isinstance(data, dict) or "features" not in data:
        return jsonify({"error": "JSON object with a 'features' list is required"}), 400
    features = data["features"]
    if not isinstance(features, list) or len(features) != EXPECTED_FEATURES:
        return jsonify({"error": f"features must be a list of {EXPECTED_FEATURES} numbers"}), 400
    try:
        values = np.asarray(features, dtype=float).reshape(1, -1)
    except (TypeError, ValueError):
        return jsonify({"error": "all features must be numeric"}), 400
    if not np.isfinite(values).all():
        return jsonify({"error": "features must be finite numbers"}), 400
    try:
        prediction = int(model.predict(values)[0])
        confidence = float(model.predict_proba(values)[0].max())
    except Exception:
        app.logger.exception("Prediction failed")
        return jsonify({"error": "prediction failed"}), 500
    return jsonify({"prediction": prediction, "confidence": confidence, "model_version": "v1.0", "timestamp": datetime.now(timezone.utc).isoformat()})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
