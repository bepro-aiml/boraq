# Module 8 - Class 3: Flask Prediction API

The matching notebook trains a full pipeline and tests [`module_8_class_3_app.py`](/C:/Users/Khamidullokhon/Documents/keep%20up%20with%20githup%20ml%20course/module_8_class_3_app.py). The API supports `GET /health` and validated `POST /predict` requests.

Example: `{"features": [30 numeric values]}`. Invalid JSON, an incorrect feature count, nonnumeric values, and non-finite values return HTTP 400.
