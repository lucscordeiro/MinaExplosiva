import pygame
import sys
from Jogo import Jogo

def main():
    pygame.init()  # Inicializa todos os módulos do Pygame
    jogo = Jogo(20, 20, 40)  # Cria uma instância do jogo com uma grade 20x20 e 40 minas
    jogo.rodar()  # Inicia o loop do jogo
    pygame.quit()  # Encerra o Pygame
    sys.exit()  # Sai do programa

if __name__ == "__main__":
    main()
