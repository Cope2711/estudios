import tkinter


class MyAutocompleteClass:
    def __init__(self, entry, suggestions):
        self.entry = entry
        self.suggestions = suggestions
        if isinstance(self.entry["textvariable"], tkinter.StringVar):
            self.var = self.entry["textvariable"]
        else:
            self.var = tkinter.StringVar()
            self.entry.config(textvariable=self.var)
        self.var.trace("w", self.changed)
        self.entry.bind("<Right>", self.complete)
        self.entry.bind("<Up>", self.up)
        self.entry.bind("<Return>", self.enter)
        self.entry.bind("<Down>", self.down)
        self.lb_up = False

    def changed(self, name, index, mode):
        if self.var.get() == '':
            if self.lb_up:
                self.lb.destroy()
                self.lb_up = False
        else:
            words = self.comparison()
            if words:
                if not self.lb_up:
                    self.lb = tkinter.Listbox(self.entry.master)
                    self.lb.bind("<Double-Button-1>", self.selection)
                    self.lb.bind("<Right>", self.selection)
                    self.lb_up = True
                self.lb.delete(0, tkinter.END)
                for w in words:
                    self.lb.insert(tkinter.END, w)
                self.lb.place(x=self.entry.winfo_x(), y=self.entry.winfo_y() + self.entry.winfo_height())
            else:
                if self.lb_up:
                    self.lb.destroy()
                    self.lb_up = False

    def selection(self, event):
        if self.lb_up:
            self.var.set(self.lb.get(tkinter.ACTIVE))
            self.lb.destroy()
            self.lb_up = False
            self.entry.icursor(tkinter.END)

    def complete(self, event):
        if self.lb_up:
            self.var.set(self.lb.get(tkinter.ACTIVE))
            self.lb.destroy()
            self.lb_up = False
            self.entry.icursor(tkinter.END)
        return 'break'

    def up(self, event):
        if self.lb_up:
            if self.lb.curselection() == ():
                index = '0'
            else:
                index = self.lb.curselection()[0]
            if index != '0':
                self.lb.selection_clear(first=index)
                index = str(int(index) - 1)
                self.lb.selection_set(first=index)
                self.lb.activate(index)
        return 'break'

    def down(self, event):
        if self.lb_up:
            if self.lb.curselection() == ():
                index = '-1'
            else:
                index = self.lb.curselection()[0]
            if index != tkinter.END:
                self.lb.selection_clear(first=index)
                index = str(int(index) + 1)
                self.lb.selection_set(first=index)
                self.lb.activate(index)
        return 'break'
    
    def enter(self, event):
        if self.lb_up:
            self.var.set(self.lb.get(tkinter.ACTIVE))
            self.lb.destroy()
            self.lb_up = False
            self.entry.icursor(tkinter.END)
        return 'break'

    def comparison(self):
        pattern = self.var.get()
        return [w for w in self.suggestions if w.startswith(pattern)]



# Ejemplo de uso
if __name__ == '__main__':
    root = tkinter.Tk()
    entry = tkinter.Entry(root)
    entry.pack()
    MyAutocompleteClass(entry, ["apple", "banana", "cherry", "date", "elderberry"])
    root.mainloop()
