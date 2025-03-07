from tkinter import *
from original import Jajanken


def get():
    windows.destroy()
    janken = Jajanken()


windows = Tk()
windows.title("JAJANKEN")
windows.minsize(width=360, height=600)
windows.maxsize(width=360, height=600)

screen = PhotoImage(file="front1.png")
rock_small = PhotoImage(file="ROCK2.png")
paper_small = PhotoImage(file="PAPER1.png")
scissor_small = PhotoImage(file="SCISSOR1.png")

canvas = Canvas(width=360, height=600, background="lightgreen")
canvas.create_image(180, 200, image=screen)
canvas.create_image(50, 450, image=rock_small)
canvas.create_image(315, 450, image=paper_small)
canvas.create_image(180, 565, image=scissor_small)
canvas.pack()

play_button = Button(command=get, background="gold", foreground="red", text="PLAY", font=("ariel", 20, "bold"))
play_button.place(x=130, y=450)

mainloop()
