import pygame
class Stage():
    def __init__(self, WIN) -> None:
        print(__file__)
        self.WIN = WIN

#WIN.blit(drawing[1][drawing[2]], (drawing[0].x, drawing[0].y))
    def drawWindow(self, listOfDrawings):
        for i in range(0, 11):
            for j in range(0, 12):
                self.WIN.blit(listOfDrawings[0][1][0], listOfDrawings[0][1][0].get_width() * i, listOfDrawings[0][1][0] * j)#[0]firstin lod [1]listoimg [0]firstimg
        for i in range(1, len(listOfDrawings)):
            self.WIN.blit(listOfDrawings[i][1][listOfDrawings[i][2]], (listOfDrawings[i][0].x, listOfDrawings[i][0].y))
        pygame.display.update()