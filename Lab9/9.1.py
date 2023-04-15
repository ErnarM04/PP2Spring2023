import pygame
import random
import time, sys

done = False
pygame.init()
clock = pygame.time.Clock()
surface = pygame.display.set_mode((400, 600))
SPEED = 5
scores = 0
font = pygame.font.SysFont("Verdana", 60)
game_over = font.render("Game Over", True, (0, 0, 0))

cx = random.randint(20, 380)
cy = random.randint(20, 400)
font_small = pygame.font.SysFont("Verdana", 20)
class Coin(pygame.sprite.Sprite):
    def __init__(self, cx, cy):
        super().__init__()
        self.cx = cx
        self.cy = cy
        self.image = pygame.image.load("coin.png")
        self.rect = self.image.get_rect()
        self.rect.center = (self.cx, self.cy)

    def move(self):
        None

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, 360), -40)

    def move(self):
        self.rect.move_ip(0, SPEED)
        if (self.rect.top > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, 360), -40)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP] and self.rect.top > -40:
            self.rect.move_ip(0, -5)
        if pressed[pygame.K_DOWN] and self.rect.bottom < 640:
            self.rect.move_ip(0,5)

        if self.rect.left > 0 and pressed[pygame.K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < 400 and pressed[pygame.K_RIGHT]:
                self.rect.move_ip(5, 0)
        pygame.display.update()

    def draw(self, surface):
        surface.blit(self.image, self.rect)

P1 = Player()
E = Enemy()
C = Coin(cx, cy)

# Creating Sprites Groups
coins = pygame.sprite.Group()
coins.add(C)
enemies = pygame.sprite.Group()
enemies.add(E)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(C)
all_sprites.add(E)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    surface.blit(pygame.image.load('car_way.png'), (0, 0))

    #Entities updating
    for entity in all_sprites:
        surface.blit(entity.image, entity.rect)
        entity.move()
        entity.update()

    #Print scores
    score = font_small.render(str(scores), True, (0, 0, 0))
    surface.blit(score, (10, 10))

    if pygame.sprite.spritecollideany(P1, enemies):
        time.sleep(0.5)

        surface.fill((255, 0, 0))
        surface.blit(game_over, (30, 250))

        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    # Collision between Player and coin
    if pygame.sprite.spritecollideany(P1, coins):
        pygame.display.update()
        scores += 1
        cx = random.randint(20, 380)
        cy = random.randint(20, 580)
        while (cx in range(P1.rect.center[0] - 40, P1.rect.center[0] + 41)) or (cy in range(P1.rect.center[1] - 78, P1.rect.center[1] + 78)):
            cx = random.randint(20, 380)
            cy = random.randint(20, 580)
        C.rect.center = (cx, cy)
        if scores % 5 == 0 and scores != 0:
            SPEED += 1

    pygame.display.update()
    pygame.display.flip()
    clock.tick(60)