import subprocess

apps = {
    "notepad": "notepad.exe",
    "calculator": "calc.exe",
    "paint": "mspaint.exe",
    "cmd": "cmd.exe",
    "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "vscode": r"C:\Users\Pradeepp\AppData\Local\Programs\Microsoft VS Code\Code.exe",
    "explorer": "explorer.exe",
    "wordpad": "write.exe",
    "powershell": "powershell.exe",
}
def launch_app(app_name):

    app_name = app_name.lower()

    if app_name in apps:

        subprocess.Popen(apps[app_name])

        return f"Opening {app_name.title()}..."

    return "Sorry, I don't know that application yet."
if __name__ == "__main__":

    print(launch_app("notepad"))