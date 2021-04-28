from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk
import lateralView
import graphModulatedView
from operations import getSensitivityFM, getSensitivityPM, getDeviationFM,getDeviationRatioFM
from operations import getPercentFM, getBandwidthRealFM, getBandwidthMinFM, getDeviationPM
from operations import getIndexPM, getPercentPM, getBandwidthRealPM, getBandwidthMinPM 

class dataView:

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
            (file='img\data_frame.png')
        self.image_panel = Label(self.window,image=self.database_frame)
        self.image_panel.pack(fill='both',expand='yes')

        #LABELS

        #Sensitivity FM 
        self.sfre_label = Label(self.window, text=str(getSensitivityFM()) + " (Hz/V)", bg="white", fg="#353534",font=("yu gothic ui", 18, "bold"))
        self.sfre_label.place(x=108, y=237)

        #Sensitivity PM 
        self.spha_label = Label(self.window, text=str(getSensitivityPM()) + " (rad/V)", bg="white", fg="#353534",font=("yu gothic ui", 18, "bold"))
        self.spha_label.place(x=790, y=237)

        #Deviation FM 
        self.dfre_label = Label(self.window, text=str(getDeviationFM()) + " Hz" , bg="white", fg="#353534",font=("yu gothic ui", 18, "bold"))
        self.dfre_label.place(x=350, y=237)

        #Deviation PM 
        self.dpha_label = Label(self.window, text=str(getDeviationPM()) + " rad" , bg="white", fg="#353534",font=("yu gothic ui", 18, "bold"))
        self.dpha_label.place(x=1025, y=237)

        #DeviationRatio FM 
        self.drfre_label = Label(self.window, text=getDeviationRatioFM(), bg="white", fg="#353534",font=("yu gothic ui", 18, "bold"))
        self.drfre_label.place(x=130, y=371)
        
        #Index PM
        self.ipha_label = Label(self.window, text=str(getIndexPM()) + "rad", bg="white", fg="#353534",font=("yu gothic ui", 18, "bold"))
        self.ipha_label.place(x=820, y=372)

        #Percent FM 
        self.pfre_label = Label(self.window, text=getPercentFM(), bg="white", fg="#353534",font=("yu gothic ui", 18, "bold"))
        self.pfre_label.place(x=365, y=371)

        #Percent PM 
        self.ppha_label = Label(self.window, text=getPercentPM(), bg="white", fg="#353534",font=("yu gothic ui", 18, "bold"))
        self.ppha_label.place(x=1050, y=372)

        #BandwidthReal FM 
        self.brfre_label = Label(self.window, text=str(getBandwidthRealFM()) + " Hz", bg="white", fg="#353534",font=("yu gothic ui", 18, "bold"))
        self.brfre_label.place(x=120, y=506)

        #BandwidthReal PM 
        self.brpha_label = Label(self.window, text=str(getBandwidthRealPM()) + " Hz", bg="white", fg="#353534",font=("yu gothic ui", 18, "bold"))
        self.brpha_label.place(x=800, y=506)

        #BandwidthMin FM 
        self.pfre_label = Label(self.window, text=str(getBandwidthMinFM()) + " Hz", bg="white", fg="#353534",font=("yu gothic ui", 18, "bold"))
        self.pfre_label.place(x=343, y=506)

        #BandwidthMin PM 
        self.ppha_label = Label(self.window, text=str(getBandwidthMinPM()) + " Hz", bg="white", fg="#353534",font=("yu gothic ui", 18, "bold"))
        self.ppha_label.place(x=1020, y=506)

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
        lateralView.lateralView(win)
        self.window.withdraw()
        win.deiconify()

    def funreturn(self):
        win = Toplevel()
        graphModulatedView.graphModulatedView(win)
        self.window.withdraw()
        win.deiconify()
        
    def click_exit(self):
        ask = messagebox.askyesnocancel("Confirmación", "¿Estás seguro que quieres salir?")
        if ask is True:
            self.window.quit()   

def win():
    window = Tk()
    dataView(window)
    window.mainloop()

if __name__ == '__main__':
    win()
