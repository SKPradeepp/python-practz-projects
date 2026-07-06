import tkinter as tk

def create_sidebar(root):

    sidebar = tk.Frame(
        root,
        bg="#2A2A2A",
        width=200
    )

    sidebar.pack(
        side="left",
        fill="y"
    )

    title = tk.Label(
        sidebar,
        text="🤖 Aura",
        bg="#2A2A2A",
        fg="white",
        font=("Segoe UI",18,"bold")
    )

    title.pack(pady=20)

    buttons = [
        "🏠 Home",
        "💬 Chat",
        "📝 Notes",
        "🧮 Calculator",
        "⚙ Settings"
    ]

    for item in buttons:

        btn = tk.Button(
            sidebar,
            text=item,
            bg="#3A3A3A",
            fg="white",
            relief="flat",
            font=("Segoe UI",11),
            width=18,
            height=2
        )

        btn.pack(pady=5)