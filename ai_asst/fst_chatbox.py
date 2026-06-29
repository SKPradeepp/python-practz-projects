import random
from datetime import datetime

bot_name = "Pradeep AI"

greetings = ["Hi!", "Hello!", "Hey!"]

happy_words = ["good", "great", "awesome", "nice"]
sad_words = ["sad", "bad", "upset", "angry"]

memory = []

while True:

    user = input("You: ").lower()

    memory.append(user)

    if user in ["hello", "hi", "hey"]:

        print(bot_name + ":", random.choice(greetings))

    elif "name" in user:

        print(bot_name + ": My name is", bot_name)

    elif "time" in user:

        current_time = datetime.now().strftime("%H:%M:%S")

        print(bot_name + ": Current time is", current_time)

    elif "python" in user:

        print(bot_name + ": Python is powerful for AI!")

    elif "ai" in user:

        print(bot_name + ": AI means Artificial Intelligence.")

    elif any(word in user for word in happy_words):

        print(bot_name + ": I'm happy you're feeling good!")

    elif any(word in user for word in sad_words):

        print(bot_name + ": Hope things get better soon.")

    elif "memory" in user:

        print(bot_name + ": You previously said:")

        for msg in memory[-5:]:
            print("-", msg)

    elif "bye" in user:

        print(bot_name + ": Goodbye!")
        break

    else:

        responses = [
            "Interesting!",
            "Tell me more.",
            "That's cool!",
            "I understand."
        ]

        print(bot_name + ":", random.choice(responses))