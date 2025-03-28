import pygame
from pygame.locals import *
from classes import todas_sprites
from classes import sapo
from sys import exit

pygame.init()

largura = 640
altura = 480

preto= (0,0,0)

tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption('Sprites')


while True:
    tela.fill(preto)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            sapo.atacar()

    todas_sprites.draw(tela)
    todas_sprites.update()
    pygame.display.flip()