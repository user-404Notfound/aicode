import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"hi|hello|hey",
        ["Hello! How can I help you?", "Hi! Nice to meet you."]
    ],
    [
        r"what is your name\??",
        ["My name is AI Chatbot.", "You can call me AI Bot."]
    ],
    [
        r"who are you\??",
        ["I am a simple rule-based chatbot using NLTK."]
    ],
    [
        r"how are you\??",
        ["I am fine, thank you!", "I am doing great."]
    ],
    [
        r"what is your course\??",
        ["I am designed for Computer Engineering students."]
    ],
    [
        r"what is python\??",
        ["Python is a high-level programming language."]
    ],
    [
        r"what is nlp\??",
        ["NLP stands for Natural Language Processing."]
    ],
    [
        r"what can you do\??",
        ["I can answer questions using predefined rules and pattern matching."]
    ],
    [
        r"thank you|thanks",
        ["You're welcome!", "Happy to help."]
    ],
    [
        r"bye|goodbye|exit",
        ["Goodbye! Have a nice day."]
    ],
    [
        r"(.*)",
        ["Sorry, I don't understand that."]
    ]
]

chatbot = Chat(pairs, reflections)

print("================================")
print("       CHATBOT                  ")
print("================================")
print("Type 'bye' or 'exit' to end the chat.\n")

while True:
    user_input = input("> ")

    if user_input.lower() in ["bye", "goodbye", "exit"]:
        print("Goodbye! Have a nice day.")
        break

    response = chatbot.respond(user_input)
    print(response)
