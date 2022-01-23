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

mainMenu = MainMenu("Main Menu", screen)
mainMenu.run()
cellWidth = mainMenu.cellWidth
FPS = mainMenu.fps

image = Image.open("middle.jpg")
image = image.resize((SCREENHEIGHT // cellWidth, SCREENHEIGHT // cellWidth), Image.ANTIALIAS)
image_array = np.array(image)

cells = []
for i in range(SCREENHEIGHT // cellWidth):
    row = []
    for j in range(SCREENWIDTH // cellWidth):
        row.append(Cell(cellWidth, (j * cellWidth, i * cellWidth), (255, 255, 255)))
    cells.append(row)

movingCell = MovingCell(cellWidth, (0, 0), (0, 0, 0))
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

    screen.fill((255, 255, 255))

    for i in range(SCREENHEIGHT // cellWidth):
        for j in range(SCREENWIDTH // cellWidth):
            cells[i][j].draw(screen)

    movingCell.draw(screen)
    movingCell.checkVisited(cells)

    if mainMenu.runningOption == "randomDrawing":
        movingCell.drawImage(image_array, cells)
        # movingCell.randomDrawing(cells)
    else:
        movingCell.control()

    pygame.display.update()
    FramePerSec.tick(FPS)

