# Example: Hyperparameter tuning for LogisticRegression using RandomizedSearchCV

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from scipy.stats import uniform

# Load data
X, y = load_breast_cancer(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define model
log_reg = LogisticRegression(max_iter=1000, solver='saga')

# Define parameter distributions
param_dist = {
    'C': uniform(0.01, 10),
    'penalty': ['l1', 'l2']
}

# Randomized search
random_search = RandomizedSearchCV(estimator=log_reg, param_distributions=param_dist,
                                   n_iter=20, cv=5, n_jobs=-1, random_state=42, scoring='accuracy')
random_search.fit(X_train, y_train)

# Best parameters
print("Best Parameters:", random_search.best_params_)
print("Best Score:", random_search.best_score_)

# Evaluate
best_model = random_search.best_estimator_
y_pred = best_model.predict(X_test)
print("\nClassification Report:\n", classification_report(y_test, y_pred))