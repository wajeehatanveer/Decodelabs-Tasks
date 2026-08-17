from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import csv


def load_data():
    recommendations = []

    with open("raw_skills.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            recommendations.append(
                {
                    "name": row["name"],
                    "skills": row["skills"],
                }
            )

    return recommendations


def calculate_scores(user_skills, recommendations):

    # User skills ko text mein convert karna
    user_text = " ".join(user_skills)

    # Career name + skills ko combine karna
    recommendation_texts = [
        f"{item['name']} {item['skills']}"
        for item in recommendations
    ]

    # User + recommendations ko ek saath vectorize karna
    all_texts = [user_text] + recommendation_texts

    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(all_texts)

    # User vector aur recommendation vectors
    user_vector = vectors[0]
    recommendation_vectors = vectors[1:]

    # Cosine Similarity calculate karna
    scores = cosine_similarity(
        user_vector,
        recommendation_vectors
    )[0]

    # Har recommendation ke saath score attach karna
    results = []

    for item, score in zip(recommendations, scores):
        results.append(
            {
                "name": item["name"],
                "score": score,
            }
        )

    return results


def sort_results(results):
    return sorted(
        results,
        key=lambda item: item["score"],
        reverse=True
    )


def filter_top_n(results, n=3):
    return results[:n]


if __name__ == "__main__":

    data = load_data()

    user_input = input(
        "\nEnter your skills/interests (comma-separated): "
    ).strip()

    user_skills = [
        skill.strip()
        for skill in user_input.split(",")
        if skill.strip()
    ]

    # -----------------------------
    # Cold Start Handling
    # -----------------------------

    if not user_skills:

        print("\nNo preferences found.")
        print("Cold Start detected.")
        print("Please enter your initial skills/interests.")

        user_input = input(
            "\nEnter your skills/interests (comma-separated): "
        ).strip()

        user_skills = [
            skill.strip()
            for skill in user_input.split(",")
            if skill.strip()
        ]

    # -----------------------------
    # Stop if still no valid input
    # -----------------------------

    if not user_skills:

        print("\nNo valid skills were provided.")
        print("Recommendation process stopped.")
        exit()

    # -----------------------------
    # Calculate Scores
    # -----------------------------

    results = calculate_scores(
        user_skills,
        data
    )

    # -----------------------------
    # Sort Results
    # -----------------------------

    sorted_results = sort_results(results)

    # -----------------------------
    # Top 3 Recommendations
    # -----------------------------

    top_results = filter_top_n(
        sorted_results,
        3
    )

    # -----------------------------
    # All Recommendations
    # -----------------------------

    print("\nAll Recommendations:")

    for result in sorted_results:

        if result["score"] == 0:

            print(
                f"{result['name']}: No Match"
            )

        else:

            print(
                f"{result['name']}: "
                f"{result['score']:.2f}"
            )

    # -----------------------------
    # Top 3 Recommendations
    # -----------------------------

    print("\nTop 3 Recommendations:")

    for index, result in enumerate(
        top_results,
        start=1
    ):

        print(
            f"{index}. {result['name']}: "
            f"{result['score']:.2f}"
        )