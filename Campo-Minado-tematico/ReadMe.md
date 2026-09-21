### EXPLICAÇÃO DO CÓDIGO

## 1. Introdução

Este projeto foi desenvolvido utilizando Python. O jogo se trata de um campo minado, tematizado com o jogo Hollow Knight, onde o jogador descobre os blocos, evitando encontrar uma mina, esperamos que aproveite o jogo, e se divirta desafiando suas capacidades ao máximo!

## 2. Funcionamento

O programa cria uma janela com um tabuleiro 9x9. Ao clicar num bloco, ele é revelado: se for uma mina, o jogo termina; se não for, mostra uma imagem representando quantas minas existem ao redor daquele bloco. Se não houver nenhuma mina ao redor, o jogo revela automaticamente os blocos vizinhos (efeito cascata). Clique com o botão direito marca um bloco suspeito com o Ferrão.

## 3. O que cada imagem representa

| Imagem | Situação | Personagem |
|---|---|---|
| ![](imagens/numero_0.png) | 0 minas ao redor | Knight |
| ![](imagens/numero_1.png) | 1 mina ao redor | Receptáculo Puro |
| ![](imagens/numero_2.png) | 2 minas ao redor | Cavaleiro Vazio |
| ![](imagens/numero_3.png) | 3 minas ao redor | Receptáculo Quebrado |
| ![](imagens/numero_4.png) | 4 minas ao redor | Mawlek |
| ![](imagens/numero_5.png) | 5 a 8 minas ao redor | Balão Infectado |
| ![](imagens/bomba.png) | Bloco era uma mina | Radiância |
| ![](imagens/bandeira.png) | Clique direito para marcar suspeita | Ferrão Puro |

Veja também `imagens/legenda.png` para conferir todas as imagens lado a lado.

## 4. Variáveis

As principais variáveis ficam dentro da classe `Bloco` (em `modelo/blocos.py`): `eBomba` (se o bloco é uma mina), `revelado` (se já foi clicado), `marcado` (se tem o Ferrão de suspeita) e `qtdBombasVizinhas` (quantas minas tem ao redor dele). O tabuleiro inteiro fica guardado na lista `self.blocos` dentro da classe `Tabuleiro`, em `campo minado.py`.

## 5. Estruturas condicionais

O programa usa `if` para decidir o que fazer ao clicar num bloco: se é mina, perde o jogo; se não é e tem minas ao redor, mostra o número/imagem correspondente; se não tem nenhuma mina ao redor, revela os vizinhos automaticamente.

## 6. Estruturas de repetição

O programa usa `for` para: criar todos os 81 blocos do tabuleiro, sortear as posições das 10 minas, calcular quantas minas cada bloco tem ao redor (olhando as 8 casas vizinhas) e verificar se todos os blocos seguros já foram revelados (condição de vitória).

## 7. Conclusão

O código permite jogar uma versão temática do clássico Campo Minado, usando personagens do Hollow Knight para representar visualmente a contagem de minas ao redor de cada bloco.
