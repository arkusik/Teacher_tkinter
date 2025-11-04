
from tkinter import *   
from konspect import *
    


def main():
    root = Tk() 
    root.attributes("-fullscreen", False)
    konspect_ = Button(text= "Конспекты", command=go_konsp, width=10, height=5)
    konspect_.place(x = 150, y = 600)
    root.mainloop()
    print('qwer')
main()