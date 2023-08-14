from tkinter import *
import random
attempts = 5
limit =random.randint(0,100)
answer = random.randint(0, limit)
def check_answer():
    global attempts
    global text
    attempts -= 1
    guess = int(entry.get())
    if attempts == 0:
        text.set("You lose the game!!")
        check_btn.pack_forget()
    elif guess > answer:
        if guess > limit:
            text.set("Your guess is out of range. you have " + str(attempts) + " attempts left.")
        else:
            text.set("Incorrect! You have " + str(attempts) + " attempts left. Your guess is too high!!")
    elif guess < answer:
        text.set("Incorrect! You have " + str(attempts) + " attempts left. Your guess is too low!!")
    elif answer == guess:
        text.set("Congratulations!! You won the game♥♥")
        check_btn.pack_forget()
    return
root = Tk()
root.geometry("650x400")
root.title("Number Guessing Game")
root.configure(bg="pink")
head = Label(root, text="☺JUST ENJOY☺", font=("Bold", 18, "bold"), bg="pink")
head.pack(pady=20, padx=50)
label = Label(root, text=f"Guess a number between 0 and {limit}", font=("bold", 15, "bold"), bg="white")
label.pack(pady=50, padx=10)
entry = Entry(root, width=40)
entry.pack(pady=20)
check_btn = Button(root, text="Check karo", command=check_answer, width=20)
check_btn.pack(pady=15)
text = StringVar()
text.set("You have 5 attempts! Good luck!")
guess_attempts = Label(root, textvariable=text, bg="white")
guess_attempts.pack()

root.mainloop()
