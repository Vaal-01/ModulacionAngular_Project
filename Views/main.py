from tkinter import *
from PIL import Image,ImageTk
import random

class mainView:
    def __init__(self,window):
        #Format Window
        self.window = window
        self.window.geometry("1280x720+0+0")
        self.window.title("Laboratorio Modulación Angular - Carvajal & Salazar")
        # self.window.iconbitmap('images/icon.ico')
        self.window.resizable(False,False)
        #self.window.eval('tk::PlaceWindow . center')

        #BACKGROUND
        self.database_frame = ImageTk.PhotoImage\
            (file='Views\img\main_frame.png')
        self.image_panel = Label(self.window,image=self.database_frame)
        self.image_panel.pack(fill='both',expand='yes')

       #TITLES

        #Title 1
        self.txt = "Señal Portadora"
        self.count = 0
        self.text = ''
        self.color = ["#f29844"]
        self.heading = Label(self.window,text=self.txt, font=("yu gothic ui", 30, "bold"),bg="white",fg="black",bd=5,relief=FLAT)
        self.heading.place(x=95,y=180,width=440)
        self.heading_color()

        #Title 2
        self.txt2 = "Señal Moduladora"
        self.heading2 = Label(self.window,text=self.txt2, font=("yu gothic ui", 30, "bold"),bg="white",fg=self.color ,bd=5,relief=FLAT)
        self.heading2.place(x=758,y=180,width=440)


        #INPUTS

        #Amplitude c Label and Entry
        self.ampc_label = Label(self.window,text="Amplitud",bg="white",fg="#353534",font=("yu gothic ui", 18, "bold"))
        self.ampc_label.place(x=150, y=260)

        self.ampc_entry = Entry(self.window, relief=FLAT,bg = "white",fg ="#6b6a69",font=("yu gothic ui semibold", 14))
        self.ampc_entry.place(x=188,y=309,width=289)

        #Frequency c Label and Entry
        self.frec_label = Label(self.window, text="Frecuencia", bg="white", fg="#353534",font=("yu gothic ui", 18, "bold"))
        self.frec_label.place(x=150, y=385)

        self.frec_entry = Entry(self.window, relief=FLAT, bg="white", fg="#6b6a69", font=("yu gothic ui semibold", 14))
        self.frec_entry.place(x=188, y=426, width=289)

        #Amplitude m Label and Entry
        self.ampm_label = Label(self.window, text="Amplitud", bg="white", fg="#353534",font=("yu gothic ui", 18, "bold"))
        self.ampm_label.place(x=798, y=260)

        self.ampm_entry = Entry(self.window, relief=FLAT, bg="white", fg="#6b6a69",font=("yu gothic ui semibold", 14))
        self.ampm_entry.place(x=845, y=309, width=289)

        #Frequency m Label and Entry
        self.frem_label = Label(self.window, text="Frecuencia", bg="white", fg="#353534",font=("yu gothic ui", 18, "bold"))
        self.frem_label.place(x=798, y=385)

        self.frem_entry = Entry(self.window, relief=FLAT, bg="white", fg="#6b6a69", font=("yu gothic ui semibold", 14))
        self.frem_entry.place(x=845, y=422, width=289)

        #BUTTON
        self.submit = ImageTk.PhotoImage\
            (file='Views\img\calculatebtn.png')
        self.submit_button = Button(self.window,image=self.submit, relief = "flat", borderwidth=0, background="#FFE65B",activebackground="#FFE65B", cursor="hand2")
        self.submit_button.place(x=477,y=608)



    def heading_color(self):
        fg = random.choice(self.color)
        self.heading.config(fg=fg)
        self.heading.after(50, self.heading_color)


def win():
    window = Tk()
    mainView(window)
    window.mainloop()

if __name__ == '__main__':
    win()