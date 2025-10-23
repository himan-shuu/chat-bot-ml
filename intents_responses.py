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
    ]
}

def get_response(intent):
    return random.choice(responses.get(intent, ["I'm not sure I understand."]))
