import streamlit as st
import tempfile
import os

from recognition import preprocess_image, extract_text


st.set_page_config(
    page_title="Machine's Optic Nerve",
    page_icon="🔍",
    layout="wide"
)


# ---------- Custom CSS ----------
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
            font-size: 18px;
            margin-bottom: 35px;
        }

        .info-card {
            padding: 22px;
            border-radius: 14px;
            border: 1px solid rgba(128, 128, 128, 0.25);
            margin-bottom: 20px;
        }

        .section-title {
            font-size: 24px;
            font-weight: 600;
            margin-bottom: 12px;
        }

        .stButton > button {
            width: 100%;
            border-radius: 10px;
            font-weight: 600;
            padding: 10px;
        }
    </style>
    """,
    unsafe_allow_html=True
)


# ---------- Header ----------
st.markdown(
    '<div class="main-title">🔍 Building the Machine\'s Optic Nerve</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'AI-powered Image & Text Recognition using OpenCV and Tesseract OCR'
    '</div>',
    unsafe_allow_html=True
)


# ---------- Information Cards ----------
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        '<div class="info-card">'
        '<b>🖼️ Image Processing</b><br>'
        'Grayscale, Gaussian Blur & Adaptive Thresholding'
        '</div>',
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        '<div class="info-card">'
        '<b>🔎 OCR Recognition</b><br>'
        'Extract text using Tesseract OCR'
        '</div>',
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        '<div class="info-card">'
        '<b>📊 Confidence Filter</b><br>'
        'Display results with 80%+ confidence'
        '</div>',
        unsafe_allow_html=True
    )


# ---------- Upload ----------
st.markdown(
    '<div class="section-title">📤 Upload Your Image</div>',
    unsafe_allow_html=True
)

uploaded_file = st.file_uploader(
    "Choose an image for text recognition",
    type=["png", "jpg", "jpeg", "webp", "jfif"]
)


if uploaded_file is not None:

    st.markdown("### 🖼️ Image Preview")

    st.image(
        uploaded_file,
        caption="Uploaded Image",
        use_container_width=True
    )

    if st.button("🔍 Recognize Text"):

        with st.spinner("Processing image and extracting text..."):

            temp_file = tempfile.NamedTemporaryFile(
                delete=False,
                suffix=os.path.splitext(uploaded_file.name)[1]
            )

            temp_file.write(uploaded_file.getvalue())
            temp_file.close()

            try:
                processed_image = preprocess_image(temp_file.name)

                results = extract_text(processed_image)

                st.markdown("### 📝 Extracted Text")

                if results:

                    extracted_text = " ".join(
                        result["text"] for result in results
                    )

                    st.text_area(
                        "High-confidence text",
                        extracted_text,
                        height=180
                    )

                    st.markdown("### 📊 Confidence Scores")

                    for result in results:
                        st.write(
                            f"**{result['text']}** — "
                            f"{result['confidence']:.2f}%"
                        )

                else:
                    st.warning(
                        "No text with 80% or higher confidence was detected."
                    )

            finally:
                os.remove(temp_file.name)

