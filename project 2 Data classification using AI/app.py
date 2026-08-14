import streamlit as st
import pandas as pd

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score


# PAGE CONFIGURATION

st.set_page_config(
    page_title="AI Flower Classification",
    page_icon="🌸",
    layout="wide"
)

# LOAD IRIS DATASET

iris = load_iris()

data = pd.DataFrame(
    iris.data,
    columns=iris.feature_names
)

data["target"] = iris.target


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


# FEATURE SCALING

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


# FIND BEST K


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


# FINAL MODEL


model = KNeighborsClassifier(
    n_neighbors=best_k
)

model.fit(X_train_scaled, y_train)

y_pred = model.predict(X_test_scaled)


# MODEL EVALUATION

accuracy = accuracy_score(y_test, y_pred)

f1 = f1_score(
    y_test,
    y_pred,
    average="weighted"
)

cm = confusion_matrix(y_test, y_pred)



# TITLE

st.title("🌸 AI Flower Classification")

st.subheader("Machine Learning Project")


# DATASET INFORMATION
# 

st.header("📊 Dataset Information")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Samples", len(data))

with col2:
    st.metric("Features", len(iris.feature_names))

with col3:
    st.metric("Flower Classes", len(iris.target_names))


st.write("### 🌼 Flower Species")

st.write(
    ", ".join(
        name.capitalize()
        for name in iris.target_names
    )
)


# MODEL PERFORMANCE

st.header("🤖 Model Performance")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Accuracy",
        f"{accuracy * 100:.2f}%"
    )

with col2:
    st.metric(
        "F1 Score",
        f"{f1:.2f}"
    )

with col3:
    st.metric(
        "Best K",
        best_k
    )


# CONFUSION MATRIX

st.subheader("📊 Confusion Matrix")

cm_df = pd.DataFrame(
    cm,
    index=iris.target_names,
    columns=iris.target_names
)

st.dataframe(cm_df)


# USER INPUT

st.header("🌸 Predict a New Flower")

st.write(
    "Enter the measurements of the flower below:"
)

col1, col2 = st.columns(2)

with col1:

    sepal_length = st.number_input(
        "Sepal Length (cm)",
        min_value=0.0,
        value=5.1,
        step=0.1
    )

    sepal_width = st.number_input(
        "Sepal Width (cm)",
        min_value=0.0,
        value=3.5,
        step=0.1
    )

with col2:

    petal_length = st.number_input(
        "Petal Length (cm)",
        min_value=0.0,
        value=1.4,
        step=0.1
    )

    petal_width = st.number_input(
        "Petal Width (cm)",
        min_value=0.0,
        value=0.2,
        step=0.1
    )

# PREDICTION BUTTON

if st.button("🔮 Predict Flower"):

    sample_flower = pd.DataFrame(
        [[
            sepal_length,
            sepal_width,
            petal_length,
            petal_width
        ]],
        columns=iris.feature_names
    )

    sample_scaled = scaler.transform(
        sample_flower
    )

    prediction = model.predict(
        sample_scaled
    )

    predicted_flower = iris.target_names[
        prediction[0]
    ].capitalize()

    st.success(
        f"🌼 Predicted Flower: {predicted_flower}"
    )