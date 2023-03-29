import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
polygon(screen, (255, 255, 255),  [[400, 0], [400, 400], [0, 400], [0, 0]])
circle(screen, (0, 0, 0), (200, 200), 102)
circle(screen, (255, 255, 0), (200, 200), 100)
circle(screen, (0, 0, 0), (155, 190), 26)
circle(screen, (0, 0, 0), (255, 190), 22)
circle(screen, (230, 0, 0), (155, 190), 25)
circle(screen, (230, 0, 0), (255, 190), 20)
circle(screen, (0, 0, 0), (155, 190), 10)
circle(screen, (0, 0, 0), (255, 190), 10)
line(screen, (0, 0, 0),  [155, 250], [255, 250], 20)
line(screen, (0, 0, 0),  [100, 140], [190, 170], 10)
line(screen, (0, 0, 0),  [220, 170], [285, 160], 10)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
