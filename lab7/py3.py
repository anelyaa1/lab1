import pygame
pygame.init()
scr = pygame.display.set_mode((600, 500))
done = False
is_red = True

x = 30
y = 30
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                        is_red = not is_red

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]: y -= 20
    if pressed[pygame.K_DOWN]: y += 20
    if pressed[pygame.K_LEFT]: x -= 20
    if pressed[pygame.K_RIGHT]: x += 20

    scr.fill((255, 255, 255))
    color = (200, 0, 0)
    pygame.draw.circle(scr, color, (x, y), 25)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()