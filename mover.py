import pygame
from pygame.locals import*
pygame.init()
pantalla = pygame.display.set_mode((320,240),0,32)

while True:
    for eventos in pygame.event.get():
        if eventos.type == pygame.QUIT:
            exit()
    pulsada = pygame.key.get_pressed()