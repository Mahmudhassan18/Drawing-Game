import pygame
from Cell import Cell, MovingCell
from pygame.locals import *
from AnimationScreens import AnimationScreens, MainMenu
from PIL import Image
import numpy as np

pygame.init()

# Setting up FPS
FramePerSec = pygame.time.Clock()

SCREENWIDTH = 600
SCREENHEIGHT = 600

screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
pygame.display.set_caption("Game")

cellWidth = 10
FPS = 60

image = Image.open("middle.jpg")
image = image.resize((SCREENHEIGHT // cellWidth, SCREENHEIGHT // cellWidth), Image.ANTIALIAS)
image_array = np.array(image)

movingCell = MovingCell(cellWidth, (0, 0), (0, 0, 0), SCREENHEIGHT)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

    screen.fill((255, 255, 255))

    movingCell.draw(screen)
    movingCell.control()

    pygame.display.update()
    FramePerSec.tick(FPS)

