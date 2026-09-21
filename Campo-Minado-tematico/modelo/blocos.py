import os
from tkinter import Button, PhotoImage

try:
    from PIL import Image, ImageTk
    _USA_PIL = True
except ImportError:
    _USA_PIL = False

PASTA_IMAGENS = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "imagens")

_cacheImagens = {}


def carregarImagem(nome):
    if nome not in _cacheImagens:
        caminho = os.path.join(PASTA_IMAGENS, nome)
        if _USA_PIL:
            img = Image.open(caminho)
            _cacheImagens[nome] = ImageTk.PhotoImage(img)
        else:
            _cacheImagens[nome] = PhotoImage(file=caminho)
    return _cacheImagens[nome]


class Bloco(Button):
    def __init__(self, master, tabuleiro, linha, coluna):
        Button.__init__(self, master)

        self.tabuleiro = tabuleiro
        self.linha = linha
        self.coluna = coluna
        self.eBomba = False
        self.revelado = False
        self.marcado = False
        self.qtdBombasVizinhas = 0

        self["image"] = carregarImagem("vazio.png")
        self["background"] = "#1b2440"
        self["borderwidth"] = 1
        self["padx"] = 0
        self["pady"] = 0
        self["command"] = self.revelar

        self.bind("<Button-3>", self.alternarMarcacao)

    def revelar(self):
        if self.tabuleiro.jogoTerminado or self.revelado or self.marcado:
            return

        self.revelado = True
        self["relief"] = "sunken"

        if self.eBomba:
            self["background"] = "#d13b3b"
            self["image"] = carregarImagem("bomba.png")
            self.tabuleiro.perder()
            return

        self["background"] = "#2f3b63"

        if self.qtdBombasVizinhas > 0:
            self["image"] = carregarImagem(f"numero_{self.qtdBombasVizinhas}.png")
        else:
            self["image"] = carregarImagem("numero_0.png")
            self.tabuleiro.revelarVizinhos(self.linha, self.coluna)

        self.tabuleiro.checarVitoria()

    def alternarMarcacao(self, evento=None):
        if self.tabuleiro.jogoTerminado or self.revelado:
            return

        self.marcado = not self.marcado
        self["image"] = carregarImagem("bandeira.png") if self.marcado else carregarImagem("vazio.png")
