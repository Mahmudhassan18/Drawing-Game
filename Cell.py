import pygame
import random


class Cell:
    def __init__(self, width, position, color):
        self.width = width
        self.position = position
        self.sides = [True, True, True, True]
        self.visited = 0
        self.color = color

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.position[0], self.position[1], self.width, self.width))
        # if self.visited == 1:
        #     pygame.draw.rect(screen, self.color, (self.position[0], self.position[1], self.width, self.width))
        # if self.sides[0]:
        #     pygame.draw.line(screen, (0, 0, 0), self.position, (self.position[0] + self.width, self.position[1]))
        # if self.sides[1]:
        #     pygame.draw.line(screen, (0, 0, 0), (self.position[0] + self.width, self.position[1]),
        #                      (self.position[0] + self.width, self.position[1] + self.width))
        # if self.sides[2]:
        #     pygame.draw.line(screen, (0, 0, 0), (self.position[0], self.position[1] + self.width),
        #                      (self.position[0] + self.width, self.position[1] + self.width))
        # if self.sides[3]:
        #     pygame.draw.line(screen, (0, 0, 0), self.position, (self.position[0], self.position[1] + self.width))


class MovingCell(Cell):
    def __init__(self, width, position, color):
        Cell(width, position, color)
        self.x = position[0]
        self.y = position[1]
        self.color = color
        self.width = width
        self.deleteMode = 0
        self.i = 0
        self.j = 0

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.width))

    def control(self):
        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[pygame.K_SPACE]:
            if self.deleteMode == 1:
                self.deleteMode = 0
            else:
                self.deleteMode = 1

        if pressed_keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.width
        elif pressed_keys[pygame.K_RIGHT] and self.x < 600 - self.width:
            self.x += self.width
        elif pressed_keys[pygame.K_UP] and self.y > 0:
            self.y -= self.width
        elif pressed_keys[pygame.K_DOWN] and self.y < 600 - self.width:
            self.y += self.width

    def checkVisited(self, cells):
        for i in range(len(cells)):
            for j in range(len(cells[0])):
                if cells[i][j].position == (self.x, self.y):
                    if self.deleteMode == 1:
                        cells[i][j].visited = 0
                    else:
                        cells[i][j].visited = 1

    def getUnvisitedNeighbors(self, cells):
        rightNeig = cells[(self.y // self.width)][((self.x // self.width) + 1) % len(cells[0])]
        leftNeig = cells[(self.y // self.width)][((self.x // self.width) - 1) % len(cells[0])]
        upperNeig = cells[((self.y // self.width) - 1) % len(cells[0])][(self.x // self.width)]
        bottomNeig = cells[((self.y // self.width) + 1) % len(cells[0])][(self.x // self.width)]
        unvisitedNeighbors = []
        if self.x == 0 and self.y == 0:
            # if rightNeig.visited == 0:
            unvisitedNeighbors.append(rightNeig)
            # if bottomNeig.visited == 0:
            unvisitedNeighbors.append(bottomNeig)

        if self.x == 0 and self.y != 0:
            # if rightNeig.visited == 0:
            unvisitedNeighbors.append(rightNeig)
            # if upperNeig.visited == 0:
            unvisitedNeighbors.append(upperNeig)
            # if bottomNeig.visited == 0:
            unvisitedNeighbors.append(bottomNeig)

        if self.x != 0 and self.y == 0:
            # if rightNeig.visited == 0:
            unvisitedNeighbors.append(rightNeig)
            # if leftNeig.visited == 0:
            unvisitedNeighbors.append(leftNeig)
            # if bottomNeig.visited == 0:
            unvisitedNeighbors.append(bottomNeig)

        if self.x != 0 and self.y != 0:
            # if rightNeig.visited == 0:
            unvisitedNeighbors.append(rightNeig)
            # if upperNeig.visited == 0:
            unvisitedNeighbors.append(upperNeig)
            # if bottomNeig.visited == 0:
            unvisitedNeighbors.append(bottomNeig)
            # if leftNeig.visited == 0:
            unvisitedNeighbors.append(leftNeig)

        return unvisitedNeighbors

    def randomDrawing(self, cells):
        unvisitedNeighbors = self.getUnvisitedNeighbors(cells)
        if len(unvisitedNeighbors) != 0:
            randNeighbor = random.choice(unvisitedNeighbors)
            self.x = randNeighbor.position[0]
            self.y = randNeighbor.position[1]
            randNeighbor.visited = 1

    def drawImage(self, color, cells):
        if self.j < (len(cells[0])):
            self.x = cells[self.j][self.i].position[0]
            self.y = cells[self.j][self.i].position[1]
            cells[self.j][self.i].color = color[self.j][self.i]
            if self.i < (len(cells[0]) - 1):
                self.i += 1
            else:
                self.i = 0
                self.j += 1





