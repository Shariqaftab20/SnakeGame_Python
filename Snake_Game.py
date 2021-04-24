import pygame
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
snake_x=45
snake_y=10
snake_size=10
fps=30

clock=pygame.time.Clock()

while not exit_game:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit_game=True
            #Right
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                snake_x=snake_x+10
            #Down
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_DOWN:
                snake_y=snake_y+10
            # Up
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                snake_y=snake_y-10
            # Left
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                snake_x=snake_x-10

    gameWindow.fill(white)
    pygame.draw.rect(gameWindow,black,[snake_x,snake_y,snake_size,snake_size])
    pygame.display.update()
    clock.tick(fps)



pygame.quit()
quit()
