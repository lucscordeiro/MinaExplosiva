import pygame

class Celula:
    def __init__(self, x, y):
        self.x = x  # Posição horizontal da célula
        self.y = y  # Posição vertical da célula
        self.revelado = False  # Indica se a célula foi revelada
        self.tem_mina = False  # Indica se a célula contém uma mina
        self.bandeira = False  # Indica se a célula tem uma bandeira
        self.vizinhos = 0  # Número de minas ao redor

    def revelar(self):
        self.revelado = True  # Marca a célula como revelada

    def alternar_bandeira(self):
        self.bandeira = not self.bandeira  # Alterna o estado da bandeira
