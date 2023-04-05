import pygame
import time
import random

speed = 15

pygame.init()

# Initialise game window
surface = pygame.display.set_mode((720, 480))

# FPS (frames per second) controller
clock = pygame.time.Clock()

# defining snake default position
snake_position = [100, 50]

# defining first 4 blocks of snake body
snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]
              ]
# fruit position
fruit_position = [random.randrange(1, (720 // 10)) * 10,
                  random.randrange(1, (480 // 10)) * 10]

fruit_spawn = True

# setting default snake direction towards
# right
direction = 'RIGHT'
change_to = direction

# initial score
score = 0
level = 1

# displaying Score function
def show_score():
    # creating font object score_font
    score_font = pygame.font.SysFont('arial', 20)

    # create the display surface object
    # score_surface
    score_surface = score_font.render('Score : ' + str(score), True, (255, 255, 255))

    # create a rectangular object for the text
    # surface object
    score_rect = score_surface.get_rect()

    # displaying text
    surface.blit(score_surface, score_rect)

def show_level():
    # creating font object level_font
    level_font = pygame.font.SysFont('arial', 20)

    # display surface object level_surface
    level_surface = level_font.render('Level: ' + str(level), True, (255, 255, 255))

    # rectangular object for font
    level_rect = level_surface.get_rect()
    level_rect.midtop = (670, 10)

    # display text
    surface.blit(level_surface, level_rect)
# game over function
def game_over():
    # creating font object my_font
    go_font = pygame.font.SysFont('times new roman', 50)

    # creating a text surface on which text
    # will be drawn
    game_over_surface = go_font.render(
        'Your Score is : ' + str(score), True, (255, 0, 0))

    # create a rectangular object for the text
    # surface object
    game_over_rect = game_over_surface.get_rect()

    # setting position of the text
    game_over_rect.midtop = (720 / 2, 480 / 4)

    # blit will draw the text on screen
    surface.blit(game_over_surface, game_over_rect)
    pygame.display.flip()

    # after 2 seconds we will quit the program
    time.sleep(2)

    # deactivating pygame library
    pygame.quit()

    # quit the program
    quit()


# Main Function
while True:

    # handling key events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_to = 'UP'
            if event.key == pygame.K_DOWN:
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_to = 'RIGHT'

    # If two keys pressed simultaneously
    # we don't want snake to move into two
    # directions simultaneously
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Moving the snake
    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

    # Snake body growing mechanism
    # if fruits and snakes collide then scores
    # will be incremented by 10
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 1
        if score % 5 == 0:
            speed += 5
            level += 1
        fruit_spawn = False
    else:
        snake_body.pop()

    if not fruit_spawn:
        fruit_position = [random.randrange(1, (720 // 10)) * 10,
                          random.randrange(1, (480 // 10)) * 10]

    fruit_spawn = True
    surface.fill((0,0,0))

    for pos in snake_body:
        pygame.draw.rect(surface, (0,255,0), pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(surface, (255, 255, 255), pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))

    # Game Over conditions
    if snake_position[0] < 0 or snake_position[0] > 720 - 10:
        game_over()
    if snake_position[1] < 0 or snake_position[1] > 480 - 10:
        game_over()

    # Touching the snake body
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    # displaying score countinuously
    show_score()
    show_level()

    # Refresh game screen
    pygame.display.update()

    # Frame Per Second /Refresh Rate
    clock.tick(speed)