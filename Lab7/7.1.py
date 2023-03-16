import datetime
from time import sleep
import pygame
import os
from math import cos, sin, pi

sang = 270 + int(datetime.datetime.now().strftime("%S")) * 6
mang = 270 + int(datetime.datetime.now().strftime("%M")) * 6
hang = 270 + (int(datetime.datetime.now().strftime("%I")) * 30) + (mang - 270) / 12

pygame.init()
screen = pygame.display.set_mode((512, 512))
done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((255, 255, 255))
    screen.blit(pygame.image.load('clock.jpeg'), (20, 20))
    color = (0,0,0)

    sleep(1)
    sang += 6

    if (sang - 270) % 360 == 0:
        mang += 6
        hang += 0.5
    min = pygame.draw.line(screen, color, (256, 256), (256 + cos((mang / 180) * pi) * 130, 256 + sin((mang / 180) * pi) * 130), 6) #minutes
    hrs = pygame.draw.line(screen, color, (256, 256), (256 + cos((hang / 180) * pi) * 100, 256 + sin((hang / 180) * pi) * 100), 7) #hours
    sec = pygame.draw.line(screen, (255, 0, 0), (256, 256), (256 + cos((sang / 180) * pi) * 150, 256 + sin((sang / 180) * pi) * 150), 5)  # seconds

    pygame.display.flip()
    clock.tick(10)