from tkinter import *
from tkinter import ttk
from numpy import place
import pandas as pd
import random
import time

points_r = 0
points_w = 0
x = random.randint(0,999)
#Funções#


def random_number():
    global x
    x = random.randint(0,999)


def new_canvas():
    global x
    global german_word
    global english_word
    random_number()
    german_word = german_words[x]
    english_word = english_words[x]
    canvas.delete(ALL)
    canvas.create_image(400,300, image=card_back_image)
    canvas.create_text(400,300, text= german_word, font=("Arial",40))
    canvas.create_text(150,100, text=f"Right answers: {points_r}", font= ("Arial",20))
    canvas.create_text(650,100, text=f"Wrong answers: {points_w}", font=("Arial",20))
    canvas.grid(row=1,column=1)
    start_button.grid(row=0,column=1)



def start_time():
    t = 0
    while t < 2:
        time.sleep(1)
        t += 1
        start_button.grid_forget()
    if t==2:
        start_button.grid_forget()
        canvas.delete(ALL)
        canvas.create_image(400,300, image=card_front_image)
        canvas.create_text(400,300, text = english_word, font=("Arial",40))
        canvas.create_text(150,100, text=f"Right answers: {points_r}", font= ("Arial",20))
        canvas.create_text(650,100, text=f"Wrong answers: {points_w}", font=("Arial",20))
        canvas.grid(row=1, column=1)
        right_botton.grid(row=2,column=2)
        wrong_botton.grid(row=2,column=0)
    

def right_word():
    global points_r
    points_r += 1
    right_botton.grid_forget()
    wrong_botton.grid_forget()
    new_canvas()

def wrong_word():
    global points_w
    points_w += 1
    right_botton.grid_forget()
    wrong_botton.grid_forget()
    new_canvas()


# Criando as palavras #

df = pd.read_csv("/Users/josel/Desktop/Flash Cards/data/german_to_english.csv")
german_words = df.German.to_list()
english_words = df.English.to_list()

german_word = german_words[x]
english_word = english_words[x]

# Interface Gráfica #

window = Tk()
window.title("Flash Card app")
window.minsize(width=800, height=600)
window.config(padx=50, pady=50)

canvas = Canvas(width=800, height=600, highlightthickness=0)
card_back_image = PhotoImage(file = "/Users/josel/Desktop/Flash Cards/images/card_back.png")
card_front_image = PhotoImage(file = "/Users/josel/Desktop/Flash Cards/images/card_front.png")
right_image = PhotoImage(file = "/Users/josel/Desktop/Flash Cards/images/right.png")
wrong_image = PhotoImage(file= "/Users/josel/Desktop/Flash Cards/images/wrong.png")
canvas.create_image(400, 300, image=card_back_image)
canvas.create_text(400,300, text=german_word, font=("Arial", 40))
canvas.create_text(150,100, text=f"Right answers: {points_r}", font= ("Arial",20))
canvas.create_text(650,100, text=f"Wrong answers: {points_w}", font=("Arial",20))
canvas.grid(row=1,column=1) 

start_button = Button(text="Start", command= start_time)
start_button.grid(row=0,column=1)



right_botton = Button(image = right_image, command=right_word, height=30,width=30)


wrong_botton = Button(image = wrong_image, command=wrong_word, height=30, width=30)



window.mainloop()

