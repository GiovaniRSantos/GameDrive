import pygame
pygame.init()

x = 400
y = 300
velocidade = 5


janela = pygame.display.set_mode((1024,800))
pygame.display.set_caption("Criando um jogo com Python")

janela_aberta = True
while janela_aberta :
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False
        comandos = pygame.key.get_pressed()
        if comandos[pygame.K_UP]:
            y-= velocidade
        if comandos[pygame.K_DOWN]:
            y+= velocidade
        if comandos[pygame.K_RIGHT]:
            x-= velocidade
        if comandos[pygame.K_LEFT]:
            x+= velocidade

    pygame.draw.circle(janela, (255,0,0), (x,y),50)
    pygame.display.update()

pygame.quit()