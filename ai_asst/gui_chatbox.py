from tkinter import *
import random

root = Tk()

root.title("Pradeep AI Chatbot")
root.geometry("500x500")


def send_message():

    user = user_input.get().lower()

    if user == "":
        return

    chat_area.insert(END, "You: " + user + "\n")

    if user in ["hi", "hello", "hey"]:

        bot = random.choice([
            "Hi!",
            "Hello!",
            "Hey there!"
        ])

    elif "name" in user:

        bot = "My name is Pradeep AI."

    elif "ai" in user:

        bot = "AI stands for Artificial Intelligence."

    elif "python" in user:

        bot = "Python is awesome for AI projects."

    elif "how are you" in user:

        bot = "I'm doing great!"

    elif "bye" in user:

        bot = "Goodbye! Have a great day!"

    else:

        bot = random.choice([
            "Interesting!",
            "Tell me more.",
            "That's cool!",
            "I understand."
        ])

    chat_area.insert(END, "Bot: " + bot + "\n\n")

    user_input.delete(0, END)


root.configure(bg="lightblue")


title_label = Label(
    root,
    text="Pradeep AI Chatbot",
    font=("Arial", 18, "bold"),
    bg="lightblue"
)

title_label.pack(pady=10)


chat_area = Text(
    root,
    height=20,
    width=55,
    font=("Arial", 12)
)

chat_area.pack(pady=10)


user_input = Entry(
    root,
    width=40,
    font=("Arial", 12)
)

user_input.pack(pady=5)


send_button = Button(
    root,
    text="Send",
    font=("Arial", 12),
    command=send_message
)

send_button.pack(pady=5)


root.mainloop()