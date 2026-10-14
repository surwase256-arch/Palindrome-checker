import tkinter as tk
from tkinter import messagebox


def check_palindrome():
    text = entry.get()

    if not text.strip():
        messagebox.showwarning("Input Required", "Please enter some text.")
        return

    # Convert to lowercase and remove spaces
    cleaned = "".join(text.lower().split())

    # Stack: Last In, First Out (LIFO)
    stack = []
    for char in cleaned:
        stack.append(char)

    reversed_text = ""
    while stack:
        reversed_text += stack.pop()

    # Queue: First In, First Out (FIFO)
    queue = []
    for char in cleaned:
        queue.append(char)

    original_text = ""
    while queue:
        original_text += queue.pop(0)

    # Compare original and reversed text
    if original_text == reversed_text:
        result_label.config(
            text="Result: It is a Palindrome!",
            fg="green"
        )
    else:
        result_label.config(
            text="Result: It is NOT a Palindrome!",
            fg="red"
        )

    details_label.config(
        text=f"Original: {original_text}\n"
             f"Reversed: {reversed_text}"
    )


def clear_fields():
    entry.delete(0, tk.END)
    result_label.config(text="Result will appear here", fg="black")
    details_label.config(text="")


# Main window
root = tk.Tk()
root.title("Palindrome Checker - Stacks and Queues")
root.geometry("600x520")
root.configure(bg="white")
root.resizable(False, False)

# Heading
title_label = tk.Label(
    root,
    text="Palindrome Checker",
    font=("Arial", 22, "bold"),
    bg="white",
    fg="#1F3A5F"
)
title_label.pack(pady=(20, 5))

subtitle = tk.Label(
    root,
    text="Implementation using Stacks and Queues",
    font=("Arial", 11),
    bg="white",
    fg="gray"
)
subtitle.pack(pady=(0, 20))

# Input section
input_label = tk.Label(
    root,
    text="Enter a word or sentence:",
    font=("Arial", 12),
    bg="white"
)
input_label.pack()

entry = tk.Entry(
    root,
    font=("Arial", 14),
    width=35,
    relief="solid",
    bd=1
)
entry.pack(pady=10)
entry.focus_set()

# Buttons
button_frame = tk.Frame(root, bg="white")
button_frame.pack(pady=10)

check_button = tk.Button(
    button_frame,
    text="Check Palindrome",
    command=check_palindrome,
    font=("Arial", 11, "bold"),
    bg="#2563EB",
    fg="white",
    padx=12,
    pady=7,
    relief="flat"
)
check_button.grid(row=0, column=0, padx=8)

clear_button = tk.Button(
    button_frame,
    text="Clear",
    command=clear_fields,
    font=("Arial", 11),
    bg="#E5E7EB",
    fg="black",
    padx=20,
    pady=7,
    relief="flat"
)
clear_button.grid(row=0, column=1, padx=8)

# Result section
result_label = tk.Label(
    root,
    text="Result will appear here",
    font=("Arial", 14, "bold"),
    bg="white",
    fg="black"
)
result_label.pack(pady=15)

details_label = tk.Label(
    root,
    text="",
    font=("Arial", 11),
    bg="white",
    fg="#374151",
    justify="center"
)
details_label.pack(pady=5)

# Explanation section
explanation = tk.LabelFrame(
    root,
    text="How It Works",
    font=("Arial", 12, "bold"),
    bg="white",
    fg="#1F3A5F",
    padx=15,
    pady=10
)
explanation.pack(fill="x", padx=25, pady=15)

tk.Label(
    explanation,
    text="Stack (LIFO): Removes characters in reverse order.\n"
         "Queue (FIFO): Removes characters in original order.\n"
         "If both strings match, the input is a palindrome.",
    font=("Arial", 10),
    bg="white",
    justify="left",
    wraplength=500
).pack(anchor="w")

# Start application
root.mainloop()