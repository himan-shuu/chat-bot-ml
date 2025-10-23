import streamlit as st
import pickle
import re
from intents_responses import get_response

# Load model & vectorizer
clf = pickle.load(open("model/logistic.pkl", "rb"))
vectorizer = pickle.load(open("model/vectorizer.pkl", "rb"))

# Preprocess function
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return text

# Streamlit UI
st.set_page_config(page_title="ML Chatbot 🤖", page_icon="🤖")
st.title("🤖 ML-Powered Chatbot")
st.write("Type your message below:")

# Maintain chat history
if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.text_input("You:", "")

if st.button("Send") and user_input:
    processed = preprocess_text(user_input)
    vec = vectorizer.transform([processed])
    intent = logistic.predict(vec)[0]
    response = get_response(intent)

    st.session_state.history.append(("You", user_input))
    st.session_state.history.append(("Bot", response))

# Display chat history
for sender, msg in st.session_state.history:
    st.markdown(f"**{sender}:** {msg}")
