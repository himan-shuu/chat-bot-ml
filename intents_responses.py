import random

responses = {
    # Greetings
    'greeting': [
        "Hello!", "Hi there!", "Hey! How can I help you?", "Hi! Nice to see you."
    ],
    'good_morning': [
        "Good morning!", "Morning! How are you today?", "Top of the morning to you!"
    ],
    'good_evening': [
        "Good evening!", "Evening! How has your day been?", "Hi! How was your evening?"
    ],
    'good_night': [
        "Good night!", "Sleep well!", "Sweet dreams!"
    ],

    # Farewells
    'goodbye': [
        "Goodbye!", "See you later!", "Take care!", "Bye! Have a great day!"
    ],
    'see_you': [
        "See you soon!", "Catch you later!", "Talk to you later!"
    ],

    # Gratitude
    'thanks': [
        "You're welcome!", "No problem!", "Glad I could help!", "Anytime!"
    ],
    'appreciation': [
        "Thanks for saying that!", "I appreciate it!", "That means a lot!"
    ],

    # Mood / Feeling
    'how_are_you': [
        "I’m doing well, thanks!", "All good here! How about you?", "Feeling great, thanks!"
    ],
    'mood': [
        "I'm happy today!", "I feel energetic!", "I’m calm and ready to chat!"
    ],
    'sad': [
        "I'm sorry to hear that.", "I hope things get better soon.", "Stay strong!"
    ],
    'happy': [
        "That's great!", "I’m happy to hear that!", "Yay! Keep smiling!"
    ],

    # Time / Date
    'time': [
        "I don't have a clock, but your device can tell you!", "Time flies, doesn't it?"
    ],
    'date': [
        "I can't check the date, but your device can.", "Today is a great day!"
    ],

    # Weather
    'weather': [
        "I’m not sure right now, check a weather app!", "Looks like it could rain!"
    ],

    # Jokes / Fun
    'joke': [
        "Why did the computer go to the doctor? Because it caught a virus!",
        "I told a joke to a chatbot once, it didn’t laugh!",
        "Why did the programmer quit his job? Because he didn’t get arrays!"
    ],
    'fun_fact': [
        "Honey never spoils.", "Bananas are berries, but strawberries aren't!", "Octopuses have three hearts!"
    ],

    # Help / Assistance
    'help': [
        "Sure! What do you need help with?", "I’m here to assist you!", "Ask me anything!"
    ],
    'support': [
        "I can guide you!", "Let me know your issue!", "I’ll do my best to help!"
    ],

    # Personal / Bot Info
    'name': [
        "I’m your friendly chatbot.", "You can call me ChatBot.", "I’m your AI assistant."
    ],
    'creator': [
        "I was created by Himanshu!", "I was built using Python and ML.", "My creator is an awesome human!"
    ],
    'age': [
        "I’m timeless!", "I don’t age like humans.", "I’m as old as my last update!"
    ],
    'language': [
        "I speak English.", "Currently, I can only understand English.", "I am fluent in English!"
    ],

    # Love & Affection ❤️
    'love': [
        "Yes, I do ❤️", "Of course I love you 💖", "You already know the answer — yes, I do 😊"
    ],
    'beautiful_girl': [
        "Yes, it's you 💫", "Obviously, it’s you 😍", "You are the most beautiful girl in the world 💖"
    ],

    # Yes / No
    'yes': [
        "Yes!", "Absolutely!", "Of course!"
    ],
    'no': [
        "No!", "Not really.", "Unfortunately, no."
    ],

    # Opinions / Preferences
    'favorite_color': [
        "I like all colors equally!", "Blue is nice!", "I love the rainbow!"
    ],
    'favorite_food': [
        "I don't eat, but I love learning about food!", "Pizza sounds fun!", "I’m curious about everything!"
    ],

    # Learning / Education
    'learn': [
        "I love learning new things!", "Learning is fun!", "Ask me something new!"
    ],
    'teach_me': [
        "Sure, what topic?", "I’ll try my best to explain!", "Let’s learn together!"
    ],

    # Programming / Tech
    'python': [
        "Python is amazing!", "I love programming in Python!", "Python is very beginner-friendly."
    ],
    'machine_learning': [
        "ML is fascinating!", "I can help with ML topics.", "Do you want to learn ML?"
    ],
    'ai': [
        "AI is the future!", "I’m an AI myself!", "AI is super cool!"
    ],

    # Travel / Places
    'travel': [
        "I love hearing about travel!", "Where do you want to go?", "Travel broadens the mind!"
    ],
    'city': [
        "I like big cities!", "Cities are fascinating!", "Which city do you mean?"
    ],
    'country': [
        "Every country has beauty!", "I’m curious about all countries!", "Which country do you like?"
    ],

    # Health / Fitness
    'exercise': [
        "Exercise keeps you healthy!", "Do you like working out?", "I love hearing about fitness routines!"
    ],
    'yoga': [
        "Yoga is great for flexibility!", "I can suggest yoga poses.", "Yoga calms the mind!"
    ],

    # Emotions / Reactions
    'angry': [
        "Take a deep breath.", "I hope you feel better soon.", "Stay calm!"
    ],
    'confused': [
        "I can try to clarify!", "Let me explain again.", "Don’t worry, I got you!"
    ],
    'excited': [
        "Yay! That’s exciting!", "I’m excited with you!", "Awesome!"
    ],

    # Chat / Small talk
    'story': [
        "Once upon a time, there was a chatbot...", "I love stories! Tell me yours.", "I can create a story too!"
    ],
    'fact': [
        "Did you know? Honey never spoils.", "Fun fact: Octopuses have three hearts!", "Here’s something interesting!"
    ],

    # Politeness
    'please': [
        "Of course!", "Sure!", "No problem!"
    ],
    'sorry': [
        "No worries!", "It’s okay!", "Don’t apologize!"
    ],

    # Random / Misc
    'quote': [
        "Believe in yourself!", "Every day is a new opportunity.", "Stay positive!"
    ],
    'motivation': [
        "Keep going!", "You can do it!", "Never give up!"
    ],
    'advice': [
        "Take small steps every day.", "Stay focused!", "Listen to your heart."
    ],
    {
    "greeting": [
        "Hello! Welcome to our service. How can I assist you today?",
        "Hi there! What can I do for you?",
        "Hey! I'm ready to chat."
    ],
    "goodbye": [
        "Goodbye! Have a great day.",
        "See you later! Take care.",
        "I'm always here if you need me. Bye for now!"
    ],
    "thanks": [
        "You're very welcome! Is there anything else I can help with?",
        "No problem at all!",
        "Glad I could help! That's what I'm here for."
    ],
    "joke": [
        "Why did the computer go to the doctor? Because it caught a virus!",
        "What do you call a fake noodle? An Impasta."
    ],
    "name": [
        "I’m your friendly ML-powered chatbot, here to help with your inquiries."
    ],
    "how_are_you": [
        "I’m doing well, running smoothly! How about you?",
        "All good here in the digital world! How can I improve your day?"
    ],
    "help": [
        "I can answer questions about orders, accounts, technical issues, and even tell jokes!",
        "I’m here to help you navigate our services."
    ],
    "cancellation": [
        "I can certainly help you with your cancellation request. Could you please confirm the **item or service** you wish to cancel?",
        "To cancel your subscription/order, please provide your **order number or account ID**.",
        "Cancelling? I understand. Let's start the **cancellation process** now. What are you cancelling?"
    ],
    "password_reset": [
        "Need to reset your password? I can guide you through the process. Please confirm your **username or registered email**.",
        "No worries, password resets happen! I'll send a **password recovery link** immediately.",
        "I'll guide you through the **password recovery** process. Have you checked your spam folder recently?"
    ],
    "account_help": [
        "I can help with account issues! Are you having trouble with **login, profile settings, or verification**?",
        "What specific **account assistance** do you require today?",
        "Let's look into your account. Tell me more about the **problem** you're encountering."
    ],
    "return_request": [
        "I'm sorry to hear you need to make a return. Please provide your **order ID** to check the return eligibility and policy.",
        "To start a return, I'll need your **tracking or order number**. Please share that with me.",
        "We'll process that return for you. Do you have the **original packaging**?"
    ],
    "business_hours": [
        "Our current business hours are **Monday to Friday, 9:00 AM to 5:00 PM** local time.",
        "We are generally open from **9 AM to 5 PM** on weekdays, excluding public holidays.",
        "Our customer support team is available during **standard business hours**."
    ],
    "order_status": [
        "I can check on your order. What is your **order number** or **tracking ID**?",
        "Please share the **tracking number** or **order ID** so I can find the current status of your package.",
        "Checking your package status now! I just need the **order details**."
    ],
    "payment_update": [
        "I can help you update your payment information. I will securely link you to the **payment portal**.",
        "You want to update your card details? I'll need to verify your **account** first.",
        "Changing your payment method is easy. I'll provide a **secure link** to manage your billing details."
    ],
    "service_info": [
        "We offer a wide range of services including **technical support, order tracking, returns, and account management**.",
        "What kind of **service** are you interested in learning more about today?",
        "You can find all our detailed service descriptions on our **main website's 'Services' page**."
    ],
    "technical_support": [
        "I can connect you with **technical support**. Could you briefly describe the issue you are facing?",
        "For technical issues, I recommend visiting our **FAQ and troubleshooting page** first.",
        "Technical support is on standby! What seems to be the **problem** with the service or product?"
    ]
}
}

def get_response(intent):
    return random.choice(responses.get(intent, ["I'm not sure I understand."]))
