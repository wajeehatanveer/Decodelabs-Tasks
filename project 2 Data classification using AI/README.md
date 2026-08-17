#Project 2
# 🌸 AI Data Classification Using K-Nearest Neighbors

## 📌 Project Overview

This project is a Machine Learning based flower classification system built using the **Iris Dataset** and the **K-Nearest Neighbors (KNN)** algorithm.

The system analyzes flower measurements and predicts the flower species:

- 🌸 Setosa
- 🌼 Versicolor
- 🌺 Virginica

The project includes both a **Python Machine Learning backend** and an interactive **Streamlit frontend**.

---

## 🎯 Project Objective

The main objective of this project is to understand and implement a complete supervised Machine Learning classification workflow.

The system performs:

1. Dataset loading
2. Dataset exploration
3. Feature and target separation
4. Train-test splitting
5. Feature scaling
6. K-value tuning
7. KNN model training
8. Model prediction
9. Model evaluation
10. New flower prediction
11. Interactive Streamlit interface

---

## 📊 Dataset

The project uses the built-in **Iris Dataset** from Scikit-learn.

### Dataset Information

- Total Samples: **150**
- Features: **4**
- Classes: **3**
- Training Samples: **120**
- Testing Samples: **30**

### Features

The model uses four flower measurements:

- Sepal Length (cm)
- Sepal Width (cm)
- Petal Length (cm)
- Petal Width (cm)

### Target Classes

| Target | Flower Species |
|--------|----------------|
| 0 | Setosa |
| 1 | Versicolor |
| 2 | Virginica |

---

## 🤖 Machine Learning Algorithm

### K-Nearest Neighbors (KNN)

KNN is a supervised Machine Learning classification algorithm.

It predicts the class of a new data point by looking at its nearest neighboring data points.

In this project, different K values are tested to find the best-performing K value.

The project checks K values from:

```text
1 to 10


##📌Project3: AI Recommendation Logic
# 🤖 Tech Stack Recommender

An AI-powered recommendation system that suggests suitable technology career roles based on user skills and interests.

## 🚀 Features

- User skills and interests input
- Cold Start handling for new users
- TF-IDF vectorization
- Cosine Similarity
- Match scoring and ranking
- No Match handling
- Top 3 recommendations
- Streamlit web interface

## 🧠 How It Works

```text
User Skills
↓
TF-IDF Vectorization
↓
Cosine Similarity
↓
Similarity Scores
↓
Ranking
↓
Top 3 Recommendations
````

## 🛠️ Tech Stack

* Python
* Streamlit
* Scikit-learn
* TF-IDF
* Cosine Similarity
* CSV

## 📂 Files

* `app.py` — Streamlit frontend
* `recommendation.py` — Recommendation logic
* `raw_skills.csv` — Career skills dataset
* `requirements.txt` — Required Python packages

## ▶️ Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```
