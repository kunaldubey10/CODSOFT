from tkinter import *
import random
import string
from tkinter import ttk
import pyperclip

root=Tk()
root.geometry("600x400")
root.title("Password Generator")
root.config(bg="#1f1f1f")
style=ttk.Style()
style.configure("TButton",background="#1f1f1f")

def generate_password():
    try:
        pass_length = int(length_entry.get())
        if pass_length <= 0:
            result.config(text="Please enter a positive length.",fg="red")
            return
    except ValueError:
        result.config(text="Please enter a valid number.", fg="red")
        return
    values = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(values) for _ in range(pass_length))
    result.config(text=f"Your password is: {password}",bg="#1f1f1f",fg="Red")

def reset_input():
    length_entry.delete(0,END) 
    result.config(text="")  

def copy_to_clipboard():
    password = result.cget("text").split(": ")[1]  
    pyperclip.copy(password)

main_frame=Frame(root,bg="#1f1f1f")
main_frame.pack()

label1=Label(main_frame,text="PASSWORD GENERATOR",font=("Gorgom",20),bg="#1f1f1f",fg="white")
label1.grid(row=0,column=0,columnspan=2,pady=10)

length = Label(root, text="Enter password length:", bg="#1f1f1f", fg="white",font=("Open Sans", 13))
length.pack(pady=10)

length_entry = Entry(root, font=("Open Sans", 12))
length_entry.pack(pady=5)

generate_button = Button(root, text="Generate Password", command=generate_password, bg="lightgrey", font=("Open Sans", 12))
generate_button.pack(pady=15)

result = Label(root, text="", bg="white", font=("Open Sans", 12))
result.pack(pady=10)


reset_button = Button(root, text="Reset", command=reset_input, font=("Open Sans", 12))
reset_button.pack(side=RIGHT,padx=40)

copy_button =Button(root, text="Copy Password", command=copy_to_clipboard, bg="lightgrey", font=("Open Sans", 12))
copy_button.pack(side=LEFT,padx=40)

root.mainloop()
