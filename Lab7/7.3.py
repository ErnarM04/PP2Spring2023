import pygame

pygame.init()
screen = pygame.display.set_mode((1920, 1000))
done = False
x = 25
y = 25

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP] and y >= 30: y -= 20
    if pressed[pygame.K_DOWN] and y <= 970: y += 20
    if pressed[pygame.K_LEFT] and x >= 30: x -= 20
    if pressed[pygame.K_RIGHT] and x <= 1890: x += 20

    screen.fill((0, 0, 0))

    pygame.draw.circle(screen, (0, 0, 225), (x, y), 25)

    pygame.display.flip()
    clock.tick(60)