import pygame
from Menu import Menu

class Tela:
    def __init__(self, largura, altura):
        self.largura = largura  # Largura da grade em células
        self.altura = altura    # Altura da grade em células
        self.tamanho_celula = 20  # Tamanho de cada célula em pixels
        self.menu = Menu(largura * self.tamanho_celula)  # Cria um menu com a largura da tela
        self.tela = pygame.display.set_mode((largura * self.tamanho_celula, altura * self.tamanho_celula + self.menu.altura))  # Define o tamanho da tela
        pygame.display.set_caption('MinaExplosiva')  # Define o título da janela do jogo
        self.font = pygame.font.Font(None, 36)  # Cria uma fonte para renderizar o texto

    def desenhar(self, celulas, minas_restantes, game_over=False):
        self.tela.fill((192, 192, 192))  # Preenche o fundo da tela com uma cor cinza
        self.menu.desenhar(self.tela)  # Desenha o menu na tela

        # Desenha o contador de minas restantes
        texto_minas = self.font.render(f'Minas: {minas_restantes}', True, (0, 0, 0))  # Renderiza o texto
        self.tela.blit(texto_minas, (10, self.menu.altura + 10))  # Desenha o texto na tela

        # Desenha as células
        for linha in celulas:
            for celula in linha:
                self.desenhar_celula(celula, game_over)

    def desenhar_celula(self, celula, game_over):
        # Calcula a posição e o retângulo da célula
        x, y = celula.x * self.tamanho_celula, celula.y * self.tamanho_celula + self.menu.altura
        rect = pygame.Rect(x, y, self.tamanho_celula, self.tamanho_celula)
        pygame.draw.rect(self.tela, (255, 255, 255), rect)  # Desenha o retângulo da célula

        if celula.revelado:
            if celula.tem_mina:
                pygame.draw.rect(self.tela, (255, 0, 0), rect)  # Desenha a célula com mina em vermelho
                pygame.draw.circle(self.tela, (0, 0, 0), rect.center, self.tamanho_celula // 3)  # Desenha um círculo preto para representar a mina
            else:
                pygame.draw.rect(self.tela, (192, 192, 192), rect)  # Desenha a célula revelada com uma cor cinza
                if celula.vizinhos > 0:
                    # Define a cor do texto com base no número de vizinhos
                    font = pygame.font.Font(None, 36)
                    cores = [(0, 0, 255), (0, 128, 0), (255, 0, 0), (0, 0, 128), (128, 0, 0), (0, 128, 128), (0, 0, 0), (128, 128, 128)]
                    cor = cores[celula.vizinhos - 1]
                    text = font.render(str(celula.vizinhos), True, cor)
                    self.tela.blit(text, rect.topleft)  # Desenha o número de minas vizinhas na célula
        else:
            pygame.draw.rect(self.tela, (128, 128, 128), rect)  # Desenha a célula não revelada em cinza
            if celula.bandeira:
                # Desenha uma bandeira se a célula tiver uma bandeira
                pygame.draw.line(self.tela, (255, 0, 0), (x + 5, y + 5), (x + 15, y + 10), 2)
                pygame.draw.line(self.tela, (255, 0, 0), (x + 5, y + 15), (x + 15, y + 10), 2)
        pygame.draw.rect(self.tela, (0, 0, 0), rect, 1)  # Desenha a borda da célula
