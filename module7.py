"""
Module: KNN Hyperparameter Tuning with Iris Dataset
Description: This program determines the optimal number of neighbors (k)
             for a KNN classifier using cross-validation. It evaluates
             different k values on the Iris dataset and visualizes
             accuracy results.
Author: Fernando Ian Patricio
Date: September 2, 2025
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.neighbors import KNeighborsClassifier

# Load Iris dataset (150 samples, 4 features, 3 classes)
iris = load_iris()
X, y = iris.data, iris.target

# Split data: 70% training, 30% testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42, stratify=y
)

# Define candidate k values (neighbors)
k_values = range(1, 31)
accuracy_scores = []

# Evaluate each k using cross-validation
for k in k_values:
    knn = KNeighborsClassifier(n_neighbors=k)
    scores = cross_val_score(knn, X_train, y_train, cv=5)  # 5-fold CV
    accuracy_scores.append(scores.mean())

# Find best k
best_k = k_values[np.argmax(accuracy_scores)]
best_score = max(accuracy_scores)

print("========================================")
print(f"Optimal number of neighbors (k): {best_k}")
print(f"Best cross-validation accuracy: {best_score:.4f}")

# Train final model using best k
final_knn = KNeighborsClassifier(n_neighbors=best_k)
final_knn.fit(X_train, y_train)

# Evaluate on test set
test_accuracy = final_knn.score(X_test, y_test)
print(f"Test set accuracy with k={best_k}: {test_accuracy:.4f}")
print("========================================")

# Plot accuracy results
plt.figure(figsize=(8, 5))
plt.plot(k_values, accuracy_scores, marker="o", linestyle="-")
plt.title("KNN Hyperparameter Tuning on Iris Dataset")
plt.xlabel("Number of Neighbors (k)")
plt.ylabel("Cross-Validation Accuracy")
plt.grid(True)
plt.axvline(x=best_k, color="red", linestyle="--", label=f"Best k = {best_k}")
plt.legend()
plt.show()
