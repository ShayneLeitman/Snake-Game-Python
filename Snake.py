import pygame
import random
import time

pygame.init()

movement = (1, 0)

blockSize = 10

class block():

    def __init__(self, position, color=(255, 0, 0)):
        self.pos = position
        self.color = color


    def draw(self, win):
        global blockSize
        x = self.pos[0]
        y = self.pos[1]
        pygame.draw.rect(win, self.color, (x, y, blockSize, blockSize))


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
    global width, height, snake, food, gameInProgress, b
    width = 400
    height = 400
    snake = 0
    food = 0
    clock = pygame.time.Clock()
    gameInProgress = True
    screen = pygame.display.set_mode((width, height))
    b = block((20, 20), color=(0,255,0))

    while gameInProgress:
        clock.tick(50)
        inputKey()
        b.draw(screen)
        pygame.display.update()


main()
