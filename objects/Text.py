import pygame as py

def render_text(text, rect, color, size, bg):
    font = py.font.Font(None, size)
    text = font.render(text, True, color)
    bg.blit(text, rect)