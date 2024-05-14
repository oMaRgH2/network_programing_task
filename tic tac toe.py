from tkinter import *
from tkinter import messagebox
window=Tk()

window.title("Welcome to The Gaming world TIC-Tac-Toe ")
window.geometry("400x300")

lbl=Label(window,text="Tic-tac-toe Game",font=('Helvetica','15'))
lbl.grid(row=0,column=0)
lbl=Label(window,text="Player 1: X",font=('Helvetica','10'))
lbl.grid(row=1,column=0)
lbl=Label(window,text="Player 2: O",font=('Helvetica','10'))
lbl.grid(row=2,column=0)

turn=1; #For first person turn.

def reset():
    global turn, flag
    flag = 1
    turn = 1
    btn1["text"]=" "
    btn2["text"]=" "
    btn3["text"]=" "
    btn4["text"]=" "
    btn5["text"]=" "
    btn6["text"]=" "
    btn7["text"]=" "
    btn8["text"]=" "
    btn9["text"]=" "

def clicked1():
    global turn
    if btn1["text"]==" ":   #For getting the text of a button
        if turn==1:
            turn =2;
            btn1["text"]="X"
        elif turn==2:
            turn=1;
            btn1["text"]="O"
        check();
def clicked2():
    global turn
    if btn2["text"]==" ":
        if turn==1:
            turn =2;
            btn2["text"]="X"
        elif turn==2:
            turn=1;
            btn2["text"]="O"
        check();
def clicked3():
    global turn
    if btn3["text"]==" ":
        if turn==1:
            turn =2;
            btn3["text"]="X"
        elif turn==2:
            turn=1;
            btn3["text"]="O"
        check();
def clicked4():
    global turn
    if btn4["text"]==" ":
        if turn==1:
            turn =2;
            btn4["text"]="X"
        elif turn==2:
            turn=1;
            btn4["text"]="O"
        check();
def clicked5():
    global turn
    if btn5["text"]==" ":
        if turn==1:
            turn =2;
            btn5["text"]="X"
        elif turn==2:
            turn=1;
            btn5["text"]="O"
        check();
def clicked6():
    global turn
    if btn6["text"]==" ":
        if turn==1:
            turn =2;
            btn6["text"]="X"
        elif turn==2:
            turn=1;
            btn6["text"]="O"
        check();
def clicked7():
    global turn
    if btn7["text"]==" ":
        if turn==1:
            turn =2;
            btn7["text"]="X"
        elif turn==2:
            turn=1;
            btn7["text"]="O"
        check();
def clicked8():
    global turn
    if btn8["text"]==" ":
        if turn==1:
            turn =2;
            btn8["text"]="X"
        elif turn==2:
            turn=1;
            btn8["text"]="O"
        check();
def clicked9():
    global turn
    if btn9["text"]==" ":
        if turn==1:
            turn =2;
            btn9["text"]="X"
        elif turn==2:
            turn=1;
            btn9["text"]="O"
        check();
flag=1;