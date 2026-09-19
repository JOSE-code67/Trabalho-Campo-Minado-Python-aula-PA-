from tkinter import messagebox

def revelar_botao( Bloco ):
    Bloco["state"] = 'disable'
    if (Bloco.isBomb):
        Bloco['background'] = 'red'
        messagebox.showinfo(title = "Perdeu", message = "Você perdeu!")
    
    else:
        if len(Bloco.clearButtons) > 0:
            Bloco.clearButtons = list(map( lambda a: a.invoke(), Bloco.clearButtons ))
            
        Bloco['background'] = 'white'
        Bloco["relief"]="groove"   
        Bloco["text"] = Bloco.qtdBomb

def rastrear_bombas( Bloco ):
    inicioRow = Bloco.grid_info()['row'] - 1
    inicioColumn = Bloco.grid_info()['column'] - 1
    Bloco.clearButtons = list()

    for i in range( inicioRow, inicioRow + 3 ):
        for j in range( inicioColumn, inicioColumn + 3 ):
            try:
                button = Bloco.master.grid_slaves( row = i, column = j )[0] if j != inicioColumn + 1 or i != inicioRow + 1 else None
                if button.isBomb:
                    Bloco.qtdBomb += 1
                else:
                    Bloco.clearButtons.append(button) 
            except:
                pass

    if Bloco.qtdBomb > 0:
        Bloco.clearButtons.clear()
    else: Bloco.qtdBomb = ''