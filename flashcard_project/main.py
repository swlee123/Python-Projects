BACKGROUND_COLOR = "#B1DDC6"
WHITE =	"#f1f0eb"
BLACK = "#000000"
INTERVAL = 3000

import tkinter as tk
import pandas
import random 
from os.path import exists



# generate random words


file_exists = exists("data/words_to_learn.csv")
if file_exists:
    vocab = pandas.read_csv("data/words_to_learn.csv")
else:
    vocab = pandas.read_csv("data/english_words.csv")

pandas.DataFrame(vocab)
a=vocab.to_dict("records")
current_card = { }
current_card = random.choice(a)


def next_card():
    global current_card
    global flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(a)
    canvas.itemconfig(card_word,text=current_card["Vocab"],fill="black")
    canvas.itemconfig(language,text="Vocab",fill="black")
    canvas.itemconfig(canvas_image, image=card_front)
    window.after(INTERVAL,func = flip_card)

def flip_card():
    global current_card
    canvas.itemconfig(card_word,text=current_card["Meaning"],fill="white")
    canvas.itemconfig(language,text="Meaning",fill="white")
    canvas.itemconfig(canvas_image, image=card_back)
    
def know_the_card():

    a.remove(current_card)
    df = pandas.DataFrame(a)
    df.to_csv("data/words_to_learn.csv", index=False)
    next_card()
    
    

# GUI interface

window = tk.Tk()
window.title("Flashy")
window.config(width=800,height=526,padx=50,pady=50,bg=BACKGROUND_COLOR)


flip_timer = window.after(INTERVAL,func = flip_card)

card_front = tk.PhotoImage(file="images/card_front.png")
card_back = tk.PhotoImage(file="images/card_back.png")

canvas = tk.Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
canvas_image = canvas.create_image(400, 263, image=card_front)
language = canvas.create_text(400,150,text="Vocab",font=("Ariel",40,"italic"),tags="lang")
card_word = canvas.create_text(400,263,text=current_card["Vocab"],font=("Ariel",60,"bold"),tags="word")
canvas.grid(column=0, row=0,columnspan=2,sticky=tk.E)

right_image = tk.PhotoImage(file="images/right.png")
right_button = tk.Button(image=right_image,command=know_the_card)
right_button.grid(column=1,row=1)

wrong_image = tk.PhotoImage(file="images/wrong.png")
wrong_button = tk.Button(image=wrong_image,command=next_card)
wrong_button.grid(column=0,row=1)

title = tk.Label()
word = tk.Label(text="Word")        








window.mainloop()


