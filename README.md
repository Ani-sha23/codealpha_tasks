# Personal Portfolio Website
 '''Create a personal portfolio showcasing your skills,projects, and resume. Use HTML for structure, CSS for styling, and add a touch of JavaScript forinteractivity.Basic ChatbotCreate a text-based chatbot that can have
 conversations with users. You can use natural language processing libraries like NLTK or spaCy to make your chatbot more conversational.'''
python
import random
import nltk
from nltk.chat.util import Chat, reflections

# Define the patterns and responses for the chatbot
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"what is your name ?",
        ["My name is ChatBot, how can I assist you?",]
    ],
    [
        r"how are you ?",
        ["I am doing well, thank you for asking!", "I'm great, how about you?",]
    ],
    [
        r"what is your age ?",
        ["I am an AI, so I don't have an age.", "I am a chatbot, I don't age.",]
    ],
    [
        r"what (.*) you (.*) ?",
        ["I can't do that, I'm just a chatbot.", "I'm sorry, I can't %2.",]
    ],
    [
        r"quit",
        ["Bye! Take care.", "It was nice talking to you. Goodbye!",]
    ],
    [
        r"(.*)",
        ["That's interesting. Tell me more.", "I see. Can you elaborate?", "I understand.",]
    ]
]

# Define the reflections dictionary for handling user input
reflections = {
    "i am": "you are",
    "i was": "you were",
    "i": "you",
    "my": "your",
    "you are": "I am",
    "you were": "I was",
    "you": "I",
    "your": "my",
}

# Create the chatbot using the Chat class from NLTK
chatbot = Chat(pairs, reflections)

# Start the conversation
print("Hi, I'm ChatBot. How can I help you today?")
chatbot.converse()


Explanation:

1. Import necessary libraries:
   - random for generating random responses.
   - nltk for natural language processing, specifically the Chat class for chatbot functionality.
   - nltk.chat.util for the reflections dictionary to handle user input variations.

2. Define patterns and responses:
   - pairs is a list of lists, where each inner list represents a pattern-response pair.
   - Patterns use regular expressions to match user input.
   - Responses can be a list of strings, allowing for variations.

3. Define reflections:
   - reflections is a dictionary mapping common user input variations to their corresponding replacements.
   - This helps make the chatbot more conversational by handling different ways of expressing the same meaning.

4. Create the chatbot:
   - chatbot = Chat(pairs, reflections) creates an instance of the Chat class, passing in the patterns and reflections.

5. Start the conversation:
   - print("Hi, I'm ChatBot. How can I help you today?") prints a greeting message.
   - chatbot.converse() starts the conversation loop, where the chatbot will listen to user input, match it to patterns, and provide responses.

How to run the code:

1. Install NLTK:
   bash
   pip install nltk
   
2. Download NLTK data:
   python
   import nltk
   nltk.download('punkt')  # for sentence tokenization
   nltk.download('averaged_perceptron_tagger')  # for part-of-speech tagging
   
3. Run the Python code:
   bash
   python chatbot.py
   

Now you can interact with the chatbot in the terminal. 
