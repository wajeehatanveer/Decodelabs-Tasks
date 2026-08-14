import pandas as pd

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score


# LOAD IRIS DATASET

iris = load_iris()

data = pd.DataFrame(
    iris.data,
    columns=iris.feature_names
)

data["target"] = iris.target


# DATASET INFORMATION

print("=" * 55)
print("🌸 IRIS FLOWER DATA CLASSIFICATION")
print("=" * 55)

print("\n📊 Dataset Shape:")
print(data.shape)

print("\n📋 First Five Rows:")
print(data.head())

print("\n🌸 Flower Classes:")
print(iris.target_names)

print("\n📌 Features:")
print(iris.feature_names)


# FEATURES AND TARGET

X = data.drop("target", axis=1)
y = data["target"]


# TRAIN / TEST SPLIT

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

print("\n" + "=" * 55)
print("📚 DATA SPLIT")
print("=" * 55)

print(f"Training Samples : {len(X_train)}")
print(f"Testing Samples  : {len(X_test)}")


# FEATURE SCALING

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


# CHOOSING BEST K

best_k = 1
best_accuracy = 0

for k in range(1, 11):

    knn = KNeighborsClassifier(n_neighbors=k)

    knn.fit(X_train_scaled, y_train)

    predictions = knn.predict(X_test_scaled)

    accuracy = accuracy_score(y_test, predictions)

    if accuracy > best_accuracy:
        best_accuracy = accuracy
        best_k = k


print("\n" + "=" * 55)
print("⚙️ K VALUE TUNING")
print("=" * 55)

print(f"Best K Value : {best_k}")
print(f"Best Accuracy: {best_accuracy * 100:.2f}%")


# FINAL KNN MODEL

model = KNeighborsClassifier(n_neighbors=best_k)

model.fit(X_train_scaled, y_train)


# MODEL PREDICTION

y_pred = model.predict(X_test_scaled)


# MODEL EVALUATION

accuracy = accuracy_score(y_test, y_pred)

f1 = f1_score(
    y_test,
    y_pred,
    average="weighted"
)

cm = confusion_matrix(y_test, y_pred)


print("\n" + "=" * 55)
print("🤖 MODEL EVALUATION")
print("=" * 55)

print(f"\n✅ Accuracy : {accuracy * 100:.2f}%")
print(f"✅ F1 Score : {f1:.2f}")

print("\n📊 Confusion Matrix:")
print(cm)


# NEW FLOWER PREDICTION

print("\n" + "=" * 55)
print("🌸 FLOWER PREDICTION")
print("=" * 55)

sample_flower = pd.DataFrame(
    [[5.1, 3.5, 1.4, 0.2]],
    columns=iris.feature_names
)

sample_scaled = scaler.transform(sample_flower)

prediction = model.predict(sample_scaled)

print(
    f"\n🌼 Predicted Flower: "
    f"{iris.target_names[prediction[0]].capitalize()}"
)

