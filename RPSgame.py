from tkinter import *
from tkinter import  ttk
import random
root=Tk()
root.geometry("300x300")
root.title("Rock,Paper,Scissor Game")
root.configure(bg="#f0f0f0")
root.resizable(False,False)
choice_list=["Rock","Paper","Scissor"]
player=0
computer=0
def result():
    global player,computer
    choice=choice_var.get()
    label4.config(text=choice)
    computer_choice=random.choice(choice_list)
    label6.config(text=computer_choice)
    if choice==computer_choice:
        result_label.config(text="It's a Tie",fg="orange")
        
    elif (choice == "Rock" and computer_choice == "Scissor") or\
    (choice == "Paper" and computer_choice == "Rock") or\
    (choice == "Scissor" and computer_choice == "Paper"):
         result_label.config(text="You Win :)", fg="green")
         player+=1
    else:
        result_label.config(text="Computer wins!", fg="red")
        computer+=1
    user_score.config(text=player)
    robot_score.config(text=computer)
def new_game():
    choice_var.set("")
    label4.config(text="")
    label6.config(text="")
    result_label.config(text="", bg=root.cget("bg"))
    user_score.config(text="")
    robot_score.config(text="")
    
main_frame=Frame(root)
main_frame.pack()
label1=Label(main_frame,text="Rock,Paper,Scissor Game",font=("Aptos", 12))
label1.grid(row=0,column=0,pady=10)
player_score=Label(main_frame,text="Player Score : ")
player_score.grid(row=1,column=0,sticky="w")
user_score=Label(main_frame,text="")
user_score.grid(row=1,column=1,sticky="w")
computer_score=Label(main_frame,text="Computer Score : ")
computer_score.grid(row=2,column=0,sticky="w")
robot_score=Label(main_frame,text="")
robot_score.grid(row=2,column=1,sticky="w")

choose_frame=Frame(root)
choose_frame.pack(pady=10)
label2=Label(choose_frame,text="Choose : ")
label2.grid(row=0,column=0)

choice_var=StringVar()
Rock_button=ttk.Radiobutton(choose_frame,text="Rock",value="Rock",command=result,variable=choice_var)
Rock_button.grid(row=0,column=1,padx=5)
paper_button=ttk.Radiobutton(choose_frame,text="Paper",value="Paper",command=result,variable=choice_var)
paper_button.grid(row=0,column=2)
scissor_button=ttk.Radiobutton(choose_frame,text="Scissor",value="Scissor",command=result,variable=choice_var)
scissor_button.grid(row=0,column=3,padx=5)


frame3=LabelFrame(root,bd=1,text="Choices",borderwidth=2,relief="groove")
frame3.pack()
label3=Label(frame3,text="Player's Choice : ")
label3.grid(row=0,column=0,sticky="w",padx=4)
label4=Label(frame3,text="          ")
label4.grid(row=0,column=1,sticky="w",padx=4)
label5=Label(frame3,text="Computer's Choice : ")
label5.grid(row=1,column=0,sticky="w",padx=4)
label6=Label(frame3,text="          ")
label6.grid(row=1,column=1,sticky="w",padx=4)

result_frame=Frame(root)
result_frame.pack()
result_label=Label(result_frame,text="")
result_label.grid(row=0,column=0,pady=10)

newgame_button = ttk.Button(root, text="New Game", command=new_game)
newgame_button.pack()

root.mainloop()