
from tkinter import Button, Label, PhotoImage
from base_UI import BaseUI
from PIL import Image, ImageTk
from brain import Questions

question = Questions()

BLACK = "#171717"
GREY = "#444444"
ROSE_RED = "#DA0037"
OFF_WHITE = "#EDEDED"

APP_WIDTH = int(1080/2.5)
APP_HEIGHT = int(1920/2.5)

title_font = "Honeybee Personal Use"
type_font = "Somatic-Rounded"

baseui = BaseUI()

image_0 = Image.open("Images/paper.png")
image_0_resized = image_0.resize((int(1920/4.5), int(1580/4.5)))
paper_img = ImageTk.PhotoImage(image_0_resized)
question_area = baseui.canvas.create_image(
    (APP_WIDTH/2), (APP_HEIGHT/2)-80,
    image = paper_img
    )

#question_text
image_2 = Image.open("Images/Question.png")
image_2_resized = image_2.resize((int(544/4), int(68/4)))
question_logo = ImageTk.PhotoImage(image_2_resized)
question_logo_canvas = baseui.canvas.create_image(APP_WIDTH/2, (APP_HEIGHT/2)-205, image=question_logo)

question_text = question.displayQuestions()
# question_text_canvas = baseui.canvas.create_text(
#     APP_WIDTH/2, (APP_HEIGHT/2), 
#     text=question_text, 
#     foreground="black",
#     font=("Arial", 25, "bold")
#     )
question = Label(
    text=question_text, 
    foreground="black",
    font=(type_font, 20, "normal"),
    justify="center",
    wraplength=(APP_WIDTH/2)+100
    )
question.place(x=70, y=230)

baseui.mainloop()