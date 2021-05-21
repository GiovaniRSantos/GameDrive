import pygame
pygame.init()

janela = pygame.display.set_mode((800,600))
pygame.display.set_caption("Criando um jogo com Python")

janela_aberta = True
while janela_aberta :

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

pygame.quit()