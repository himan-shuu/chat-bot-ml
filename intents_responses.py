import random

responses = {
    'greeting': ["Hello!", "Hi there!", "Hey! How can I help you?"],
    'goodbye': ["Goodbye!", "See you later!", "Take care!"],
    'thanks': ["You're welcome!", "No problem!", "Glad I could help!"],
    'weather': ["I’m not sure right now, check a weather app!"],
    'time': ["I don't have a clock, but your device can tell you!"],
    'mood': ["I'm good, thanks for asking! How about you?"],
    'joke': ["Why did the computer go to the doctor? Because it caught a virus!", "I told a joke to a chatbot once, it didn’t laugh!"],
    'help': ["Sure! What do you need help with?", "I’m here to assist you!"],
    # Add more intent responses if needed
}

def get_response(intent):
    return random.choice(responses.get(intent, ["I'm not sure I understand."]))
