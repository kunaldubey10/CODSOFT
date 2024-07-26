import tkinter as tk
from tkinter import messagebox
import math

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simple Calculator")
        self.geometry("400x500")
        self.expression = ""
        
        self.entry = tk.Entry(self, font=("Arial", 24), bd=10, insertwidth=2, width=14, borderwidth=4)
        self.entry.grid(row=0, column=0, columnspan=4)
        
        buttons = [
            '7', '8', '9', '/', '4', '5', '6', '*',
            '1', '2', '3', '-', '0', '.', '=', '+'
        ]
        
        for i, button in enumerate(buttons):
            action = lambda x=button: self.on_button_click(x)
            tk.Button(self, text=button, padx=20, pady=20, font=("Arial", 18), command=action).grid(row=1+i//4, column=i%4)
        
        tk.Button(self, text='C', padx=20, pady=20, font=("Arial", 18), command=self.clear).grid(row=6, column=3)
    
    def on_button_click(self, char):
        if char == '=':
            try:
                self.expression = str(eval(self.expression))
            except ZeroDivisionError:
                messagebox.showerror("Error", "Cannot divide by zero")
                self.expression = ""
            except Exception as e:
                messagebox.showerror("Error", str(e))
                self.expression = ""
        else:
            self.expression += str(char)
        self.update_entry()
    
    def clear(self):
        self.expression = ""
        self.update_entry()
    
    def update_entry(self):
        self.entry.delete(0, tk.END)
        self.entry.insert(0, self.expression)

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()

