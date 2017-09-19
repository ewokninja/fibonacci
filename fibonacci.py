import tkinter
from tkinter import *
from tkinter import ttk


class SequenceUI(object):

    def __init__(self):
        self.root = tkinter.Tk()
        self.style = ttk.Style()

        self.frm = ttk.Frame(self.root)
        self.btn = ttk.Button(self.frm, text='Start')
        self.clr = ttk.Button(self.frm, text='Clear')
        self.lb = Listbox(self.frm)

        self.sb = Scrollbar(self.frm, orient=VERTICAL)
        self.sb.config(command=self.lb.yview)
        self.lb.configure(yscrollcommand=self.sb.set)

        self.frm.pack(expand=True, fill='both')
        self.sb.pack(side=RIGHT, fill=Y)
        self.lb.pack(fill=BOTH, expand=True)
        self.btn.pack()
        self.clr.pack()

    def add_to_list(self, item):
        self.lb.insert(END, item)



app = SequenceUI()
app.root.title('Sequence This')
app.root.minsize(200, 100)
app.root.mainloop()