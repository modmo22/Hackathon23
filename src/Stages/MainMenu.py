import pygame
import os, sys
class MainMenu():
    def __init__(self, WIN):
        self.WIN = WIN
        self.BUTTWIDTH = 100
        self.BUTTHEIGHT = 100

    def draw(self):
        TITLEWIDTH = 600
        TITLEHEIGHT = 100
        Title = pygame.image.load(os.path.join('src','Stages','Sprites', 'floor.png'))
        Title = pygame.transform.scale(Title, (TITLEWIDTH, TITLEHEIGHT))
        BUTT1 = pygame.image.load(os.path.join('src','Stages','Sprites', 'floor.png'))#unfinished
        BUTT1 = pygame.transform.scale(BUTT1, (self.BUTTWIDTH, self.BUTTHEIGHT))
        self.button1 = pygame.Rect(300, 300, self.BUTTWIDTH, self.BUTTHEIGHT)
        BUTT2 = pygame.image.load(os.path.join('src','Stages','Sprites', 'floor.png'))#unfinished
        BUTT2 = pygame.transform.scale(BUTT2, (self.BUTTWIDTH, self.BUTTHEIGHT))
        self.button2 = pygame.Rect(700, 300, self.BUTTWIDTH, self.BUTTHEIGHT)
        BUTT3 = pygame.image.load(os.path.join('src','Stages','Sprites', 'floor.png'))#unfinished
        BUTT3 = pygame.transform.scale(BUTT3, (self.BUTTWIDTH, self.BUTTHEIGHT))
        self.button3 = pygame.Rect(700, 300, self.BUTTWIDTH, self.BUTTHEIGHT)
        BUTT4 = pygame.image.load(os.path.join('src','Stages','Sprites', 'floor.png'))#unfinished
        BUTT4 = pygame.transform.scale(BUTT4, (self.BUTTWIDTH, self.BUTTHEIGHT))
        self.button4 = pygame.Rect(700, 700, self.BUTTWIDTH, self.BUTTHEIGHT)
        BACKGROUND = pygame.image.load(os.path.join('src','Stages','Sprites', 'floor.png'))#place holder image for now
        self.WIN.blit(BACKGROUND, (0,0))
        self.WIN.blit(Title, (675 - (TITLEWIDTH//2), 100))
        self.WIN.blit(BUTT1, (self.button1.x, self.button1.y))
        self.WIN.blit(BUTT2, (self.button2.x, self.button2.y))
        self.WIN.blit(BUTT1, (self.button3.x, self.button3.y))
        self.WIN.blit(BUTT1, (self.button4.x, self.button4.y))
        pygame.display.update()

    def run(self):
        #window is 1350 by 750
        end = 0
        while(end == 0):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.draw()
            pygame.event.get()
            mousePos = pygame.mouse.get_pos()
            mouseState = pygame.mouse.get_pressed()
            if mouseState[0] == True:
                if (mousePos[0] >= self.button1.x and mousePos[0] <= (self.button1.x + self.BUTTWIDTH)) and (mousePos[1] >= self.button1.y and mousePos[1] <= (self.button1.y + self.BUTTHEIGHT)):
                    return 1
                elif (mousePos[0] >= self.button2.x and mousePos[0] <= (self.button2.x + self.BUTTWIDTH)) and (mousePos[1] >= self.button2.y and mousePos[1] <= (self.button2.y + self.BUTTHEIGHT)):
                    return 2
                elif (mousePos[0] >= self.button3.x and mousePos[0] <= (self.button3.x + self.BUTTWIDTH)) and (mousePos[1] >= self.button3.y and mousePos[1] <= (self.button3.y + self.BUTTHEIGHT)):
                    return 3
                elif (mousePos[0] >= self.button4.x and mousePos[0] <= (self.button4.x + self.BUTTWIDTH)) and (mousePos[1] >= self.button4.y and mousePos[1] <= (self.button4.y + self.BUTTHEIGHT)):
                    return 4