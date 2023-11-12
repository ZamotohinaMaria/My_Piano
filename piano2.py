# ПОРАБОТАТЬ НАД ВТОРОЙ РАСКЛАДКОЙ, ДРУГИМ ВИДОМ И ПРОКРУТКОЙ
# В БУДУЩЕМ - ЗАЩИЩЕННОСТЬ (ФЛЕШКА И КЛЮЧ), ЦВЕТОВАЯ ТЕМА, УЧИТЬСЯ ИГРАТЬ
import pygame
import piano_lists as pl
import piano_list2 as pl2
import functions as f
from pygame import mixer
import os

pygame.init()
pygame.mixer.set_num_channels(50)

font = pygame.font.Font('assets/timesnrcyrmt.ttf', 48)
medium_font = pygame.font.Font('assets/timesnrcyrmt_bold.ttf', 28)
small_font = pygame.font.Font('assets/timesnrcyrmt_inclined.ttf', 16)
real_small_font = pygame.font.Font('assets/timesnrcyrmt.ttf', 10)


timer = pygame.time.Clock()
WIDTH = 1200
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Python Piano - CopyAssignment")

white_sounds = []
black_sounds = []
active_whites = []
active_blacks = []

lenght_key = (WIDTH - 20)/29
fps = 60

key_list = pl2.key_list
piano_notes2 = pl2.get_notes_dict()
white_notes = pl2.white_notes
black_flats = pl2.black_flats
white_sounds, black_sounds = f.get_sounds(white_notes, black_flats)

current_size = screen.get_size()
virtual_surface = pygame.Surface((WIDTH, HEIGHT))

#this function will draw the piano keys on the window of Piano in Python
def draw_piano(whites, blacks):
    print(type(screen))
    pygame.draw.rect(screen, 'black', [10, HEIGHT - 500, lenght_key * 29 + 4, 504], 2, 2)
    
    white_rects = []
    for i in range(len(white_notes)):
        #we made use of rect() function in order to draw the key of the piano for white keys
        rect = pygame.draw.rect(screen, 'white', [10 + i * lenght_key, HEIGHT - 300, lenght_key, 300], 2, 2)
        white_rects.append(rect)      
        #this variable will handle all the labels that the keys will have in our project
        
    #this will move the green block from white spaces to another white spaces
    for i in range(len(whites)):
        if whites[i][1] > 0:
            j = whites[i][0]
            pygame.draw.rect(screen, 'gray', [10 + j * lenght_key, HEIGHT - 300, lenght_key, 300], 0, 2)
            f.gradientRect(screen, 'white', (204, 255, 153), pygame.Rect(10 + j * lenght_key, HEIGHT - 496, lenght_key, 196)) 
            whites[i][1] -= 1
            
    for i in range(len(white_notes)):
        pygame.draw.rect(screen, 'black', [10 + i * lenght_key, HEIGHT - 300, lenght_key + 1, 300], 2, 2)
        key_label = small_font.render(white_notes[i], True, 'black')
        screen.blit(key_label, (10 + i * lenght_key + lenght_key / 4, HEIGHT - 20))
        
    skip_count = 0
    last_skip = 3
    skip_track = 0
    black_rects = []
    
    for i in range(len(black_flats)):
        #this is to draw the small black rectangles on the larger keys in GUI Piano in Python
        rect = pygame.draw.rect(screen, 'black', [10 + lenght_key/1.5 + (i * lenght_key) + (skip_count * lenght_key), HEIGHT - 300, lenght_key/1.4, 200], 0, 2)
        black_rects.append(rect)
        
        for q in range(len(blacks)):
            #this conditional will keep thrack of the green marker that we want to show up on each key
            #whenever a user pesses the key of Piano App in Python, a green marker should show up
            if blacks[q][0] == i:
                if blacks[q][1] > 0:
                    pygame.draw.rect(screen, (96, 96, 96), [10 + lenght_key/1.5 + (i * lenght_key) + (skip_count * lenght_key), HEIGHT - 300, lenght_key/1.4, 200], 0, 2)
                    pygame.draw.rect(screen, 'black', [10 + lenght_key/1.5 + (i * lenght_key) + (skip_count * lenght_key), HEIGHT - 300, lenght_key/1.4, 200], 2, 2)
                    f.gradientRect(screen, 'white', (76, 153, 0), pygame.Rect(10 + lenght_key/1.5 + (i * lenght_key) + (skip_count * lenght_key), HEIGHT - 496, lenght_key/1.4, 196)) 
                    blacks[q][1] -= 1
                    
        key_label = real_small_font.render(black_flats[i], True, 'white')
        screen.blit(key_label, (10 + lenght_key/1.5 + (i * lenght_key) + (skip_count * lenght_key) + (lenght_key/(4.5*1.5)), HEIGHT - 120))
        
        skip_track += 1
        if last_skip == 2 and skip_track == 3:
            last_skip = 3
            skip_track = 0
            skip_count += 1
        elif last_skip == 3 and skip_track == 2:
            last_skip = 2
            skip_track = 0
            skip_count += 1
            
    

    return white_rects, black_rects, whites, blacks

#this will draw the upper section of Piano GUI In Python
# def draw_title_bar():
#     instruction_text = medium_font.render('Up/Down Arrows Change Left Hand', True, 'black')
#     screen.blit(instruction_text, (WIDTH - 500, 10))
#     instruction_text2 = medium_font.render('Left/Right Arrows Change Right Hand', True, 'black')
#     screen.blit(instruction_text2, (WIDTH - 500, 50))
#     title_text = font.render('CopyAssignment Paino!', True, 'white')
#     screen.blit(title_text, (298, 18))
#     title_text = font.render('CopyAssignment Paino!', True, 'black')
#     screen.blit(title_text, (300, 20))



run = True
#while loop for all the keys
while run: 
    timer.tick(fps)
    screen.fill('white')
    white_keys, black_keys, active_whites, active_blacks = draw_piano(active_whites, active_blacks)
    #draw_hands(right_oct, left_oct, right_hand, left_hand)
    #draw_title_bar()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
        if event.type == pygame.VIDEORESIZE:
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            WIDTH = event.w
            HEIGHT = event.h
            lenght_key = (WIDTH - 20)/29
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            black_key = False
            for i in range(len(black_keys)):
                if black_keys[i].collidepoint(event.pos):
                    black_sounds[i].play(0, 1500)
                    black_key = True
                    active_blacks.append([i, 30])
                    
            for i in range(len(white_keys)):
                if white_keys[i].collidepoint(event.pos) and not black_key:
                    white_sounds[i].play(0, 1500)
                    active_whites.append([i, 30])
                
        if event.type == pygame.KEYDOWN:
            if event.key in key_list:
                if piano_notes2[str(event.key)] in black_flats:
                    index = black_flats.index(piano_notes2[str(event.key)])
                    black_sounds[index].play(0, 1000)
                    active_blacks.append([index, 30])
                if piano_notes2[str(event.key)] in white_notes:
                    index = white_notes.index(piano_notes2[str(event.key)])
                    white_sounds[index].play(0, 1000)
                    active_whites.append([index, 30])


    pygame.display.flip()
#this will quite the  window of the pygame 
pygame.quit()