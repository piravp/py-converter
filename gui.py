from tkinter.filedialog import askopenfilename
from tkinter import *
from filehandler import convert



class Application(Frame):

    def getPath(self):
        return askopenfilename()

    # create buttons, binding, positioning
    def createWidgets(self):
        self.hello = Entry(self)
        self.hello["text"] = StringVar(value="Please choose a file...")
        self.hello["bg"] = "grey"
        self.hello["fg"] = "white"
        self.hello.pack(side="left")

        self.quit_btn = Button(self)
        self.quit_btn["text"] = "Quit"
        self.quit_btn["fg"] = "red"
        self.quit_btn["command"] = self.quit
        self.quit_btn.pack(side="right")

        self.loadFile_btn = Button(self)
        self.loadFile_btn["text"] = "Load file"
        self.loadFile_btn["command"] = path = self.getPath()
        self.loadFile_btn.pack(side="right")        # positioning


        print("Your chosen file is", path)
        self.hello["text"] = StringVar(value="Converted!")

        return path



    # initialize window
    def __init__(self, master=None):
        Frame.__init__(self, master)
        master.title("Python 3.5 translator")
        master.minsize(width=220, height=100)
        master.maxsize(width=400,height=200)
        master.iconbitmap(r'C:\Users\Bruker\Pictures\python.ico')
        self.pack(side="top")
        filepath = self.createWidgets()
        convert(filepath)
        print("funksjonen returnerte ", filepath)

root = Tk()
app = Application(master=root)
app.mainloop()
#root.destroy()



