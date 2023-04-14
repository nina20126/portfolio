'''
kids math game (add prize: pic, sound or something else (negative/positive)) 
Two numbers are shown on labels 
User adds the sum to a textbox With a button sum is checked 
Then new values are generated to labels 
Right and wrong answers are shown
'''

import random
from tkinter import *

app = Tk()
app.title("Kids math game")
canvas = Canvas(app, width=240, height=300)
canvas.pack()
app.geometry("400x300")
app.resizable(False, False)

num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

label1 = Label()

def submt(var1):
    if var1.get() == str(resultPLUS()):
        correct = Label(app, text="Correct!", fg="green", font=("Courier", 16))
        correct.place(relx=0.35, rely=0.14, relwidth=0.3, relheight=0.2)
        photo_label.place(relx=0, rely=0, relwidth=0.3, relheight=0.6)
    else:
        wrong = Label(app, text="Wrong!", fg="red", font=("Courier", 16))
        wrong.place(relx=0.35, rely=0.14, relwidth=0.3, relheight=0.2)
        photo_label2.place(relx=0, rely=0, relwidth=0.3, relheight=0.6)


def try_again():
    answer_clear()
    photo_label.place_forget()
    photo_label2.place_forget()

    try_again.num1_update = random.choice(num)
    try_again.num2_update = random.choice(num)
    new_math_problem = Label(
        app, text=f"{try_again.num1_update}+{try_again.num2_update}", font=("Courier", 16),
    )
    new_math_problem.place(relx=0.35, rely=0.14, relwidth=0.35, relheight=0.20)

def answer_clear():
    answer.delete(0, END)

def resultPLUS():
    try_again
    return try_again.num1_update + try_again.num2_update

photo = PhotoImage(file="star.png")
photo_label = Label(master=app, image=photo)

photo2 = PhotoImage(file="sad_face.png")
photo_label2 = Label(master=app, image=photo2)

start = Button(app, text="Start", command=try_again)
start.place(relx=0.45, rely=0.2)

answer = Entry(app)
answer.place(relx=0.35, rely=0.4, relwidth=0.34, relheight=0.23)

submit = Button(app, text="Submit", command=lambda: submt(answer))
submit.place(relx=0.35, rely=0.64, relwidth=0.34, relheight=0.23)

try_again = Button(app, text="Try Again", command=try_again)
try_again.place(relx=0.42, rely=0.9)

app.mainloop()