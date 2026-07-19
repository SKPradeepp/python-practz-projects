from core.commands import *
from core.ai_chat import ask_ai
from core.memory import remember, recall
from core.notes import save_note, read_notes
from core.system_utils import take_screenshot, open_screenshot_folder
from core.file_search import find_file
from core.app_launcher import launch_app
from core.web_launcher import open_website
def process_command(command):
    command = command.lower().strip()
    og_command = command
    command = command.replace(".", "")
    command = command.replace(",", "")
    command = command.replace("!", "")
    command = command.replace("?", "")
    if any(word in command for word in ["open", "launch", "start"]):

        target = command

        remove_words = [
        "please",
        "can",
        "could",
        "you",
        "me",
        "open",
        "launch",
        "start"
    ]

        for word in remove_words:
            target = target.replace(word, "")

        target = " ".join(target.split())

        if open_website(target):
            return f"Opening {target.title()}..."

        app = launch_app(target)

        if app:
            return app

        return "Sorry, I don't know that application or website."

    elif "time" in command:
        return f"The current time is {get_time()}."

    elif "date" in command:
        return f"Today's date is {get_date()}."

    elif "hello" in command or "hi" in command:
        return "Hello Pradeepp! 👋"

    elif "how are you" in command:
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
    elif "take note" in command:

        note = command.replace("take note", "").strip()

        if note:
            save_note(note)
            return "Note saved successfully."

        return "What should I write?"

    elif "show notes" in command:

        notes = read_notes()

        if len(notes) == 0:
            return "You don't have any notes."

        text = "📝 Your Notes\n\n"

        for i, note in enumerate(notes, 1):
            text += f"{i}. {note}"

        return text
    
    elif command.startswith("search"):

        query = command.replace("search", "").strip()

        if query:

            search_google(query)

            return f"Searching Google for {query}"

        return "What should I search?"
    elif "take screenshot" in command:

        path = take_screenshot()

        return f"Screenshot saved successfully.\n{path}"

    elif "open screenshots" in command:

        open_screenshot_folder()

        return "Opening screenshots folder..."

    elif og_command.startswith("find file"):

        filename = og_command.replace("find file", "").strip()

        if filename:

            path = find_file(filename, "C:\\Users\\Pradeepp")

            if path:
                return f"Found!\n{path}"

            return "Sorry, I couldn't find that file."

        return "Which file should I search for?"

    return "Sorry, I don't understand that yet."