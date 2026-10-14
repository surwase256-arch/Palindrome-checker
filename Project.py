import tkinter as tk
from tkinter import messagebox

# ---------------- COLORS ----------------
BG = "#0F172A"
CARD = "#FFFFFF"
PRIMARY = "#6366F1"
PRIMARY_HOVER = "#4F46E5"
GREEN = "#16A34A"
RED = "#DC2626"
TEXT = "#1E293B"
MUTED = "#64748B"
LIGHT = "#F1F5F9"


# ---------------- FUNCTIONS ----------------
def check_palindrome(event=None):
    text = entry.get()

    if not text.strip():
        messagebox.showwarning(
            "Input Required",
            "Please enter a word or sentence."
        )
        entry.focus_set()
        return

    # Ignore spaces and letter case
    cleaned = "".join(text.lower().split())

    # Stack: LIFO
    stack = []
    for char in cleaned:
        stack.append(char)

    reversed_text = ""
    while stack:
        reversed_text += stack.pop()

    # Queue: FIFO
    queue = []
    for char in cleaned:
        queue.append(char)

    original_text = ""
    while queue:
        original_text += queue.pop(0)

    # Check result
    if original_text == reversed_text:
        result_label.config(
            text="✓  It's a Palindrome!",
            fg=GREEN
        )
        status_label.config(
            text="Great! The text reads the same backward.",
            fg=GREEN
        )
        result_card.config(bg="#F0FDF4")
    else:
        result_label.config(
            text="✗  Not a Palindrome",
            fg=RED
        )
        status_label.config(
            text="The text changes when reversed.",
            fg=RED
        )
        result_card.config(bg="#FEF2F2")

    details_label.config(
        text=f"Original : {original_text}\n"
             f"Reversed : {reversed_text}"
    )


def clear_fields():
    entry.delete(0, tk.END)

    result_label.config(
        text="Your result will appear here",
        fg=TEXT
    )

    status_label.config(
        text="Enter text above to get started.",
        fg=MUTED
    )

    details_label.config(text="")
    result_card.config(bg=LIGHT)
    entry.focus_set()


def on_enter(event):
    check_palindrome()


# ---------------- MAIN WINDOW ----------------
root = tk.Tk()
root.title("Palindrome Checker")
root.geometry("760x760")
root.configure(bg=BG)
root.resizable(False, False)

# ---------------- HEADER ----------------
header = tk.Frame(root, bg=BG)
header.pack(fill="x", pady=(28, 20))

icon = tk.Label(
    header,
    text="↔",
    font=("Arial", 30, "bold"),
    bg=BG,
    fg="#A5B4FC"
)
icon.pack()

title = tk.Label(
    header,
    text="Palindrome Checker",
    font=("Arial", 25, "bold"),
    bg=BG,
    fg="white"
)
title.pack(pady=(2, 5))

subtitle = tk.Label(
    header,
    text="A simple demonstration of Stacks and Queues",
    font=("Arial", 11),
    bg=BG,
    fg="#CBD5E1"
)
subtitle.pack()


# ---------------- MAIN CARD ----------------
main_card = tk.Frame(
    root,
    bg=CARD,
    highlightbackground="#334155",
    highlightthickness=1
)
main_card.pack(fill="both", expand=True, padx=35, pady=(0, 28))

# Input heading
tk.Label(
    main_card,
    text="ENTER YOUR TEXT",
    font=("Arial", 10, "bold"),
    bg=CARD,
    fg=TEXT
).pack(anchor="w", padx=30, pady=(28, 10))

# Input box
input_frame = tk.Frame(
    main_card,
    bg=LIGHT,
    highlightbackground="#CBD5E1",
    highlightthickness=1
)
input_frame.pack(fill="x", padx=30)

entry = tk.Entry(
    input_frame,
    font=("Arial", 15),
    bg=LIGHT,
    fg=TEXT,
    insertbackground=TEXT,
    relief="flat",
    bd=0
)
entry.pack(fill="x", padx=14, pady=14)
entry.focus_set()

entry.bind("<Return>", on_enter)

# Example hint
tk.Label(
    main_card,
    text="Example: madam, level, racecar",
    font=("Arial", 10),
    bg=CARD,
    fg=MUTED
).pack(anchor="w", padx=32, pady=(7, 15))


# ---------------- BUTTONS ----------------
button_frame = tk.Frame(main_card, bg=CARD)
button_frame.pack(fill="x", padx=30)

check_button = tk.Button(
    button_frame,
    text="  Check Palindrome  →",
    command=check_palindrome,
    font=("Arial", 11, "bold"),
    bg=PRIMARY,
    fg="white",
    activebackground=PRIMARY_HOVER,
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    padx=15,
    pady=12
)
check_button.pack(side="left", fill="x", expand=True, padx=(0, 8))

check_button.bind(
    "<Enter>",
    lambda e: check_button.config(bg=PRIMARY_HOVER)
)
check_button.bind(
    "<Leave>",
    lambda e: check_button.config(bg=PRIMARY)
)

clear_button = tk.Button(
    button_frame,
    text="Clear  ↺",
    command=clear_fields,
    font=("Arial", 11, "bold"),
    bg="#E2E8F0",
    fg=TEXT,
    activebackground="#CBD5E1",
    relief="flat",
    cursor="hand2",
    padx=18,
    pady=12
)
clear_button.pack(side="left")


# ---------------- RESULT CARD ----------------
result_card = tk.Frame(
    main_card,
    bg=LIGHT,
    highlightbackground="#E2E8F0",
    highlightthickness=1
)
result_card.pack(fill="x", padx=30, pady=(25, 18))

result_label = tk.Label(
    result_card,
    text="Your result will appear here",
    font=("Arial", 17, "bold"),
    bg=LIGHT,
    fg=TEXT
)
result_label.pack(pady=(18, 5))

status_label = tk.Label(
    result_card,
    text="Enter text above to get started.",
    font=("Arial", 10),
    bg=LIGHT,
    fg=MUTED
)
status_label.pack(pady=(0, 10))

details_label = tk.Label(
    result_card,
    text="",
    font=("Consolas", 11),
    bg=LIGHT,
    fg=TEXT,
    justify="left"
)
details_label.pack(pady=(0, 18))


# ---------------- HOW IT WORKS ----------------
tk.Label(
    main_card,
    text="HOW IT WORKS",
    font=("Arial", 11, "bold"),
    bg=CARD,
    fg=TEXT
).pack(anchor="w", padx=30, pady=(5, 12))

concepts = tk.Frame(main_card, bg=CARD)
concepts.pack(fill="x", padx=30)

# Stack box
stack_box = tk.Frame(
    concepts,
    bg="#EEF2FF",
    highlightbackground="#C7D2FE",
    highlightthickness=1
)
stack_box.pack(side="left", fill="both", expand=True, padx=(0, 7))

tk.Label(
    stack_box,
    text="📚  STACK",
    font=("Arial", 11, "bold"),
    bg="#EEF2FF",
    fg="#4338CA"
).pack(anchor="w", padx=12, pady=(12, 5))

tk.Label(
    stack_box,
    text="LIFO\nLast In, First Out\n\nReverses the characters",
    font=("Arial", 10),
    bg="#EEF2FF",
    fg=TEXT,
    justify="left"
).pack(anchor="w", padx=12, pady=(0, 12))

# Queue box
queue_box = tk.Frame(
    concepts,
    bg="#ECFDF5",
    highlightbackground="#A7F3D0",
    highlightthickness=1
)
queue_box.pack(side="left", fill="both", expand=True, padx=(7, 0))

tk.Label(
    queue_box,
    text="⇢  QUEUE",
    font=("Arial", 11, "bold"),
    bg="#ECFDF5",
    fg="#047857"
).pack(anchor="w", padx=12, pady=(12, 5))

tk.Label(
    queue_box,
    text="FIFO\nFirst In, First Out\n\nPreserves the order",
    font=("Arial", 10),
    bg="#ECFDF5",
    fg=TEXT,
    justify="left"
).pack(anchor="w", padx=12, pady=(0, 12))


# ---------------- FOOTER ----------------
tk.Label(
    main_card,
    text="DATA STRUCTURES  •  STACKS & QUEUES",
    font=("Arial", 9, "bold"),
    bg=CARD,
    fg="#94A3B8"
).pack(pady=(18, 18))


# ---------------- START APPLICATION ----------------
root.mainloop()
