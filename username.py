
from tkinter import Button, Canvas, Entry, Label, PhotoImage, Tk
from PIL import Image, ImageTk
from base_UI import BaseUI

def getCategory():
    baseui.destroy()
    import category

BLACK = "#171717"
GREY = "#444444"
ROSE_RED = "#DA0037"
OFF_WHITE = "#EDEDED"

APP_WIDTH = int(1080/2.5)
APP_HEIGHT = int(1920/2.5)

title_font = "Honeybee Personal Use"
type_font = "Somatic-Rounded"

baseui = BaseUI()

username_tag = baseui.canvas.create_text(
    APP_WIDTH/2, (APP_HEIGHT/2)-170, 
    text="A Nice Username!", 
    fill=OFF_WHITE,
    font=(title_font, 40, "normal")
    )

enter_username = baseui.canvas.create_text(
    (APP_WIDTH/2)-107, (APP_HEIGHT/2)-100, 
    text="Enter username:", 
    fill=OFF_WHITE,
    font=(type_font, 15, "normal")
    )

username_entry = Entry(width=13, font=(type_font, 35, "normal"))
username_entry.place(x=35, y=300)

username_rules = Label(
    text="-Username should contain a mix of characters and digits", 
    font=("Arial", 10, "normal"),
    background=BLACK,
    foreground="red"
    )
username_rules.place(x=30, y=370)

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
    command=getCategory
    )
next_button.place(x=175, y=450)

baseui.mainloop()