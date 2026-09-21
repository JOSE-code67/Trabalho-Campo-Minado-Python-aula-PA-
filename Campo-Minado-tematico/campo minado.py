import random
from tkinter import Tk, Frame, Toplevel, Label, Button, messagebox
from modelo.blocos import Bloco, carregarImagem

LINHAS = 9
COLUNAS = 9
BOMBAS = 10


class Tabuleiro:
    def __init__(self, master):
        self.master = master
        self.jogoTerminado = False

        # Container principal
        self.container = Frame(master, bg="#0d1229", padx=10, pady=10)
        self.container.pack()

        # Tabuleiro
        self.frame_tabuleiro = Frame(self.container, bg="#0d1229")
        self.frame_tabuleiro.pack()

        self.blocos = [[None for _ in range(COLUNAS)] for _ in range(LINHAS)]

        for linha in range(LINHAS):
            for coluna in range(COLUNAS):
                bloco = Bloco(self.frame_tabuleiro, self, linha, coluna)
                bloco.grid(row=linha, column=coluna, padx=1, pady=1)
                self.blocos[linha][coluna] = bloco

        # Legenda abaixo do tabuleiro
        self.frame_legenda = Frame(self.container, bg="#0d1229", pady=8)
        self.frame_legenda.pack()

        Label(
            self.frame_legenda,
            text="Legenda",
            bg="#0d1229",
            fg="#8aa0c8",
            font=("Segoe UI", 9, "bold"),
        ).pack()

        img_legenda = carregarImagem("legenda.png")
        lbl_legenda = Label(self.frame_legenda, image=img_legenda, bg="#0d1229")
        lbl_legenda.image = img_legenda  # mantém referência
        lbl_legenda.pack(pady=(4, 0))

        self._colocarBombas()
        self._calcularVizinhos()

    def _todasPosicoes(self):
        return [(linha, coluna) for linha in range(LINHAS) for coluna in range(COLUNAS)]

    def _colocarBombas(self):
        for (linha, coluna) in random.sample(self._todasPosicoes(), BOMBAS):
            self.blocos[linha][coluna].eBomba = True

    def _vizinhos(self, linha, coluna):
        for deltaLinha in (-1, 0, 1):
            for deltaColuna in (-1, 0, 1):
                if deltaLinha == 0 and deltaColuna == 0:
                    continue
                l, c = linha + deltaLinha, coluna + deltaColuna
                if 0 <= l < LINHAS and 0 <= c < COLUNAS:
                    yield l, c

    def _calcularVizinhos(self):
        for linha in range(LINHAS):
            for coluna in range(COLUNAS):
                bloco = self.blocos[linha][coluna]
                if not bloco.eBomba:
                    bloco.qtdBombasVizinhas = sum(
                        1 for (l, c) in self._vizinhos(linha, coluna) if self.blocos[l][c].eBomba
                    )

    def revelarVizinhos(self, linha, coluna):
        for (l, c) in self._vizinhos(linha, coluna):
            vizinho = self.blocos[l][c]
            if not vizinho.revelado and not vizinho.eBomba:
                vizinho.revelar()

    def _mostrarTelaFinal(self, titulo, imagem, mensagem):
        """Abre uma janela personalizada com a imagem de vitória ou derrota."""
        janela = Toplevel(self.master)
        janela.title(titulo)
        janela.configure(bg="#0d1229")
        janela.resizable(False, False)
        janela.transient(self.master)
        janela.grab_set()

        janela.update_idletasks()
        x = self.master.winfo_x() + (self.master.winfo_width() // 2) - 200
        y = self.master.winfo_y() + (self.master.winfo_height() // 2) - 250
        janela.geometry(f"+{max(0, x)}+{max(0, y)}")

        img = carregarImagem(imagem)
        lbl_img = Label(janela, image=img, bg="#0d1229")
        lbl_img.image = img
        lbl_img.pack(padx=15, pady=(15, 5))

        Label(
            janela,
            text=mensagem,
            bg="#0d1229",
            fg="#c8d0f0",
            font=("Segoe UI", 11),
            wraplength=420,
            justify="center",
        ).pack(padx=15, pady=5)

        btn = Button(
            janela,
            text="OK",
            command=janela.destroy,
            bg="#2f3b63",
            fg="white",
            activebackground="#3d4f82",
            activeforeground="white",
            relief="flat",
            padx=20,
            pady=6,
            font=("Segoe UI", 10, "bold"),
        )
        btn.pack(pady=(5, 15))

        janela.wait_window()

    def perder(self):
        self.jogoTerminado = True
        for linha in self.blocos:
            for bloco in linha:
                if bloco.eBomba:
                    bloco.revelado = True
                    bloco["background"] = "#d13b3b"
                    bloco["image"] = carregarImagem("bomba.png")

        self._mostrarTelaFinal(
            "Game Over",
            "game_over.png",
            "Você encontrou a Radiância!\nIn attempting the feat, one proves their courage.\nMay your Shade at last find rest.",
        )

    def checarVitoria(self):
        for linha in self.blocos:
            for bloco in linha:
                if not bloco.eBomba and not bloco.revelado:
                    return

        self.jogoTerminado = True
        self._mostrarTelaFinal(
            "Vitória!",
            "vitoria.png",
            "Você limpou o campo minado!\nO Knight prevaleceu sobre a Infecção.",
        )


janela = Tk()
janela.title("Campo Minado — Hollow Knight")
janela.configure(bg="#0d1229")
Tabuleiro(janela)
janela.mainloop()
