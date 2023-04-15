import pygame
import os

'''
get_ticks() returns milliseconds
60 FPS
1 frame takes 16.67 ms
16.67 * 20 = 334 ms
'''

FPS = 60
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SNHEIGHT = 40
SNWIDTH = 40
JUMPHEIGHT = 30#constant for how hight snek gets
JUMPVEL = 5


ground0 = pygame.Rect(200, 350, 200, 5)
ground = [ground0]

snek = pygame.Rect(300, 300, SNWIDTH, SNHEIGHT)
wall = pygame.image.load(os.path.join('sprites', 'wall2.png'))
#wall = pygame.transform.scale(wall, (150, 75))
snakeRight1 = pygame.image.load(os.path.join('sprites', 'snake_right1.png'))
snakeRight1 = pygame.transform.scale(snakeRight1,(SNWIDTH, SNHEIGHT))
snakeRight2 = pygame.image.load(os.path.join('sprites', 'snake_right2.png'))
snakeRight2 = pygame.transform.scale(snakeRight2,(SNWIDTH, SNHEIGHT))
snakeRight3 = pygame.image.load(os.path.join('sprites', 'snake_right3.png'))
snakeRight3 = pygame.transform.scale(snakeRight3,(SNWIDTH, SNHEIGHT))

snakeLeft1 = pygame.image.load(os.path.join('sprites', 'snake_left1.png'))
snakeLeft1 = pygame.transform.scale(snakeLeft1,(SNWIDTH, SNHEIGHT))
snakeLeft2 = pygame.image.load(os.path.join('sprites', 'snake_left2.png'))
snakeLeft2 = pygame.transform.scale(snakeLeft2,(SNWIDTH, SNHEIGHT))
snakeLeft3 = pygame.image.load(os.path.join('sprites', 'snake_left3.png'))
snakeLeft3 = pygame.transform.scale(snakeLeft3,(SNWIDTH, SNHEIGHT))

staticSnake1 = pygame.image.load(os.path.join('sprites', 'staticSnake1.png'))
staticSnake1 = pygame.transform.scale(staticSnake1,(SNWIDTH, SNHEIGHT))
staticSnake2 = pygame.image.load(os.path.join('sprites', 'staticSnake2.png'))
staticSnake2 = pygame.transform.scale(staticSnake2,(SNWIDTH, SNHEIGHT))
staticSnake3 = pygame.image.load(os.path.join('sprites', 'staticSnake3.png'))
staticSnake3 = pygame.transform.scale(staticSnake3,(SNWIDTH, SNHEIGHT))

snJump1 = pygame.image.load(os.path.join('sprites', 'snJump1.png'))
snJump1 = pygame.transform.scale(snJump1, (SNWIDTH, SNHEIGHT))
snJump2 = pygame.image.load(os.path.join('sprites', 'snJump2.png'))
snJump2 = pygame.transform.scale(snJump2, (SNWIDTH, SNHEIGHT))
snJump3 = pygame.image.load(os.path.join('sprites', 'snJump3.png'))
snJump3 = pygame.transform.scale(snJump3, (SNWIDTH, SNHEIGHT))
snJump4 = pygame.image.load(os.path.join('sprites', 'snJump4.png'))
snJump4 = pygame.transform.scale(snJump4, (SNWIDTH, SNHEIGHT))
snJump5 = pygame.image.load(os.path.join('sprites', 'snJump5.png'))
snJump5 = pygame.transform.scale(snJump5, (SNWIDTH, SNHEIGHT))
snJump6 = pygame.image.load(os.path.join('sprites', 'snJump6.png'))
snJump6 = pygame.transform.scale(snJump6, (SNWIDTH, SNHEIGHT))
snJump7 = pygame.image.load(os.path.join('sprites', 'snJump7.png'))
snJump7 = pygame.transform.scale(snJump7, (SNWIDTH, SNHEIGHT))
snJump8 = pygame.image.load(os.path.join('sprites', 'snJump8.png'))
snJump8 = pygame.transform.scale(snJump8, (SNWIDTH, SNHEIGHT))

snJump = [snJump1, snJump2, snJump3, snJump4, snJump5, snJump6, snJump7, snJump8]
rightMove = [snakeRight1, snakeRight2, snakeRight3, snakeRight2]#though not created first snakeright2 looks best as a standing still
leftMove = [snakeLeft1, snakeLeft2, snakeLeft3, snakeLeft2]
staticSn = [staticSnake1, staticSnake2, staticSnake3, staticSnake2]



def drawWindow(snek, rightMove, rightMoveInd, direction, leftMove, leftMoveInd, staticSn, staticSnInd, snJump, snJumpInd):
    WIN.fill(WHITE)
    for i in range(0,8):
        for j in range(0, 8):
            WIN.blit(wall,(wall.get_width() * i, wall.get_height() * j))
    pygame.draw.rect(WIN, BLACK, ground0)
    if direction == 'right':
        WIN.blit(rightMove[rightMoveInd], (snek.x, snek.y))
    elif direction == 'left':
        WIN.blit(leftMove[leftMoveInd], (snek.x, snek.y))
    elif direction == 'up':
        WIN.blit(snJump[snJumpInd], (snek.x, snek.y))
    else:
        WIN.blit(staticSn[staticSnInd], (snek.x, snek.y))
    pygame.display.update()

def main():
    curJumpHeight = 0#variable for how much left the snek has to jump
    direction = 'none'
    rightMoveInd = 0
    leftMoveInd = 0
    staticSnInd = 0
    snJumpInd = 0
    clock = pygame.time.Clock()
    run = True
    startTime = pygame.time.get_ticks()
    while(run):
        clock.tick(FPS)#insures we dont go over FPS(60) frames per second
        for event in pygame.event.get(): #gets list of all events and loops through them
            if event.type == pygame.QUIT: #if the event is quit
                run = False
                pygame.quit()

        if curJumpHeight != 0:
            curJumpHeight -= JUMPVEL
            snek.y -= JUMPVEL
        elif snek.collidelist(ground) == -1:
            snek.y += 1

        keysPressed = pygame.key.get_pressed()
        if (keysPressed[pygame.K_w] or keysPressed[pygame.K_SPACE]) and snek.collidelist(ground) != -1:
            curJumpHeight = JUMPHEIGHT
            for i in range(0,8):
                drawWindow(snek, rightMove, rightMoveInd, 'up', leftMove, leftMoveInd, staticSn, staticSnInd, snJump, snJumpInd)
                snJumpInd = (snJumpInd + 1)% 8
                pygame.time.delay(20)

        if keysPressed[pygame.K_d]:
            direction = 'right'
            snek.x += 2
            currentTime = pygame.time.get_ticks()
            if currentTime - startTime >= 100:
                rightMoveInd = (rightMoveInd + 1) % 4
                startTime = currentTime
        elif keysPressed[pygame.K_a]:
            direction = 'left'
            snek.x -= 2
            currentTime = pygame.time.get_ticks()
            if currentTime - startTime >= 100:
                leftMoveInd = (leftMoveInd + 1) % 4
                startTime = currentTime
        else:
            direction = 'none'
            currentTime = pygame.time.get_ticks()
            if currentTime - startTime >= 166:
                staticSnInd = (staticSnInd + 1) % 4
                startTime = currentTime

        drawWindow(snek, rightMove, rightMoveInd, direction, leftMove, leftMoveInd, staticSn, staticSnInd, snJump, snJumpInd)

if __name__ == "__main__":
    main()