"""Machine Learning basics examples (pure NumPy implementations).

This file contains small, educational implementations of:
- train_test_split
- Linear Regression (closed-form normal equation + gradient descent)
- Logistic Regression (gradient descent)
- k-Nearest Neighbors (simple)
- Basic metrics: accuracy, precision, recall, f1, confusion matrix

Run this file to see demonstrations on synthetic data.
"""

from __future__ import annotations

import math
import random
from typing import Tuple

import numpy as np


def train_test_split(X: np.ndarray, y: np.ndarray, test_size: float = 0.2, seed: int | None = None) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    if seed is not None:
        np.random.seed(seed)
    n = X.shape[0]
    idx = np.arange(n)
    np.random.shuffle(idx)
    split = int(n * (1 - test_size))
    train_idx = idx[:split]
    test_idx = idx[split:]
    return X[train_idx], X[test_idx], y[train_idx], y[test_idx]


# Linear Regression - closed form (normal equation)
def linear_regression_closed_form(X: np.ndarray, y: np.ndarray) -> np.ndarray:
    # add intercept
    Xb = np.hstack([np.ones((X.shape[0], 1)), X])
    # normal equation: w = (X^T X)^-1 X^T y
    w = np.linalg.pinv(Xb.T.dot(Xb)).dot(Xb.T).dot(y)
    return w


def predict_linear(X: np.ndarray, w: np.ndarray) -> np.ndarray:
    Xb = np.hstack([np.ones((X.shape[0], 1)), X])
    return Xb.dot(w)


# Linear Regression - gradient descent
def linear_regression_gd(X: np.ndarray, y: np.ndarray, lr: float = 0.01, epochs: int = 1000) -> np.ndarray:
    Xb = np.hstack([np.ones((X.shape[0], 1)), X])
    w = np.zeros(Xb.shape[1])
    n = Xb.shape[0]
    for _ in range(epochs):
        preds = Xb.dot(w)
        grad = (2.0 / n) * Xb.T.dot(preds - y)
        w -= lr * grad
    return w


# Logistic regression (binary) using sigmoid and gradient descent
def sigmoid(z: np.ndarray) -> np.ndarray:
    return 1.0 / (1.0 + np.exp(-z))


def logistic_regression_gd(X: np.ndarray, y: np.ndarray, lr: float = 0.1, epochs: int = 1000) -> np.ndarray:
    Xb = np.hstack([np.ones((X.shape[0], 1)), X])
    w = np.zeros(Xb.shape[1])
    n = Xb.shape[0]
    for _ in range(epochs):
        preds = sigmoid(Xb.dot(w))
        grad = (1.0 / n) * Xb.T.dot(preds - y)
        w -= lr * grad
    return w


def predict_logistic(X: np.ndarray, w: np.ndarray, threshold: float = 0.5) -> np.ndarray:
    Xb = np.hstack([np.ones((X.shape[0], 1)), X])
    probs = sigmoid(Xb.dot(w))
    return (probs >= threshold).astype(int)


# k-NN simple implementation (brute force)
def knn_predict(X_train: np.ndarray, y_train: np.ndarray, X_test: np.ndarray, k: int = 3) -> np.ndarray:
    preds = []
    for x in X_test:
        # compute distances
        dists = np.linalg.norm(X_train - x, axis=1)
        nn_idx = np.argsort(dists)[:k]
        vals, counts = np.unique(y_train[nn_idx], return_counts=True)
        preds.append(vals[np.argmax(counts)])
    return np.array(preds)


# Metrics
def accuracy(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    return float((y_true == y_pred).mean())


def confusion_matrix(y_true: np.ndarray, y_pred: np.ndarray) -> np.ndarray:
    tp = int(((y_true == 1) & (y_pred == 1)).sum())
    tn = int(((y_true == 0) & (y_pred == 0)).sum())
    fp = int(((y_true == 0) & (y_pred == 1)).sum())
    fn = int(((y_true == 1) & (y_pred == 0)).sum())
    return np.array([[tn, fp], [fn, tp]])


def precision_recall_f1(y_true: np.ndarray, y_pred: np.ndarray) -> Tuple[float, float, float]:
    cm = confusion_matrix(y_true, y_pred)
    tn, fp, fn, tp = cm.ravel()
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0.0
    return precision, recall, f1


# Small demos with synthetic data
def _demo_linear_regression():
    print("--- Linear Regression Demo ---")
    # create synthetic linear data y = 3 * x + 2 + noise
    rng = np.random.default_rng(0)
    X = rng.uniform(-5, 5, size=(100, 1))
    y = 3.0 * X[:, 0] + 2.0 + rng.normal(0, 2.0, size=100)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, seed=0)
    w_closed = linear_regression_closed_form(X_train, y_train)
    w_gd = linear_regression_gd(X_train, y_train, lr=0.01, epochs=5000)

    preds_closed = predict_linear(X_test, w_closed)
    preds_gd = predict_linear(X_test, w_gd)

    mse_closed = np.mean((preds_closed - y_test) ** 2)
    mse_gd = np.mean((preds_gd - y_test) ** 2)
    print(f"closed-form weights: {w_closed}")
    print(f"gd weights: {w_gd}")
    print(f"MSE closed-form: {mse_closed:.3f}, MSE gd: {mse_gd:.3f}")


def _demo_classification_logistic():
    print("\n--- Logistic Regression Demo ---")
    rng = np.random.default_rng(1)
    # create two gaussian clusters
    n = 200
    X0 = rng.normal(loc=[-2, -2], scale=1.0, size=(n // 2, 2))
    X1 = rng.normal(loc=[2, 2], scale=1.0, size=(n // 2, 2))
    X = np.vstack([X0, X1])
    y = np.array([0] * (n // 2) + [1] * (n // 2))

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, seed=1)
    w_log = logistic_regression_gd(X_train, y_train, lr=0.5, epochs=2000)
    y_pred = predict_logistic(X_test, w_log)

    acc = accuracy(y_test, y_pred)
    prec, rec, f1 = precision_recall_f1(y_test, y_pred)
    print(f"accuracy: {acc:.3f}")
    print(f"precision: {prec:.3f}, recall: {rec:.3f}, f1: {f1:.3f}")


def _demo_knn():
    print("\n--- k-NN Demo ---")
    rng = np.random.default_rng(2)
    n = 150
    X0 = rng.normal(loc=[0, 0], scale=1.0, size=(n // 3, 2))
    X1 = rng.normal(loc=[5, 5], scale=1.0, size=(n // 3, 2))
    X2 = rng.normal(loc=[0, 5], scale=1.0, size=(n // 3, 2))
    X = np.vstack([X0, X1, X2])
    y = np.array([0] * (n // 3) + [1] * (n // 3) + [2] * (n // 3))

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, seed=2)
    y_pred = knn_predict(X_train, y_train, X_test, k=5)
    acc = accuracy(y_test, y_pred)
    print(f"k-NN accuracy (k=5): {acc:.3f}")


def main():
    _demo_linear_regression()
    _demo_classification_logistic()
    _demo_knn()


if __name__ == '__main__':
    main()
