from tkinter import Frame
import controller.applicationController as applicationController

class Application():
    blocos = list()
    def __init__(self, master = None):
        self.primeiroContainer = Frame(master)

        applicationController.add_botoes( self )

        self.primeiroContainer.pack()