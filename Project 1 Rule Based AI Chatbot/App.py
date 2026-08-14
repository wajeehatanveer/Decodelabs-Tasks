import streamlit as st
from Chatbot import get_response

# Page Configuration

st.set_page_config(
    page_title="Rulebot AI Chatbot",
    page_icon="🤖",
    layout="centered"
)


# Custom Styling

st.markdown("""
<style>

.main {
    background-color: #0e1117;
}

.title {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    margin-bottom: 30px;
}

</style>
""", unsafe_allow_html=True)


# Header

st.markdown(
    '<div class="title">🤖 Rulebot AI Chatbot</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Rule-Based Artificial Intelligence Assistant</div>',
    unsafe_allow_html=True
)


# Get User Name

if "name" not in st.session_state:

    name = st.text_input(
        "👤 Enter your name:",
        placeholder="Enter your name..."
    )

    if name:
        st.session_state.name = name
        st.session_state.messages = []

        st.success(
            f"Hello, {name}! Nice to meet you. 😊"
        )

else:

    name = st.session_state.name


# Chat Interface

if "name" in st.session_state:

    st.divider()

    st.subheader("💬 Chat with Rulebot")

    # Display previous messages
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:

        with st.chat_message(message["role"]):
            st.write(message["content"])


    # User Input
    user_input = st.chat_input(
        "Type your message..."
    )

    if user_input:

        # Display user message
        st.session_state.messages.append({
            "role": "user",
            "content": user_input
        })

        with st.chat_message("user"):
            st.write(user_input)


        # Get Rulebot response
        response, should_exit = get_response(
            user_input,
            name
        )


        # Display bot response
        st.session_state.messages.append({
            "role": "assistant",
            "content": response
        })

        with st.chat_message("assistant"):
            st.write(response)


# Sidebar

with st.sidebar:

    st.title("🤖 Rulebot")

    st.write(
        "A simple rule-based AI chatbot "
        "built using Python."
    )

    st.divider()

    st.subheader("💡 Try asking:")

    st.write("• Hello")
    st.write("• How are you")
    st.write("• What is AI")
    st.write("• What is Python")
    st.write("• Who are you")
    st.write("• Help")

    st.divider()

    if st.button("🗑️ Clear Chat"):

        st.session_state.messages = []

        st.rerun()