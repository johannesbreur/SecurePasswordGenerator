import string
import random
import tkinter as tk
from tkinter import messagebox

def generate_password(length=12):
    """Generate a secure password with letters, digits, and symbols."""
    if length < 8:
        raise ValueError("Password length should be at least 8 characters.")

    # Character sets
    letters = string.ascii_letters      # a-z + A-Z
    digits = string.digits              # 0-9
    symbols = string.punctuation        # !@#$ etc.

    all_chars = letters + digits + symbols

    # Make sure we include at least one of each type
    password = [
        random.choice(letters),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the rest of the password
    password += [random.choice(all_chars) for _ in range(length - 3)]

    # Shuffle to avoid predictable order
    random.shuffle(password)

    return "".join(password)

def on_generate():
    """Handle Generate button click."""
    try:
        length_str = length_entry.get().strip()
        if not length_str:
            raise ValueError("Please enter a password length.")
        length = int(length_str)

        password = generate_password(length)
        password_var.set(password)

    except ValueError as e:
        messagebox.showerror("Input Error", str(e))

def on_copy():
    """Copy the generated password to clipboard."""
    pwd = password_var.get()
    if not pwd:
        messagebox.showinfo("Copy Password", "No password to copy yet.")
        return
    root.clipboard_clear()
    root.clipboard_append(pwd)
    root.update()  # keeps clipboard after window closes on some systems
    messagebox.showinfo("Copy Password", "Password copied to clipboard!")

# --- GUI setup ---

root = tk.Tk()
root.title("Secure Password Generator")

# Optional: fix a small size and padding
root.resizable(False, False)
pad = 10

# Frame for content
frame = tk.Frame(root, padx=pad, pady=pad)
frame.grid(row=0, column=0)

# Length label + entry
length_label = tk.Label(frame, text="Password length (8 or more):")
length_label.grid(row=0, column=0, sticky="w")

length_entry = tk.Entry(frame, width=10)
length_entry.grid(row=0, column=1, padx=(5, 0))
length_entry.insert(0, "12")  # default value

# Generate button
generate_button = tk.Button(frame, text="Generate", command=on_generate)
generate_button.grid(row=0, column=2, padx=(5, 0))

# Password display
password_label = tk.Label(frame, text="Generated password:")
password_label.grid(row=1, column=0, columnspan=3, sticky="w", pady=(pad, 0))

password_var = tk.StringVar()
password_entry = tk.Entry(frame, textvariable=password_var, width=40)
password_entry.grid(row=2, column=0, columnspan=3, pady=(5, 0))

# Copy button
copy_button = tk.Button(frame, text="Copy to Clipboard", command=on_copy)
copy_button.grid(row=3, column=0, columnspan=3, pady=(pad, 0))

root.mainloop()