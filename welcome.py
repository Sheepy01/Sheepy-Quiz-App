
from tkinter import Button, Canvas, PhotoImage, Tk
from PIL import Image, ImageTk

def getUsername():
    window.destroy()
    import username

BLACK = "#171717"
GREY = "#444444"
ROSE_RED = "#DA0037"
OFF_WHITE = "#EDEDED"

APP_WIDTH = int(1080/2.5)
APP_HEIGHT = int(1920/2.5)

title_font = "Honeybee Personal Use"
type_font = "Somatic-Rounded"

window = Tk()
window.title("Sheppy Quiz App")
window.geometry(f"{APP_WIDTH}x{APP_HEIGHT}")

canvas = Canvas(width=APP_WIDTH, height=APP_HEIGHT, background=BLACK, highlightthickness=0)
canvas.place(x=0, y=0)

#red_circle
image_0 = Image.open("Images/Circle.png")
image_0_resized = image_0.resize((int(320/2), int(322/2)))
circle = ImageTk.PhotoImage(image_0_resized)
circle_canvas = canvas.create_image(
    APP_WIDTH/2, APP_HEIGHT/2,
    image=circle
    )

#sheep_logo
image_1 = Image.open("Images/Logo.png")
image_1_resised = image_1.resize((int(1011/7.5), int(973/7.5)))
sheep_logo = ImageTk.PhotoImage(image_1_resised)
sheep_logo_canvas = canvas.create_image(APP_WIDTH/2, (APP_HEIGHT/2)-125, image=sheep_logo)

#sheep_text
title = canvas.create_text(
    APP_WIDTH/2, (APP_HEIGHT/2)-15, 
    text="Sheepy", 
    font=(title_font, 65, "normal"), 
    fill=OFF_WHITE
    )

#question_text``
image_2 = Image.open("Images/Question.png")
image_2_resized = image_2.resize((int(544/4), int(68/4)))
question_logo = ImageTk.PhotoImage(image_2_resized)
question_logo_canvas = canvas.create_image(APP_WIDTH/2, (APP_HEIGHT/2)+50, image=question_logo)

#enter_button
pixel = PhotoImage(width=1, height=1)
enter = Button(
    text="Enter", 
    font=(type_font, 30, "normal"), 
    foreground=OFF_WHITE, 
    background=ROSE_RED,
    activebackground=ROSE_RED, 
    image=pixel, 
    compound="center",
    width=125,
    height=50,
    command=getUsername
    )
enter.place(x=(APP_WIDTH/2)-65, y=(APP_HEIGHT/2)+250)

window.mainloop()
