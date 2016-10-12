# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 17:49:38 2016
@author: soma0sd
# pyGame install
(아나콘다 프롬프트)
>>> pip install pygame
"""
import pygame

background_colour = (255, 255, 255)
width, height = 400, 400

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('pygame01')
screen.fill(background_colour)

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
