"""Examples showing scikit-learn usage and comparing to the pure-NumPy implementations.

This script attempts to import scikit-learn. If sklearn isn't installed the demo will print
an informative message and exit cleanly.
"""

from __future__ import annotations

import sys

try:
    from sklearn.linear_model import LinearRegression, LogisticRegression
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.model_selection import train_test_split as sk_train_test_split
    from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
    SKLEARN_AVAILABLE = True
except Exception as e:  # ImportError or others
    SKLEARN_AVAILABLE = False
    _IMPORT_ERROR = e

import numpy as np


def demo_sklearn_linear():
    print("--- scikit-learn LinearRegression demo ---")
    rng = np.random.default_rng(0)
    X = rng.uniform(-5, 5, size=(200, 1))
    y = 3.0 * X[:, 0] + 2.0 + rng.normal(0, 2.0, size=200)

    X_train, X_test, y_train, y_test = sk_train_test_split(X, y, test_size=0.2, random_state=0)
    model = LinearRegression()
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    mse = np.mean((preds - y_test) ** 2)
    print(f"coefficients: intercept={model.intercept_:.4f}, coef={model.coef_}")
    print(f"MSE (sklearn): {mse:.4f}")


def demo_sklearn_logistic():
    print("--- scikit-learn LogisticRegression demo ---")
    rng = np.random.default_rng(1)
    n = 300
    X0 = rng.normal(loc=[-2, -2], scale=1.0, size=(n // 2, 2))
    X1 = rng.normal(loc=[2, 2], scale=1.0, size=(n // 2, 2))
    X = np.vstack([X0, X1])
    y = np.array([0] * (n // 2) + [1] * (n // 2))

    X_train, X_test, y_train, y_test = sk_train_test_split(X, y, test_size=0.3, random_state=1)
    clf = LogisticRegression(solver='lbfgs', max_iter=1000)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    print(f"accuracy: {accuracy_score(y_test, y_pred):.3f}")
    print(f"precision: {precision_score(y_test, y_pred):.3f}, recall: {recall_score(y_test, y_pred):.3f}, f1: {f1_score(y_test, y_pred):.3f}")


def demo_sklearn_knn():
    print("--- scikit-learn k-NN demo ---")
    rng = np.random.default_rng(2)
    n = 180
    X0 = rng.normal(loc=[0, 0], scale=1.0, size=(n // 3, 2))
    X1 = rng.normal(loc=[5, 5], scale=1.0, size=(n // 3, 2))
    X2 = rng.normal(loc=[0, 5], scale=1.0, size=(n // 3, 2))
    X = np.vstack([X0, X1, X2])
    y = np.array([0] * (n // 3) + [1] * (n // 3) + [2] * (n // 3))

    X_train, X_test, y_train, y_test = sk_train_test_split(X, y, test_size=0.3, random_state=2)
    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    print(f"k-NN accuracy (sklearn k=5): {accuracy_score(y_test, y_pred):.3f}")


def main():
    if not SKLEARN_AVAILABLE:
        print("scikit-learn is not available in this environment.")
        print("Import error:", _IMPORT_ERROR)
        print("If you want to run these demos, install scikit-learn (e.g., pip install scikit-learn) and run again.")
        return

    demo_sklearn_linear()
    demo_sklearn_logistic()
    demo_sklearn_knn()


if __name__ == '__main__':
    main()
