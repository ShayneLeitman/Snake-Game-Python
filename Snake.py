import pygame
import random
import time

pygame.init()

movement = (1, 0)

blockSize = 10


class block:

    def __init__(self, position, color=(255, 0, 0)):
        self.pos = position
        self.color = color

    def changePos(self, position):
        self.pos = position

    def getPos(self):
        return self.pos

    def getXPos(self):
        return self.pos[0]

    def getYPos(self):
        return self.pos[1]

    def draw(self, win):
        global blockSize
        x = self.pos[0]
        y = self.pos[1]
        pygame.draw.rect(win, self.color, (x, y, blockSize, blockSize))


class food:

    def __init__(self, x, y, color):
        self.unit = block((x, y), color)

    def newFood(self, curFoodList, snake):
        temp = 1



class snake:

    snakeList = []

    def __init__(self, x, y, size, color):
        self.size = size
        for i in range(size):
            self.snakeList.append(block((x - i * 10, y) , color))


    def addBodyPart(self, x, y, color):
        pass

    def move(self, direction):
        headBlock = self.snakeList[self.size - 1]
        for i in reversed(self.snakeList):
            if i == headBlock:
                self.updateHead(i, direction)



    def updateHead(self, bl, direction):
        newX = bl.getXPos() + direction[0] * blockSize
        newY = bl.getYPos() + direction[1] * blockSize
        bl.changePos((newX, newY))

# Things I need:
# create new food
# check for food collision
# check for snake - self collision
# check for key being input

# Snake obj:
# needs

def inputKey():
    global movement, gameInProgress
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameInProgress = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                movement = (-1, 0)
            elif event.key == pygame.K_RIGHT:
                movement = (1, 0)
            elif event.key == pygame.K_UP:
                movement = (0, -1)
            elif event.key == pygame.K_DOWN:
                movement = (0, 1)


def main():
    global width, height, movement, gameInProgress, b, numFood
    width = 400
    height = 400
    movement = (1, 0)
    clock = pygame.time.Clock()
    gameInProgress = True
    screen = pygame.display.set_mode((width, height))
    b = block((20, 20), color=(0, 255, 0))
    f = food(40, 40, color=(255, 255, 0))
    tmpSize = 1
    s = snake(120, 120, tmpSize, color=(100, 100, 100))

    while gameInProgress:
        clock.tick(50)
        inputKey()
        b.draw(screen)
        f.unit.draw(screen)
        #print(f.unit.getXPos())
        #print(s.snakeList[0].getPos())
        s.move(movement)
        for bodyPart in s.snakeList:
            bodyPart.draw(screen)
            #print(bodyPart.getPos())
        pygame.display.update()
        gameInProgress = False

main()
