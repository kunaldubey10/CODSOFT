import customtkinter as ctk
import math

def on_button_click(value):
    current_text = entry.get()
    if value == "=":
        try:
            result = eval(current_text)
            entry.delete(0, ctk.END)
            entry.insert(0, str(result))
        except Exception:
            entry.delete(0, ctk.END)
            entry.insert(0, "Error")
    elif value == "sqrt":
        try:
            result = math.sqrt(float(current_text))
            entry.delete(0, ctk.END)
            entry.insert(0, str(result))
        except Exception:
            entry.delete(0, ctk.END)
            entry.insert(0, "Error")
    elif value == "C":
        entry.delete(0, ctk.END)
    else:
        entry.insert(ctk.END, value)

root = ctk.CTk()
root.title("Custom Calculator")

# Create the entry widget
entry = ctk.CTkEntry(root, font=("Arial", 20), justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define button labels
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+",
    "sqrt", "%", "C"  # Our magical "C" button!
]

# Create buttons
for i, label in enumerate(buttons):
    row = i // 4 + 1
    col = i % 4
    btn = ctk.CTkButton(root, text=label, font=("Arial", 22), command=lambda val=label: on_button_click(val))
    btn.grid(row=row, column=col, padx=5, pady=5)

root.mainloop()
