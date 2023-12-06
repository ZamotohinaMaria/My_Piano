# ПОРАБОТАТЬ НАД ВТОРОЙ РАСКЛАДКОЙ, ДРУГИМ ВИДОМ И ПРОКРУТКОЙ
# В БУДУЩЕМ - ЗАЩИЩЕННОСТЬ (ФЛЕШКА И КЛЮЧ), ЦВЕТОВАЯ ТЕМА, УЧИТЬСЯ ИГРАТЬ
import pygame
import piano_lists as pl
import piano_list2 as pl2
import functions as f

pygame.init()
pygame.mixer.set_num_channels(50)

timer = pygame.time.Clock()
infoObject = pygame.display.Info()
WIDTH = infoObject.current_w
HEIGHT = infoObject.current_h - 60
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Python Piano - CopyAssignment")

active_whites = []
active_blacks = []

active_button_white = []
active_button_black = []

fps = 60

key_list = pl2.key_list

piano_notes_key = pl2.get_notes_dict()
white_notes_label = pl2.white_notes
black_flats_label = pl2.black_flats

white_sounds, black_sounds = f.get_sounds(white_notes_label, black_flats_label)

current_size = screen.get_size()

run = True
if_record = False
sec =0
mins = 0
track = stream.Score()
#while loop for all the keys
while run: 
    
    timer.tick(fps)
    screen.fill('white')
    white_keys, black_keys, active_whites, active_blacks = f.draw_piano(active_whites, active_blacks, screen, HEIGHT, WIDTH)
    f.draw_keyboard(active_button_white, active_button_black, screen, HEIGHT, WIDTH)
    btn_record, btn_stop_record = f.menu(screen, HEIGHT, WIDTH)
    sec, mins = f.record_timer(screen, HEIGHT, WIDTH, if_record, sec, mins)
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
            
            if btn_record.collidepoint(event.pos):
                if_record = True
                sec =0
                mins = 0
                
            if btn_stop_record.collidepoint(event.pos):
                if_record = False
                track.write('midi', fp='my_music.mid')
                
        if event.type == pygame.KEYDOWN:
            if event.key in key_list:
                if piano_notes_key[str(event.key)] in black_flats_label:
                    print(piano_notes_key[str(event.key)])
                    index = black_flats_label.index(piano_notes_key[str(event.key)])
                    black_sounds[index].play(0, 1000)
                    active_blacks.append([index, 30])
                    active_button_black.append([index, 30])
                    if if_record == True:
                        print()
                    
                if piano_notes_key[str(event.key)] in white_notes_label:
                    index = white_notes_label.index(piano_notes_key[str(event.key)])
                    white_sounds[index].play(0, 1000)
                    active_whites.append([index, 30])
                    active_button_white.append([index, 30])
                    if if_record == True:
                        print()
                
            
    pygame.display.flip()
#this will quite the  window of the pygame 
pygame.quit()