from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import graphSpectrumsView
import main
from operations import getCarrierPower, getTotalPowerFM, getTotalPowerPM, getLateralPowerFM, getLateralPowerPM

class powerView:

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
            (file='img\power_frame.png')
        self.image_panel = Label(self.window,image=self.database_frame)
        self.image_panel.pack(fill='both',expand='yes')

        #LABELS

        #Carrier Power 
        self.cpow_label = Label(self.window, text=str(getCarrierPower()) + " W", bg="white", fg="#353534",font=("yu gothic ui", 18, "bold"))
        self.cpow_label.place(x=130, y=392)

        #Total Power FM 
        self.totalpf_label = Label(self.window, text=str(getTotalPowerFM()) + " W", bg="white", fg="#353534",font=("yu gothic ui", 18, "bold"))
        self.totalpf_label.place(x=350, y=280)

        #Total Power PM 
        self.totalpp_label = Label(self.window, text=str(getTotalPowerPM()) + " W", bg="white", fg="#353534",font=("yu gothic ui", 18, "bold"))
        self.totalpp_label.place(x=350, y=500)

        #Components power FM 
        self.cpowf_label = Label(self.window, text=getLateralPowerFM(), bg="white", fg="#353534",font=("yu gothic ui", 18, "bold"))
        self.cpowf_label.place(x=475, y=265)

        #Components power PM 
        self.cpowp_label = Label(self.window, text=getLateralPowerPM(), bg="white", fg="#353534",font=("yu gothic ui", 18, "bold"))
        self.cpowp_label.place(x=475, y=483)

        #BUTTON
        self.next = ImageTk.PhotoImage\
            (file='img\sbtnmain1.png')
        self.next_button = Button(self.window,image=self.next, relief = "flat", borderwidth=0, background="#FFE65B",activebackground="#FFE65B", cursor="hand2", command=self.funnext)
        self.next_button.place(x=990,y=625)

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
        main.main(win)
        self.window.withdraw()
        win.deiconify()

    def funreturn(self):
        win = Toplevel()
        graphSpectrumsView.graphSpectrumsView(win)
        self.window.withdraw()
        win.deiconify()

    def click_exit(self):
        ask = messagebox.askyesnocancel("Confirmación", "¿Estás seguro que quieres salir?")
        if ask is True:
            self.window.quit()    
    

def win():
    window = Tk()
    powerView(window)
    window.mainloop()

if __name__ == '__main__':
    win()
