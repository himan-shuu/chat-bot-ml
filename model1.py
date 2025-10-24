import streamlit as st
import pickle
import re
import random
import sys
import os
import json

# --- File Paths ---
MODEL_PATH = "model/logistic.pkl"
VECTORIZER_PATH = "model/vectorizer.pkl"
RESPONSES_PATH = "responses.json" # Path for external response file

# -------------------------------
# Load trained model, vectorizer, and responses
# -------------------------------

try:
    # Attempt to load the real models
    with open(MODEL_PATH, "rb") as f:
        logistic = pickle.load(f)
    
    with open(VECTORIZER_PATH, "rb") as f:
        vectorizer = pickle.load(f)
    
    # Load responses from external JSON file
    with open(RESPONSES_PATH, "r") as f:
        responses = json.load(f)
    
    # Indicate success if models loaded
    st.success(f"✅ Successfully loaded ML model, vectorizer, and responses.")
    
except FileNotFoundError as e:
    # If any file is not found, display an error and halt the application
    st.error(f"❌ Error: Required file not found: {e.filename}. Please check your file paths.")
    st.warning("Ensure 'logistic.pkl' and 'vectorizer.pkl' are in a 'model/' folder and 'responses.json' is in the root directory.")
    sys.exit()
except (EOFError, pickle.UnpicklingError):
    # Handle corrupted or invalid pickle files
    st.error("❌ Error loading the pickled model or vectorizer. Check file integrity.")
    sys.exit()
except json.JSONDecodeError:
    # Handle error in JSON file structure
    st.error("❌ Error loading responses: 'responses.json' file is corrupted or improperly formatted.")
    sys.exit()

# -------------------------------
# Preprocess function
# -------------------------------
def preprocess_text(text):
    """Cleans the input text for vectorization."""
    text = text.lower()
    # Remove non-alphanumeric characters (except spaces)
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return text

# -------------------------------
# Intent-based response retrieval
# -------------------------------
def get_response(intent):
    """Retrieves a random response based on the predicted intent from the loaded dictionary."""
    # The 'responses' dictionary is now loaded globally from the JSON file
    return random.choice(responses.get(intent, ["I'm sorry, I'm not sure how to respond to that intent."]))

# -------------------------------
# Streamlit UI
# -------------------------------
st.set_page_config(page_title="ML Chatbot 🤖", page_icon="🤖", layout="centered")

st.markdown("""
    <style>
        /* General page configuration for dark mode */
        body {
            color: #E0E0E0; /* Light grey text */
            background-color: #1E1E1E; /* Dark background */
        }
        .st-emotion-cache-1jm69d1 { padding-top: 2rem; }
        .stButton>button {
            border: 2px solid #4CAF50;
            color: white;
            background-color: #4CAF50;
            padding: 0.5rem 1rem;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
            border-radius: 8px;
            transition: all 0.3s;
        }
        .stButton>button:hover {
            background-color: #45a049;
            border-color: #45a049;
        }
        /* User Message (You) - Dark mode style */
        .chat-message-you {
            background-color: #004D40; /* Dark Teal background */
            color: #E0E0E0; /* Light text */
            padding: 10px;
            border-radius: 15px 15px 5px 15px;
            margin-bottom: 10px;
            align-self: flex-end;
            width: fit-content;
            max-width: 80%;
            border-left: 5px solid #00BCD4;
        }
        /* Bot Message - Dark mode style */
        .chat-message-bot {
            background-color: #311B92; /* Dark Violet background */
            color: #E0E0E0; /* Light text */
            padding: 10px;
            border-radius: 15px 15px 15px 5px;
            margin-bottom: 10px;
            align-self: flex-start;
            width: fit-content;
            max-width: 80%;
            border-right: 5px solid #7C4DFF;
        }
        /* Chat Container - Dark mode style */
        .chat-container {
            display: flex;
            flex-direction: column;
            gap: 5px;
            max-height: 400px;
            overflow-y: auto;
            padding: 10px;
            /* Using a subtle dark border */
            border: 1px solid #444444; 
            background-color: #2D2D2D; /* Dark grey container background */
            border-radius: 10px;
            margin-bottom: 20px;
        }
        /* Style for the predicted intent text within the user message */
        .chat-message-you small {
            color: #80DEEA !important; /* Lighter color for better visibility */
        }
    </style>
""", unsafe_allow_html=True)

st.title("🤖 ML-Powered Chatbot")
st.markdown("Try asking about **'password reset'**, **'order status'**, or **'business hours'** to see the new customer service responses!")

# Initialize chat history
if "history" not in st.session_state:
    st.session_state.history = []

# Text input and Send button wrapped in a form for better submission handling
with st.form(key='chat_form', clear_on_submit=True):
    col1, col2 = st.columns([4, 1])
    with col1:
        user_input = st.text_input("Your Message:", "", key="input_text_field", placeholder="Ask me anything...", label_visibility="collapsed")
    with col2:
        send_button = st.form_submit_button("Send")

    if send_button and user_input:
        # Manually set state for processing if submitted via button
        st.session_state.input = user_input 
        
        # 1. Preprocess
        processed = preprocess_text(user_input)
        
        # 2. Predict Intent
        vec = vectorizer.transform([processed]) 
        intent = logistic.predict(vec)[0]
        
        # 3. Get Response
        response = get_response(intent)

        # 4. Save to History
        st.session_state.history.append(("You", user_input, intent))
        st.session_state.history.append(("Bot", response, None))
        
        # input_text_field is cleared by clear_on_submit=True in the form

# Display chat history
st.subheader("Chat History")
# Use the custom styled chat container
st.markdown('<div class="chat-container">', unsafe_allow_html=True)

for sender, msg, intent in st.session_state.history:
    if sender == "You":
        # Displaying the predicted intent for the user's message
        st.markdown(f'<div class="chat-message-you">**You:** {msg} <br><small style="color:#80DEEA;">*Intent: {intent}*</small></div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="chat-message-bot">**Bot:** {msg}</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
