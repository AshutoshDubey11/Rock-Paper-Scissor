from tkinter import *
from tkinter import messagebox
import random


class Jajanken:
    def __init__(self):
        self.value = 0
        self.comp = 0
        self.score1 = 0
        self.score2 = 0
        self.check = 0

        self.windows = Tk()
        self.windows.title("JAN KEN ROCK")
        self.windows.minsize(width=360, height=600)
        self.windows.maxsize(width=360, height=600)
        self.windows.config(background="lightgreen")

        self.rock_image = PhotoImage(file="rock.jpg")
        self.paper_image = PhotoImage(file="paperdominator.jpg")
        self.scissor_image = PhotoImage(file="scissor.jpg")

        self.rock_up = PhotoImage(file="rockup.jpg")
        self.paper_up = PhotoImage(file="paperdominatoring.jpg")
        self.scissor_up = PhotoImage(file="scissorup.jpg")

        self.rock_small = PhotoImage(file="ROCK2.png")
        self.paper_small = PhotoImage(file="PAPER1.png")
        self.scissor_small = PhotoImage(file="SCISSOR1.png")

        self.images_human = [self.rock_image, self.paper_image, self.scissor_image]
        self.images_comp = [self.rock_up, self.paper_up, self.scissor_up]

        self.canvas = Canvas(width=360, height=500, background="lightgreen", highlightthickness=0)
        self.canvas.create_oval(-40, 200, 50, 300, fill="peachpuff")

        self.label = Label(text="", background="lightgreen", foreground="gray")
        self.label.place(x=180, y=250)

        self.canvas.pack()

        self.label1 = Label(text=self.score1, font=("ariel", 20, "bold"), foreground="red", background="peachpuff")
        self.label1.place(x=0, y=259)

        self.label2 = Label(text=self.score2, font=("ariel", 20, "bold"), foreground="blue", background="peachpuff")
        self.label2.place(x=0, y=210)

        self.result = self.canvas.create_text(180, 250, text="", font=("ariel", 25, "normal"))

        self.canvas.create_line(0, 252, 50, 252)

        def nulify():
            self.rock_button.config(command=party)
            self.paper_button.config(command=party)
            self.scissor_button.config(command=party)

        def party():
            messagebox.showinfo(title="Oops", message="Please wait for the previous round to finish.")

        def timing():

            if self.check == 1:
                pass
            else:
                self.canvas.itemconfig(self.result, text="  YOU  LOSE", fill="red")
                self.score2 += 1
                self.windows.after(3000, depth)

            self.check = 0
            self.rock_button.config(background="white")
            self.paper_button.config(background="white")
            self.scissor_button.config(background="white")

            self.label2.config(text=self.score2)

        def timer(count):
            if count >= 0:
                self.label.config(text=count, font=("ariel", 25, "bold"))

                self.windows.after(1000, timer, count-1)
            else:
                self.label.config(text="")


        def show():
            nulify()
            self.human = self.canvas.create_image(180, 390, image=self.images_human[self.value - 1])
            self.computer = self.canvas.create_image(180, 110, image=self.images_comp[self.comp - 1])

            def score():
                if self.value == self.comp:
                    self.canvas.itemconfig(self.result, text=" D R A W", fill="gray")
                elif self.value == 1 and self.comp == 3:
                    self.canvas.itemconfig(self.result, text="YOU WIN", fill="darkorange")
                    self.score1 += 1
                elif self.value == 3 and self.comp == 1:
                    self.canvas.itemconfig(self.result, text=" YOU  LOSE", fill="red")
                    self.score2 += 1
                elif self.value > self.comp:
                    self.canvas.itemconfig(self.result, text="YOU WIN", fill="darkorange")
                    self.score1 += 1
                else:
                    self.canvas.itemconfig(self.result, text=" YOU  LOSE", fill="red")
                    self.score2 += 1
                self.label2.config(text=self.score2)
                self.label1.config(text=self.score1)

            def work():
                self.canvas.delete(self.human)
                self.canvas.delete(self.computer)
                self.canvas.itemconfig(self.result, text="")

            def buttons():
                self.rock_button.config(command=rock)
                self.paper_button.config(command=paper)
                self.scissor_button.config(command=scissor)

            self.windows.after(1000, score)
            self.windows.after(5000, work)
            self.windows.after(5000, depth)
            self.windows.after(5000, buttons)

        def rock():
            nulify()
            self.check = 1
            self.value = 1
            self.comp = int(random.randint(1, 3))

            self.rock_button.config(background="orange")
            self.windows.after(3000, show)

        def paper():
            nulify()
            self.check = 1
            self.value = 2
            self.comp = int(random.randint(1, 3))

            self.paper_button.config(background="orange")
            self.windows.after(3000, show)

        def scissor():
            nulify()
            self.check = 1
            self.value = 3
            self.comp = int(random.randint(1, 3))

            self.scissor_button.config(background="orange")
            self.windows.after(3000, show)

        self.rock_button = Button(image=self.rock_small, highlightthickness=2, command=rock)
        self.rock_button.place(x=45, y=500)

        self.paper_button = Button(image=self.paper_small, highlightthickness=2, command=paper)
        self.paper_button.place(x=150, y=500)

        self.scissor_button = Button(image=self.scissor_small, highlightthickness=2, command=scissor)
        self.scissor_button.place(x=255, y=500)

        def depth():
            self.canvas.itemconfig(self.result, text="")
            timer(3)
            self.windows.after(4000, timing)

        depth()

        self.windows.mainloop()
