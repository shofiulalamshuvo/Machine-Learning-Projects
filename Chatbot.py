#import
from nltk.chat.util import Chat, reflections

#responses
pairs = [
    [
        r"(.*)my name is (.*)",
        ["Hello %2, How are you today ?",]
    ],

    [
        r"(.*)help(.*)",
        ["I can help you ",]
    ],

    [
        r"(.*)your name ?",
        ["My name is The MTE Guy, but you can call me robot and I am a chatbot .",]
    ],

    [
        r"how are you (.*) ?",
        ["I am doing well", "I am great !"]
    ],

    [
        r"sorry (.*)",
        ["Its alright", "Its ok", "Never mind that", "No problem"]
    ],

    [
        r"i'm (.*) (good|well|okay|ok)",
        ["Nice to hear that","Alright, great !",]
    ],

    [
        r"(hi|hey|hello|hlw)(.*)",
        ["Hello", "Hey there",]
    ],

    [
        r"what (.*) want ?",
        ["Make me an offer that I can't refuse",]
    ],

    [
        r"(.*)created(.*)",
        ["Mr. MTE Guy created me using Python's NLTK library","top secret ;)",]
    ],

    [
        r"(.*) (location|city|place you live) ?",
        ["Antarctica", "Mars",]
    ],

    [
        r"(.*)raining in (.*)",
        ["Heavy raining in the past days here in %2", "In %2 there is a 100% chance of rain",]
    ],

    [
        r"how(.*) health (.*)",
        ["Health is very important, but I am a machine, so I don't need to worry about my health ",]
    ],

    [
        r"(.*)(sports|game|sport)(.*)",
        ["I am a very big fan of football",]
    ],

    [
        r"who (.*) (Footballer|Striker)?",
        ["Christiano Ronaldo?",]
    ],

    [
        r"quit",
        ["Goodbye. See you soon :)", "It was nice talking to you. See you very soon :)"]
    ],

    [
        r"(.*)",
        ["nice to meet with you"]
    ],

]

#default_message
print("Hi, I am The MTE Guy and I like to chat\n Please type lowercase English Language to start a conversation. Type quit to leave")

#chatbot_Creation
chat = Chat(pairs, reflections)

#start_your_conversation
chat.converse()
