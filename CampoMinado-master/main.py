from tkinter import Tk
from model.application import Application

if __name__ == '__main__':
    root = Tk()
    root.title("Campo Minado")
    Application(root)
    root.mainloop()