import datetime
from time import sleep
import pygame
import os
from math import cos, sin, pi

_image_library = {}
sang = 270 + int(datetime.datetime.now().strftime("%S")) * 6
mang = 270 + int(datetime.datetime.now().strftime("%M")) * 6
hang = 270 + (int(datetime.datetime.now().strftime("%I")) * 30) + (mang - 270) / 12

def get_image(path):
    global _image_library
    image = _image_library.get(path)
    if image == None:
        canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
        image = pygame.image.load(canonicalized_path)
        _image_library[path] = image
    return image


pygame.init()
screen = pygame.display.set_mode((512, 512))
done = False
clock = pygame.time.Clock()
secang = 0

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((255, 255, 255))
    screen.blit(get_image('clock.jpeg'), (20, 20))
    color = (0,0,0)

    sleep(1)
    sang += 6

    if sang % 90 == 0:
        mang += 6
        hang += 0.5
    min = pygame.draw.line(screen, color, (256, 255), (256 + cos((mang / 180) * pi) * 160, 255 + sin((mang / 180) * pi) * 160), 7) #minutes
    hrs = pygame.draw.line(screen, color, (256, 255), (256 + cos((hang / 180) * pi) * 120, 255 + sin((hang / 180) * pi) * 120), 7) #hours
    sec = pygame.draw.line(screen, color, (256, 255), (256 + cos((sang / 180) * pi) * 180, 255 + sin((sang / 180) * pi) * 180), 5)  # seconds

    pygame.display.flip()
    clock.tick(10)