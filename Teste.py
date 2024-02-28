import pygame
import sys

# Inicialize o Pygame
pygame.init()

# Carregue a imagem que deseja usar como ícone
icone = pygame.image.load("icon.png")

# Defina as dimensões da janela
largura = 800
altura = 600

# Defina a cor 
cor = (224, 224, 224)

# Defina o ícone da janela
pygame.display.set_icon(icone)

# Crie a janela
janela = pygame.display.set_mode((largura, altura))

# Defina o título da janela
pygame.display.set_caption("Testando Python")

# Loop principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Preencha a tela com a cor 
    janela.fill(cor)

    # Atualize a tela
    pygame.display.flip()