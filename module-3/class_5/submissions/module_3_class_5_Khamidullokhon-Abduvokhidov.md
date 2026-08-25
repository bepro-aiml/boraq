# Module 3 - Class 5 Assignment: Pipelines

**Khamidullokhon Abduvokhidov**

The matching notebook creates numeric and categorical pipelines, combines them with `ColumnTransformer`, trains a Random Forest, evaluates it, and saves/reloads the complete pipeline.

```python
# Save the full pipeline and confirm that the reloaded model works.
import joblib
joblib.dump(full_pipe, 'rf_pipeline.joblib')
loaded = joblib.load('rf_pipeline.joblib')
print('Loaded model test accuracy:', round(loaded.score(X_test, y_test), 4))
```
