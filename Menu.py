import pygame

class Menu:
    def __init__(self, largura):
        self.largura = largura  # Largura total do menu
        self.altura = 40  # Altura do menu

    def desenhar(self, tela):
        pygame.draw.rect(tela, (192, 192, 192), (0, 0, self.largura, self.altura))  # Desenha o fundo do menu
        fonte = pygame.font.Font(None, 36)  # Cria uma fonte para o texto
        texto_reiniciar = fonte.render('Reiniciar', True, (0, 0, 0))  # Texto para o botão "Reiniciar"
        texto_sair = fonte.render('Sair', True, (0, 0, 0))  # Texto para o botão "Sair"
        tela.blit(texto_reiniciar, (self.largura // 4 - texto_reiniciar.get_width() // 2, 5))  # Desenha o texto "Reiniciar"
        tela.blit(texto_sair, (3 * self.largura // 4 - texto_sair.get_width() // 2, 5))  # Desenha o texto "Sair"

    def verificar_clique(self, pos):
        x, y = pos
        if 0 <= y <= self.altura:  # Verifica se o clique está dentro da área do menu
            if self.largura // 4 - 50 <= x <= self.largura // 4 + 50:  # Verifica se o clique está no botão "Reiniciar"
                return 'restart'
            elif 3 * self.largura // 4 - 50 <= x <= 3 * self.largura // 4 + 50:  # Verifica se o clique está no botão "Sair"
                return 'exit'
        return None
