import pygame, math

pygame.init()
WIDTH, HEIGHT = 720, 480
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
color = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)


pressed = pygame.key.get_pressed()


class Circle():
    def __init__(self, start_pos):
        self.start_pos = start_pos  # (x1, y1)
        self.end_pos = start_pos  # (x2, y2)

    def draw(self):
        start_pos_x = self.start_pos[0]
        start_pos_y = self.start_pos[1]

        end_pos_x = self.end_pos[0]
        end_pos_y = self.end_pos[1]

        pygame.draw.circle(SCREEN, color, (start_pos_x, start_pos_y), math.sqrt((end_pos_x - start_pos_x) ** 2 + (end_pos_y - start_pos_y) ** 2), 5)

    def handle(self, mouse_pos):
        self.end_pos = mouse_pos

class Rectangle():
    def __init__(self, start_pos):
        self.start_pos = start_pos  # (x1, y1)
        self.end_pos = start_pos  # (x2, y2)

    def draw(self):
        start_pos_x = min(self.start_pos[0], self.end_pos[0])
        start_pos_y = min(self.start_pos[1], self.end_pos[1])
        end_pos_x = max(self.start_pos[0], self.end_pos[0])
        end_pos_y = max(self.start_pos[1], self.end_pos[1])

        pygame.draw.rect(SCREEN, color, (start_pos_x, start_pos_y, end_pos_x - start_pos_x, end_pos_y - start_pos_y), 5)

    def handle(self, mouse_pos):
        self.end_pos = mouse_pos

class Eraser():
    def __init__(self, start_pos):
        self.mouse_pos = start_pos

    def handle(self, mouse_pos):
        None

    def draw(self):
        pygame.draw.rect(SCREEN, WHITE, pygame.Rect(self.mouse_pos[0] - 20, self.mouse_pos[1] - 20, 40, 40))

class Colors():
    def __init__(self):
        None

    def draw(self):
        self.red = pygame.draw.rect(SCREEN, (255, 0, 0), pygame.Rect(5, 5, 40, 40))
        self.green = pygame.draw.rect(SCREEN, (0, 255, 0), pygame.Rect(5, 50, 40, 40))
        self.blue = pygame.draw.rect(SCREEN, (0, 0, 255), pygame.Rect(5, 95, 40, 40))
        self.orange = pygame.draw.rect(SCREEN, (255, 102, 0), pygame.Rect(5, 140, 40, 40))
        self.purple = pygame.draw.rect(SCREEN, (153, 0, 255), pygame.Rect(5, 185, 40, 40))
        self.black = pygame.draw.rect(SCREEN, (0, 0, 0), pygame.Rect(5, 230, 40, 40))

clock = pygame.time.Clock()
active_obj = None
colors = Colors()
objects = [colors]
current_shape = Rectangle

while True:
    SCREEN.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                current_shape = Rectangle
            if event.key == pygame.K_2:
                current_shape = Circle
            if event.key == pygame.K_3:
                current_shape = Eraser

        if event.type == pygame.MOUSEBUTTONDOWN:
            if colors.red.collidepoint(event.pos):
                color = pygame.Color(255, 0, 0)
            if colors.green.collidepoint(event.pos):
                color = pygame.Color(0, 255, 0)
            if colors.blue.collidepoint(event.pos):
                color = pygame.Color(0, 0, 255)
            if colors.orange.collidepoint(event.pos):
                color = pygame.Color(255, 102, 0)
            if colors.purple.collidepoint(event.pos):
                color = pygame.Color(153, 0, 255)
            if colors.black.collidepoint(event.pos):
                color = pygame.Color(0, 0, 0)
            else:
                active_obj = current_shape(start_pos=event.pos)

        if event.type == pygame.MOUSEMOTION and active_obj is not None:
            active_obj.handle(pygame.mouse.get_pos())
            active_obj.draw()

        if event.type == pygame.MOUSEBUTTONUP and active_obj is not None:
            objects.append(active_obj)
            active_obj = None

    for obj in objects:
        obj.draw()

    clock.tick(60)
    pygame.display.flip()