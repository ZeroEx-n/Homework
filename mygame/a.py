import tkinter as tk

def increment_score():
    global score
    score += 2
    score_label.config(text=f"Human's died: {score}")


def increment_score_10():
    global score
    score += 10
    score_label.config(text=f"Human's died: {score}")


def oo():
    global score
    score *= 2
    score_label.config(text=f"Human's died: {score}")

def ao():
    global score
    score *= 100
    score_label.config(text=f"Human's died: {score}")

def aa():
    global score
    score = 0
    score_label.config(text=f"RESETED: {score}")

window = tk.Tk()
window.title("")
window.geometry("550x350")

score = 0



score_label = tk.Label(window, text=f"Human's died: {score}", font=("Comic Sans MS", 14))
score_label.pack(pady=20)

click_ao = tk.Button(window, text="Click and *100", command=ao, font=("Comic Sans MS", 14))
click_ao.pack()


click_oo = tk.Button(window, text="Click and *2", command=oo, font=("Comic Sans MS", 14))
click_oo.pack()

<<<<<<< HEAD:a.py
click_button = tk.Button(window, text="Click and people 2 die!", command=increment_score, font=("Comic Sans MS", 14))
click_button.pack()

click_button_10 = tk.Button(window, text="Click and people 10 die!", command=increment_score_10, font=("Comic Sans MS", 14))
=======
click_button = tk.Button(window, text="Click and Human 2 die!", command=increment_score, font=("Comic Sans MS", 14))
click_button.pack()

click_button_10 = tk.Button(window, text="Click and Human 10 die!", command=increment_score_10, font=("Comic Sans MS", 14))
>>>>>>> 3532ef7 (first commit):mygame/a.py
click_button_10.pack(pady=5)

reset_btn = tk.Button(window, text="RESET ", command=aa, font=("Comic Sans MS", 14))
reset_btn.pack(pady=20)
window.mainloop()
