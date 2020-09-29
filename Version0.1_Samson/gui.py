from tkinter import Tk, Label, Button, Entry, W , E, Scale, HORIZONTAL, Checkbutton, Radiobutton, StringVar, OptionMenu, Text, END
from lib.sitepackages import pypyodbc

class MyFirstGUI:
    
    def __init__(self, master):
        self.master = master
        master.title("Hotel GUI")

        self.label1 = Label(master, text="Enter Name")
        self.label1.pack()

        self.entryName = Entry()
        self.entryName.pack()
        
    
        self.labelAge = Label(master, text="How old is the guest?")

        self.scaleAge = Scale(master, from_=0, to=120, orient=HORIZONTAL)
        self.scaleAge.pack()

        self.student = StringVar(value="1")
        self.studentBtn = Checkbutton(master,text="Guest stay longer than 1 night?", variable=self.student, onvalue="Yes" , offvalue="No").pack()

        self.roomVariable = StringVar(master)
        self.roomVariable.set("Single Room")

        self.roomOptions = OptionMenu(master, self.roomVariable, "Single Room", "Double Room", "Resident Suite")
        self.roomOptions.pack()


        self.gender  =  StringVar(value="1")

        self.maleBtn = Radiobutton(master, text="Male", variable=self.gender,value="Male").pack()

        self.femaleBtn = Radiobutton(master, text="Female", variable=self.gender, value="Female").pack()

        self.priceLabel = Label(master,text="Price per Night").pack()
        self.priceEntry = Entry(master)
        self.priceEntry.pack()

        self.txt =  Text(root, width="30", height="10")
        self.txt.pack()
        
        self.quitButton = Button(master, text="QUIT", fg="red",command=lambda: self.master.destroy()).pack()
        self.adToDatabase = Button(master, text="Add to Database", fg="red",command=self.addToDB).pack()
        self.displayDatabase = Button(master, text="Display out of Database", fg="red",command=self.showDB).pack()


    def addToDB(self):
        self.txt.delete(1.0,END)
        DBfile = '.\\hotel.mdb'
        conn = pypyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb)};DBQ='+DBfile)
        myCursor = conn.cursor()
        SQL_insert = "insert into guest(gname,gender,roomtype,price) values ('"+self.entryName.get()+"','"+self.gender.get()+"','"+self.roomVariable+"','"+self.priceEntry.get()+"')"
        myCursor.execute(SQL_insert)
        myCursor.commit()
        self.txt.insert(END,"Saved to Database")
        self.txt.insert(END,"\n")
    
    def showDB(self):
        self.txt.delete(1.0,END)
        DBfile = '.\\hotel.mdb'
        conn = pypyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb)};DBQ='+DBfile)
        myCursor = conn.cursor()
        SQL = "SELECT * FROM guest"
        guests = myCursor.execute(SQL)
        self.txt.insert(END,"Hotelguest: ")
        for guest in guests:
             self.txt.insert(END,'Name: '+ guest[0] +" is gender: " + guest[1] + " stays at room: " + guest[2] + " for the price: " +guest[3]+ "Euros")

    
       
  

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
