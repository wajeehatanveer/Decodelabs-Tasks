from colorama import Fore, init

init(autoreset=True)

# Knowledge Base
responses = {

    "hi": "Hello {name}! How can I assist you today? 😊",

    "hello": "Hello {name}! How can I assist you today? 😊",

    "hey": "Hey {name}! Nice to see you! 😊",

    "assalam u alaikum":
        "Wa alaikum assalam, {name}! How can I assist you today? 😊",

    "how are you":
        "I am just a chatbot, but I'm functioning well! How about you? 😊",

    "what is your name":
        "I am Rulebot, a simple rule-based AI chatbot.",

    "who are you":
        "I am Rulebot, a rule-based chatbot built using Python. 🤖",

    "who created you":
        "I was created by Wajeeha using Python to build a simple rule-based chatbot. 😊",

    "what can you do":
        "I can answer basic questions about AI, Python, greetings, and other predefined queries.",

    "what is ai":
        "AI stands for Artificial Intelligence. It enables machines to perform tasks that normally require human intelligence.",

    "what is python":
        "Python is a popular programming language used for AI, web development, automation, and data science.",

    "help":
        "You can ask me about AI, Python, greetings, or my basic information.",

    "thank you":
        "You're welcome! Happy to help. 😊",

    "thanks":
        "You're welcome! Happy to help. 😊",

    "good morning":
        "Good morning, {name}! I hope you have a fantastic day ahead. 🌞",

    "good afternoon":
        "Good afternoon, {name}! 😊",

    "good evening":
        "Good evening, {name}! 🌆",

    "good night":
        "Good night, {name}! Sleep well and have sweet dreams. 🌙"
}


# Fallback
fallback = (
    "I'm sorry, I didn't understand that. "
    "Please try another question or type 'help'."
)


def get_response(user_input, name):
    """
    Process user input using the rule-based knowledge base.
    """

    # Sanitization
    clean_input = user_input.lower().strip()

    # Exit commands
    if clean_input in ["bye", "exit", "quit", "by"]:
        return (
            f"Goodbye {name}! It was nice talking to you. "
            "Have a great day! 👋"
        ), True

    # Dictionary lookup + fallback
    reply = responses.get(clean_input, fallback)

    return reply.format(name=name), False