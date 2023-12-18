import pygame
from pygame import mixer
import piano_list2 as pl2
import time
import mido
from cryptography.fernet import Fernet
from music21 import note, stream, duration

pygame.init()
timer_font = pygame.font.Font('assets/timesnrcyrmt_bold.ttf', 24)
#key_font = pygame.font.Font('assets/timesnrcyrmt_inclined.ttf', 16)
key_font = pygame.font.Font('assets/timesnrcyrmt.ttf', 18)
button_font = pygame.font.Font('assets/timesnrcyrmt.ttf', 12)
bold_button_font = pygame.font.Font('assets/timesnrcyrmt_bold.ttf', 16)

lock_image = pygame.image.load('assets/images/lock.png')
lock_image = pygame.transform.scale(lock_image, (20, 20))

button_label = pl2.button_list
piano_notes_label = pl2.piano_notes

white_notes_label = pl2.white_notes
black_flats_label = pl2.black_flats

white_button_list = pl2.white_button_list
black_button_list = pl2.black_button_list

not_note_buttom = [0, 1, 2, 3, 4, 5, 6, 7, 20, 33, 46, 47]
clock = pygame.time.Clock()

learn_samples = pl2.learn_samples
license_keys = pl2.licence_keys

def get_sounds(white_notes :list, black_flats :list) -> tuple:
    white_sounds = []
    for i in range(len(white_notes)):
        try:
            white_sounds.append(mixer.Sound(f'assets\\notes\\{white_notes[i]}.wav'))
        except IOError:
            print('File error')
        
    black_sounds = []
    for i in range(len(black_flats)):
        try:
            black_sounds.append(mixer.Sound(f'assets\\notes\\{black_flats[i]}.wav'))
        except IOError:
            print('File error')
        
    return white_sounds, black_sounds


def gradientRect( window, left_colour, right_colour, target_rect ):
    """ Draw a horizontal-gradient filled rectangle covering <target_rect> """
    colour_rect = pygame.Surface( ( 2, 2 ) )                                   # tiny! 2x2 bitmap
    pygame.draw.line( colour_rect, left_colour,  ( 0,0 ), ( 1,0 ) )            # left colour line
    pygame.draw.line( colour_rect, right_colour, ( 0,1 ), ( 1,1 ) )            # right colour line
    colour_rect = pygame.transform.smoothscale( colour_rect, ( target_rect.width, target_rect.height ) )  # stretch!
    window.blit( colour_rect, target_rect )                                    # paint it
    
    
def draw_piano(active_whites, active_blacks, screen, HEIGHT, WIDTH, track, sec, mins):
    lenght_key = (WIDTH - 20)/29
    height_key = HEIGHT/4
    
    #pygame.draw.rect(screen, 'black', [10, HEIGHT - (8/5)*height_key, lenght_key * 29 + 4, (9/5)*height_key], 1, 2)
    
    white_rects = []
    for i in range(len(white_notes_label)):
        rect = pygame.draw.rect(screen, 'white', [10 + i * lenght_key, HEIGHT - height_key, lenght_key, height_key], 0, 2)
        white_rects.append(rect)      
        
    i = 0
    len_white = len(active_whites)
    while i < len_white and len_white > 0:
        if active_whites[i][1] == 0:
            if active_whites[i][3] == 1:
                track.append(mido.Message('note_off', note=active_whites[i][2], velocity=100, time=round((sec + time.time() % 1 + mins * 60) * 65)))
            active_whites.pop(i)
            len_white -= 1
        elif active_whites[i][1] > 0:
            j = active_whites[i][0]
            pygame.draw.rect(screen, (204, 204, 255), [10 + j * lenght_key, HEIGHT - height_key, lenght_key, height_key], 0, 2)
            gradientRect(screen, (240, 240, 255), (204, 204, 255), pygame.Rect(10 + j * lenght_key, HEIGHT - (height_key*(7/5) - 1), lenght_key, height_key*(2/5))) 
            active_whites[i][1] -= 1
        if len(active_whites) > 10000:
            active_whites.clear()
        if i < len_white:
            i +=1
            
    for i in range(len(white_notes_label)):
        pygame.draw.rect(screen, 'black', [10 + i * lenght_key, HEIGHT - height_key, lenght_key + 1, height_key], 2, 2)
        key_label = key_font.render(white_notes_label[i], True, 'black')
        center = key_label.get_rect( center = (10 + i * lenght_key + lenght_key / 2 , HEIGHT - height_key*(1/6)))
        screen.blit(key_label, center)
        
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
                    if active_blacks[q][3] == 1:
                        track.append(mido.Message('note_off', note=active_blacks[q][2], velocity=100, time=round((sec + time.time() % 1 + mins * 60) * 65)))
                    active_blacks.pop(q)
                    len_black -= 1
                elif active_blacks[q][1] > 0:
                    pygame.draw.rect(screen, (130, 130, 255), [10 + lenght_key*(1/1.5 + i + skip_count), HEIGHT - height_key, lenght_key/1.4, height_key*2/3], 0, 2)
                    pygame.draw.rect(screen, 'black', [10 + lenght_key*(1/1.5 + i + skip_count), HEIGHT - height_key, lenght_key/1.4, height_key*2/3], 2, 2)
                    gradientRect(screen, (245, 245, 255), (130, 130, 255), pygame.Rect(10 + lenght_key*(1/1.5 + i + skip_count), HEIGHT - (height_key*(7/5) -1), lenght_key/1.4, height_key*(2/5))) 
                    active_blacks[q][1] -= 1
                if len(active_blacks) > 10000:
                    active_blacks.clear()
            if q < len_black:
                    q += 1
            
                           
        key_label = key_font.render(black_flats_label[i], True, 'white')
        center = key_label.get_rect( center = (10 + lenght_key*(1/1.5 + i + skip_count)  + lenght_key/(1.4*2), HEIGHT - height_key*(1/2)))
        screen.blit(key_label, center)
        
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


def draw_keyboard(active_white, active_black, screen, HEIGHT, WIDTH):
    lenght_button = WIDTH/30
    height_button = HEIGHT/13.4
    height_place = 7.7
    
    i = 0      
    len_white = len(active_white)
    
    while i < len_white and len_white > 0:
        if active_white[i][1] == 0:
            active_white.pop(i)
            len_white -= 1
        elif active_white[i][1] > 0:
            q = active_white[i][0]
            if q == 0 or q == 6:
                pygame.draw.rect(screen, '#CCCCFF', [WIDTH/2 + (white_button_list[q][1] - 7)*lenght_button, (height_place - white_button_list[q][0])*height_button, lenght_button*(19/20) * 2, height_button*(4/5)], 0, 2)
            elif q == 13:
                pygame.draw.rect(screen, '#CCCCFF', [WIDTH/2 + (white_button_list[q][1] - 7)*lenght_button, (height_place - white_button_list[q][0])*height_button, lenght_button*(19/20) * 1.5, height_button*(4/5)], 0, 2)
            else: 
                pygame.draw.rect(screen, '#CCCCFF', [WIDTH/2 + (white_button_list[q][1] - 7)*lenght_button, (height_place - white_button_list[q][0])*height_button, lenght_button*(19/20) * 1, height_button*(4/5)], 0, 2)
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
            pygame.draw.rect(screen, '#CCCCFF', [WIDTH/2 + (black_button_list[q][1] - 7)*lenght_button, (height_place - black_button_list[q][0])*height_button, lenght_button*(19/20) * 1, height_button*(4/5)], 0, 2)
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
                pygame.draw.rect(screen, 'black', [WIDTH/2 + (j - 7)*lenght_button, (height_place - i)*height_button, lenght_button*(19/20) * 7.3, height_button*(4/5)], 1, 2)
                key_label = button_font.render(button_label[key_count], True, 'gray')
                center = key_label.get_rect(center = (WIDTH/2 + (j - 7 + (19/40) * 7.3)*lenght_button , (height_place + 0.4 - i)*height_button))
                screen.blit(key_label, center)
                j += 7
                key_count += 1
                
            if (j == 0 or j == 12) and i == 1:
                pygame.draw.rect(screen, 'black', [WIDTH/2 + (j - 7)*lenght_button, (height_place - i)*height_button, lenght_button*(19/20) * 2, height_button*(4/5)], 1, 2)
                key_label = bold_button_font.render(button_label[key_count], True, 'black')
                center = key_label.get_rect(center = (WIDTH/2 + (j - 7 + (19/20))*lenght_button , (height_place + 0.2 - i)*height_button))
                screen.blit(key_label, center)
                
                key_label = button_font.render(piano_notes_label[notes_count], True, 'black')
                center = key_label.get_rect(center = (WIDTH/2 + (j - 7 + (19/20))*lenght_button , (height_place + 0.6 - i)*height_button))
                screen.blit(key_label, center)
                key_count += 1
                notes_count += 1
                j += 2
                
            if (j == 0 or j == 12.5) and i ==2:
                pygame.draw.rect(screen, 'black', [WIDTH/2 + (j - 7)*lenght_button, (height_place - i)*height_button, lenght_button*(19/20) * 1.5, height_button*(4/5)], 1, 2)
                
                if key_count == 32:
                    key_label = bold_button_font.render(button_label[key_count], True, 'black')
                    center = key_label.get_rect(center = (WIDTH/2 + (j - 7 + (19/40) * 1.5)*lenght_button , (height_place + 0.2 - i)*height_button))
                    screen.blit(key_label, center)
                
                    key_label = button_font.render(piano_notes_label[notes_count], True, 'black')
                    center = key_label.get_rect(center = (WIDTH/2 + (j - 7 + (19/40) * 1.5)*lenght_button , (height_place + 0.6 - i)*height_button))
                    screen.blit(key_label, center)
                    notes_count += 1
                else:
                    key_label = button_font.render(button_label[key_count], True, 'gray')
                    center = key_label.get_rect(center = (WIDTH/2 + (j - 7 + (19/40) * 1.5)*lenght_button , (height_place + 0.4 - i)*height_button))
                    screen.blit(key_label, center)
                j += 1.5
                key_count += 1

            if j <= 13:
                pygame.draw.rect(screen, 'black', [WIDTH/2 + (j - 7)*lenght_button, (height_place - i)*height_button, lenght_button*(19/20), height_button*(4/5)], 1, 2)                 
                
                if key_count not in not_note_buttom:
                    key_label = bold_button_font.render(button_label[key_count], True, 'black')
                    center = key_label.get_rect(center = (WIDTH/2 + (j - 6.5)*lenght_button , (height_place + 0.2 - i)*height_button))
                    screen.blit(key_label, center)
                
                    key_label = button_font.render(piano_notes_label[notes_count], True, 'black')
                    center = key_label.get_rect(center = (WIDTH/2 + (j - 6.5)*lenght_button , (height_place + 0.6 - i)*height_button))
                    screen.blit(key_label, center)
                    notes_count += 1
                else:
                    key_label = button_font.render(button_label[key_count], True, 'gray')
                    center = key_label.get_rect(center = (WIDTH/2 + (j - 6.5)*lenght_button , (height_place + 0.4 - i)*height_button))
                    screen.blit(key_label, center)
                j += 1
                key_count += 1

def record_timer(screen, HEIGHT, WIDTH, if_record, curr_sec, sec, mins):
    if if_record == True:
        pygame.draw.rect(screen, 'red', [WIDTH*(9/20) , HEIGHT*(7/40), WIDTH/10, HEIGHT/20], 1, 2) 
        record_time = timer_font.render('{}:{}'.format(mins, sec), True, 'red')
        record_rect = record_time.get_rect(center = (WIDTH*(1/2), HEIGHT*(4/20)))
        if (curr_sec - time.time()//1) != 0: 
            curr_sec = time.time()//1
            sec += 1
        screen.blit(record_time, record_rect)
        if sec > 60:
            sec = 0
            mins += 1
    return curr_sec, sec, mins
      
def view_sample(screen, WIDTH, HEIGHT, view, key_learn):
    if view == True:
        if key_learn == None:
            pygame.draw.rect(screen, 'red', [WIDTH*(8/20) , HEIGHT*(7/40), WIDTH*(2/10), HEIGHT/20], 1, 2) 
            warn_text = bold_button_font.render('Выберите композицию', True, 'red')
            warn_rect = warn_text.get_rect(center = (WIDTH*(1/2), HEIGHT*(4/20)))
            screen.blit(warn_text, warn_rect)
        else:  
            pygame.draw.rect(screen, 'black', [WIDTH*(3/20) , HEIGHT/15 + HEIGHT*(1/40), WIDTH*(7/10), HEIGHT*(3/20)], 1, 2) 
            sample_text = bold_button_font.render(learn_samples[key_learn], True, 'black')
            sample_rect = sample_text.get_rect(center = (WIDTH*(3/20) + WIDTH*(7/20), HEIGHT/15 + HEIGHT*(1/40) + HEIGHT*(3/40)))
            screen.blit(sample_text, sample_rect)
            
def view_lock(screen, WIDTH, HEIGHT, if_lock):
    if if_lock == True:
        screen.blit(lock_image, (WIDTH/150 + WIDTH*(40/50), HEIGHT*(1/120)))
        pygame.draw.rect(screen, 'red', [WIDTH*(8/20) , HEIGHT*(7/80), WIDTH*(2/10), HEIGHT/20], 1, 2) 
        warn_text = timer_font.render('Введите лицензионный ключ', True, 'red')
        warn_rect = warn_text.get_rect(center = (WIDTH*(1/2), HEIGHT*(7/80) + HEIGHT/40))
        screen.blit(warn_text, warn_rect)
        
def input_key(screen, WIDTH, HEIGHT, if_input, input_key):
    if if_input == True:
        pygame.draw.rect(screen, '#CCCCFF', [WIDTH*(8/20) , HEIGHT*(7/40), WIDTH*(2/10), HEIGHT/20], 0, 2)
        pygame.draw.rect(screen, '#9A9AFF', [WIDTH*(8/20) , HEIGHT*(7/40), WIDTH*(2/10), HEIGHT/20], 2, 2)
        input_text = bold_button_font.render(input_key, True, 'black')
        input_rect = input_text.get_rect(center = (WIDTH*(8/20) + WIDTH*(1/10), HEIGHT*(7/40) + HEIGHT/40))
        screen.blit(input_text, input_rect)
        
def check_key(screen, WIDTH, HEIGHT, if_check_key, key):
    if if_check_key == True:
        if key in license_keys:
            pygame.draw.rect(screen, '#CDFFD0', [WIDTH*(8/20) , HEIGHT*(7/40), WIDTH*(2/10), HEIGHT/20], 0, 2)
            pygame.draw.rect(screen, '#6DCA73', [WIDTH*(8/20) , HEIGHT*(7/40), WIDTH*(2/10), HEIGHT/20], 2, 2)
            input_text = bold_button_font.render('Ключ успешно введен', True, 'black')
            input_rect = input_text.get_rect(center = (WIDTH*(8/20) + WIDTH*(1/10), HEIGHT*(7/40) + HEIGHT/40))
            screen.blit(input_text, input_rect)
            return True
        else:
            pygame.draw.rect(screen, '#FFBCBC', [WIDTH*(8/20) , HEIGHT*(7/40), WIDTH*(2/10), HEIGHT/20], 0, 2)
            pygame.draw.rect(screen, '#D06868', [WIDTH*(8/20) , HEIGHT*(7/40), WIDTH*(2/10), HEIGHT/20], 2, 2)
            input_text = bold_button_font.render('Ключ успешно введен', True, 'black')
            input_rect = input_text.get_rect(center = (WIDTH*(8/20) + WIDTH*(1/10), HEIGHT*(7/40) + HEIGHT/40))
            screen.blit(input_text, input_rect)
            return False