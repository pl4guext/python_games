# coding=utf-8

import pygame

pygame.init()

window_size = (600,400)

gameDisplay = pygame.display.set_mode( window_size )

pygame.display.set_caption('Titulo')

clock = pygame.time.Clock()

crashed = False


while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        print event

    pygame.display.update()

    clock.tick(60) # fps

pygame.quit()
quit()