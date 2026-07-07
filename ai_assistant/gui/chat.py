import tkinter as tk
from tkinter import scrolledtext


def create_chat(root):

    main = tk.Frame(root, bg="#1E1E1E")
    main.pack(side="right", fill="both", expand=True)

    # ---------------- Chat Area ---------------- #

    chat_box = scrolledtext.ScrolledText(
        main,
        bg="#252526",
        fg="white",
        insertbackground="white",
        font=("Segoe UI", 11),
        relief="flat",
        wrap="word"
    )

    chat_box.pack(fill="both", expand=True, padx=15, pady=15)

    chat_box.insert(tk.END, "🤖 Aura:\n")
    chat_box.insert(tk.END, "Hello Pradeepp! 👋\n")
    chat_box.insert(tk.END, "How can I help you today?\n\n")

    chat_box.config(state="disabled")

    # ---------------- Bottom Area ---------------- #

    bottom = tk.Frame(main, bg="#1E1E1E")
    bottom.pack(fill="x", padx=15, pady=15)

    entry = tk.Entry(
        bottom,
        bg="#2A2A2A",
        fg="white",
        insertbackground="white",
        relief="flat",
        font=("Segoe UI", 12)
    )

    entry.pack(side="left", fill="x", expand=True, padx=(0, 10))

    # ---------------- Send Function ---------------- #

    def send_message(event=None):

        message = entry.get().strip()

        if message == "":
            return

        chat_box.config(state="normal")

        chat_box.insert(tk.END, f"🧑 You:\n{message}\n\n")

        msg = message.lower()

        if msg == "hello":
            reply = "Hello Pradeepp! 👋"

        elif msg == "how are you":
            reply = "I'm doing great! 😄"

        elif msg == "bye":
            reply = "See you later! 👋"

        else:
            reply = "Sorry, I don't understand that yet."

        chat_box.insert(tk.END, f"🤖 Aura:\n{reply}\n\n")

        chat_box.config(state="disabled")

        chat_box.yview(tk.END)

        entry.delete(0, tk.END)

    # ---------------- Send Button ---------------- #

    send = tk.Button(
        bottom,
        text="➤ Send",
        bg="#00C853",
        fg="white",
        activebackground="#00E676",
        activeforeground="white",
        relief="flat",
        bd=0,
        font=("Segoe UI", 11, "bold"),
        width=10,
        cursor="hand2",
        command=send_message
    )

    send.pack(side="right")

    entry.bind("<Return>", send_message)