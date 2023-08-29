import turtle
import pandas as pd
from tkinter import *
from tkinter import messagebox

df = pd.read_csv("50_states.csv")

screen = turtle.Screen()
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
turtle.penup()

score = 0
answers = []

# Loop through dataframe and track game progress

# Winner alert box
while len(answers) < 50:
    screen.title("U.S. States Game")
    if score == 50:
        top = Tk()
        top.geometry("100x100")
        messagebox.showinfo("Winner, Winner", "Chicken Dinner")
        top.mainloop()
# Make the input popup
    answer_state = screen.textinput(title=f"{score}/50 Guess the State", prompt="What is A U.S. State?").title()

    if answer_state == "Exit":
        break
# put correct answers on map
    if answer_state in df.values and answer_state not in answers:
        row_num = df[df["state"] == answer_state].index
        x = int(df.iloc[row_num]["x"])
        y = int(df.iloc[row_num]["y"])
        # print(x, y)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(x, y)
        t.write(answer_state)
        score += 1
        answers.append(answer_state)

# Create a csv of states missed
states_to_learn = []
for state in df.state:
    if state not in answers:
        states_to_learn.append(state)
states_df = pd.DataFrame(states_to_learn)

states_df.to_csv("states_to_learn.csv")
