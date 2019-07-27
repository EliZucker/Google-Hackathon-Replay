import pygame, sys, os, time
from pygame.locals import *

def init_display():
    os.putenv('SDL_FBDEV', '/dev/fb1')
    pygame.init()
    pygame.mouse.set_visible(False)

def display_text(text_to_display): 
    size = [320, 240]
    screen = pygame.display.set_mode(size)
    basicfont = pygame.font.SysFont(None, 48)
    text = basicfont.render(text_to_display, True, (255, 0, 0), (255, 255, 255))
    textrect = text.get_rect()
    textrect.centerx = screen.get_rect().centerx
    textrect.centery = screen.get_rect().centery
    screen.fill((255, 255, 255))
    screen.blit(text, textrect)
    pygame.display.update()
