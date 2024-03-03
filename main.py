from tkinter import *
import pandas
import random
from config import *

window = Tk()
window.title(WINDOW_TITLE)
window.config(padx=PADDING_X, pady=PADDING_Y, bg=BACKGROUND_COLOR)

current_row = {}


def correct_func():
    words_dict.remove(current_row)
    data_to_save = pandas.DataFrame(words_dict)
    data_to_save.to_csv("data/words_to_learn.csv", index=False)
    new_card()


def new_card():
    global current_row, after_id
    window.after_cancel(id=after_id)
    canvas.itemconfig(card_image_id, image=IMG_card_front)
    current_row = random.choice(words_dict)
    new_word = current_row["Japanese"]
    canvas.itemconfig(country_id, text="Japanese", fill="black")
    canvas.itemconfig(word_id, text=new_word, fill="black")
    after_id = window.after(DELAY, flip_the_card)


def flip_the_card():
    canvas.itemconfig(card_image_id, image=IMG_card_back)
    canvas.itemconfig(country_id, text="English", fill="white")
    canvas.itemconfig(word_id, text=current_row["English"], fill="white")
    window.after_cancel(id=after_id)


IMG_card_front = PhotoImage(file="images/card_front.png")
IMG_card_back = PhotoImage(file="images/card_back.png")
IMG_button_wrong = PhotoImage(file="images/wrong.png")
IMG_button_right = PhotoImage(file="images/right.png")

canvas = Canvas(width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg=BACKGROUND_COLOR, highlightthickness=0)
card_image_id = canvas.create_image(WINDOW_WIDTH/2, WINDOW_HEIGHT/2, image=IMG_card_front)
canvas.grid(row=0, column=0, columnspan=2)
country_id = canvas.create_text(WINDOW_WIDTH/2, WINDOW_HEIGHT/2-TEXT_OFFSET, text="", fill="black", font=COUNTRY_FONT)
word_id = canvas.create_text(WINDOW_WIDTH/2, WINDOW_HEIGHT/2, text="", fill="black", font=WORD_FONT)

BTN_wrong = Button(image=IMG_button_wrong, highlightthickness=0, command=new_card)
BTN_wrong.grid(row=1, column=0)
BTN_right = Button(image=IMG_button_right, highlightthickness=0, command=correct_func)
BTN_right.grid(row=1, column=1)

try:
    words_data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    words_data = pandas.read_csv("data/japanese_words.csv")
words_dict = words_data.to_dict(orient="records")

after_id = window.after(DELAY, flip_the_card)
new_card()

window.mainloop()
