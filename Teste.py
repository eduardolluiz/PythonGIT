import pygame
import sys

# Inicialize o Pygame
pygame.init()

# Defina as dimensões da janela
largura = 800
altura = 600

# Defina a cor preta
preto = (0, 0, 0)

# Crie a janela
janela = pygame.display.set_mode((largura, altura))

# Defina o título da janela
pygame.display.set_caption("Janela com Fundo Preto")

# Loop principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Preencha a tela com a cor preta
    janela.fill(preto)

    # Atualize a tela
    pygame.display.flip()
