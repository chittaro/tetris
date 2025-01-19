import pygame as py
from pygame.locals import *
from objects.Matrix import Matrix
from objects.Tetromino import Tetromino
from components.Text import *
from constants import *
from components.Button import Button
import time, os

# define helper funcs
def draw_lines(screen):
    for i in range(1, MINO_HGT + 1):
        y = i * MINO_SIZE - 1
        py.draw.line(screen, DARK_GREY, (0, y), (WIDTH, y), 2)
    for i in range(1, MINO_WID + 1):
        x = i * MINO_SIZE
        py.draw.line(screen, DARK_GREY, (x, 0), (x, HEIGHT), 2)

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

# Initialize sounds
move_sound = py.mixer.Sound(os.path.join('Sounds', 'move.mp3'))
rotate_sound = py.mixer.Sound(os.path.join('Sounds', 'rotate.mp3'))
clear_sound = py.mixer.Sound(os.path.join('Sounds', 'line_clear.mp3'))
clear_sound.set_volume(0.2)

# Initialize buttons
play_button = Button("Play", BLACK, DARK_GREY, 100, (WIDTH/2, 300), screen)
restart_button = Button("Play Again", YELLOW, DARK_GREY, 80,
                        (WIDTH/2, 400), screen)

# Initialize game vars
score = 0
keypress_time = 0
game_state = "lobby"
passed_time = time.time()

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
             center=(50, 50), bg_color=GREY, screen=screen)

running = True
py.mixer.pause()
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

    mos_pos = py.mouse.get_pos()
    pressed = py.mouse.get_pressed()

    # check game over condition
    if tetromino.game_over:
        game_state = "game over"

    # start screen state
    if game_state == "lobby":
        screen.blit(background, (0, 0))
        render_text("TETRIS", BLACK, 100, (WIDTH/2, 150), screen)
        play_button.draw(mos_pos)
        if play_button.is_pressed(mos_pos, pressed):
            screen.blit(background, (0, 0))
            game_state = "play"

    # game play state
    elif game_state == "play":
        # update drop speed
        if time.time() - passed_time > 20:
            tetromino.inc_speed()
            passed_time = time.time()

        # shift tetromino
        tetromino.update()
        if tetromino.waited >= tetromino.drop_wait:
            tetromino.drop()

        # check tetromino fall state
        if tetromino.is_landed:
            tetromino.lock_tetromino()
            points = matrix.line_clear()
            tetromino.reset()
            if points > 0:
                score += points
                py.mixer.Sound.play(clear_sound)

        # draw display
        draw_lines(screen)
        text_with_bg(text=str(score), text_color=BLACK, size=100, 
                            center=(50, 50), bg_color=GREY, screen=screen)

    # game over state
    elif game_state == "game over":
        text_with_bg(text="GAME OVER", text_color=RED, size=80,
                     center=(WIDTH/2, 300), bg_color=WHITE, screen=screen)
        restart_button.draw(mos_pos)
        if restart_button.is_pressed(mos_pos, pressed):
            game_state = "play"
            # reset game
            score = 0
            screen.blit(background, (0,0))
            matrix.clear_grid()
            tetromino.reset()

    py.display.update()
