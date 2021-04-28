from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import graphSpectrumsView
import dataView
from operations import getCarrierPM, getCarrierFM, getComponentsFM, getComponentsPM, getLateralFM, getLateralPM


class lateralView:

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
            (file='img\lateral_frame.png')
        self.image_panel = Label(self.window,image=self.database_frame)
        self.image_panel.pack(fill='both',expand='yes')

        #LABELS

        #Components FM 
        self.comf_label = Label(self.window, text=getComponentsFM(), bg="white", fg="#353534",font=("yu gothic ui", 18, "bold"))
        self.comf_label.place(x=172, y=278)

        #Components PM 
        self.comp_label = Label(self.window, text=getComponentsPM(), bg="white", fg="#353534",font=("yu gothic ui", 18, "bold"))
        self.comp_label.place(x=172, y=493)

        #Carrier FM 
        self.carf_label = Label(self.window, text=getCarrierFM(), bg="white", fg="#353534",font=("yu gothic ui", 18, "bold"))
        self.carf_label.place(x=377, y=265)

        #Carrier PM 
        self.carp_label = Label(self.window, text=getCarrierPM(), bg="white", fg="#353534",font=("yu gothic ui", 18, "bold"))
        self.carp_label.place(x=375, y=483)

        #Components FM 
        self.carf_label = Label(self.window, text=getLateralFM(), bg="white", fg="#353534",font=("yu gothic ui", 18, "bold"))
        self.carf_label.place(x=475, y=265)

        #Components PM 
        self.carp_label = Label(self.window, text=getLateralPM(), bg="white", fg="#353534",font=("yu gothic ui", 18, "bold"))
        self.carp_label.place(x=475, y=483)

        #BUTTON
        self.next = ImageTk.PhotoImage\
            (file='img\sbtnnext1.png')
        self.next_button = Button(self.window,image=self.next, relief = "flat", borderwidth=0, background="#FFE65B",activebackground="#FFE65B", cursor="hand2", command=self.funnext)
        self.next_button.place(x=980,y=620)

        self.returnbtn = ImageTk.PhotoImage\
            (file='img\sbtnreturn1.png')
        self.returnbtn_button = Button(self.window,image=self.returnbtn, relief = "flat", borderwidth=0, background="#FEC667",activebackground="#FEC667", cursor="hand2", command=self.funreturn)
        self.returnbtn_button.place(x=5,y=620)

        #Exit
        self.exit_img = ImageTk.PhotoImage \
            (file='img\sbtnexit.png')
        self.exit_button = Button(self.window, image=self.exit_img, relief="flat", activebackground="#FFF157", borderwidth=0, background="#FFF157", cursor="hand2", command=self.click_exit)
        self.exit_button.place(x=1200, y=25)
        
    def funnext(self):
        win = Toplevel()
        graphSpectrumsView.graphSpectrumsView(win)
        self.window.withdraw()
        win.deiconify()

    def funreturn(self):
        win = Toplevel()
        dataView.dataView(win)
        self.window.withdraw()
        win.deiconify()
    
    def click_exit(self):
        ask = messagebox.askyesnocancel("Confirmación", "¿Estás seguro que quieres salir?")
        if ask is True:
            self.window.quit()   

def win():
    window = Tk()
    lateralView(window)
    window.mainloop()

if __name__ == '__main__':
    win()
