import pygame as py
from pygame.locals import *
from objects.Matrix import Matrix
from objects.Tetromino import Tetromino
from text_funcs import *
from constants import *
from helpers import *
import time, os

# Initialize game, clock, audio
py.init()
py.font.init()
py.mixer.init()
screen = py.display.set_mode((WIDTH, HEIGHT))
py.display.set_caption("Tetris")
clock = py.time.Clock()
py.mixer.music.set_volume(0.2)
music = py.mixer.music.load(os.path.join('Sounds', 'tetris_theme.mp3'))
py.mixer.music.play(-1)

# Initialize vars
move_sound = py.mixer.Sound(os.path.join('Sounds', 'move.mp3'))
rotate_sound = py.mixer.Sound(os.path.join('Sounds', 'rotate.mp3'))
clear_sound = py.mixer.Sound(os.path.join('Sounds', 'line_clear.mp3'))
clear_sound.set_volume(0.2)
score = 0
keypress_time = 0

# Initialize & blit background
background = py.Surface(screen.get_size()).convert()
background.fill(GREY)
screen.blit(background, (0, 0))
py.display.flip()

# Initialize game objects
matrix = Matrix()
tetromino = Tetromino(screen, matrix.grid, background)

# Draw scoreboard
text_with_bg(text=str(score), text_color=BLACK, size=80, 
             pos=(50, 50), bg_color=GREY, screen=screen)

running = True
while running:
    clock.tick(100)

    for event in py.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            press_time = 0
            if event.key == K_UP:
                py.mixer.Sound.play(rotate_sound)
                tetromino.rotate()
            elif event.key == K_LEFT:
                py.mixer.Sound.play(move_sound)
                tetromino.shift(-1)
            elif event.key == K_RIGHT:
                py.mixer.Sound.play(move_sound)
                tetromino.shift(1)
            elif event.key == K_DOWN:
                tetromino.toggle_speedy(True)
        elif event.type == KEYUP:
            if event.key == K_DOWN:
                tetromino.toggle_speedy(False)

    # check game over condition
    if tetromino.game_over:
        text_with_bg(text="GAME OVER", text_color=RED, size=80,
                     pos=(WIDTH/2, HEIGHT/2), bg_color=WHITE, screen=screen)

    else:
        # shift tetromino
        tetromino.update()
        if tetromino.waited >= tetromino.drop_wait:
            tetromino.drop()

        # check tetromino fall state
        if tetromino.is_landed:
            tetromino.lock_tetromino()
            points = matrix.line_clear()
            if points > 0:
                score += points
                py.mixer.Sound.play(clear_sound)

        # draw display
        draw_lines(screen)
        text_with_bg(text=str(score), text_color=BLACK, size=100, 
                            pos=(50, 50), bg_color=GREY, screen=screen)
    py.display.update()
