import pygame
import random
import time

pygame.init()

movement = (1, 0)

blockSize = 10

width = 400
height = 400


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

    def setColor(self, color):
        self.color = color

    def draw(self, win):
        global blockSize
        x = self.pos[0]
        y = self.pos[1]
        pygame.draw.rect(win, self.color, [x, y, blockSize, blockSize])


class food:
    foodList = []

    def __init__(self, size):
        self.size = size

    def startCreateFood(self, tmpSnake, color):
        for i in range(self.size):
            self.newRandFood(tmpSnake, color)

    def newRandFood(self, tmpSnake, color):
        tmp = True
        x = random.randrange(0, width, 10)
        y = random.randrange(0, height, 10)
        while tmp:
            tmp = False
            for i in tmpSnake.snakeList:
                if i.getXPos == x and i.getYPos == y:
                    tmp = True
                    break

            for n in self.foodList:
                if i.getXPos == x and i.getYPos == y:
                    tmp = True
                    break

        self.foodList.append(block((x, y), color))



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
            #print(self.snakeList[i].getPos())

        newX = self.snakeList[0].getXPos() + direction[0] * blockSize
        newY = self.snakeList[0].getYPos() + direction[1] * blockSize
        self.snakeList[0].setPos((newX, newY))
        #print(self.snakeList[0].getPos())


    def updateHead(self, bl, direction):
        newX = bl.getXPos() + direction[0] * blockSize
        newY = bl.getYPos() + direction[1] * blockSize
        bl.setPos((newX, newY))

    def getHeadXPos(self):
        return self.snakeList[0].getXPos()

    def getHeadYPos(self):
        return self.snakeList[0].getYPos()



def foodSnakeCollision(tmpSnake, tmpFood):
    for foodPiece in tmpFood.foodList:
        if tmpSnake.getHeadXPos() == foodPiece.getXPos() and tmpSnake.getHeadYPos() == foodPiece.getYPos():
            # print("COLLIDE!")
            tmpFood.foodList.remove(foodPiece)
            print(tmpFood.foodList)
            


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
            if event.key == pygame.K_LEFT and movement != (1, 0):
                movement = (-1, 0)
                break
            elif event.key == pygame.K_RIGHT and movement != (-1, 0):
                movement = (1, 0)
                break
            elif event.key == pygame.K_UP and movement != (0, 1):
                movement = (0, -1)
                break
            elif event.key == pygame.K_DOWN and movement != (0, -1):
                movement = (0, 1)
                break


def main():
    global width, height, movement, gameInProgress, b, numFood
    # width = 400
    # height = 400
    movement = (1, 0)
    clock = pygame.time.Clock()
    gameInProgress = True
    screen = pygame.display.set_mode((width, height))
    tmpSize = 5
    s = snake(120, 120, tmpSize, color=(200, 50, 200))
    numFood = 2
    f = food(numFood)
    f.startCreateFood(s, color=(200, 200, 200))


    while gameInProgress:
        screen.fill(color=((60, 160, 220)))
        clock.tick(15)
        inputKey()
        s.move(movement)
        foodSnakeCollision(s, f)
        for bodyPart in s.snakeList:
            bodyPart.draw(screen)

        for foodPiece in f.foodList:
            foodPiece.draw(screen)

        pygame.display.update()
        #gameInProgress = False


main()
