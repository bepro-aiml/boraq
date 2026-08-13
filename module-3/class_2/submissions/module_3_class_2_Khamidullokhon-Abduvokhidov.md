# Module 3 - Class 2 Assignment: Scaling

**Khamidullokhon Abduvokhidov**

The corresponding notebook contains separate commented cells for loading the Telco data, MinMax, Standard, and Robust scaling, histogram comparison, and the train-first leakage-safe scaling procedure.

```python
# Split first, then fit scaling only on training data to avoid leakage.
from sklearn.model_selection import train_test_split
X_train, X_test = train_test_split(X, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_test_s = scaler.transform(X_test)
print('Train mean:', X_train_s.mean(axis=0).round(2))
print('Test mean:', X_test_s.mean(axis=0).round(2))
```
