
from tkinter import Button, Label, OptionMenu, PhotoImage, StringVar, Tk
from base_UI import BaseUI
from brain import Difficulty

diff = Difficulty()

def startGame():
    difficulty = variable.get()
    type = variable2.get()
    if difficulty == "Easy":
        diff.changeDiffAttribute(value=0)
    elif difficulty == "Normal":
        diff.changeDiffAttribute(value=1)
    else:
        diff.changeDiffAttribute(value=2)
    if type == "True/False":
        diff.changeTypeAttribute(value="True/False")
    else:
        diff.changeTypeAttribute(value="Multiple Choice Questions")   
    baseui.destroy()
    import main

difficulty = Difficulty()

BLACK = "#171717"
GREY = "#444444"
ROSE_RED = "#DA0037"
OFF_WHITE = "#EDEDED"

APP_WIDTH = int(1080/2.5)
APP_HEIGHT = int(1920/2.5)

title_font = "Honeybee Personal Use"
type_font = "Somatic-Rounded"

baseui = BaseUI()

options = difficulty.difficulty_list

variable = StringVar()
variable.trace('w', startGame)
variable.set(f"{options[0]}")

difficulty_select_title = Label(
    text="Select Difficulty Level",
    foreground=OFF_WHITE,
    font=(title_font, 30, "normal"),
    background=BLACK,
    justify="center"
    )
difficulty_select_title.place(x=85, y=120)

dropdown = OptionMenu(baseui, variable, *options)
dropdown.config(
    width=20, 
    font=(type_font, 17, "normal"),
    background=OFF_WHITE,
    )
dropdown.place(x=57, y=190)

type_select_title = Label(
    text="Select Question Type",
    foreground=OFF_WHITE,
    font=(title_font, 30, "normal"),
    background=BLACK,
    justify="center"
    )
type_select_title.place(x=85, y=270)

options2 = difficulty.type_list 

variable2 = StringVar()
variable2.trace('w', startGame)
variable2.set(f"Select Question Type")

dropdown2 = OptionMenu(baseui, variable2, *options2)
dropdown2.config(
    width=20, 
    font=(type_font, 17, "normal"),
    background=OFF_WHITE,
    )
dropdown2.place(x=57, y=340)

pixel = PhotoImage(width=1, height=1)
next_button = Button(
    text="Next",
    image=pixel,
    font=(type_font, 20, "normal"),
    background=ROSE_RED,
    activebackground=ROSE_RED,
    width=70,
    height=40,
    compound="center",
    command=startGame
    )
next_button.place(x=175, y=500)

baseui.mainloop()
