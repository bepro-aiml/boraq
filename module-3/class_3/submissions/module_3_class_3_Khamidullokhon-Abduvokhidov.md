# Module 3 - Class 3 Assignment: Categorical Encoding

**Khamidullokhon Abduvokhidov**

The matching notebook completes all required categorical encoding tasks: object-column discovery, distribution checking, dummy encoding (including `drop_first`), `OneHotEncoder`, binary mapping, and multi-column encoding.

```python
# Encode several categorical features together.
multi = pd.get_dummies(df[['gender', 'InternetService', 'TechSupport', 'Contract']], drop_first=True)
print('Shape:', multi.shape)
multi.head()
```
