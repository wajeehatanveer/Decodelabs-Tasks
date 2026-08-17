**DecodеLabs — Project 3: AI Recommendation Logic**
# 🤖 Tech Stack Recommender

An AI-powered recommendation system that recommends suitable technology career roles based on a user's skills and interests.

## 📌 Project Overview

The system uses a content-based recommendation approach to compare user skills with the skills required for different technology roles.

It calculates similarity scores, ranks the results, and provides the **Top 3 recommendations**.

## 🚀 Features

- 🎯 Skills and interests input
- ❄️ Cold Start handling for new users
- 📋 All career recommendations
- 📊 Match percentage scores
- 🚫 No Match handling
- 🏆 Top 3 recommendations
- 🔢 TF-IDF vectorization
- 🔍 Cosine Similarity
- 📈 Result sorting and Top-N filtering
- 🌐 Streamlit web interface

## 🧠 Recommendation Process

```text
User Skills & Interests
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
* CSV Dataset

## 📂 Project Structure

```text
Project 3 AI Recommendation Logic/
│
├── app.py
├── recommendation.py
├── raw_skills.csv
├── requirements.txt
└── README.md
```

## 💡 Example

### Input

```text
Python, Cloud, Automation
```

### Output

```text
1. Cloud Architect
2. DevOps Engineer
3. System Administrator
```

The recommendations are ranked according to their calculated similarity scores.

## ❄️ Cold Start

New users can select their interests from the provided options. These interests are mapped to relevant skills and used to generate initial recommendations.

## ▶️ How to Run

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```
