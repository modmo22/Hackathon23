import pygame
import os

WHITE = (255, 255, 255)
FPS = 60
WIDTH, HEIGHT = 1350, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

listOfDrawings = []
#[(Rect, listofIMG, IMGindex)]
#in stationary objects listofIMG is one image

def drawWindow(listOfDrawings):
    WIN.fill(WHITE)
    for drawing in listOfDrawings:
        WIN.blit(drawing[1][drawing[2]], (drawing[0].x, drawing[0].y))
    pygame.display.update()

def main():
    clock = pygame.time.Clock()
    run = True
    while(run):
        clock.tick(FPS)#insures we dont go over FPS(60) frames per second
        for event in pygame.event.get(): #gets list of all events and loops through them
            if event.type == pygame.QUIT: #if the event is quit
                run = False
                pygame.quit()

        drawWindow(listOfDrawings)
main()