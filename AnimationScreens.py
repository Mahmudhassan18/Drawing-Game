import pygame
import time
from pygame.locals import *

FONT = "Retro.ttf"


class Text:
    def __init__(self, text, font, size, color):
        self.text = text
        self.font = font
        self.size = size
        self.color = color

    def getText(self):
        newFont = pygame.font.Font(self.font, self.size)
        newText = newFont.render(self.text, 0, self.color)
        return newText


class AnimationScreens:
    def __init__(self, name, screen, text, runnable):
        self.screen = screen
        self.name = name
        self.screenSize = screen.get_size()
        self.i = 0
        self.text = text
        self.runningAnimation = runnable
        self.pressed_keys = pygame.key.get_pressed()

    def run(self):
        if self.pressed_keys[pygame.K_UP]:
            if self.i != 0:
                self.text[self.i][0].color = (255, 255, 255)
                self.i -= 1
        elif self.pressed_keys[pygame.K_DOWN]:
            if self.i < len(self.text) - 1:
                self.text[self.i][0].color = (255, 255, 255)
                self.i += 1
        elif self.pressed_keys[pygame.K_RETURN]:
            if self.i == len(self.text) - 1:
                pygame.quit()
                quit()
            else:
                self.runningAnimation = self.text[self.i][1]

        self.text[self.i][0].color = (0, 0, 0)
        self.screen.fill((100, 10, 100))
        text_rect = []
        for j in range(len(self.text)):
            text_rect.append(self.text[j][0].getText().get_rect())
            self.screen.blit(self.text[j][0].getText(),
                             (self.screenSize[0] // 2 - (text_rect[j][2] // 2), self.screenSize[0] // 2 + (j * 60)))
        pygame.display.update()
        self.pressed_keys = pygame.key.get_pressed()
        time.sleep(0.1)

class MainMenu(AnimationScreens):
    def __init__(self, name, screen):
        self.text = [(Text("START", FONT, 75, (255, 255, 255)), StartMenu("Start Menu", screen)),
                     (Text("OPTIONS", FONT, 75, (255, 255, 255)), "OPTIONS TODO"),
                     (Text("QUIT", FONT, 75, (255, 255, 255)), "quit")]
        self.runnable = True
        super(MainMenu, self).__init__(name, screen, self.text, self)

class StartMenu(AnimationScreens):
    def __init__(self, name, screen):
        self.text = [(Text("RANDOM DRAWING", FONT, 75, (255, 255, 255)), "RANDOM TODO"),
                     (Text("CONTROLLED DRAWING", FONT, 75, (255, 255, 255)), "CONTROLLED TODO")]
        super(StartMenu, self).__init__(name, screen, self.text, self)


