import pygame
import os

WHITE = (255, 255, 255)
FPS = 60
WIDTH, HEIGHT = 1350, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

wall = pygame.image.load(os.path.join('src','Stages','sprites', 'wall2.png'))
floor = pygame.image.load(os.path.join('src','Stages','sprites', 'floor.png'))
floor = pygame.transform.scale(floor, (600, 60))

listOfDrawings = []

def drawWindow(listOfDrawings):
    WIN.fill(WHITE)
    for i in range(0,11):
        for j in range(0, 12):
            WIN.blit(wall,(wall.get_width() * i, wall.get_height() * j))
    for i in range(0, 3):
        WIN.blit(floor, (floor.get_width() * i, 500))
    
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