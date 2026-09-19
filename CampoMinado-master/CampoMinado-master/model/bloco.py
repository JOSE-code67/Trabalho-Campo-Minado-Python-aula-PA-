from tkinter import messagebox, Button
import controller.blocoController as blocoController

class Bloco( Button ):
    isBomb = False
    master = None 
    qtdBomb = 0
    def __init__( self, master = None ):
        Button.__init__( self, master )
        self.master = master
        self["width"] = 4
        self["height"] = 2
        self["command"] = self._on_click
        self["background"] = 'grey'
        self["borderwidth"] = 1   
        self["font"] = (12)

    def  _on_click( self ):
        blocoController.revelar_botao( self )

    
    def count( self ):
        blocoController.rastrear_bombas( self )
