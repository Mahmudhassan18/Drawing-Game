import pygame
import random

visitedCells = set()


class Cell:
    def __init__(self, width, position, color):
        self.width = width
        self.position = position
        self.visited = 0
        self.color = color

    def draw(self, screen):
        for cell in visitedCells:
            pygame.draw.rect(screen, cell.color, (
                cell.position[0], cell.position[1], cell.width, cell.width))
        pygame.draw.rect(screen, self.color, (self.position[0], self.position[1], self.width, self.width))


class MovingCell(Cell):
    def __init__(self, width, position, color, screenSize):
        super(MovingCell, self).__init__(width, position, color)
        self.deleteMode = 0
        self.screenSize = screenSize

    def control(self):
        pressed_keys = pygame.key.get_pressed()
        add = True
        if pressed_keys[pygame.K_SPACE]:
            if self.deleteMode == 1:
                self.deleteMode = 0
            else:
                self.deleteMode = 1
        for cell in visitedCells:
            if cell.position == self.position:
                add = False
        if add:
            visitedCells.add(Cell(self.width, self.position, (128, 0, 128)))

        if pressed_keys[pygame.K_LEFT] and self.position[0] > 0:
            self.position = (self.position[0] - self.width, self.position[1])
        elif pressed_keys[pygame.K_RIGHT] and self.position[0] < self.screenSize - self.width:
            self.position = (self.position[0] + self.width, self.position[1])
        elif pressed_keys[pygame.K_UP] and self.position[1] > 0:
            self.position = self.position = (self.position[0], self.position[1] - self.width)
        elif pressed_keys[pygame.K_DOWN] and self.position[1] < self.screenSize - self.width:
            self.position = self.position = (self.position[0], self.position[1] + self.width)

    def getNeighbors(self, cells):
        neighbors = []
        rightNeighbor = cells[(self.position[1] // self.width)][((self.position[0] // self.width) + 1)]
        leftNeighbor = cells[(self.position[1] // self.width)][((self.position[0] // self.width) - 1)]
        upperNeighbor = cells[((self.position[1] // self.width) - 1)][(self.position[0] // self.width)]
        bottomNeighbor = cells[((self.position[1] // self.width) + 1)][(self.position[0] // self.width)]
        if self.position[0] + (2 * self.width) <= self.screenSize:
            neighbors.append(rightNeighbor)
        if self.position[0] - self.width >= 0:
            neighbors.append(leftNeighbor)
        if self.position[1] + (2 * self.width) <= self.screenSize:
            neighbors.append(bottomNeighbor)
        if self.position[1] - self.width >= 0:
            neighbors.append(upperNeighbor)
        return neighbors

    def randomDrawing(self, cells):
        neighbors = self.getNeighbors(cells)
        if len(neighbors) != 0:
            randNeighbor = random.choice(neighbors)
            self.position = randNeighbor.position
            visitedCells.append(randNeighbor)
