import subprocess

apps = {

    "notepad": ["notepad", "notes"],

    "calculator": ["calculator", "calc"],

    "paint": ["paint", "mspaint"],

    "cmd": ["cmd", "command prompt"],

    "chrome": ["chrome", "google chrome", "browser"],

    "vscode": ["vscode", "vs code", "visual studio code", "code"],

    "explorer": ["explorer", "file explorer"],

    "wordpad": ["wordpad"],

    "powershell": ["powershell", "power shell"]

}
executables = {

    "notepad": "notepad.exe",

    "calculator": "calc.exe",

    "paint": "mspaint.exe",

    "cmd": "cmd.exe",

    "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",

    "vscode": r"D:\vscode\Microsoft VS Code\Code.exe",
    
    "explorer": "explorer.exe",

    "wordpad": "write.exe",

    "powershell": "powershell.exe"

}
def launch_app(app_name):

    app_name = app_name.lower().strip()

    for app, aliases in apps.items():

        if app_name in aliases:
            print("Launching:", app)
            print("Path:", executables[app])
            subprocess.Popen(executables[app])
            return f"Opening {app.title()}..."
    return None