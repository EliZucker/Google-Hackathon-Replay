import pygame, sys, os, time
from pygame.locals import *

def init_display():
    os.putenv('SDL_FBDEV', '/dev/fb1')
    pygame.init()
    pygame.mouse.set_visible(False)
    size = [320, 240]
    screen = pygame.display.set_mode(size)
    return screen

def display_text(text_to_display, screen): 
    basicfont = pygame.font.SysFont(None, 12)
    text = basicfont.render(text_to_display, True, (0, 255, 255), (0, 0, 0))
    textrect = text.get_rect()
    textrect.centerx = 50
    textrect.centery = 50
    screen.fill((0, 0, 0))
    screen.blit(text, textrect)
    pygame.display.update()
    # basicfont = pygame.font.SysFont(None, 48)
    # text = basicfont.render(text_to_display, True, (255, 0, 0), (255, 255, 255))
    # textrect = text.get_rect()
    # textrect.centerx = screen.get_rect().centerx
    # textrect.centery = screen.get_rect().centery
    # screen.fill((255, 255, 255))
    # screen.blit(text, textrect)
    # pygame.display.update()
screen = init_display()
display_text('button', screen)
time.sleep(10)


# def set_live_transcription_text(text_to_display, screen):


# def draw_passive_interface():

# def draw_file_browsing_interface():
    

#def animate_live_transcription_text(text_to_display)
