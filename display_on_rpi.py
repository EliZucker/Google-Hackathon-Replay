import pygame, sys, os, time
from pygame.locals import *

def init_display():
    os.putenv('SDL_FBDEV', '/dev/fb1')
    pygame.init()
    pygame.mouse.set_visible(False)
    size = [320, 240]
    screen = pygame.display.set_mode(size)
    screen.fill((0, 0, 0))
    return screen

def draw_file_browsing_interface(screen):
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 200, 320, 240))
    basicfont = pygame.font.SysFont(None, 30)
    text1 = basicfont.render("3", True, (0, 255, 200), (0, 0, 0))
    textrect1 = text1.get_rect()
    textrect1.centerx = 27
    textrect1.centery = 220
    screen.blit(text1, textrect1)

    text2 = basicfont.render("6", True, (0, 255, 200), (0, 0, 0))
    textrect2 = text2.get_rect()
    textrect2.centerx = 114
    textrect2.centery = 220
    screen.blit(text2, textrect2)

    basicfont3 = pygame.font.SysFont(None, 19)
    text3 = basicfont3.render("NEXT", True, (0, 255, 200), (0, 0, 0))
    textrect3 = text3.get_rect()
    textrect3.centerx = 207
    textrect3.centery = 220
    screen.blit(text3, textrect3)

    basicfont4 = pygame.font.SysFont(None, 19)
    text4 = basicfont4.render("EXIT", True, (255, 20, 20), (0, 0, 0))
    textrect4 = text4.get_rect()
    textrect4.centerx = 290
    textrect4.centery = 220
    screen.blit(text4, textrect4)
    pygame.display.update()

def display_text(text, screen, pos=(10,10)):
    color=pygame.Color('white')
    font=pygame.font.SysFont('Arial', 19)
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = screen.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_screen = font.render(word, 0, color)
            word_width, word_height = word_screen.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            screen.blit(word_screen, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.
    pygame.display.update()

def draw_passive_interface(screen):
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 200, 320, 240))
    basicfont = pygame.font.SysFont(None, 20)
    text1 = basicfont.render("Prev", True, (0, 255, 50), (0, 0, 0))
    textrect1 = text1.get_rect()
    textrect1.centerx = 27
    textrect1.centery = 220
    screen.blit(text1, textrect1)

    text2 = basicfont.render("Next", True, (0, 255, 50), (0, 0, 0))
    textrect2 = text2.get_rect()
    textrect2.centerx = 114
    textrect2.centery = 220
    screen.blit(text2, textrect2)

    basicfont3 = pygame.font.SysFont(None, 15)
    text3 = basicfont.render("Listen", True, (0, 255, 255), (0, 0, 0))
    textrect3 = text3.get_rect()
    textrect3.centerx = 207
    textrect3.centery = 220
    screen.blit(text3, textrect3)

    basicfont4 = pygame.font.SysFont(None, 19)
    text4 = basicfont4.render("BACK", True, (255, 20, 20), (0, 0, 0))
    textrect4 = text4.get_rect()
    textrect4.centerx = 290
    textrect4.centery = 220
    screen.blit(text4, textrect4)
    pygame.display.update()

###### EXAMPLE USE:
# text = "This is a really long sentence with a couple of breaks.\nSometimes it will break even if there isn't a break " \
#        "in the sentence, but that's because the text is too long to fit the screen.\nIt can look strange sometimes.\n" \
#        "This function doesn't check if the text is too high to fit on the height of the surface though, so sometimes " \
#        "text will disappear underneath the surface"

# screen = init_display()
# display_text(text, screen)
# draw_file_browsing_interface(screen)
# time.sleep(5)

# def animate_live_transcription_text(text_to_display, screen, pos=(10,10)):
#     color=pygame.Color('white')
#     font=pygame.font.SysFont('Arial', 25)
#     words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
#     space = font.size(' ')[0]  # The width of a space.
#     max_width, max_height = screen.get_size()
#     x, y = pos
#     for i in range(len(words)):
#         word_subset = words[0:i]
#         for line in word_subset:
#             for word in line:
#                 word_screen = font.render(word, 0, color)
#                 word_width, word_height = word_screen.get_size()
#                 if x + word_width >= max_width:
#                     x = pos[0]  # Reset the x.
#                     y += word_height  # Start on new row.
#                 screen.blit(word_screen, (x, y))
#                 x += word_width + space
#             x = pos[0]  # Reset the x.
#             y += word_height  # Start on new row.
#         pygame.display.update()
#         draw_file_browsing_interface(screen)
#         x, y = pos
#         time.sleep(2)