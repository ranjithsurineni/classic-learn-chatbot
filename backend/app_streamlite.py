import streamlit as st
import numpy as np
import re
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Load FAQ Data
def load_faq_data(filename="data01.json"):
    """Loads FAQ data from a JSON file."""
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)


# Initialize Data
data = load_faq_data()
questions = [item["question"] for item in data]
answers = [item["answer"] for item in data]

# TF-IDF Vectorization
vectorizer = TfidfVectorizer()
question_vectors = vectorizer.fit_transform(questions)


def find_best_match(user_query):
    """Finds the best matching answer for a user query."""
    query_vector = vectorizer.transform([user_query])
    similarities = cosine_similarity(query_vector, question_vectors).flatten()
    
    best_match_index = np.argmax(similarities)
    best_match_score = similarities[best_match_index]
    
    if best_match_score > 0.5:
        return answers[best_match_index]
    
    # Keyword Matching Fallback
    user_keywords = set(re.findall(r'\w+', user_query.lower()))
    best_match = "I'm sorry, I couldn't find an exact answer. Please visit our website for more details."
    max_overlap = 0

    for idx, question in enumerate(questions):
        question_keywords = set(re.findall(r'\w+', question.lower()))
        overlap = len(user_keywords & question_keywords)
        
        if overlap > max_overlap:
            max_overlap = overlap
            best_match = answers[idx]
    
    return best_match


# --- Streamlit App ----------------------------

st.set_page_config( page_title=" Classic Learn Chatbot", page_icon="💬")

# Custom CSS for Styling
st.markdown("""
    <style>
    .main {
        background-color: #d4edda;
    }
    .chat-container {
        border-radius: 10px;
        padding: 10px;
        background: white;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
    }
    .chat-history {
        max-height: 300px;
        overflow-y: auto;
        padding: 10px;
        border-radius: 10px;
    }
            
     /* Change text input field background color */
    div[data-testid="stTextInput"] input {
        background-color: #f0f0f5;  /* Light grey background */
        color: #333333;  /* Dark text */
        border-radius: 8px;
        padding: 10px;
        font-size: 16px;
    }
    </style>
""", unsafe_allow_html=True)


# App Title
st.markdown("<h1 style='text-align: center; color: #2E86C1;'>🤖 Classic Learn Chatbot 💬</h1>", unsafe_allow_html=True)

st.markdown(
    """
    <p style='text-align: center; color: #555;'>Your friendly assistant for Classic Learn queries!</p>
    <p style='text-align: center; color: #555;'>Ask me anything about courses, schedules, and more!</p>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    ### 📝 How to Use:
    1. Type your question in the input box below.  
    2. Click **Enter** or press the **Ask** button.  
    3. The chatbot will provide an answer based on predefined FAQs.  
    4. If no exact match is found, it will suggest the closest relevant answer.  

    ⚡ *Tip: Try asking about courses, schedules, or general Classic Learn queries!*
    """,
    unsafe_allow_html=True
)

# Initialize Session State for Chat History
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# User Input
st.markdown("### Ask me anything about Classic Learn!")
user_input = st.text_input("Enter your question here:", "")

if st.button("Ask"):
    if user_input.strip() != "":
        response = find_best_match(user_input)
        st.session_state.chat_history.append({"user": user_input, "bot": response})
        st.markdown(f"**Bot:** {response}")

# Clear Chat History
if st.button("Clear Chat"):
    st.session_state.chat_history = []
    st.rerun()



# Chat History Display
st.markdown("### Chat History")
with st.container():
    chat_box = st.empty()
    if st.session_state.chat_history:
        chat_box.markdown("<div class='chat-container'><div class='chat-history'>", unsafe_allow_html=True)
        for entry in st.session_state.chat_history:
            st.markdown(f"**You:** {entry['user']}  \n**Bot:** {entry['bot']}", unsafe_allow_html=True)
        chat_box.markdown("</div></div>", unsafe_allow_html=True)
    