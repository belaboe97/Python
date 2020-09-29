from tkinter import Tk, Label, Button, Entry, W , E, Scale, HORIZONTAL, Checkbutton, Radiobutton, StringVar
# from pythonp.PIL import Image
class MyFirstGUI:
    
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")
        root.geometry('500x750') 

        self.studentList = []
        self.label = Label(master ,text="Register",font=10, fg="red").grid(column=0,row=0,padx=20,pady=20)
        self.label1 = Label(master, text="Male Or Female?",fg="blue", font=10).grid(column=0,row=1)

        self.mOF  =  StringVar()

       # self.mimg = Image.open("male2.png")
       # self.male_img = ImageTk.PhotoImage(self.mimg)
       # self.maleBtn = Radiobutton(root, text="Male", indicatoron=0, image=self.male_img, variable=self.mOF,value="Male",compound='top')
        self.maleBtn = Radiobutton(root, text="Male", indicatoron=0,  variable=self.mOF,value="Male",compound='top')
       # self.img = Image.open("lana.png")
       # self.female_img = ImageTk.PhotoImage(self.img)
       # self.femaleBtn = Radiobutton(root, text="Female", indicatoron=0, image=self.female_img, variable=self.mOF,value="Female",compound='top')
        self.femaleBtn = Radiobutton(root, text="Female", indicatoron=0, variable=self.mOF,value="Female",compound='top')
         
        self.maleBtn.grid(column=0,row=3,pady=20)
        self.femaleBtn.grid(column=1,row=3,pady=20)
        
        self.smoker = StringVar()
        self.smokeBtn = Checkbutton(master,text="Are you a Smoker?", variable=self.smoker,font=10,fg="blue").grid(column=0, row=4,pady=20)

        
        self.scaleAge = Scale(master, from_=0, to=120, orient=HORIZONTAL).grid(column=0,row=5)

                
        self.quitButton = Button(master, text="QUIT", fg="red",command=lambda: self.master.destroy()).grid(column=0,row=6)
        self.adToListButton = Button(master, text="AddToList", fg="red",command=self.adToList).grid(column=1,row=6)
        self.getAvgAgeButton = Button(master, text="GetAvarageAge", fg="red",command=self.avgAge).grid(column=2,row=6)


   
    def avgAge(self):

        membersAvgAge=0
        avgAge = 0
        for member in self.memberList:
            avgAge += member.getAge()
        membersAvgAge = avgAge/ len(self.memberList)
        self.ageOutput = Label(self.master,fg="red",text=f"The Members are {membersAvgAge} years old in avarage").grid(column=0,row=7)
        self.clear_text()
    
    def adToList(self):
        self.memberList.append(Member( self.entryName.get(),self.scaleAge.get(),self.smoker.get(),self.variable.get()))
        self.labelOutputMemberAdd = Label(root,fg='red',text=f'The Member {self.entryName.get()} that is  {self.scaleAge.get()} years old added to the List').grid(column=0,row=8)
        self.clear_text()
    
    def clear_text(self):
        self.entryName.delete(0, 'end')
        self.scaleAge.set(0)
        self.mOF.set(value="0")
        self.variable.set(value="1")
        
    

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
