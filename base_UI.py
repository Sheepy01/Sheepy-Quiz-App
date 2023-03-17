
from tkinter import Button, Canvas, PhotoImage, Tk, Radiobutton
from PIL import Image, ImageTk

class BaseUI(Tk):

    def __init__(self):
        super().__init__()
        self.BLACK = "#171717"
        self.GREY = "#444444"
        self.ROSE_RED = "#DA0037"
        self.OFF_WHITE = "#EDEDED"
        self.APP_WIDTH = int(1080/2.5)
        self.APP_HEIGHT = int(1920/2.5)
        self.title_font = "Honeybee Personal Use"
        self.type_font = "Somatic-Rounded"
        self.title("Sheppy Quiz App")
        self.geometry(f"{self.APP_WIDTH}x{self.APP_HEIGHT}")
        self.canvas = Canvas(width=int(self.APP_WIDTH), height=int(self.APP_HEIGHT), background=self.BLACK, highlightthickness=0)
        self.canvas.place(x=0, y=0)
        
        #red_circle
        self.image_0 = Image.open("Images/Circle.png")
        self.image_0_resized = self.image_0.resize((int(320/7), int(322/7)))
        self.circle = ImageTk.PhotoImage(self.image_0_resized)
        self.cicle_canvas = self.canvas.create_image(
            (self.APP_WIDTH/2)-180, (self.APP_HEIGHT/2)-305,
            image=self.circle
            )

        #sheep_logo
        self.image_1 = Image.open("Images/Logo.png")
        self.image_1_resised = self.image_1.resize((int(1011/20), int(973/20)))
        self.sheep_logo = ImageTk.PhotoImage(self.image_1_resised)
        self.sheep_logo_canvas = self.canvas.create_image((self.APP_WIDTH/2)-180, (self.APP_HEIGHT/2)-350, image=self.sheep_logo)

        #sheep_text
        self.title = self.canvas.create_text(
            (self.APP_WIDTH/2)-180, (self.APP_HEIGHT/2)-310, 
            text="Sheepy", 
            font=(self.title_font, 20, "normal"), 
            fill=self.OFF_WHITE
            )

        #question_text
        self.image_2 = Image.open("Images/Question.png")
        self.image_2_resized = self.image_2.resize((int(544/13), int(68/13)))
        self.question_logo = ImageTk.PhotoImage(self.image_2_resized)
        self.question_logo_canvas = self.canvas.create_image((self.APP_WIDTH/2)-180, (self.APP_HEIGHT/2)-290, image=self.question_logo)

class AnswerUI():
    def __init__(self):
        self.BLACK = "#171717"
        self.GREY = "#444444"
        self.ROSE_RED = "#DA0037"
        self.OFF_WHITE = "#EDEDED"
        self.APP_WIDTH = int(1080/2.5)
        self.APP_HEIGHT = int(1920/2.5)
        self.title_font = "Honeybee Personal Use"
        self.type_font = "Somatic-Rounded"

    def answerTypeTrueFalse(self):
        #correct
        image_3 = Image.open("Images/Correct.png")
        image_3_resized = image_3.resize((int(2580/14), int(2580/14)))
        correct_logo = ImageTk.PhotoImage(image_3_resized)
        correct_logo_button = Button(
            image=correct_logo,
            background=self.BLACK,
            activebackground=self.BLACK,
            highlightthickness=0
            )
        correct_logo_button.place(
            x=(self.APP_WIDTH/2) , y=(self.APP_HEIGHT/2)+130
            )

        #incorrect
        image_4 = Image.open("Images/Incorrect.png")
        image_4_resized = image_4.resize((int(2580/14), int(2580/14)))
        incorrect_logo = ImageTk.PhotoImage(image_4_resized)
        incorrect_logo_button = Button(
            image=incorrect_logo,
            background=self.BLACK,
            activebackground=self.BLACK,
            highlightthickness=0
            )
        incorrect_logo_button.place(
            x=(self.APP_WIDTH/2)-190 , y=(self.APP_HEIGHT/2)+130
            )

    def answerTypeMCQ(self, radio1, radio2):
        first_radio = Radiobutton(text=radio1)
        first_radio.place(x=(self.APP_WIDTH/2)-190, y=(self.APP_HEIGHT/2)+130)