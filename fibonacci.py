import tkinter
from tkinter import *
from tkinter import ttk


class SequenceUI(object):

    def __init__(self):
        self.root = tkinter.Tk()
        self.style = ttk.Style()

        # Setup references
        self.frm = ttk.Frame(self.root)
        self.btn = ttk.Button(self.frm, text='Start', command=self.fibonacci)
        self.clr = ttk.Button(self.frm, text='Clear', command=self.clear_list)
        self.lbl = ttk.Label(self.frm, text='Times to iterate:')
        self.spn = Spinbox(self.frm, from_=1, to=100)
        self.lb = Listbox(self.frm)
        self.sb = Scrollbar(self.frm, orient=VERTICAL)

        # Configuration
        self.sb.config(command=self.lb.yview)
        self.lb.configure(yscrollcommand=self.sb.set)

        # Pack it all up
        self.frm.pack(expand=True, fill='both')
        self.sb.pack(side=RIGHT, fill=Y)
        self.lb.pack(fill=BOTH, expand=True)
        self.lbl.pack(side=LEFT)
        self.spn.pack(side=LEFT)
        self.clr.pack()
        self.btn.pack()

    def add_to_list(self, item):
        self.lb.insert(END, item)

    def clear_list(self):
        self.lb.delete(0, END)

    def fibonacci(self):
        a = 0
        b = 1
        cnt = int(self.spn.get())

        if cnt < 1:
            cnt = 1
            self.add_to_list('Iterating once only.')
        if cnt > 100:
            cnt = 100
            self.add_to_list('Capping iteration at {}'.format(cnt))

        if cnt == 1:
            self.add_to_list(a)
            return

        if cnt == 2:
            self.add_to_list(a)
            self.add_to_list(b)
            return

        self.add_to_list(a)
        self.add_to_list(b)
        cnt = cnt-2

        for _ in range(cnt):
            tmp = a+b
            self.add_to_list(tmp)
            a = b
            b = tmp

app = SequenceUI()
app.root.title('Sequence This')
app.root.minsize(200, 100)
app.root.mainloop()