pip install pytest

import pytest
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score

# -----------------------------
# Load Wine Quality Dataset
# -----------------------------
def load_wine_data():
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
    data = pd.read_csv(url, sep=';')
    X = data.drop('quality', axis=1).values
    # Convert to binary classification: 1 = high quality (>=6), 0 = low quality (<6)
    y = (data['quality'] >= 6).astype(int).values
    return X, y

# -----------------------------
# Test Data Loading
# -----------------------------
def test_data_loading():
    X, y = load_wine_data()
    assert X.shape[0] == y.shape[0]  # Number of samples matches
    assert X.shape[1] == 11         # 11 features in wine dataset
    assert set(np.unique(y)) <= {0,1}  # Only binary labels

# -----------------------------
# Test Train/Test Split
# -----------------------------
def test_train_test_split():
    X, y = load_wine_data()
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    assert X_train.shape[0] + X_test.shape[0] == X.shape[0]
    assert X_train.shape[1] == X.shape[1]
    assert y_train.shape[0] == X_train.shape[0]

# -----------------------------
# Test Perceptron Model Training and Prediction
# -----------------------------
def test_perceptron_fit_predict():
    X, y = load_wine_data()
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # Scale features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Initialize and train Perceptron
    clf = Perceptron(max_iter=1000, tol=1e-3, random_state=42)
    clf.fit(X_train_scaled, y_train)

    # Predict
    y_pred = clf.predict(X_test_scaled)

    # Check prediction shape
    assert y_pred.shape == y_test.shape

    # Check that accuracy is reasonable (>50%)
    acc = accuracy_score(y_test, y_pred)
    assert 0.5 <= acc <= 1.0

# -----------------------------
# Optional: Test reproducibility
# -----------------------------
def test_reproducibility():
    X, y = load_wine_data()
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    clf1 = Perceptron(max_iter=1000, tol=1e-3, random_state=42)
    clf1.fit(X_train_scaled, y_train)
    y_pred1 = clf1.predict(X_test_scaled)

    clf2 = Perceptron(max_iter=1000, tol=1e-3, random_state=42)
    clf2.fit(X_train_scaled, y_train)
    y_pred2 = clf2.predict(X_test_scaled)

    # Predictions should be identical
    np.testing.assert_array_equal(y_pred1, y_pred2)
