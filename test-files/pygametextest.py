# My first PyGame program.


import pygame

pygame.init()

win = pygame.display.set_mode((500,500))

pygame.display.set_caption("KUULGAME")

x_coord = 50
y_coord = 420

run = True

while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        y_coord -= 10
    if keys[pygame.K_DOWN]:
        y_coord += 10

    win.fill((0,0, 0))
    pygame.draw.rect(win, (255,0,0), (x_coord, y_coord, 40, 60))
    pygame.display.update()

exit()

