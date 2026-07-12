from core.commands import *
from core.memory import remember, recall
from core.notes import save_note, read_notes
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
    elif "youtube" in command:

        open_youtube()

        return "Opening YouTube..."
    elif "github" in command:

        open_github()

        return "Opening GitHub..."
    elif "google" in command:

        open_google()

        return "Opening Google..."
    elif "chatgpt" in command:

        open_chatgpt()

        return "Opening ChatGPT...(web version)"
    elif command.startswith("search"):

        query = command.replace("search", "").strip()

        if query:

            search_google(query)

            return f"Searching Google for {query}"

        return "What should I search?"

    return "Sorry, I don't understand that yet."