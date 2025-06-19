import tkinter as tk
from tkinter import ttk


def compute_fibonacci(count):
    """Return a list containing ``count`` Fibonacci numbers."""
    if count < 1:
        raise ValueError("count must be >= 1")

    a, b = 0, 1
    result = [a]

    if count == 1:
        return result

    result.append(b)
    for _ in range(count - 2):
        a, b = b, a + b
        result.append(b)
    return result

""" UI method """
class SequenceUI(object):

    def __init__(self):
        self.root = tk.Tk()
        self.style = ttk.Style()

        # Setup references
        self.frm = ttk.Frame(self.root)
        self.btn = ttk.Button(self.frm, text='Start', command=self.fibonacci)
        self.clr = ttk.Button(self.frm, text='Clear', command=self.clear_list)
        self.lbl = ttk.Label(self.frm, text='Times to iterate:')
        self.spn = tk.Spinbox(self.frm, from_=1, to=100)
        self.lb = tk.Listbox(self.frm)
        self.sb = tk.Scrollbar(self.frm, orient=tk.VERTICAL)

        # Configuration
        self.sb.config(command=self.lb.yview)
        self.lb.configure(yscrollcommand=self.sb.set)

        # Pack it all up
        self.frm.pack(expand=True, fill='both')
        self.sb.pack(side=tk.RIGHT, fill=tk.Y)
        self.lb.pack(fill=tk.BOTH, expand=True)
        self.lbl.pack(side=tk.LEFT)
        self.spn.pack(side=tk.LEFT)
        self.clr.pack()
        self.btn.pack()

    def add_to_list(self, item):
        self.lb.insert(tk.END, item)

    def clear_list(self):
        self.lb.delete(0, tk.END)

    def fibonacci(self):
        try:
            cnt = int(self.spn.get())
        except (TypeError, ValueError):
            cnt = 1
            self.add_to_list('Invalid input, iterating once only.')

        self.clear_list()

        if cnt < 1:
            cnt = 1
            self.add_to_list('Iterating once only.')
        if cnt > 100:
            cnt = 100
            self.add_to_list('Capping iteration at {}'.format(cnt))

        for num in compute_fibonacci(cnt):
            self.add_to_list(num)

if __name__ == '__main__':
    app = SequenceUI()
    app.root.title('Sequence This')
    app.root.minsize(200, 100)
    app.root.mainloop()
