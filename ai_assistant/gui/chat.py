import tkinter as tk
from gui.bubbles import create_chat_area, add_message
from core.assistant import process_command
from core.voice import speak, listen
import threading
def create_chat(root):

    main = tk.Frame(root, bg="#1E1E1E")
    main.pack(side="right", fill="both", expand=True)

    # ---------------- Chat Area ---------------- #

    canvas, chat_frame = create_chat_area(main)

    # ---------------- Bottom Area ---------------- #

    add_message(
    canvas,
    chat_frame,
    "Hello Pradeepp! 👋",
    "bot"
)
    add_message(
        canvas,
        chat_frame,
        "How can I help you today?",
        "bot"
    )

    # ---------------- Bottom Area ---------------- #

    status = tk.Label(
    main,
    text="🟢 Ready",
    bg="#1E1E1E",
    fg="#AAAAAA",
    anchor="w",
    font=("Segoe UI", 9)
    )

    status.pack(fill="x", padx=15, pady=(0, 5))
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
    entry.insert(0, "Type a message...")
    entry.config(fg="gray")
    # ---------------- Send Function ---------------- #
    def clear_placeholder(event):

        if entry.get() == "Type a message...":
            entry.delete(0, tk.END)
            entry.config(fg="white")
    def restore_placeholder(event):

        if entry.get() == "":
            entry.insert(0, "Type a message...")
            entry.config(fg="gray")
    def clear_chat():

        for widget in chat_frame.winfo_children():
            widget.destroy()

        add_message(
        canvas,
        chat_frame,
        "Hello Pradeepp! 👋",
        "bot"
    )

        add_message(
        canvas,
        chat_frame,
        "How can I help you today?",
        "bot"
    )

        status.config(text="🟢 Ready")
    def voice_message():

        status.config(text="🎤 Listening...")
        
        command = listen()

        if command is None or command.strip() == "":
            status.config(text="🟢 Ready")
            return
        add_message(
            canvas,
            chat_frame,
            command,
            "user"
        )
        reply = process_command(command)

        add_message(
            canvas,
            chat_frame,
            reply,
            "bot"
            )

        status.config(text="🔊 Speaking...")
        speak(reply)
        status.config(text="🟢 Ready")
    def send_message(event=None):

        message = entry.get().strip()

        if message == "" or message == "Type a message...":
            return

        add_message(
            canvas,
            chat_frame,
            message,
            "user"
        )

        msg = message.lower()
        status.config(text="🤔 Thinking...")
        reply = process_command(msg)
        threading.Thread(target=speak, args=(reply,), daemon=True).start()
        status.config(text="🟢 Ready")
        add_message(
            canvas,
            chat_frame,
            reply,
            "bot"
        )

        entry.delete(0, tk.END)
        restore_placeholder(None)

    # ---------------- Send Button ---------------- #
    mic = tk.Button(
        bottom,
        text="🎤",
        bg="#2E2E2E",
        fg="white",
        relief="flat",
        bd=0,
        font=("Segoe UI", 12),
        width=4,
        cursor="hand2",
        command=lambda: threading.Thread(target=voice_message, daemon=True).start()
    )

    mic.pack(side="right", padx=(0, 10))
    clear = tk.Button(
    bottom,
    text="🗑",
    bg="#2E2E2E",
    fg="white",
    relief="flat",
    bd=0,
    font=("Segoe UI", 12),
    width=4,
    cursor="hand2",
    command=clear_chat
)

    clear.pack(side="right", padx=(0, 10))
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
    entry.bind("<Return>", lambda event: send_message())
    entry.bind("<FocusIn>", clear_placeholder)
    entry.bind("<FocusOut>", restore_placeholder)
    root.after(100, lambda: root.focus_set())