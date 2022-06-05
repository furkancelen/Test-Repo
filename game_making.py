import pygame

# In object oriented manner

# class Game:
#     _window_width, _window_height = 600, 800
#     _window_size = (_window_width, _window_height)
#     _black = (0,0,0)
#     _screen = pygame.display.set_mode(_window_size)

# In normal manner

pygame.init()

win = pygame.display.set_mode((1000, 500))
bg_image = pygame.image.load("castle_game.png")
bg = pygame.transform.scale(bg_image, (1000, 500))

pygame.display.set_caption("Castle Defense")

x = 250
y = 250
radius = 15
vel_x = 10
vel_y = 10
jump = False
i = 0
width=1000

#Main Loop
run = True
while run:

    pygame.draw.circle(win, (255, 255, 255), (int(x), int(y)), radius)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    # win.blit(bg,(i, 0))
    # win.blit(bg, (width + i,0))

    # if i == -width:
    #     win.blit(bg, (width + i, 0))
    #     i = 0
    # i -= 1


    #Movement
    user_Input = pygame.key.get_pressed()
    if user_Input[pygame.K_LEFT] and x > 0:
        x -= vel_x
    if user_Input[pygame.K_RIGHT] and x < 500:
        x += vel_x
    
    if jump is False and user_Input[pygame.K_SPACE]:
        jump = True

    if jump is True:
        y -= vel_y
        vel_y -= 1
        if vel_y < -10:
            jump = False
            vel_y = 10

    pygame.time.delay(30)
    pygame.display.update()