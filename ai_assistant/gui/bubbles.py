import tkinter as tk

def create_chat_area(parent):

    canvas = tk.Canvas(
        parent,
        bg="#252526",
        highlightthickness=0
    )

    scrollbar = tk.Scrollbar(
    parent,
    orient="vertical",
    command=canvas.yview,
    width=8
    )

    chat_frame = tk.Frame(
        canvas,
        bg="#252526"
    )

    chat_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window(
        (8, 8),
        window=chat_frame,
        anchor="nw"
    )

    canvas.configure(
        yscrollcommand=scrollbar.set
    )

    canvas.pack(
        side="left",
        fill="both",
        expand=True
    )

    scrollbar.pack(
        side="right",
        fill="y"
    )

    return canvas, chat_frame
def add_message(canvas, chat_frame, text, sender="bot"):

    container = tk.Frame(
        chat_frame,
        bg="#252526"
    )
    label = tk.Label(
    container,
    text="You" if sender == "user" else "Aura",
    bg="#252526",
    fg="#AAAAAA",
    font=("Segoe UI", 8, "bold")
    )

    container.pack(fill="x", padx=12, pady=7)

    label.pack(anchor="w")

    if sender == "user":
        bubble = tk.Label(
        container,
        text=text,
        bg="#0078D7",
        fg="white",
        wraplength=420,
        justify="left",
        padx=12,
        pady=8,
        font=("Segoe UI", 11)
    )
    else:
        bubble = tk.Label(
        container,
        text=text,
        bg="#3A3A3A",
        fg="white",
        wraplength=420,
        justify="left",
        padx=12,
        pady=8,
        font=("Segoe UI", 11)
    )

    bubble.pack(anchor="w")

    canvas.update_idletasks()

    canvas.yview_moveto(1.0)