from core.commands import *


def process_command(command):

    command = command.lower()

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

    elif command == "hello":
        return "Hello Pradeepp! 👋"

    elif "how are you" in command:
        return "I'm doing great! 😄"

    elif "bye" in command:
        return "See you later! 👋"

    return "Sorry, I don't understand that yet."