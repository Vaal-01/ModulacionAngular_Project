from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import graphCarrierView
from graphics import ModulatinggraphFM
from graphics import ModulatinggraphPM
from graphics import Carriergraph
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
            (file='img\main_frame.png')
        self.image_panel = Label(self.window,image=self.database_frame)
        self.image_panel.pack(fill='both',expand='yes')

       #TITLES

        #Title 1
        self.txt = "Señal Portadora"
        self.count = 0
        self.text = ''
        self.color = ["#f29844"]
        self.heading = Label(self.window,text=self.txt, font=("yu gothic ui", 30, "bold"),bg="white",fg="black",bd=5,relief=FLAT)
        self.heading.place(x=125,y=185,width=300)
        self.heading_color()

        #Title 2
        self.txt2 = "Señal Moduladora"
        self.heading2 = Label(self.window,text=self.txt2, font=("yu gothic ui", 30, "bold"),bg="white",fg=self.color ,bd=5,relief=FLAT)
        self.heading2.place(x=825,y=185,width=350)
        
        #Title 3
        self.txt3 = "Datos Generales"
        self.heading3 = Label(self.window,text=self.txt3, font=("yu gothic ui", 20, "bold"),bg="white",fg=self.color ,bd=5,relief=FLAT)
        self.heading3.place(x=537,y=185,width=198)

        #INPUTS

        #Amplitude c Label and Entry
        self.ampc_label = Label(self.window,text="Amplitud",bg="white",fg="#353534",font=("yu gothic ui", 18, "bold"))
        self.ampc_label.place(x=150, y=260)

        self.ampc_entry = Entry(self.window, relief=FLAT,bg = "white",fg ="#6b6a69",font=("yu gothic ui semibold", 14))
        self.ampc_entry.place(x=188,y=304,width=205)

        #Frequency c Label and Entry
        self.frec_label = Label(self.window, text="Frecuencia", bg="white", fg="#353534",font=("yu gothic ui", 18, "bold"))
        self.frec_label.place(x=150, y=370)

        self.frec_entry = Entry(self.window, relief=FLAT, bg="white", fg="#6b6a69", font=("yu gothic ui semibold", 14))
        self.frec_entry.place(x=188, y=419, width=205)

        #Amplitude m Label and Entry
        self.ampm_label = Label(self.window, text="Amplitud", bg="white", fg="#353534",font=("yu gothic ui", 18, "bold"))
        self.ampm_label.place(x=870, y=260)

        self.ampm_entry = Entry(self.window, relief=FLAT, bg="white", fg="#6b6a69",font=("yu gothic ui semibold", 14))
        self.ampm_entry.place(x=925, y=303, width=205)

        #Frequency m Label and Entry
        self.frem_label = Label(self.window, text="Frecuencia", bg="white", fg="#353534",font=("yu gothic ui", 18, "bold"))
        self.frem_label.place(x=870, y=370)

        self.frem_entry = Entry(self.window, relief=FLAT, bg="white", fg="#6b6a69", font=("yu gothic ui semibold", 14))
        self.frem_entry.place(x=925, y=418, width=205)

        #Modulation index Label and Entry
        self.modi_label = Label(self.window, text="Índice de\n Modulación", bg="white", fg="#353534",font=("yu gothic ui", 17, "bold"))
        self.modi_label.place(x=565, y=235)

        self.modi_entry = Entry(self.window, relief=FLAT, bg="white", fg="#6b6a69",font=("yu gothic ui semibold", 14))
        self.modi_entry.place(x=565, y=301, width=150)

        #Load Resistance Label and Entry
        self.lres_label = Label(self.window, text="Resistencia\n de Carga", bg="white", fg="#353534",font=("yu gothic ui", 17, "bold"))
        self.lres_label.place(x=573, y=345)

        self.lres_entry = Entry(self.window, relief=FLAT, bg="white", fg="#6b6a69", font=("yu gothic ui semibold", 14))
        self.lres_entry.place(x=565, y=418, width=150)
       
        #Additional Label
        self.adl_label = Label(self.window, text="Estos valores se tomarán para\n ambas señales. Si no escribe\n ninguno, se tomarán por defecto. ", bg="white", fg="#595958",font=("yu gothic ui", 9, "bold"))
        self.adl_label.place(x=540, y=480)
       
        #BUTTON
        self.submit = ImageTk.PhotoImage\
            (file='img\calculatebtn.png')
        self.submit_button = Button(self.window,image=self.submit, relief = "flat", borderwidth=0, background="#FFE65B",activebackground="#FFE65B", cursor="hand2", command=self.calculate)
        self.submit_button.place(x=465,y=608)

    def heading_color(self):
        fg = random.choice(self.color)
        self.heading.config(fg=fg)
        self.heading.after(50, self.heading_color)

    def calculate(self):
        ampc = self.ampc_entry.get()
        frec = self.frec_entry.get()
        ampm = self.ampm_entry.get()
        frem = self.frem_entry.get()

        #Null validation 
        if ampc == "" or frec == "" or ampm == "" or frem == "":
            messagebox.showerror("Incompleto", "Por favor, Ingresa todos los datos solicitados")
        else:
            try:
                if float(ampc) and float(frec) and float(ampm) and float(frem): 
                    Carriergraph(ampc,frec)
                    ModulatinggraphFM(ampm, frem)
                    ModulatinggraphPM(ampm,frem)
                    win = Toplevel()
                    graphCarrierView.graphCarrierView(win)
                    self.window.withdraw()
                    win.deiconify()
                    #mostrarCalculos(ampc,frec,ampm,frem)
            except (ValueError):
                messagebox.showerror("Error", "Revisa que las entradas sean un números. Si tu entrada es un número decimal escribe (.) punto para separar")


def win():
    window = Tk()
    mainView(window)
    window.mainloop()

if __name__ == '__main__':
    win()