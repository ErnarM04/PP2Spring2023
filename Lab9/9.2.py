import pygame, time, random, datetime

speed = 15
pygame.init()
surface = pygame.display.set_mode((720, 480))
clock = pygame.time.Clock()

# defining snake default position
snake_position = [100, 50]

t1 = datetime.datetime.now().second
t2 = 0

# defining first 4 blocks of snake body
snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]
              ]
# fruit position
fruit_position = [random.randrange(1, (720 // 10)) * 10, random.randrange(1, (480 // 10)) * 10]
temp_fruit_pos = [random.randrange(1, (720 // 10)) * 10, random.randrange(1, (480 // 10)) * 10]

fruit_spawn = True
temp_fruit_spawn = False
direction = 'RIGHT'
change_to = direction
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
    level_rect.midtop = (670, 0)

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

    game_over_rect = game_over_surface.get_rect()
    # setting position of the text
    game_over_rect.midtop = (720 / 2, 480 / 4)

    surface.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()

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
        score += random.randint(1, 3)
        if score % 5 == 0:
            speed += 5
            level += 1
        fruit_spawn = False
    else:
        snake_body.pop()

    if not fruit_spawn:
        fruit_position = [random.randrange(1, (720 // 10)) * 10, random.randrange(1, (480 // 10)) * 10]
    fruit_spawn = True

    if snake_position[0] == temp_fruit_pos[0] and snake_position[1] == temp_fruit_pos[1]:
        score += 1
        if score % 5 == 0:
            speed += 5
            level += 1
        temp_fruit_spawn = False
        t1 = datetime.datetime.now().second


    if not temp_fruit_spawn:
        temp_fruit_pos = [random.randrange(1, (720 // 10)) * 10, random.randrange(1, (480 // 10)) * 10]

    t2 = datetime.datetime.now().second

    if t2 - t1 == 60:
        temp_fruit_spawn = True
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

    # displaying score and level countinuously
    show_score()
    show_level()
    pygame.display.update()
    clock.tick(speed)