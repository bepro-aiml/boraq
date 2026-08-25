# Module 3 - Class 4 Assignment: Feature Selection

**Khamidullokhon Abduvokhidov**

The matching notebook builds the requested numeric-plus-one-hot feature set, ranks features with mutual information, plots those scores, selects three features using RFE, and compares logistic-regression test accuracy.

```python
# Compare logistic-regression accuracy with every feature and only the selected three.
m_all = LogisticRegression(max_iter=1000).fit(X_tr, y_tr)
print('All features:', round(accuracy_score(y_te, m_all.predict(X_te)), 4))
idx = np.where(rfe.support_)[0]
m_top = LogisticRegression(max_iter=1000).fit(X_tr[:, idx], y_tr)
print('Top 3:', round(accuracy_score(y_te, m_top.predict(X_te[:, idx])), 4))
```
