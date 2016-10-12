# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 18:15:49 2016
@author: soma0sd
"""
import pygame

background_colour = (255, 255, 255)
width, height = 400, 400


class Particle:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.colour = (0, 0, 255)
        self.thickness = 1

    def display(self):
        pygame.draw.circle(screen, self.colour,
                           (self.x, self.y), self.size, self.thickness)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('pygame 2')
screen.fill(background_colour)

p1 = Particle(150, 50, 15)
p1.display()

pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
