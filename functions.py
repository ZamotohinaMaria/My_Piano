import pygame
from pygame import mixer

def get_sounds(white_notes :list, black_flats :list) -> tuple:
    white_sounds = []
    for i in range(len(white_notes)):
        white_sounds.append(mixer.Sound(f'assets\\notes\\{white_notes[i]}.wav'))

    black_sounds = []
    for i in range(len(black_flats)):
        black_sounds.append(mixer.Sound(f'assets\\notes\\{black_flats[i]}.wav'))
        
    return white_sounds, black_sounds


def gradientRect( window, left_colour, right_colour, target_rect ):
    """ Draw a horizontal-gradient filled rectangle covering <target_rect> """
    colour_rect = pygame.Surface( ( 2, 2 ) )                                   # tiny! 2x2 bitmap
    pygame.draw.line( colour_rect, left_colour,  ( 0,0 ), ( 1,0 ) )            # left colour line
    pygame.draw.line( colour_rect, right_colour, ( 0,1 ), ( 1,1 ) )            # right colour line
    colour_rect = pygame.transform.smoothscale( colour_rect, ( target_rect.width, target_rect.height ) )  # stretch!
    window.blit( colour_rect, target_rect )                                    # paint it
