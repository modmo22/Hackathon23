import pygame


from Abstract.mob import Mob
class Snek(Mob):
    def __init__(self):
        self._JUMPHEIGHT = 30
        super().__init__()
        # print(__file__)

        self.image = pygame


    def move(keys_pressed):
        """controls the movement of the snake by receiving key presses from the level module."""
        if (keys_pressed[pygame.K_w] or keys_pressed[pygame.K_SPACE]) and snek.collidelist(ground) != -1:
            snCrouchInd = 0
            curJumpHeight = self._JUMPHEIGHT
            for i in range(0,8):
                # I'm pretty sure this is going to be a method in the Springboard class. Import springboard
                # drawWindow(snek, rightMove, rightMoveInd, 'up', leftMove, leftMoveInd, staticSn, staticSnInd, snJump, snJumpInd, snCrouch, snCrouchInd)
                snJumpInd = (snJumpInd + 1)% 8
                pygame.time.delay(20)

        if keys_pressed[pygame.K_d]:
            snCrouchInd = 0
            direction = 'right'
            snek.x += 2
            currentTime = pygame.time.get_ticks()
            if currentTime - startTime >= 100:
                rightMoveInd = (rightMoveInd + 1) % 4
                startTime = currentTime
        elif keys_pressed[pygame.K_a]:
            snCrouchInd = 0
            direction = 'left'
            snek.x -= 2
            currentTime = pygame.time.get_ticks()
            if currentTime - startTime >= 100:
                leftMoveInd = (leftMoveInd + 1) % 4
                startTime = currentTime
        elif keys_pressed[pygame.K_s]:
            direction = 'down'
            currentTime = pygame.time.get_ticks()
            if currentTime - startTime >= 100:
                if snCrouchInd != 3:
                    snCrouchInd = (snCrouchInd + 1) % 4
                startTime = currentTime
        else:
            snCrouchInd = 0
            direction = 'none'
            currentTime = pygame.time.get_ticks()
            if currentTime - startTime >= 166:
                staticSnInd = (staticSnInd + 1) % 4
                startTime = currentTime
        

    def run():
        """Runs the game and controls the level flow."""
