import pygame
import asyncio
from Mobs.bat import Bat
from Mobs.aligator import Aligator
from Mobs.snek import Snek
from Stages.MainMenu import MainMenu
from Stages.Level1 import Level1
from Stages.Level2 import Level2
from Stages.Level3 import Level3

#GLOBALS 
WHITE = (255, 255, 255)
FPS = 60
WIDTH, HEIGHT = 1350, 750


class Springboard():
    def __init__(self):
        print(__file__)

    def run(self):
        WIN = pygame.display.set_mode((WIDTH, HEIGHT))  
        clock = pygame.time.Clock()
        run = asyncio.run(self.sprang(WIN))
        # != False is very intentional, do not replace with while(run)!!!!
        while(run != False):
            clock.tick(FPS)#insures we dont go over FPS(60) frames per second
            for event in pygame.event.get(): #gets list of all events and loops through them
                if event.type == pygame.QUIT: #if the event is quit
                    run = False
                    pygame.quit()
    
    async def sprang(WIN: pygame.Surface):
        sel = 0
        while (sel != -1):
            if sel == 0:
                sel = MainMenu(WIN).run()
            elif sel == 1:
                sel = Level1(WIN).run()
            elif sel == 2:
                sel = Level2(WIN).run()
            elif sel == 3:
                sel = Level3(WIN).run()
        return False

              

