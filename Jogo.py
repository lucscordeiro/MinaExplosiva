import pygame
from Tela import Tela
from Celula import Celula
from Menu import Menu
import random

class Jogo:
    def __init__(self, largura, altura, num_minas):
        self.largura = largura  # Número de colunas da grade
        self.altura = altura    # Número de linhas da grade
        self.num_minas = num_minas  # Número total de minas
        self.tela = Tela(self.largura, self.altura)  # Cria uma instância da classe Tela
        self.celulas = [[Celula(x, y) for y in range(altura)] for x in range(largura)]  # Cria uma grade de células
        self.colocar_minas()  # Distribui as minas na grade
        self.calcular_vizinhos()  # Calcula o número de minas vizinhas para cada célula
        self.game_over = False  # Flag que indica se o jogo terminou
        self.minas_restantes = num_minas  # Contador de minas restantes

    def colocar_minas(self):
        minas_colocadas = 0
        while minas_colocadas < self.num_minas:
            x = random.randint(0, self.largura - 1)  # Seleciona uma posição aleatória para a mina
            y = random.randint(0, self.altura - 1)
            if not self.celulas[x][y].tem_mina:  # Verifica se a célula já tem uma mina
                self.celulas[x][y].tem_mina = True  # Coloca uma mina na célula
                minas_colocadas += 1  # Incrementa o contador de minas colocadas

    def calcular_vizinhos(self):
        for x in range(self.largura):  # Itera sobre todas as células na grade
            for y in range(self.altura):
                if self.celulas[x][y].tem_mina:
                    continue  # Pular células que já têm minas
                self.celulas[x][y].vizinhos = self.contar_minas_vizinhas(x, y)  # Conta o número de minas vizinhas

    def contar_minas_vizinhas(self, x, y):
        count = 0
        for i in range(-1, 2):  # Itera sobre a área ao redor da célula
            for j in range(-1, 2):
                nx, ny = x + i, y + j
                if 0 <= nx < self.largura and 0 <= ny < self.altura and self.celulas[nx][ny].tem_mina:
                    count += 1  # Conta minas vizinhas
        return count

    def rodar(self):
        rodando = True
        while rodando:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    rodando = False  # Encerra o loop se a janela for fechada
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    acao = self.tela.menu.verificar_clique((x, y))  # Verifica a ação do clique no menu
                    if acao == 'restart':
                        self.__init__(self.largura, self.altura, self.num_minas)  # Reinicia o jogo
                    elif acao == 'exit':
                        rodando = False  # Encerra o jogo
                    elif not self.game_over and y > self.tela.menu.altura:
                        grid_x, grid_y = x // self.tela.tamanho_celula, (y - self.tela.menu.altura) // self.tela.tamanho_celula
                        if event.button == 1:
                            self.revelar(grid_x, grid_y)  # Revela a célula ao clicar com o botão esquerdo
                        elif event.button == 3:
                            self.celulas[grid_x][grid_y].alternar_bandeira()  # Alterna bandeira ao clicar com o botão direito
                            self.minas_restantes += -1 if self.celulas[grid_x][grid_y].bandeira else 1  # Atualiza o contador de minas restantes

            self.tela.desenhar(self.celulas, self.minas_restantes, self.game_over)  # Desenha a tela com o estado atual do jogo
            pygame.display.flip()  # Atualiza a tela

    def revelar(self, x, y):
        if self.celulas[x][y].revelado or self.celulas[x][y].bandeira:
            return  # Não faz nada se a célula já estiver revelada ou tiver uma bandeira
        self.celulas[x][y].revelar()  # Revela a célula
        if self.celulas[x][y].tem_mina:
            self.game_over = True  # Se a célula contém uma mina, o jogo termina
        elif self.celulas[x][y].vizinhos == 0:
            # Se a célula não tem minas vizinhas, revela células vizinhas
            for i in range(-1, 2):
                for j in range(-1, 2):
                    nx, ny = x + i, y + j
                    if 0 <= nx < self.largura and 0 <= ny < self.altura:
                        self.revelar(nx, ny)
