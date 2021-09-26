import tkinter
import PIL
from PIL import ImageTk
from PIL import Image
import random

# Initialisation of window
window = tkinter.Tk()
window.geometry('400x400')
window.title('Dermots Dice Roll')


l0 = tkinter.Label(window, text="")
l0.pack()


l1 = tkinter.Label(window, text="Hello from Dermot!",
                   fg="light green", bg="dark green",
                   font="Times_New_Roman 16 ")
l1.pack()

# images provided for GUI to visualise the  dice roll
dice = ['die1.PNG', 'die2.PNG', 'die3.PNG', 'die4.PNG', 'die5.PNG', 'die6.PNG']
diceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))

label1 = tkinter.Label(window, image=diceImage)
label1.image = diceImage

label1.pack(expand=True)


# functionality of the dice-rolling
def rolling_dice():
    diceImage = ImageTk.PhotoImage(Image.open(random.choice(dice)))

    label1.configure(image=diceImage)

    label1.image = diceImage


# interface for the button
button = tkinter.Button(window, text="Go on have a roll!!",
                        fg='blue', command=rolling_dice)
button.pack(expand=True)

# entry point to start program
window.mainloop()
