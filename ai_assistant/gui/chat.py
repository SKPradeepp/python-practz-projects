import tkinter as tk

def create_chat(root):

    main = tk.Frame(
        root,
        bg="#1E1E1E"
    )

    main.pack(
        side="right",
        fill="both",
        expand=True
    )

    welcome = tk.Label(

        main,

        text="Hello Pradeepp!\n\nHow can I help you today?",

        bg="#1E1E1E",

        fg="white",

        font=("Segoe UI",18)

    )

    welcome.pack(pady=120)

    entry = tk.Entry(
    main,
    bg="#2A2A2A",
    fg="white",
    insertbackground="white",
    relief="flat",
    font=("Segoe UI", 12),
    width=45
    )

    entry.pack(side="left", padx=20, pady=20)

    send = tk.Button(
    main,
    text="➤ Send",
    bg="#00C853",
    fg="white",
    activebackground="#00E676",
    activeforeground="white",
    relief="flat",
    bd=0,
    font=("Segoe UI", 11, "bold"),
    width=10,
    cursor="hand2"
    )

    send.pack(side="left", pady=20)