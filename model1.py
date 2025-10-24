import streamlit as st
import pickle
import re
import random
import sys
import os

# -------------------------------
# Load trained model & vectorizer
# -------------------------------

# Define the relative path based on the structure (e.g., inside 'model' directory)
MODEL_PATH = "model/logistic.pkl"
VECTORIZER_PATH = "model/vectorizer.pkl"

try:
    # Attempt to load the real models from the expected paths
    with open(MODEL_PATH, "rb") as f:
        logistic = pickle.load(f)
    
    with open(VECTORIZER_PATH, "rb") as f:
        vectorizer = pickle.load(f)
    
    # Indicate success if models loaded
    st.success(f"✅ Successfully loaded ML model from {MODEL_PATH} and {VECTORIZER_PATH}.")
    
except FileNotFoundError:
    # If files are not found, display an error and halt the application
    st.error(f"❌ Error: Model files not found at {MODEL_PATH} or {VECTORIZER_PATH}.")
    st.warning("Please ensure your 'logistic.pkl' and 'vectorizer.pkl' are placed inside a 'model/' directory in your project structure.")
    sys.exit()
except (EOFError, pickle.UnpicklingError):
    # Handle corrupted or invalid pickle files
    st.error("❌ Error loading the pickled model or vectorizer. Check file integrity.")
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
# Intent-based responses (EXPANDED)
# -------------------------------
responses = {
    # General Intents (From original snippet)
    'greeting': ["Hello! Welcome to our service. How can I assist you today?", "Hi there! What can I do for you?", "Hey! I'm ready to chat."],
    'goodbye': ["Goodbye! Have a great day.", "See you later! Take care.", "I'm always here if you need me. Bye for now!"],
    'thanks': ["You're very welcome! Is there anything else I can help with?", "No problem at all!", "Glad I could help! That's what I'm here for."],
    'joke': ["Why did the computer go to the doctor? Because it caught a virus!", "What do you call a fake noodle? An Impasta."],
    'name': ["I’m your friendly ML-powered chatbot, here to help with your inquiries."],
    'how_are_you': ["I’m doing well, running smoothly! How about you?", "All good here in the digital world! How can I improve your day?"],
    'help': ["I can answer questions about orders, accounts, technical issues, and even tell jokes!", "I’m here to help you navigate our services."],

    # Customer Service Intents (From CSV analysis)
    'cancellation': [
        "I can certainly help you with your cancellation request. Could you please confirm the **item or service** you wish to cancel?",
        "To cancel your subscription/order, please provide your **order number or account ID**.",
        "Cancelling? I understand. Let's start the **cancellation process** now. What are you cancelling?"
    ],
    'password_reset': [
        "Need to reset your password? I can guide you through the process. Please confirm your **username or registered email**.",
        "No worries, password resets happen! I'll send a **password recovery link** immediately.",
        "I'll guide you through the **password recovery** process. Have you checked your spam folder recently?"
    ],
    'account_help': [
        "I can help with account issues! Are you having trouble with **login, profile settings, or verification**?",
        "What specific **account assistance** do you require today?",
        "Let's look into your account. Tell me more about the **problem** you're encountering."
    ],
    'return_request': [
        "I'm sorry to hear you need to make a return. Please provide your **order ID** to check the return eligibility and policy.",
        "To start a return, I'll need your **tracking or order number**. Please share that with me.",
        "We'll process that return for you. Do you have the **original packaging**?"
    ],
    'business_hours': [
        "Our current business hours are **Monday to Friday, 9:00 AM to 5:00 PM** local time.",
        "We are generally open from **9 AM to 5 PM** on weekdays, excluding public holidays.",
        "Our customer support team is available during **standard business hours**."
    ],
    'order_status': [
        "I can check on your order. What is your **order number** or **tracking ID**?",
        "Please share the **tracking number** or **order ID** so I can find the current status of your package.",
        "Checking your package status now! I just need the **order details**."
    ],
    'payment_update': [
        "I can help you update your payment information. I will securely link you to the **payment portal**.",
        "You want to update your card details? I'll need to verify your **account** first.",
        "Changing your payment method is easy. I'll provide a **secure link** to manage your billing details."
    ],
    'service_info': [
        "We offer a wide range of services including **technical support, order tracking, returns, and account management**.",
        "What kind of **service** are you interested in learning more about today?",
        "You can find all our detailed service descriptions on our **main website's 'Services' page**."
    ],
    'technical_support': [
        "I can connect you with **technical support**. Could you briefly describe the issue you are facing?",
        "For technical issues, I recommend visiting our **FAQ and troubleshooting page** first.",
        "Technical support is on standby! What seems to be the **problem** with the service or product?"
    ]
}

def get_response(intent):
    """Retrieves a random response based on the predicted intent."""
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

# Function to handle prediction and response generation
def handle_input():
    user_input = st.session_state.input
    if user_input:
        processed = preprocess_text(user_input)
        
        # Use the real vectorizer and model
        vec = vectorizer.transform([processed]) 
        intent = logistic.predict(vec)[0]
        response = get_response(intent)

        # Save to history
        st.session_state.history.append(("You", user_input, intent))
        st.session_state.history.append(("Bot", response, None))
        
        # Clear input box
        st.session_state.input = ""

# Text input and Send button wrapped in a form for better submission handling
with st.form(key='chat_form', clear_on_submit=True):
    col1, col2 = st.columns([4, 1])
    with col1:
        user_input = st.text_input("Your Message:", "", key="input_text_field", placeholder="Ask me anything...", label_visibility="collapsed")
    with col2:
        send_button = st.form_submit_button("Send")

    if send_button and user_input:
        st.session_state.input = user_input # Manually set state for processing
        processed = preprocess_text(user_input)
        
        # Use the real vectorizer and model
        vec = vectorizer.transform([processed]) 
        intent = logistic.predict(vec)[0]
        response = get_response(intent)

        # Save to history
        st.session_state.history.append(("You", user_input, intent))
        st.session_state.history.append(("Bot", response, None))
        
        # Note: input_text_field is cleared by clear_on_submit=True in the form

# Display chat history
st.subheader("Chat History")
st.markdown('<div class="chat-container">', unsafe_allow_html=True)

for sender, msg, intent in st.session_state.history:
    if sender == "You":
        # Displaying the predicted intent for the user's message is helpful for debugging/demo
        st.markdown(f'<div class="chat-message-you">**You:** {msg} <br><small style="color:#80DEEA;">*Intent: {intent}*</small></div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="chat-message-bot">**Bot:** {msg}</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Run handle_input() if the text field was populated and enter key was pressed, but we use the form submit now.
# st.text_input("", on_change=handle_input, key="input", label_visibility="collapsed")
