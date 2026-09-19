import random
from model.bloco import Bloco

def add_botoes( Application ):
    for i in range( 0, 121 ):
        Application.block = Bloco( Application.primeiroContainer )
        if ( len(Application.blocos) < 20 ):
            Application.block.isBomb = True
            
        Application.blocos.append( Application.block )
            
    random.shuffle( Application.blocos )

    a = 0
    for i in range( 1, 12 ):
        for j in range ( 1, 12 ):
            Application.blocos[a].grid( column = i, row = j )
            a+=1

    Application.blocos = list(map( lambda c: c.count(), Application.blocos ))