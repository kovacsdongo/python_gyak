from Tkinter import *

class calculator:


    def __init__ (self):

        self.error=False
        window = Tk()
        window.title("Calculator")
        window.configure(background="white")

        self.string = StringVar()
        entry = Entry(window,textvariable = self.string, font = "Helvetica 17 bold")
        entry.grid(row = 0, column = 0, columnspan = 6)
        entry.bind('<KeyPress>', self.key_press)
        entry.focus()

        values = ["7","8","9","/","Clear","<-",
                  "4","5","6","*",",","(",")","1","2","3","-","=","0",".","%","+"]

        i=0
        row=1
        col=0
        for txt in values:
            padx = 10
            pady = 10

            if (i==6):
                row=2
                col=0
            if (i==12):
                row=3
                col=0
            if (i ==17):
                col=0
                row = 4
            if (txt == "="):
                btn = Button(window, height = 2, width = 4, padx = 23, pady = 23, text = txt,
                             command = lambda :self.equals())
                btn.grid(row = row, column = col, columnspan = 2, rowspan = 2, padx = 1, pady = 1)
            elif (txt == "Clear"):
                btn = Button(window, height=1, width=2, padx=padx, pady=pady, text=txt,
                             command=lambda :self.clear_txt())
                btn.grid(row=row, column=col, padx=1, pady=1)
            elif (txt == "<-"):
                btn = Button(window, height=1, width=2, padx=padx, pady=pady, text=txt,
                             command=lambda : self.delete())
                btn.grid(row=row, column=col, padx=1, pady=1)
            else:
                btn = Button(window, height=1, width=2, padx=padx, pady=pady, text=txt,
                             command=lambda txt=txt:self.add_char(txt))
                btn.grid(row=row, column=col, padx=1, pady=1)
            col = col+1
            i = i+1

        window.mainloop()
    def key_press(self, event):

        #https://www.youtube.com/watch?v=SeJKd98WdR0
        #  11:27
        allowedValues = ["KP_0","KP_1","KP_2","KP_3","KP_4","KP_5","KP_6","KP_7","KP_8","KP_9","7","8","9","KP_Divide","slash","4","5","6"]

        if (not self.error):
            if event.keysym in("Return","KP_Enter"):
                self.equals()
            elif event.keysym not in allowedValues:
                return 'break';
        else:
            return 'break'
    def clear_txt(self):
        self.string.set("")
        self.error=False
    def equals(self):
        result = ""
        try:
            res = eval(self.string.get())
        except:
            self.error=True
            result = "Error"
        self.string.set(result)
    def add_char(self, char):
        if (not self.error):
            self.string.set(self.string.get() + (str(char)))
    def delete(self):
        if (not self.error):
            self.string.set(self.string.get()[0:-1])



calculator()