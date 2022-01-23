import pygame
from pygame.locals import *

font = "Retro.ttf"
def text_format(message, textFont, textSize, textColor):
    newFont = pygame.font.Font(textFont, textSize)
    newText = newFont.render(message, 0, textColor)
    return newText


class AnimationScreens:
    def __init__(self, name, screen):
        self.screen = screen
        self.screenName = name

    def run(self):
        pass

class MainMenu(AnimationScreens):
    def __init__(self, name, screen):
        super(MainMenu, self).__init__(name, screen)
        self.name = name
        self.cellWidth = 10
        self.fps = 10000
        self.runningOption = "randomDrawing"

    def run(self):
        runnable = True
        selected = "start"
        optionsMenu = OptionMenu("Options Menu", self.screen)
        startMenu = StartMenu("Start Menu", self.screen)
        while runnable:
            self.screen.fill((100, 10, 100))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and selected == "quit":
                        selected = "options"
                    elif event.key == pygame.K_UP and selected == "options":
                        selected = "start"
                    if event.key == pygame.K_DOWN and selected == "start":
                        selected = "options"
                    elif event.key == pygame.K_DOWN and selected == "options":
                        selected = "quit"
                    if event.key == pygame.K_RETURN:
                        if selected == "start":
                            startMenu.run()
                            self.runningOption = startMenu.selected
                            runnable = False
                        if selected == "options":
                            optionsMenu.run()
                            self.cellWidth = optionsMenu.cellWidth
                            self.fps = optionsMenu.fps
                        if selected == "quit":
                            pygame.quit()
                            quit()

            if selected == "start":
                text_start = text_format("START", font, 75, (255, 255, 255))
            else:
                text_start = text_format("START", font, 75, (0, 0, 0))

            if selected == "options":
                text_options = text_format("OPTIONS", font, 75, (255, 255, 255))
            else:
                text_options = text_format("OPTIONS", font, 75, (0, 0, 0))

            if selected == "quit":
                text_quit = text_format("QUIT", font, 75, (255, 255, 255))
            else:
                text_quit = text_format("QUIT", font, 75, (0, 0, 0))

            start_rect = text_start.get_rect()
            options_rect = text_options.get_rect()
            quit_rect = text_quit.get_rect()

            # Main Menu Text
            self.screen.blit(text_start, (600 / 2 - (start_rect[2] / 2), 300))
            self.screen.blit(text_options, (600 / 2 - (options_rect[2] / 2), 360))
            self.screen.blit(text_quit, (600 / 2 - (quit_rect[2] / 2), 420))
            pygame.display.update()

class OptionMenu(AnimationScreens):
    def __init__(self, name, screen):
        super(OptionMenu, self).__init__(name, screen)
        self.cellWidth = 10
        self.fps = 10000

    def run(self):
        runnable = True
        selected = "cellWidth"
        while runnable:
            self.screen.fill((100, 10, 100))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        selected = "cellWidth"

                    if event.key == pygame.K_DOWN:
                        selected = "fps"

                    if event.key == pygame.K_RIGHT:
                        if selected == "cellWidth":
                            if self.cellWidth < 30:
                                self.cellWidth += 1
                        else:
                            self.fps += 1

                    elif event.key == pygame.K_LEFT:
                        if selected == "cellWidth":
                            if self.cellWidth > 1:
                                self.cellWidth -= 1
                        else:
                            if self.fps > 5:
                                self.fps -= 1

                    if event.key == pygame.K_RETURN:
                        runnable = False

            if selected == "cellWidth":
                text_cellWidth = text_format("CELL WIDTH:" + str(self.cellWidth), font, 75, (255, 255, 255))
            else:
                text_cellWidth = text_format("CELL WIDTH:" + str(self.cellWidth), font, 75, (0, 0, 0))

            if selected == "fps":
                text_fps = text_format("FPS:" + str(self.fps), font, 75, (255, 255, 255))
            else:
                text_fps = text_format("FPS:" + str(self.fps), font, 75, (0, 0, 0))

            cellWidth_rect = text_cellWidth.get_rect()
            fps_rect = text_fps.get_rect()

            self.screen.blit(text_cellWidth, (300 - (cellWidth_rect[2] / 2), 300))
            self.screen.blit(text_fps, (300 - (fps_rect[2] / 2), 360))
            pygame.display.update()

class StartMenu(AnimationScreens):
    def __init__(self, name, screen):
        super(StartMenu, self).__init__(name, screen)
        self.selected = "randomDrawing"

    def run(self):
        runnable = True
        while runnable:
            self.screen.fill((100, 10, 100))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.selected = "randomDrawing"
                    if event.key == pygame.K_DOWN:
                        self.selected = "controlledDrawing"
                    if event.key == pygame.K_RETURN:
                        runnable = False

                if self.selected == "randomDrawing":
                    text_randomDrawing = text_format("RANDOM DRAWING", font, 75, (255, 255, 255))
                else:
                    text_randomDrawing = text_format("RANDOM DRAWING", font, 75, (0, 0, 0))

                if self.selected == "controlledDrawing":
                    text_controlledDrawing = text_format("CONTROLLED DRAWING", font, 75, (255, 255, 255))
                else:
                    text_controlledDrawing = text_format("CONTROLLED DRAWING", font, 75, (0, 0, 0))

                controlledDrawing_rect = text_controlledDrawing.get_rect()
                randomDrawing_rect = text_randomDrawing.get_rect()

                self.screen.blit(text_randomDrawing, (300 - (randomDrawing_rect[2] / 2), 300))
                self.screen.blit(text_controlledDrawing, (300 - (controlledDrawing_rect[2] / 2), 360))
                pygame.display.update()






