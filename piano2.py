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
button_font = pygame.font.Font('assets/timesnrcyrmt.ttf', 14)
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
active_button_white = []
active_button_black = []

lenght_key = (WIDTH - 20)/29
height_key = HEIGHT/4
lenght_button = WIDTH/20
height_button = HEIGHT/12
fps = 60

key_list = pl2.key_list
button_label = pl2.button_list
piano_notes_label = pl2.piano_notes
piano_notes_key = pl2.get_notes_dict()
white_notes_label = pl2.white_notes
black_flats_label = pl2.black_flats
white_button_list = pl2.white_button_list
black_button_list = pl2.black_button_list
white_sounds, black_sounds = f.get_sounds(white_notes_label, black_flats_label)
not_note_buttom = [0, 1, 2, 3, 4, 5, 6, 7, 20, 33, 46, 47]

current_size = screen.get_size()
virtual_surface = pygame.Surface((WIDTH, HEIGHT))

def draw_piano(active_whites, active_blacks):
    pygame.draw.rect(screen, 'black', [10, HEIGHT - (9/5)*height_key, lenght_key * 29 + 4, (9/5)*height_key], 1, 2)
    
    white_rects = []
    for i in range(len(white_notes_label)):
        rect = pygame.draw.rect(screen, 'white', [10 + i * lenght_key, HEIGHT - height_key, lenght_key, height_key], 2, 2)
        white_rects.append(rect)      
        
    i = 0
    len_white = len(active_whites)
    while i < len_white and len_white > 0:
        if active_whites[i][1] == 0:
            active_whites.pop(i)
            len_white -= 1
        elif active_whites[i][1] > 0:
            j = active_whites[i][0]
            pygame.draw.rect(screen, 'gray', [10 + j * lenght_key, HEIGHT - height_key, lenght_key, height_key], 0, 2)
            f.gradientRect(screen, 'white', (204, 255, 153), pygame.Rect(10 + j * lenght_key, HEIGHT - (height_key*(8/5) - 1), lenght_key, height_key*(3/5))) 
            active_whites[i][1] -= 1
        if len(active_whites) > 10000:
            active_whites.clear()
        if i < len_white:
            i +=1
            
    for i in range(len(white_notes_label)):
        pygame.draw.rect(screen, 'black', [10 + i * lenght_key, HEIGHT - height_key, lenght_key + 1, 300], 2, 2)
        key_label = small_font.render(white_notes_label[i], True, 'black')
        screen.blit(key_label, (10 + i * lenght_key + lenght_key / 4, HEIGHT - height_key*(1/6)))
        
    skip_count = 0
    last_skip = 3
    skip_track = 0
    black_rects = []
    
    for i in range(len(black_flats_label)):
        rect = pygame.draw.rect(screen, 'black', [10 + lenght_key*(1/1.5 + i + skip_count), HEIGHT - height_key, lenght_key/1.4, height_key*2/3], 0, 2)
        black_rects.append(rect)
        
        q = 0
        len_black = len(active_blacks)
        while q < len_black and len_black > 0:
            if active_blacks[q][0] == i:
                if active_blacks[q][1] == 0:
                    active_blacks.pop(q)
                    len_black -= 1
                elif active_blacks[q][1] > 0:
                    pygame.draw.rect(screen, (96, 96, 96), [10 + lenght_key*(1/1.5 + i + skip_count), HEIGHT - height_key, lenght_key/1.4, height_key*2/3], 0, 2)
                    pygame.draw.rect(screen, 'black', [10 + lenght_key*(1/1.5 + i + skip_count), HEIGHT - height_key, lenght_key/1.4, height_key*2/3], 2, 2)
                    f.gradientRect(screen, 'white', (76, 153, 0), pygame.Rect(10 + lenght_key*(1/1.5 + i + skip_count), HEIGHT - (height_key*(8/5) -1), lenght_key/1.4, height_key*(3/5))) 
                    active_blacks[q][1] -= 1
                if len(active_blacks) > 10000:
                    active_blacks.clear()
            if q < len_black:
                    q += 1
            
                    
        key_label = real_small_font.render(black_flats_label[i], True, 'white')
        screen.blit(key_label, (10 + lenght_key*(1/1.5 + i + skip_count + 1/(4.5*1.5)), HEIGHT - height_key*(1/2)))
        
        skip_track += 1
        if last_skip == 2 and skip_track == 3:
            last_skip = 3
            skip_track = 0
            skip_count += 1
        elif last_skip == 3 and skip_track == 2:
            last_skip = 2
            skip_track = 0
            skip_count += 1

    return white_rects, black_rects, active_whites, active_blacks

def draw_keyboard(active_white, active_black):
    i = 0      
    len_white = len(active_white)
    
    while i < len_white and len_white > 0:
        if active_white[i][1] == 0:
            active_white.pop(i)
            len_white -= 1
        elif active_white[i][1] > 0:
            q = active_white[i][0]
            if q == 0 or q == 6:
                pygame.draw.rect(screen, 'gray', [WIDTH/2 + (white_button_list[q][1] - 7)*lenght_button, (5 - white_button_list[q][0])*height_button, lenght_button*(19/20) * 2, height_button*(4/5)], 0, 2)
            elif q == 13:
                pygame.draw.rect(screen, 'gray', [WIDTH/2 + (white_button_list[q][1] - 7)*lenght_button, (5 - white_button_list[q][0])*height_button, lenght_button*(19/20) * 1.5, height_button*(4/5)], 0, 2)
            else: 
                pygame.draw.rect(screen, 'gray', [WIDTH/2 + (white_button_list[q][1] - 7)*lenght_button, (5 - white_button_list[q][0])*height_button, lenght_button*(19/20) * 1, height_button*(4/5)], 0, 2)
            active_white[i][1] -= 1
        elif len(active_white) > 10000:
            active_white.clear()
        if i < len_white:
            i += 1 
    
    i = 0      
    len_black = len(active_black)
    while i < len_black and len_black > 0:
        if active_black[i][1] == 0:
            active_black.pop(i)
            len_black -= 1
        elif active_black[i][1] > 0:
            q = active_black[i][0]
            pygame.draw.rect(screen, 'gray', [WIDTH/2 + (black_button_list[q][1] - 7)*lenght_button, (5 - black_button_list[q][0])*height_button, lenght_button*(19/20) * 1, height_button*(4/5)], 0, 2)
            active_black[i][1] -= 1
        elif len(active_black) > 10000:
            active_black.clear()
        if i < len_black:
            i += 1  
    key_count = 0
    notes_count = 0
    for i in range(5):
        j = 0
        while j <= 13:
            if j == 3 and i == 0:
                pygame.draw.rect(screen, 'black', [WIDTH/2 + (j - 7)*lenght_button, (5 - i)*height_button, lenght_button*(19/20) * 7.3, height_button*(4/5)], 1, 2)
                key_label = button_font.render(button_label[key_count], True, 'black')
                center = key_label.get_rect(center = (WIDTH/2 + (j - 7 + (19/40) * 7.3)*lenght_button , (5.4 - i)*height_button))
                screen.blit(key_label, center)
                j += 7
                key_count += 1
                
            if (j == 0 or j == 12) and i == 1:
                pygame.draw.rect(screen, 'black', [WIDTH/2 + (j - 7)*lenght_button, (5 - i)*height_button, lenght_button*(19/20) * 2, height_button*(4/5)], 1, 2)
                key_label = button_font.render(button_label[key_count], True, 'black')
                center = key_label.get_rect(center = (WIDTH/2 + (j - 7 + (19/20))*lenght_button , (5.2 - i)*height_button))
                screen.blit(key_label, center)
                
                key_label = button_font.render(piano_notes_label[notes_count], True, 'black')
                center = key_label.get_rect(center = (WIDTH/2 + (j - 7 + (19/20))*lenght_button , (5.6 - i)*height_button))
                screen.blit(key_label, center)
                key_count += 1
                notes_count += 1
                j += 2
                
            if (j == 0 or j == 12.5) and i ==2:
                pygame.draw.rect(screen, 'black', [WIDTH/2 + (j - 7)*lenght_button, (5 - i)*height_button, lenght_button*(19/20) * 1.5, height_button*(4/5)], 1, 2)
                
                if key_count == 32:
                    key_label = button_font.render(button_label[key_count], True, 'black')
                    center = key_label.get_rect(center = (WIDTH/2 + (j - 7 + (19/40) * 1.5)*lenght_button , (5.2 - i)*height_button))
                    screen.blit(key_label, center)
                
                    key_label = button_font.render(piano_notes_label[notes_count], True, 'black')
                    center = key_label.get_rect(center = (WIDTH/2 + (j - 7 + (19/40) * 1.5)*lenght_button , (5.6 - i)*height_button))
                    screen.blit(key_label, center)
                    notes_count += 1
                else:
                    key_label = button_font.render(button_label[key_count], True, 'black')
                    center = key_label.get_rect(center = (WIDTH/2 + (j - 7 + (19/40) * 1.5)*lenght_button , (5.4 - i)*height_button))
                    screen.blit(key_label, center)
                j += 1.5
                key_count += 1

            if j <= 13:
                pygame.draw.rect(screen, 'black', [WIDTH/2 + (j - 7)*lenght_button, (5 - i)*height_button, lenght_button*(19/20), height_button*(4/5)], 1, 2)                 
                
                if key_count not in not_note_buttom:
                    key_label = button_font.render(button_label[key_count], True, 'black')
                    center = key_label.get_rect(center = (WIDTH/2 + (j - 6.5)*lenght_button , (5.2 - i)*height_button))
                    screen.blit(key_label, center)
                
                    key_label = button_font.render(piano_notes_label[notes_count], True, 'black')
                    center = key_label.get_rect(center = (WIDTH/2 + (j - 6.5)*lenght_button , (5.6 - i)*height_button))
                    screen.blit(key_label, center)
                    notes_count += 1
                else:
                    key_label = button_font.render(button_label[key_count], True, 'black')
                    center = key_label.get_rect(center = (WIDTH/2 + (j - 6.5)*lenght_button , (5.4 - i)*height_button))
                    screen.blit(key_label, center)
                j += 1
                key_count += 1
    
    

                

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
    draw_keyboard(active_button_white, active_button_black)
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
            height_key = HEIGHT/4
            lenght_button = WIDTH/20
            height_button = HEIGHT/13.4
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            black_key = False
            for i in range(len(black_keys)):
                if black_keys[i].collidepoint(event.pos):
                    black_sounds[i].play(0, 1500)
                    black_key = True
                    active_blacks.append([i, 30])
                    active_button_black.append([i, 30])
                    
                    
            for i in range(len(white_keys)):
                if white_keys[i].collidepoint(event.pos) and not black_key:
                    white_sounds[i].play(0, 1500)
                    active_whites.append([i, 30])
                    active_button_white.append([i, 30])
                
        if event.type == pygame.KEYDOWN:
            if event.key in key_list:
                if piano_notes_key[str(event.key)] in black_flats_label:
                    index = black_flats_label.index(piano_notes_key[str(event.key)])
                    black_sounds[index].play(0, 1000)
                    active_blacks.append([index, 30])
                    active_button_black.append([index, 30])
                    
                if piano_notes_key[str(event.key)] in white_notes_label:
                    index = white_notes_label.index(piano_notes_key[str(event.key)])
                    white_sounds[index].play(0, 1000)
                    active_whites.append([index, 30])
                    active_button_white.append([index, 30])
    pygame.display.flip()
#this will quite the  window of the pygame 
pygame.quit()