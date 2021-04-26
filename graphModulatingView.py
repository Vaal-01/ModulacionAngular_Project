from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import graphCarrierView
import graphModulatedView
import random

class graphModulatingView:
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
            (file='img\graphsmodra_frame.png')
        self.image_panel = Label(self.window,image=self.database_frame)
        self.image_panel.pack(fill='both',expand='yes')

        #LABELS

        #Signal FM
        self.graph1 = ImageTk.PhotoImage\
            (file='img\graphicModraFM.png')
        self.graph1_label = Label(self.window,image= self.graph1,bg="white",fg="#353534",font=("yu gothic ui", 18, "bold"))
        self.graph1_label.place(x=25, y=145)

        #Signal PM
        self.graph2 = ImageTk.PhotoImage\
            (file='img\graphicModraPM.png')
        self.graph2_label = Label(self.window,image= self.graph2,bg="white",fg="#353534",font=("yu gothic ui", 18, "bold"))
        self.graph2_label.place(x=655, y=145)

        #BUTTON
        self.next = ImageTk.PhotoImage\
            (file='img\sbtnnext1.png')
        self.next_button = Button(self.window,image=self.next, relief = "flat", borderwidth=0, background="#FFE65B",activebackground="#FFE65B", cursor="hand2", command=self.funnext)
        self.next_button.place(x=980,y=620)

        self.returnbtn = ImageTk.PhotoImage\
            (file='img\sbtnreturn1.png')
        self.returnbtn_button = Button(self.window,image=self.returnbtn, relief = "flat", borderwidth=0, background="#FEC667",activebackground="#FEC667", cursor="hand2", command=self.funreturn)
        self.returnbtn_button.place(x=5,y=620)

    def funnext(self):
        win = Toplevel()
        graphModulatedView.graphModulatedView(win)
        self.window.withdraw()
        win.deiconify()

    def funreturn(self):
        win = Toplevel()
        graphCarrierView.graphCarrierView(win)
        self.window.withdraw()
        win.deiconify()
        

def win():
    window = Tk()
    graphModulatingView(window)
    window.mainloop()

if __name__ == '__main__':
    win()