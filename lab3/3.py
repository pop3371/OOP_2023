import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((800, 500))
polygon(screen, (255, 250, 205),  [[0, 0], [800, 0], [800, 500], [0, 500]])
polygon(screen, (253, 219, 109),  [[0, 0], [800, 0], [800, 100], [0, 100]])
polygon(screen, (253, 219, 109),  [[0, 200], [800, 200], [800, 500], [0, 500]])

pi = 3.14
polygon(screen, (244, 169, 0),  [[0, 180], [350, 160], [370, 180], [0, 200]])
polygon(screen, (244, 169, 0),  [[390, 160], [750, 140], [800, 160], [370, 180]])
polygon(screen, (244, 169, 0),  [[0, 180], [125, 50], [340, 175], [340, 176]])
polygon(screen, (244, 169, 0),  [[125, 50], [200, 75], [250, 150], [125, 100]])
polygon(screen, (244, 169, 0),  [[390, 160], [420, 140], [460, 170], [390, 175]])
polygon(screen, (244, 169, 0),  [[420, 140], [480, 130], [500, 170], [460, 175]])
polygon(screen, (244, 169, 0),  [[480, 130], [560, 50], [700, 140], [460, 175]])
polygon(screen, (244, 169, 0),  [[680, 140], [740, 100], [760, 160], [460, 175]])


ellipse(screen, (183, 65, 14), (-50, 200, 100, 190))
ellipse(screen, (183, 65, 14), (25, 150, 110, 200))
polygon(screen, (183, 65, 14),  [[220, 270], [220, 350], [0, 400], [180, 225]])
polygon(screen, (183, 65, 14),  [[150, 400], [400, 400], [300, 210], [260, 200]])
polygon(screen, (183, 65, 14),  [[300, 210], [350, 270], [350, 400], [300, 400]])
polygon(screen, (183, 65, 14),  [[350, 270], [500, 250], [500, 400], [350, 400]])
ellipse(screen, (183, 65, 14), (450, 200, 110, 150))
polygon(screen, (183, 65, 14),  [[545, 400], [545, 225], [625, 260], [625, 400]])
polygon(screen, (183, 65, 14),  [[580, 260], [670, 225], [700, 240], [700, 400]])
polygon(screen, (183, 65, 14),  [[800, 160], [670, 225], [670, 400], [800, 400]])

polygon(screen, (204, 136, 153),  [[800, 300], [800, 500], [0, 500], [0, 320]])

circle(screen, (255, 255, 0), (400, 70), 50)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True