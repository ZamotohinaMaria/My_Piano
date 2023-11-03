# ПОРАБОТАТЬ НАД ВТОРОЙ РАСКЛАДКОЙ, ДРУГИМ ВИДОМ И ПРОКРУТКОЙ
# В БУДУЩЕМ - ЗАЩИЩЕННОСТЬ (ФЛЕШКА И КЛЮЧ), ЦВЕТОВАЯ ТЕМА, УЧИТЬСЯ ИГРАТЬ
import pygame
import piano_lists as pl
import piano_list2 as pl2
from pygame import mixer
import os

#this will initialize the pygame library
pygame.init()
pygame.mixer.set_num_channels(50)

#this is the path to fonts that we will use
#other variables for the sound and window 

font = pygame.font.Font('assets/timesnrcyrmt.ttf', 48)
medium_font = pygame.font.Font('assets/timesnrcyrmt_bold.ttf', 28)
small_font = pygame.font.Font('assets/timesnrcyrmt_inclined.ttf', 16)
real_small_font = pygame.font.Font('assets/timesnrcyrmt.ttf', 10)


#enables the creation of a fresh Clock object that may be used to monitor time. 
# Additionally, the clock offers a number of options for regulating the framerate of a game. 
#Every frame should include one call to this function. It will calculate the number of milliseconds since the last call.
timer = pygame.time.Clock()
WIDTH = 52 * 34
HEIGHT = 600
screen = pygame.display.set_mode([WIDTH, HEIGHT])
white_sounds = []
black_sounds = []
active_whites = []
active_blacks = []
left_oct = 2
right_oct = 4
lenght_key = 34
fps = 60
black_type = 'sharp'

piano_notes = pl.piano_notes
white_notes = pl.white_notes
black_flats = pl.black_flats
black_sharps = pl.black_sharps

#for loop is for accessing notes from the assets folder for all the white key on piano
for i in range(len(white_notes)):
    white_sounds.append(mixer.Sound(f'assets\\notes\\{white_notes[i]}.wav'))

#this for loop will access all the music files from the assets folder for black notes
for i in range(len(black_flats)):
    black_sounds.append(mixer.Sound(f'assets\\notes\\{black_flats[i]}.wav'))
#this is to give a title to our pygame window for gui Piano in Python project
pygame.display.set_caption("Python Piano - CopyAssignment")

#this function will draw the piano keys on the window of Piano in Python
def draw_piano(whites, blacks):
    white_rects = []
    for i in range(52):
        #we made use of rect() function in order to draw the key of the piano for white keys
        rect = pygame.draw.rect(screen, 'white', [i * lenght_key, HEIGHT - 300, lenght_key, 300], 0, 2)
        white_rects.append(rect)
        #same goes for black keys on paino
        pygame.draw.rect(screen, 'black', [i * lenght_key, HEIGHT - 300, lenght_key, 300], 2, 2)
        
        #this variable will handle all the labels that the keys will have in our project
        key_label = small_font.render(white_notes[i], True, 'black')
        screen.blit(key_label, (i * lenght_key + 3, HEIGHT - 20))
        
    skip_count = 0
    last_skip = 2
    skip_track = 2
    black_rects = []
    
    for i in range(36):
        #this is to draw the small black rectangles on the larger keys in GUI Piano in Python
        rect = pygame.draw.rect(screen, 'black', [23 + (i * lenght_key) + (skip_count * lenght_key), HEIGHT - 300, 24, 200], 0, 2)
        black_rects.append(rect)
        
        #this variable will handle all the labels that the keys will have in our project
        if black_type == 'sharp':
            key_label = real_small_font.render(black_sharps[i], True, 'white')
        else: 
            key_label = real_small_font.render(black_flats[i], True, 'white')
        screen.blit(key_label, (25 + (i * lenght_key) + (skip_count * lenght_key), HEIGHT - 120))
        
        for q in range(len(blacks)):
            #this conditional will keep thrack of the green marker that we want to show up on each key
            #whenever a user pesses the key of Piano App in Python, a green marker should show up
            if blacks[q][0] == i:
                if blacks[q][1] > 0:
                    pygame.draw.rect(screen, 'green', [23 + (i * lenght_key) + (skip_count * lenght_key), HEIGHT - 300, 24, 200], 2, 2)
                    blacks[q][1] -= 1
                    
        skip_track += 1
        if last_skip == 2 and skip_track == 3:
            last_skip = 3
            skip_track = 0
            skip_count += 1
        elif last_skip == 3 and skip_track == 2:
            last_skip = 2
            skip_track = 0
            skip_count += 1
            
    #this will move the green block from white spaces to another white spaces
    for i in range(len(whites)):
        if whites[i][1] > 0:
            j = whites[i][0]
            pygame.draw.rect(screen, 'green', [j * lenght_key, HEIGHT - 100, lenght_key, 100], 2, 2)
            whites[i][1] -= 1

    return white_rects, black_rects, whites, blacks

#this will draw the upper section of Piano GUI In Python
def draw_title_bar():
    instruction_text = medium_font.render('Up/Down Arrows Change Left Hand', True, 'black')
    screen.blit(instruction_text, (WIDTH - 500, 10))
    instruction_text2 = medium_font.render('Left/Right Arrows Change Right Hand', True, 'black')
    screen.blit(instruction_text2, (WIDTH - 500, 50))
    title_text = font.render('CopyAssignment Paino!', True, 'white')
    screen.blit(title_text, (298, 18))
    title_text = font.render('CopyAssignment Paino!', True, 'black')
    screen.blit(title_text, (300, 20))


run = True
#while loop for all the keys
while run:
    left_dict = pl.get_left_dict(left_oct)
    right_dict = pl.get_right_dict(right_oct)
    black_sharps_dict = pl.get_black_sharps_dict(left_oct, right_oct)
    black_flats_dict = pl.get_black_flats_dict(left_oct, right_oct)
    
    timer.tick(fps)
    screen.fill('white')
    white_keys, black_keys, active_whites, active_blacks = draw_piano(active_whites, active_blacks)
    #draw_hands(right_oct, left_oct, right_hand, left_hand)
    draw_title_bar()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
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
                    
        if event.type == pygame.TEXTINPUT:
            # print(event.text)
            # print(right_dict[event.text])
            if event.text in left_dict:
                if left_dict[event.text] in piano_notes:
                    index = white_notes.index(left_dict[event.text])
                    white_sounds[index].play(0, 1000)
                    active_whites.append([index, 30])
                    
            if event.text in right_dict:
                if right_dict[event.text] in piano_notes:
                    index = white_notes.index(right_dict[event.text])
                    white_sounds[index].play(0, 1000)
                    active_whites.append([index, 30])
            
            if event.text in black_sharps_dict and black_type == 'sharp':
                if black_sharps_dict[event.text] in piano_notes:
                    index = black_sharps.index(black_sharps_dict[event.text])
                    black_sounds[index].play(0, 1000)
                    active_blacks.append([index, 30])
                
            if event.text in black_flats_dict and black_type == 'flat':
                if black_flats_dict[event.text] in piano_notes:
                    index = black_flats.index(black_flats_dict[event.text])
                    black_sounds[index].play(0, 1000)
                    active_blacks.append([index, 30])
                
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if right_oct < 8:
                    right_oct += 1
            if event.key == pygame.K_LEFT:
                if right_oct > 0:
                    right_oct -= 1
            if event.key == pygame.K_UP:
                if left_oct < 8:
                    left_oct += 1
            if event.key == pygame.K_DOWN:
                if left_oct > 0:
                    left_oct -= 1
            if event.key == pygame.K_TAB:
                if black_type == 'sharp':
                    black_type = 'flat'
                else:
                    black_type = 'sharp'


    pygame.display.flip()
#this will quite the  window of the pygame 
pygame.quit()