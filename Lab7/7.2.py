import pygame

clock = pygame.time.Clock()
_songs = ['Bring Me The Horizon Can You Feel My Heart.mp3', 'C418 Aria Math Minecraft Volume Beta.mp3', 'Minecraft OST Pigstep.mp3', 'Rick Astley Never Gonna Give You Up Official Music Video.mp3', 'Smash Mouth All Star HQ.mp3']

pygame.mixer.init()
pygame.display.set_mode((200,100))
pygame.mixer.music.load("Bring Me The Horizon Can You Feel My Heart.mp3")
pygame.mixer.music.play(0)
clock.tick(10)

def play_next_song():
    global _songs
    _songs = _songs[1:] + [_songs[0]] # move current song to the back of the list
    pygame.mixer.music.load(_songs[0])
    pygame.mixer.music.play(0)

def play_prev_song():
    global _songs
    _songs = [_songs[-1]] + _songs[:-1]
    pygame.mixer.music.load(_songs[0])
    pygame.mixer.music.play(0)

i = 0

def muspause():
    global i
    if i == 1:
        pygame.mixer.music.unpause()
        i = 0
    else:
        pygame.mixer.music.pause()
        i = 1
    clock.tick(10)

while pygame.mixer.music.get_busy():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_LEFT]: play_prev_song()
    if pressed[pygame.K_RIGHT]: play_next_song()
    if pressed[pygame.K_SPACE]: muspause()
    if pressed[pygame.K_DOWN]: pygame.mixer.music.stop()
    pygame.event.poll()
    clock.tick(10)

