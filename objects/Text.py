import pygame as py

def un_center_pos(pos, size):
    x_pos = int(pos[0] - (size[0] / 2))
    y_pos = int(pos[1] - (size[1] / 2))
    return (x_pos, y_pos)

def render_text(text, color, size, pos, screen):
    # pos = center of text
    font = py.font.Font(None, size)
    font_surface = font.render(text, True, color)
    screen.blit(font_surface, un_center_pos(pos, font.size(text)))

def render_with_bg(text, text_color, size, pos, bg_color, screen):
    # get text surface
    font = py.font.Font(None, size)
    font_surface = font.render(text, True, text_color)
    
    # get background surface
    # gap = (int(font.size(text)[0] * 0.2), int
    gap = tuple(int(dim * 0.2) for dim in font.size(text))
    bg_dims = tuple(g*2 + dim for g, dim in zip(gap, font.size(text)))
    bg_rect = py.Rect(un_center_pos(pos=pos, size=bg_dims), bg_dims)

    # blit surfaces
    py.draw.rect(screen, bg_color, bg_rect)
    screen.blit(font_surface, un_center_pos(pos, font.size(text)))