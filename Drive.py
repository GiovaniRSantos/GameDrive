import pygame
pygame.init()

janela = pygame.display.set_mode((1024,800))
pygame.display.set_caption("Criando um jogo com Python")

janela_aberta = True
while janela_aberta :
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    pygame.draw.circle(janela, (255,0,0), (400,300),50)
    pygame.display.update()

pygame.quit()