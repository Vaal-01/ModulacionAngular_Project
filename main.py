from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import graphCarrierView
from graphics import ModulatinggraphFM , ModulatinggraphPM, ModulatedgraphFM, ModulatedgraphPM, Carriergraph
from operations import calculationsFM , calculationsPM
from bessel import getJn
from spectrums import graphicspectrumFM, graphicspectrumPM 
import random

class main:
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
        self.heading2.place(x=820,y=185,width=350)
        
        #Title 3
        self.txt3 = "Datos\n Adicionales"
        self.heading3 = Label(self.window,text=self.txt3, font=("yu gothic ui", 20, "bold"),bg="white",fg=self.color ,bd=5,relief=FLAT)
        self.heading3.place(x=537,y=180,width=198)

        #INPUTS

        #Amplitude c Label and Entry
        self.ampc_label = Label(self.window,text="Amplitud [v]",bg="white",fg="#353534",font=("yu gothic ui", 18, "bold"))
        self.ampc_label.place(x=150, y=260)

        self.ampc_entry = Entry(self.window, relief=FLAT,bg = "white",fg ="#6b6a69",font=("yu gothic ui semibold", 14))
        self.ampc_entry.place(x=186,y=304,width=205)

        #Frequency c Label and Entry
        self.frec_label = Label(self.window, text="Frecuencia [Hz]", bg="white", fg="#353534",font=("yu gothic ui", 18, "bold"))
        self.frec_label.place(x=150, y=370)

        self.frec_entry = Entry(self.window, relief=FLAT, bg="white", fg="#6b6a69", font=("yu gothic ui semibold", 14))
        self.frec_entry.place(x=186, y=417, width=205)

        #Amplitude m Label and Entry
        self.ampm_label = Label(self.window, text="Amplitud [v]", bg="white", fg="#353534",font=("yu gothic ui", 16, "bold"))
        self.ampm_label.place(x=855, y=260)

        self.ampm_entry = Entry(self.window, relief=FLAT, bg="white", fg="#6b6a69",font=("yu gothic ui semibold", 14))
        self.ampm_entry.place(x=905, y=304, width=205)

        #Frequency m Label and Entry
        self.frem_label = Label(self.window, text="Frecuencia [Hz]", bg="white", fg="#353534",font=("yu gothic ui", 16, "bold"))
        self.frem_label.place(x=855, y=370)

        self.frem_entry = Entry(self.window, relief=FLAT, bg="white", fg="#6b6a69", font=("yu gothic ui semibold", 14))
        self.frem_entry.place(x=905, y=417, width=205)

        #Modulation index Frequency Label and Entry
        self.modif_label = Label(self.window, text="Índice de Modulación\n (Frecuencia)", bg="white", fg="#353534",font=("yu gothic ui", 12, "bold"))
        self.modif_label.place(x=553, y=324)

        self.modif_entry = Entry(self.window, relief=FLAT, bg="white", fg="#6b6a69",font=("yu gothic ui semibold", 14))
        self.modif_entry.place(x=558, y=368, width=150)

        #Modulation index phase Label and Entry
        self.modip_label = Label(self.window, text="Índice de Modulación\n (Fase) [rad]", bg="white", fg="#353534",font=("yu gothic ui", 12, "bold"))
        self.modip_label.place(x=553, y=400)

        self.modip_entry = Entry(self.window, relief=FLAT, bg="white", fg="#6b6a69",font=("yu gothic ui semibold", 14))
        self.modip_entry.place(x=558, y=445, width=150)

        #Load Resistance Label and Entry
        self.lres_label = Label(self.window, text="Resistencia de Carga* [ohm]", bg="white", fg="#353534",font=("yu gothic ui", 12, "bold"))
        self.lres_label.place(x=532, y=265)

        self.lres_entry = Entry(self.window, relief=FLAT, bg="white", fg="#6b6a69", font=("yu gothic ui semibold", 14))
        self.lres_entry.place(x=558, y=290, width=150)
       
        #Additional Label
        self.adl_label = Label(self.window, text="*Este valor se tomará para\n ambas señales. Si no escribe\n ninguno, se tomará por defecto. ", bg="white", fg="#595958",font=("yu gothic ui", 9, "bold"))
        self.adl_label.place(x=540, y=495)
       
        #BUTTON

        #Calculate
        self.submit = ImageTk.PhotoImage\
            (file='img\calculatebtn.png')
        self.submit_button = Button(self.window,image=self.submit, relief = "flat", borderwidth=0, background="#FFE65B",activebackground="#FFE65B", cursor="hand2", command=self.calculate)
        self.submit_button.place(x=465,y=608)

        #Exit
        self.exit_img = ImageTk.PhotoImage \
            (file='img\sbtnexit.png')
        self.exit_button = Button(self.window, image=self.exit_img, relief="flat", activebackground="#FFF157", borderwidth=0, background="#FFF157", cursor="hand2", command=self.click_exit)
        self.exit_button.place(x=1200, y=25)

    def heading_color(self):
        fg = random.choice(self.color)
        self.heading.config(fg=fg)
        self.heading.after(50, self.heading_color)

    def click_exit(self):
        ask = messagebox.askyesnocancel("Confirmación", "¿Estás seguro que quieres salir?")
        if ask is True:
            self.window.quit()    

    def calculate(self):
        ampc = self.ampc_entry.get()
        frec = self.frec_entry.get()
        ampm = self.ampm_entry.get()
        frem = self.frem_entry.get()
        modif = self.modif_entry.get()
        modip = self.modip_entry.get()
        r = self.lres_entry.get()

        #Null validation 
        if ampc == "" or frec == "" or ampm == "" or frem == "" or modif == "" or modip == "":
            messagebox.showerror("Incompleto", "Por favor, Ingresa todos los datos solicitados")
        else:
            try:
                if r == "" :
                    messagebox.showinfo("Incompleto", "No has introducido la resistencia de carga, se tomará por defecto un valor de 12 ohms")
                    r=12

                if float(ampc) and float(frec) and float(ampm) and float(frem) and float(modif) and float(modip) and float(r): 
                    global  paresF_freq, paresF_phas
                    #Graphs
                    Carriergraph(ampc,frec)
                    ModulatinggraphFM(ampm, frem)
                    ModulatinggraphPM(ampm,frem)
                    messagebox.showinfo("Cargando", "Espera un momento, por favor")
                    ModulatedgraphFM(ampc,frec,modif,frem)
                    ModulatedgraphPM(ampc,frec,modip,frem)
                    #calculations
                    calculationsFM(modif,ampm,frem,ampc,r)
                    calculationsPM(modip,ampm,frem,ampc,r)
                    #Spectrum
                    paresF_freq = getJn(modif,ampc)
                    paresF_phas = getJn(modip,ampc)
                    graphicspectrumFM(paresF_freq)
                    graphicspectrumPM(paresF_phas)
                    #Cambio de vista
                    win = Toplevel()
                    graphCarrierView.graphCarrierView(win)
                    self.window.withdraw()
                    win.deiconify()
            except (ValueError):
                messagebox.showerror("Error", "Revisa que las entradas sean un números. Si tu entrada es un número decimal escribe (.) punto para separar")


def win():
    window = Tk()
    main(window)
    window.mainloop()

if __name__ == '__main__':
    win()