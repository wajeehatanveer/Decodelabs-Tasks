import streamlit as st
from recommendation import load_data, calculate_scores, sort_results, filter_top_n

st.set_page_config(
    page_title="Tech Stack Recommender", page_icon="🤖", layout="centered"
)

# -----------------------------
# Custom Styling
# -----------------------------

st.markdown(
    """
    <style>
    .main-title {
        font-size: 42px;
        font-weight: 700;
        text-align: center;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        color: #666;
        font-size: 16px;
        margin-bottom: 30px;
    }

    .section-title {
        font-size: 24px;
        font-weight: 600;
        margin-top: 25px;
        margin-bottom: 15px;
    }

    .recommendation-card {
        padding: 14px 18px;
        border-radius: 10px;
        background-color: #f5f7fa;
        margin-bottom: 10px;
        border: 1px solid #e1e5ea;
    }

    .top-card {
        padding: 18px;
        border-radius: 12px;
        background-color: #e8f5e9;
        margin-bottom: 12px;
        border: 1px solid #c8e6c9;
    }

    .score {
        font-weight: 600;
    }

    .info-box {
        padding: 15px;
        border-radius: 10px;
        background-color: #eef4ff;
        border: 1px solid #d6e4ff;
        margin-top: 20px;
        margin-bottom: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# -----------------------------
# Header
# -----------------------------

st.markdown(
    '<div class="main-title">🤖 Tech Stack Recommender</div>', unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    "AI-powered recommendations based on your skills and interests"
    "</div>",
    unsafe_allow_html=True,
)


# -----------------------------
# Input Section
# -----------------------------

st.markdown(
    '<div class="section-title">🎯 Your Skills & Interests</div>',
    unsafe_allow_html=True,
)

user_input = st.text_input(
    "Enter your skills/interests", placeholder="e.g. Python, Cloud, Machine Learning"
)

st.caption("Enter multiple skills separated by commas.")

st.markdown("### ❄️ New User? Select Your Interests")

st.write("Choose one or more interests to get started:")

interest_options = [
    "Python",
    "AI / Machine Learning",
    "Cloud Computing",
    "Web Development",
    "Data Science",
    "DevOps & Automation",
    "Cybersecurity",
    "Backend Development",
    "Frontend Development",
    "Prompt Engineering",
]

interest_skill_mapping = {
    "Python": ["Python"],
    "AI / Machine Learning": ["AI", "Machine Learning", "Deep Learning", "Python"],
    "Cloud Computing": ["Cloud", "AWS", "Azure", "Networking"],
    "Web Development": ["HTML", "CSS", "JavaScript", "Web Development"],
    "Data Science": ["Python", "Machine Learning", "Statistics", "Data Analysis"],
    "DevOps & Automation": [
        "Python",
        "Cloud",
        "Automation",
        "Docker",
        "CI/CD",
        "Linux",
    ],
    "Cybersecurity": ["Networking", "Linux", "Security", "Cybersecurity", "Python"],
    "Backend Development": ["Python", "APIs", "Backend", "SQL", "Databases"],
    "Frontend Development": ["HTML", "CSS", "JavaScript", "React", "UI"],
    "Prompt Engineering": ["Prompt Engineering", "AI", "Python", "LLM"],
}

selected_interests = st.multiselect("Select your interests", interest_options)

# -----------------------------
# Recommendation Button
# -----------------------------
# -----------------------------
# Recommendation Button
# -----------------------------

if st.button("🚀 Get Recommendations", use_container_width=True):

    typed_skills = [skill.strip() for skill in user_input.split(",") if skill.strip()]

    selected_skills = []

    for interest in selected_interests:
        selected_skills.extend(interest_skill_mapping[interest])

    user_skills = typed_skills + selected_skills

    # -----------------------------
    # Cold Start Handling
    # -----------------------------

    if not user_skills:

        st.warning(
            "❄️ Cold Start detected! "
            "Please enter at least one skill or interest "
            "to generate recommendations."
        )

    else:

        data = load_data()

        results = calculate_scores(user_skills, data)

        sorted_results = sort_results(results)

        top_results = filter_top_n(sorted_results, 3)

        # -----------------------------
        # User Preferences
        # -----------------------------

        st.markdown(
            '<div class="section-title">' "📌 Your Selected Skills" "</div>",
            unsafe_allow_html=True,
        )

        st.write(" • ".join(user_skills))
    # -----------------------------
    # All Recommendations
    # -----------------------------

    st.markdown(
        '<div class="section-title">' "📋 All Recommendations" "</div>",
        unsafe_allow_html=True,
    )

    for result in sorted_results:

        score = result["score"]

        if score <= 0:

            st.markdown(
                f"""
                    <div class="recommendation-card">
                        <strong>{result['name']}</strong>
                        <span style="float:right;">
                            No Match
                        </span>
                    </div>
                    """,
                unsafe_allow_html=True,
            )

        else:

            percentage = score * 100

            st.markdown(
                f"""
                    <div class="recommendation-card">
                        <strong>{result['name']}</strong>
                        <span style="float:right;" class="score">
                            {percentage:.0f}% Match
                        </span>
                    </div>
                    """,
                unsafe_allow_html=True,
            )

    # -----------------------------
    # Top 3 Recommendations
    # -----------------------------

    st.markdown(
        '<div class="section-title">' "🏆 Top 3 Recommendations" "</div>",
        unsafe_allow_html=True,
    )

    for index, result in enumerate(top_results, start=1):

        percentage = result["score"] * 100

        st.markdown(
            f"""
                <div class="top-card">
                    <strong>
                        {index}. {result['name']}
                    </strong>
                    <span style="float:right;">
                        {percentage:.0f}% Match
                    </span>
                </div>
                """,
            unsafe_allow_html=True,
        )

    # -----------------------------
    # Methodology
    # -----------------------------

    st.markdown(
        """
            <div class="info-box">
                <strong>💡 How it works</strong><br>
                Recommendations are generated using
                <strong>TF-IDF</strong> feature weighting and
                <strong>Cosine Similarity</strong>.
                Results are then sorted and filtered to provide
                the Top 3 matches.
            </div>
            """,
        unsafe_allow_html=True,
    )


# -----------------------------
# Footer
# -----------------------------

st.markdown("---")

st.caption("AI Recommendation Logic • DecodеLabs Project 3")
