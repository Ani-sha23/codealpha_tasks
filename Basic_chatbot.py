import nltk
import random
import string

from nltk.chat.util import Chat, reflections
nltk.download('punkt')

# Define pairs for conversation
pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hi there!", "Hey! How can I help you?"]
    ],
    [
        r"how are you?",
        ["I'm just a bot, but I'm doing well!", "All good here. How about you?"]
    ],
    [
        r"what is your name?",
        ["I'm a basic chatbot.", "You can call me ChatBuddy."]
    ],
    [
        r"what do you do?",
        ["I can chat with you and answer simple questions.", "I'm here to talk to you!"]
    ],
    [
        r"(.*) your favorite (color|food|movie)?",
        ["I don't have preferences, I'm a bot!", "Bots don't eat or watch movies, but I like talking to you!"]
    ],
    [
        r"bye|exit|quit",
        ["Goodbye!", "See you soon!", "Have a great day!"]
    ],
    [
        r"(.*)",
        ["Interesting...", "Tell me more.", "That's nice!", "I see."]
    ]
]

# Create and start chat
def chatbot():
    print("ChatBot: Hi! Type 'bye' or 'quit' to end the conversation.")
    chat = Chat(pairs, reflections)
    chat.converse()

chatbot()
