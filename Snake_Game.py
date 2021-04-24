import pygame
import random
pygame.init()

#color
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)

#screen dimention
screen_width=1200
screen_height=600

gameWindow=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("MySnakeGame")
pygame.display.update()

exit_game=False
quite_game=False
food_x=random.randint(0,screen_width)
food_y=random.randint(0,screen_height)
velocity_x=0
velocity_y=0
snake_x=45
snake_y=10
food_size_x=10
food_size_y=10
snake_size_x=10
snake_size_y=10
score=0
fps=30

clock=pygame.time.Clock()

while not exit_game:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit_game=True
        if event.type==pygame.KEYDOWN:
            #Right
            if event.key==pygame.K_RIGHT:
                velocity_x=5
                velocity_y=0
            #Down
            if event.key==pygame.K_DOWN:
                velocity_x = 0
                velocity_y = 5
            # Up
            if event.key==pygame.K_UP:
                velocity_x = 0
                velocity_y = -5
            # Left
            if event.key==pygame.K_LEFT:
                velocity_x = -5
                velocity_y = 0
    if abs(snake_x-food_x)<6 and abs(snake_y-food_y)<6:
        snake_size_x+=10
        score+=1
        print("Score:",score)
        food_x = random.randint(0, screen_width)
        food_y = random.randint(0, screen_height)

    snake_x+=velocity_x
    snake_y+=velocity_y
    gameWindow.fill(white)
    pygame.draw.rect(gameWindow,red,[food_x,food_y,food_size_x,food_size_y])
    pygame.draw.rect(gameWindow,black,[snake_x,snake_y,snake_size_x,snake_size_y])
    pygame.display.update()
    clock.tick(fps)



pygame.quit()
quit()
