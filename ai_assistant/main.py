import tkinter as tk
import os
from gui.chat import create_chat
from gui.sidebar import create_sidebar

root = tk.Tk()
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
icon = tk.PhotoImage(file=os.path.join(BASE_DIR, "assets", "icons", "icon.png"))
root.iconphoto(True, icon)
root.title("Aura AI Assistant")

window_width = 1000
window_height = 650

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

root.geometry(f"{window_width}x{window_height}+{x}+{y}")

root.configure(bg="#1E1E1E")

root.resizable(False, False)

create_sidebar(root)

create_chat(root)
status = tk.Label(
    root,
    text="Ready",
    bg="#222222",
    fg="white",
    anchor="w",
    padx=10
)

status.pack(side="bottom", fill="x")
root.mainloop()