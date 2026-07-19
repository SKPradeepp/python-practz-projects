import webbrowser

websites = {

    "google": "https://www.google.com",
    "youtube": "https://www.youtube.com",
    "github": "https://github.com",
    "chatgpt": "https://chat.openai.com",
    "gmail": "https://mail.google.com",
    "linkedin": "https://www.linkedin.com"

}

def open_website(name):

    name = name.lower().strip()

    if name in websites:
        webbrowser.open(websites[name])
        return True

    return False