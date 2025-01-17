import pygame as py
from components.Text import *

class Button:
    def __init__(self, text, text_color, bg_color, size, pos, screen):
        self.text = text
        self.text_color = text_color
        self.dark_bg = bg_color
        self.light_bg = tuple(c + 10 for c in bg_color)
        self.screen = screen

        self.font = py.font.Font(None, size)
        self.pos = pos
        self.size = size
        self.font_size = self.font.size(text)
        self.rect = py.Rect(un_center_pos(pos, (self.font_size[0], self.font_size[1])), self.font.size(text))


    def draw(self, mos_pos):
        color = self.dark_bg if self.is_hover(mos_pos) else self.light_bg
        py.draw.rect(self.screen, color, self.rect)
        render_text(self.text, self.text_color, self.size, self.pos, self.screen)

    def is_hover(self, mos_pos):
        return self.rect.collidepoint(mos_pos)
    
    def is_pressed(self, mos_pos, pressed):
        return self.is_hover and pressed[0]