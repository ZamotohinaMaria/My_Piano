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
    
# def draw_piano(whites, blacks, screen :):
#     pygame.draw.rect(screen, 'black', [10, HEIGHT - 500, lenght_key * 29 + 4, 504], 2, 2)
    
#     white_rects = []
#     for i in range(len(white_notes)):
#         #we made use of rect() function in order to draw the key of the piano for white keys
#         rect = pygame.draw.rect(screen, 'white', [10 + i * lenght_key, HEIGHT - 300, lenght_key, 300], 2, 2)
#         white_rects.append(rect)      
#         #this variable will handle all the labels that the keys will have in our project
        
#     #this will move the green block from white spaces to another white spaces
#     for i in range(len(whites)):
#         if whites[i][1] > 0:
#             j = whites[i][0]
#             pygame.draw.rect(screen, 'gray', [10 + j * lenght_key, HEIGHT - 300, lenght_key, 300], 0, 2)
#             gradientRect(screen, 'white', (204, 255, 153), pygame.Rect(10 + j * lenght_key, HEIGHT - 496, lenght_key, 196)) 
#             whites[i][1] -= 1
            
#     for i in range(len(white_notes)):
#         pygame.draw.rect(screen, 'black', [10 + i * lenght_key, HEIGHT - 300, lenght_key + 1, 300], 2, 2)
#         key_label = small_font.render(white_notes[i], True, 'black')
#         screen.blit(key_label, (10 + i * lenght_key + lenght_key / 4, HEIGHT - 20))
        
#     skip_count = 0
#     last_skip = 3
#     skip_track = 0
#     black_rects = []
    
#     for i in range(len(black_flats)):
#         #this is to draw the small black rectangles on the larger keys in GUI Piano in Python
#         rect = pygame.draw.rect(screen, 'black', [10 + lenght_key/1.5 + (i * lenght_key) + (skip_count * lenght_key), HEIGHT - 300, lenght_key/1.4, 200], 0, 2)
#         black_rects.append(rect)
        
#         for q in range(len(blacks)):
#             #this conditional will keep thrack of the green marker that we want to show up on each key
#             #whenever a user pesses the key of Piano App in Python, a green marker should show up
#             if blacks[q][0] == i:
#                 if blacks[q][1] > 0:
#                     pygame.draw.rect(screen, (96, 96, 96), [10 + lenght_key/1.5 + (i * lenght_key) + (skip_count * lenght_key), HEIGHT - 300, lenght_key/1.4, 200], 0, 2)
#                     pygame.draw.rect(screen, 'black', [10 + lenght_key/1.5 + (i * lenght_key) + (skip_count * lenght_key), HEIGHT - 300, lenght_key/1.4, 200], 2, 2)
#                     gradientRect(screen, 'white', (76, 153, 0), pygame.Rect(10 + lenght_key/1.5 + (i * lenght_key) + (skip_count * lenght_key), HEIGHT - 496, lenght_key/1.4, 196)) 
#                     blacks[q][1] -= 1
                    
#         key_label = real_small_font.render(black_flats[i], True, 'white')
#         screen.blit(key_label, (10 + lenght_key/1.5 + (i * lenght_key) + (skip_count * lenght_key) + (lenght_key/(4.5*1.5)), HEIGHT - 120))
        
#         skip_track += 1
#         if last_skip == 2 and skip_track == 3:
#             last_skip = 3
#             skip_track = 0
#             skip_count += 1
#         elif last_skip == 3 and skip_track == 2:
#             last_skip = 2
#             skip_track = 0
#             skip_count += 1
            

#     return white_rects, black_rects, whites, blacks