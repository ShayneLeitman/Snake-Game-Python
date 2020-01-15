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

    def setPos(self, position):
        self.pos = position

    def getPos(self):
        return self.pos

    def getXPos(self):
        return self.pos[0]

    def getYPos(self):
        return self.pos[1]

    def getColor(self):
        return self.color

    def draw(self, win):
        global blockSize
        x = self.pos[0]
        y = self.pos[1]
        pygame.draw.rect(win, self.color, [x, y, blockSize, blockSize])


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
            self.snakeList.append(block((x - i * 10, y), color))

    def addBodyPart(self, x, y, color):
        pass

    def move(self, direction):
        # headBlock = self.snakeList[0]
        direct = direction
        newList = []
        for i in range(len(self.snakeList) - 1, 0, -1):
            self.snakeList[i].setPos(self.snakeList[i - 1].getPos())
            print(self.snakeList[i].getPos())

        newX = self.snakeList[0].getXPos() + direction[0] * blockSize
        newY = self.snakeList[0].getYPos() + direction[1] * blockSize
        self.snakeList[0].setPos((newX, newY))
        print(self.snakeList[0].getPos())


    def updateHead(self, bl, direction):
        newX = bl.getXPos() + direction[0] * blockSize
        newY = bl.getYPos() + direction[1] * blockSize
        bl.setPos((newX, newY))


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
    tmpSize = 5
    s = snake(120, 120, tmpSize, color=(100, 100, 100))

    while gameInProgress:
        screen.fill(color=((60, 160, 220)))
        clock.tick(5)
        inputKey()
        #b.draw(screen)
        #f.unit.draw(screen)
        print("MOVE")
        s.move(movement)
        for bodyPart in s.snakeList:
            bodyPart.draw(screen)

        pygame.display.update()
        #gameInProgress = False


main()
