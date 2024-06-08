from tkinter import *
import random
import time
import requests

root = Tk()
root.geometry("800x800")

refresh_sec = 0.01

welcome_message = Label(root, text='Welcome to Hangman game', font='Courier 20 bold')
welcome_message.pack()

wordlist = requests.get("https://random-word-api.herokuapp.com/all").json()

def StartButton():
    start_button.pack_forget()  
    word = random.choice(wordlist)
    secret_word = ['_'] * len(word)
    wrong_ans = 0

    def check_guess():
        guess = entry.get()
        entry.delete(0, END)
        if guess == '':
            return
        nonlocal wrong_ans
        if guess not in word:
            message.config(text='Fail, try again')
            wrong_ans += 1
            draw_man(wrong_ans)
        else:
            message.config(text='Correct guess')
            for i in range(len(word)):
                if word[i] == guess:
                    secret_word[i] = guess
        secret_word_label.config(text=' '.join(secret_word),fg='white')
        if '_' not in secret_word or wrong_ans >= 7:
            entry.config(state=DISABLED)
            check_button.config(state=DISABLED)
            if '_' not in secret_word:
                message.config(text='Congratulations, you found the word')
                secret_word_label.config(text=' '.join(word))
            else:
                message.config(text='Fail!\nThe word was ')
                secret_word_label.config(text=' '.join(word),fg='red')
          
    entry = Entry(root, font='Courier 20 bold')
    entry.pack()

    check_button = Button(root, text='Check Guess', font='Courier 10', command=check_guess)
    check_button.pack()

    message = Label(root, text='', font='Courier 20 bold')
    message.pack()

    secret_word_label = Label(root, text=' '.join(secret_word), font='Courier 20 bold')
    secret_word_label.pack()

    

start_button = Button(root, text='Click to start the game', font='Courier 10', command=StartButton)
start_button.pack()


canvas = Canvas(root,width=400,height=400)
canvas.pack()

canvas.create_line(400, 100, 400, 400, width=4)
canvas.create_line(250,100,400,100,width=4)


def draw_man(x):
    if x == 1:
        canvas.create_line(250,100,250,150,width=4)
    if x == 2:
        canvas.create_oval(225,150,275,200,width=4)
    if x == 3:
        canvas.create_line(250,200,250,280,width=4)
    if x == 4:
        canvas.create_line(250,240,190,200,width=4)
    if x == 5:
        canvas.create_line(250,240,310,200,width=4)
    if x == 6:
        canvas.create_line(250,280,190,320,width=4)
    if x == 7:
        canvas.create_line(250,280,310,320,width=4)
    
    


root.mainloop()
