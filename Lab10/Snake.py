import pygame, time, random, psycopg2

speed = 15
pygame.init()
surface = pygame.display.set_mode((720, 480))
clock = pygame.time.Clock()
snake_position = [100, 50]
snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]
              ]
fruit_position = [random.randrange(1, (720 // 10)) * 10,
                  random.randrange(1, (480 // 10)) * 10]
fruit_spawn = True
direction = 'RIGHT'
change_to = direction
score = 0
level = 1
conn = psycopg2.connect(host='localhost',
                        dbname='Snake',
                        user='postgres',
                        password='20112004erkow',
                        port='6566')
cur = conn.cursor()

def show_score():
    score_font = pygame.font.SysFont('arial', 20)
    score_surface = score_font.render('Score : ' + str(score), True, (255, 255, 255))
    score_rect = score_surface.get_rect()
    surface.blit(score_surface, score_rect)

def show_level():
    level_font = pygame.font.SysFont('arial', 20)
    level_surface = level_font.render('Level: ' + str(level), True, (255, 255, 255))
    level_rect = level_surface.get_rect()
    level_rect.midtop = (30, 20)
    surface.blit(level_surface, level_rect)

def game_over():
    go_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = go_font.render(
        'Your Score is : ' + str(score), True, (255, 0, 0))

    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (720 / 2, 480 / 4)
    surface.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()

def add_data(nick, score):
    cur = conn.cursor()
    cur.execute("INSERT INTO Scores (nickname, score) VALUES (%s, %s)", (nick, score))
    conn.commit()
    cur.close()

def search_nick(nick):
    cur = conn.cursor()
    cur.execute("SELECT * FROM Scores WHERE nickname ILIKE %s", (nick,))
    rows = cur.fetchall()
    cur.close()
    return rows

def delete_score(nick):
    cur = conn.cursor()
    cur.execute("DELETE FROM Scores WHERE nickname ILIKE %s", (nick,))
    conn.commit()
    cur.close()

font = pygame.font.SysFont(None, 100)
nick = ""
input_active = True

while input_active:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and input_active:
            if event.key == pygame.K_RETURN:
                input_active = False
            elif event.key == pygame.K_BACKSPACE:
                nick = nick[:-1]
            else:
                nick += event.unicode

    surface.fill(0)
    text_surf = font.render(nick, True, (255, 0, 0))
    surface.blit(text_surf, text_surf.get_rect(center=surface.get_rect().center))
    pygame.display.flip()

input_active = True
row = search_nick(nick)
if row:
    score = row[0][1]
    font = pygame.font.SysFont(None, 40)
    while input_active:
        pressed = pygame.key.get_pressed()
        score_surf = font.render(f"Welcome back, {nick}! Your current score is {score}.", True, (255, 0, 0))
        text_surf = font.render("Do you want to renew your scores?(Y/N)", True, (255, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and input_active:
                if event.key == pygame.K_y:
                    score = 0
                    delete_score(nick)
                    input_active = False
                if event.key == pygame.K_n:
                    quit()
        surface.fill(0)
        surface.blit(score_surf, score_surf.get_rect(center=(360, 200)))
        surface.blit(text_surf, text_surf.get_rect(center=surface.get_rect().center))
        pygame.display.flip()

while True:
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
            if event.key == pygame.K_ESCAPE:
                add_data(nick, score)
                quit()

    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    if direction == 'UP':
        snake_position[1] -= 10
    if direction == 'DOWN':
        snake_position[1] += 10
    if direction == 'LEFT':
        snake_position[0] -= 10
    if direction == 'RIGHT':
        snake_position[0] += 10

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

    if snake_position[0] < 0 or snake_position[0] > 720 - 10:
        add_data(nick, score)
        game_over()
    if snake_position[1] < 0 or snake_position[1] > 480 - 10:
        add_data(nick, score)
        game_over()

    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            add_data(nick, score)
            game_over()

    show_score()
    show_level()
    pygame.display.update()
    clock.tick(speed)