from tkinter import END, MULTIPLE, Button, Label, Listbox, PhotoImage
from base_UI import BaseUI
from brain import Category, Questions

category = Category()
questions = Questions()
category.getCategory()

def getDifficulty():
    baseui.destroy()
    import difficulty

def selectedCat(event):
    selection_list = []
    category.selected_list = selection_list
    for i in listbox.curselection():
        item = listbox.get(i)
        if item in selection_list:
            pass
        else:
            selection_list.append(item)
    print(category.selected_list)
    print(selection_list)

def selectAll():
    category.changeSelAttribute(value=1)
    listbox.select_set(0, END)

def clearAll():
    category.select_all = 0
    listbox.select_clear(0, END)
    
BLACK = "#171717"
GREY = "#444444"
ROSE_RED = "#DA0037"
OFF_WHITE = "#EDEDED"

APP_WIDTH = int(1080/2.5)
APP_HEIGHT = int(1920/2.5)

title_font = "Honeybee Personal Use"
type_font = "Somatic-Rounded"

baseui = BaseUI()

choose_heading = Label(
    text="<Question Category>",
    justify="center", 
    font=(title_font, 35, "normal"), 
    foreground=OFF_WHITE,
    background=BLACK,
    )
choose_heading.place(x=50, y=100)

listbox = Listbox(
    height=20, 
    width=32,
    foreground="white",
    background=GREY,
    highlightcolor=OFF_WHITE,
    highlightbackground=OFF_WHITE,
    selectbackground=ROSE_RED,
    highlightthickness=2,
    selectmode=MULTIPLE,
    font=(type_font, 14, "normal")
    )
listbox.bind("<<ListboxSelect>>", selectedCat)
listbox.place(x=36, y=210)

for x in range(len(category.category_list)):
    listbox.insert(x, category.category_list[x])

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
    command=getDifficulty
    )
next_button.place(x=175, y=705)

pixel_1 = PhotoImage(width=1, height=1)
select_all = Button(
    image=pixel_1,
    text="Select All",
    font=(type_font, 10, "normal"),
    background=OFF_WHITE,
    activebackground=OFF_WHITE,
    foreground=BLACK,
    compound="center",
    command=selectAll,
    width=80,
    height=20
    )
select_all.place(x=36, y=180)

pixel_2 = PhotoImage(width=1, height=1)
clear_all = Button(
    image=pixel_2,
    text="Clear All",
    font=(type_font, 10, "normal"),
    background=ROSE_RED,
    activebackground=ROSE_RED,
    foreground=OFF_WHITE,
    compound="center",
    command=clearAll,
    width=80,
    height=20
    )
clear_all.place(x=125, y=180)

baseui.mainloop()