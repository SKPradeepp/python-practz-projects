from core.commands import *
from core.memory import remember, recall

def process_command(command):

    command = command.lower().strip()
    command = command.replace(".", "")
    command = command.replace(",", "")
    command = command.replace("!", "")
    command = command.replace("?", "")
    if "open notepad" in command:
        open_notepad()
        return "Opening Notepad..."

    elif "open calculator" in command:
        open_calculator()
        return "Opening Calculator..."

    elif "time" in command:
        return f"The current time is {get_time()}."

    elif "date" in command:
        return f"Today's date is {get_date()}."

    elif "hello" in command or "hi" in command:
        return "Hello Pradeepp! 👋"

    elif "howareyou" in command:
        return "I'm doing great! 😄"

    elif "bye" in command:
        return "See you later! 👋"
    
    elif "remember" in command:

        text = command.replace("remember", "").strip()

        if " is " in text:

            key, value = text.split(" is ", 1)

            remember(key.strip(), value.strip())

            return "Okay! I'll remember that."

        return "Tell me what to remember."

    elif "what is my" in command:

        key = command.replace("what is my", "").strip()

        value = recall(key)

        if value:

            return f"Your {key} is {value}."

        return "I don't know that yet."

    return "Sorry, I don't understand that yet."