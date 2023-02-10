import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Combobox
import csv
from tkinter import filedialog




class Subjects():
    def __init__(self, root):
        filepath = Label(root, width=25)
        filepath.config(text="Data path", bg="darkblue")
        filepath.grid(row=0, column=0, padx=(5, 10), pady=(20, 0))

        self.EntryPath = Entry(root)
        self.EntryPath.grid(row=0, column=1, padx=(0, 0), pady=(20, 0), columnspan=2, sticky=W + E)

        Year = Label(root, width=10)
        Year.config(text="Year", bg="darkblue")
        Year.grid(row=1, column=0, padx=(5, 10), pady=(20, 0), sticky=W + E)
        year = tk.StringVar()
        self.Yearcombo = ttk.Combobox(root, width=5, textvariable=year)
        self.Yearcombo['values'] = ('1', '2', '3', '4', '5')
        self.Yearcombo.grid(row=1, column=1, padx=(5, 10), pady=(20, 0), sticky=W + E)
        self.Yearcombo.current()

        Subject = Label(root, width=20)
        Subject.config(text="Department", bg="darkblue")
        Subject.grid(row=1, column=2, pady=(5, 10), padx=(20, 0), sticky=W + E)

        self.Entrysubject = Entry(root)
        self.Entrysubject.grid(row=1, column=3, pady=(5, 10), padx=(20, 0), sticky=W + E)

        Display = Button(root, command=self.file_csv)
        Display.config(text="Display", bg="darkblue")
        Display.grid(row=3, column=1, pady=(5, 10), padx=(20, 0), sticky=W + E)

        Clear = Button(root, command=self.clear_all)
        Clear.config(text="Clear", bg="darkblue")
        Clear.grid(row=3, column=2, pady=(5, 10), padx=(20, 0), sticky=W + E)

        Save = Button(root, command=self.save_them)
        Save.config(text="Save", bg="darkblue")
        Save.grid(row=3, column=3, pady=(5, 10), padx=(20, 0), sticky=W + E)

        Mysubjects = Label(root)
        Mysubjects.config(text="My subjects", bg="darkblue")
        Mysubjects.grid(row=3, column=0, pady=(5, 10), padx=(20, 0), sticky=W + E)
        self.Mysubjectsx = Listbox(root, width=25, selectmode=MULTIPLE)
        self.Mysubjectsx.grid(row=4, column=0, pady=(5, 10), padx=(20, 0), sticky=W + E)
        self.Mysubjectsx.bind("<<ListBox>>", self.select_)

        Subjectselcet = Label(root)
        Subjectselcet.config(text="Select department", bg="darkblue")
        Subjectselcet.grid(row=3, column=4, pady=(5, 10), padx=(20, 0), sticky=W + E)
        self.Subjectselectx = Listbox(root, width=25)
        self.Subjectselectx.grid(row=4, column=4, pady=(5, 10), padx=(20, 0), sticky=W + E)
        #self.Subjectselectx.bind("<<ListboxSelect>>", self.select_)



    def file_csv(self):
        year = self.Yearcombo.get()
        department = self.Entrysubject.get()
        filepath = self.EntryPath.get()
        with open(filepath, 'r',encoding="utf-8", errors="ignore") as file:

            for i in file:
                if len(department)==0 and len(year)==0:
                        self.Mysubjectsx.insert("end", i)
                elif i.split()[1][0] == year and len(department)==0:
                    self.Mysubjectsx.insert("end", i)

                elif i.split()[0] == department and len(year)==0:
                    self.Mysubjectsx.insert("end", i)
                elif i.split()[1][0]==year and i.split()[0]==department:
                    self.Mysubjectsx.insert("end",i)


        """these are 3 functions(I have tried even more...) to select items and move them to the other listbox, but they didn't work"""

    subjects=[]
    def select_(self,event):

        global inserted_data
        selection = self.Mysubjectsx.curselection()
        if len(self.subjects) < 6:
            for select in selection:
                data = event.widget.get(select)
                if data.split(",") not in self.subjects:
                    self.subjects.append(data.split(","))
                    print(self.subjects)
                    inserted_data = "Added " + str(data.split(',')[0])
                    self.Subjectselectx.insert("end", inserted_data)
           #else:
              ## self.warning()

    #def select_(self,val):
       # indexlist=self.Mysubjectsx.curselection()
        ##index=indexlist[0]
        #val=self.Mysubjectsx.get(index)
        #eturn self.Subjectselectx.insert(END,val)

    ###def select_(self):
        ##for i in self.Mysubjectsx.curselection():
            #print(self.Subjectselectx.get(i))

    ######def select_(self,val):
        #####sender=val.widget
        ####idx=sender.curselection()
        ###value=sender.get(idx)
        ##print(value)
        #self.Subjectselectx.insert("end",value)


    def clear_all(self):
        self.Mysubjectsx.delete(0, END)
        self.Subjectselectx.delete(0, END)

    def save_them(self):
        choice = self.Subjectselectx.curselection()

        return choice


root = Tk()
root.resizable(0, 0)
root.geometry("1200x600+400+200")
root.wm_title(" " * 50 + "Course Tool")
root.configure(background='lightblue')
Subjects(root)
root.mainloop()