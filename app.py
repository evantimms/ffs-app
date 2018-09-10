# Imports
import numpy as np
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from tkinter import *
import pyaudio as pya
import wave

class app:

    def __init__(self,master):
        #master refers to root
        master.title("App")
        frame = Frame(master, height=0, width = 1000)
        self.create_widgets(frame,master)
        
        

    def create_widgets(self,frame,master):
        #Menu
        menubar = Menu(master)

        fileMenu = Menu(master, tearoff=0)
        fileMenu.add_command(label="Quit", command=quit)

        editMenu = Menu(master, tearoff=0)

        menubar.add_cascade(label="File", menu=fileMenu)
        menubar.add_cascade(label="Edit", menu=editMenu)
        master.config(menu=menubar)


        #Toolbar
        toolbar = Frame(master, bd=1, relief=RAISED)

        recordButton = Button(toolbar, text="Start Record", command=self.record_sound)
        recordButton.pack(side=LEFT)

        stopRecordButton = Button(toolbar, text="Stop Record", command=self.stop_record_sound)
        stopRecordButton.pack(side=LEFT)
        toolbar.pack(side=TOP, fill=X)


        # Canvas, just a dummy for now
        fig = Figure(figsize=(5,5), dpi=100)
        a = fig.add_subplot(111)
        a.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])

        canvas = FigureCanvasTkAgg(fig, master=master)
        canvas.show()
        canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=True)

        navToolbar = NavigationToolbar2TkAgg(canvas,master)
        navToolbar.update()
        canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=True)
        

        #Statusbar
        self.status = Label(master, text="Text", bd=1, relief=SUNKEN, anchor=S)
        self.status.pack(side=BOTTOM, fill=X)
        frame.pack()

    def measure_values(self):
        pass

    def change_status(self):
        '''
        This will eventually be used for displaying the identified song.
        '''
        self.status.config(text="New Text")
        self.status.update_idletasks()

    def record_sound(self):
        print("Recording Sound")

    def stop_record_sound(self):
        print("Stopping recording")



if __name__ == '__main__':
    root = Tk()
    app = app(root)
    root.mainloop()
