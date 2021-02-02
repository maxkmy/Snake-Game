import pygame
import time
import random
 
pygame.init()
 
WHITE = (255, 255, 255)
YELLOW = (255, 255, 102)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)
 
WIDTH = 600
HEIGHT = 400
 
display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake Game by Max')
 
clock = pygame.time.Clock()
 
BLOCK_SIZE = 10
SNAKE_SPEED = 10
 
font_style = pygame.font.SysFont("comicsansms", 10)
score_font = pygame.font.SysFont("comicsansms", 10)
 
 
def displayScore(score):
    value = score_font.render("Your Score: " + str(score), True, YELLOW)
    display.blit(value, [0, 0])
 
 
def displaySnake(BLOCK_SIZE, snakeList):
    for block in snakeList:
        pygame.draw.rect(display, BLACK, [block[0], block[1], BLOCK_SIZE, BLOCK_SIZE])
 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    display.blit(mesg, [WIDTH / 3, HEIGHT / 2])
 
 
def main():
    gameOver = False
    gameClose = False
 
    x1 = WIDTH / 2
    y1 = HEIGHT / 2
 
    x1_change = 0
    y1_change = 0
 
    snakeList = []
    snakeLength = 1
 
    foodx = round(random.randrange(0, WIDTH - BLOCK_SIZE) / 10.0) * 10.0
    foody = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / 10.0) * 10.0
 
    while not gameOver:
 
        while gameClose == True:
            display.fill(BLUE)
            message("You Lost! Press C-Play Again or Q-Quit", RED)
            displayScore(snakeLength - 1)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameOver = True
                        gameClose = False
                    if event.key == pygame.K_c:
                        main()
                elif event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -BLOCK_SIZE
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = BLOCK_SIZE
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -BLOCK_SIZE
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = BLOCK_SIZE
                    x1_change = 0
 
        if x1 >= WIDTH or x1 < 0 or y1 >= HEIGHT or y1 < 0:
            gameClose = True
            
        x1 += x1_change
        y1 += y1_change
        display.fill(BLUE)
        pygame.draw.rect(display, GREEN, [foodx, foody, BLOCK_SIZE, BLOCK_SIZE])
        snakeHead = []
        snakeHead.append(x1)
        snakeHead.append(y1)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList[0]
 
        for block in snakeList[:-1]:
            if block == snakeHead:
                gameClose = True
 
        displaySnake(BLOCK_SIZE, snakeList)
        displayScore(snakeLength - 1)
 
        pygame.display.update()
 
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, WIDTH - BLOCK_SIZE) / 10.0) * 10.0
            foody = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / 10.0) * 10.0
            snakeLength += 1
 
        clock.tick(SNAKE_SPEED)
 
    pygame.quit()
    quit()
 
main()
