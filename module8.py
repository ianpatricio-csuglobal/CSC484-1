"""
=====================================================
 Diabetes Prediction using Neural Networks (Keras)
 Author: Fernando Ian Patricio
 Date: September 7, 2025
=====================================================

Project Description:
--------------------
This program builds a machine learning model to predict
whether a patient has diabetes based on health indicators
from the Pima Indians Diabetes dataset. It demonstrates a
complete ML workflow:
    - Data loading & preprocessing
    - Model definition & training
    - Evaluation on test data
    - Visualization of training progress

Dataset Source:
---------------
Pima Indians Diabetes Dataset
https://www.openml.org/search?type=data&sort=runs&id=43483&status=active

Target Variable:
----------------
Outcome (0 = No diabetes, 1 = Diabetes)

=====================================================
"""

# -----------------------
# 1. Import Libraries
# -----------------------
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, classification_report
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input

# -----------------------
# 2. Load and Explore Data
# -----------------------
# Column names for the dataset
column_names = [
    "Pregnancies", "Glucose", "BloodPressure", "SkinThickness",
    "Insulin", "BMI", "DiabetesPedigreeFunction", "Age", "Outcome"
]

# Load dataset (downloaded and saved locally)
df = pd.read_csv("PimaIndiansDiabetes.csv", header=None, names=column_names)

print("===== Dataset Preview =====")
print(df.head(), "\n")
print("===== Dataset Info =====")
print(df.info(), "\n")

# -----------------------
# 3. Prepare Features and Target
# -----------------------
X = df.drop("Outcome", axis=1)   # Features
y = df["Outcome"]                # Target

# Split into train/test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Standardize features for neural network
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# -----------------------
# 4. Build Neural Network
# -----------------------
model = Sequential([
    Input(shape=(X_train.shape[1],)),   # Explicit Input layer
    Dense(16, activation='relu'),       # Hidden layer 1
    Dense(8, activation='relu'),        # Hidden layer 2
    Dense(1, activation='sigmoid')      # Output layer (binary classification)
])

# Compile model
model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# -----------------------
# 5. Train the Model
# -----------------------
history = model.fit(
    X_train, y_train,
    validation_split=0.2,
    epochs=100,
    batch_size=16,
    verbose=1
)

# -----------------------
# 6. Evaluate the Model
# -----------------------
loss, accuracy = model.evaluate(X_test, y_test, verbose=0)
print("===== Model Evaluation on Test Data =====")
print(f"Test Loss     : {loss:.4f}")
print(f"Test Accuracy : {accuracy:.4f}\n")

# -----------------------
# 7. Make Predictions
# -----------------------
y_pred_prob = model.predict(X_test)
y_pred = (y_pred_prob > 0.5).astype(int)

print("===== Confusion Matrix =====")
print(confusion_matrix(y_test, y_pred), "\n")

print("===== Classification Report =====")
print(classification_report(y_test, y_pred))

# -----------------------
# 8. Visualize Training History
# -----------------------
plt.figure(figsize=(12, 5))

# Accuracy curve
plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], label='Train Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.title('Training vs Validation Accuracy')
plt.legend()

# Loss curve
plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], label='Train Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('Training vs Validation Loss')
plt.legend()

plt.tight_layout()
plt.show()
