import pygame
import pygame_widgets
from pygame_widgets.button import Button
from pygame_widgets.dropdown import Dropdown
import mido
from mido import MidiFile, MidiTrack
import time

import piano_list2 as pl2
import functions as f
import buttons


pygame.init()
pygame.mixer.set_num_channels(50)
pygame.mixer.init()

timer = pygame.time.Clock()
infoObject = pygame.display.Info()
WIDTH = infoObject.current_w
HEIGHT = infoObject.current_h - 60
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Python Piano - CopyAssignment")
current_size = screen.get_size()

fps = 60
key_learn = None

key_list = pl2.key_list
piano_notes_key = pl2.notes_dict
white_notes_label = pl2.white_notes
black_flats_label = pl2.black_flats
midi_notes = pl2.midi_notes

white_sounds, black_sounds = f.get_sounds(white_notes_label, black_flats_label)

active_whites = []
active_blacks = []
active_button_white = []
active_button_black = []

run = True
if_record = False
sec =0
mins = 0
curr_sec = 0

btn_font = pygame.font.Font('assets/timesnrcyrmt.ttf', 16)
lock_image = pygame.image.load('assets/images/lock.png')
lock_image = pygame.transform.scale(lock_image, (20, 20))
btn_record, btn_stop_record, btn_play_music, btn_stop_music, drop_learn_samples = buttons.create_buttons(screen, WIDTH, HEIGHT)

mid = MidiFile()
track = MidiTrack()
while run: 
    timer.tick(fps)
    screen.fill('#F5F5FF')

    white_keys, black_keys, active_whites, active_blacks = f.draw_piano(active_whites, active_blacks, screen, HEIGHT, WIDTH, track, sec, mins)
    f.draw_keyboard(active_button_white, active_button_black, screen, HEIGHT, WIDTH)
    pygame.draw.rect(screen, '#CCCCFF', [0, 0, WIDTH, HEIGHT/15], 0, 2) 
    
    curr_sec, sec, mins = f.record_timer(screen, HEIGHT, WIDTH, if_record, curr_sec, sec, mins)
    
    mouse = pygame.mouse.get_pos()
    
    if (btn_record.getX() <= mouse[0] and (btn_record.getWidth() + btn_record.getX()) >= mouse[0] and 
        btn_record.getY() <= mouse[1] and (btn_record.getHeight() + btn_record.getY()) >= mouse[1]):
        pygame.draw.rect(screen, 'white', [btn_record.getWidth() + btn_record.getX(),
                                             btn_record.getHeight() + btn_record.getY(), 
                                             WIDTH*(3/31), HEIGHT/25], 0, 2)
        key_label = btn_font.render('Начать запись', True, 'black')
        center = key_label.get_rect(center = (btn_record.getWidth() + btn_record.getX() + WIDTH*(3/62), 
                                              btn_record.getHeight() + btn_record.getY() + HEIGHT/50))
        screen.blit(key_label, center) 
        
    if (btn_stop_record.getX() <= mouse[0] and (btn_stop_record.getWidth() + btn_stop_record.getX()) >= mouse[0] and 
        btn_stop_record.getY() <= mouse[1] and (btn_stop_record.getHeight() + btn_stop_record.getY()) >= mouse[1]):
        pygame.draw.rect(screen, 'white', [btn_stop_record.getWidth() + btn_stop_record.getX(),
                                             btn_stop_record.getHeight() + btn_stop_record.getY(), 
                                             WIDTH*(3/31), HEIGHT/25], 0, 2)
        key_label = btn_font.render('Остановить запись', True, 'black')
        center = key_label.get_rect(center = (btn_stop_record.getWidth() + btn_stop_record.getX() + WIDTH*(3/62), 
                                              btn_stop_record.getHeight() + btn_stop_record.getY() + HEIGHT/50))
        screen.blit(key_label, center)
        
    if (btn_play_music.getX() <= mouse[0] and (btn_play_music.getWidth() + btn_play_music.getX()) >= mouse[0] and 
        btn_play_music.getY() <= mouse[1] and (btn_play_music.getHeight() + btn_play_music.getY()) >= mouse[1]):
        pygame.draw.rect(screen, 'white', [btn_play_music.getWidth() + btn_play_music.getX(),
                                             btn_play_music.getHeight() + btn_play_music.getY(), 
                                             WIDTH*(4/31), HEIGHT/25], 0, 2)
        key_label = btn_font.render('Воспроизвести музыку', True, 'black')
        center = key_label.get_rect(center = (btn_play_music.getWidth() + btn_play_music.getX() + WIDTH*(4/62), 
                                              btn_play_music.getHeight() + btn_play_music.getY() + HEIGHT/50))
        screen.blit(key_label, center)
        
    if (btn_stop_music.getX() <= mouse[0] and (btn_stop_music.getWidth() + btn_stop_music.getX()) >= mouse[0] and 
        btn_stop_music.getY() <= mouse[1] and (btn_stop_music.getHeight() + btn_stop_music.getY()) >= mouse[1]):
        pygame.draw.rect(screen, 'white', [btn_stop_music.getWidth() + btn_stop_music.getX(),
                                             btn_stop_music.getHeight() + btn_stop_music.getY(), 
                                             WIDTH*(4/30), HEIGHT/25], 0, 2)
        key_label = btn_font.render('Остановить воспроизведение', True, 'black')
        center = key_label.get_rect(center = (btn_stop_music.getWidth() + btn_stop_music.getX() + WIDTH*(4/60), 
                                              btn_stop_music.getHeight() + btn_stop_music.getY() + HEIGHT/50))
        screen.blit(key_label, center)
    
    events = pygame.event.get()
    for event in events:
        
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
                    active_button_black.append([i, 30])
                    if if_record == True:
                        active_blacks.append([i, 30, midi_notes[black_flats_label[i]], 1])
                        track.append(mido.Message('note_on', note=midi_notes[black_flats_label[i]], velocity=100, time=round((sec + time.time() % 1 + mins * 60 ) * 65)))
                    else:
                        active_blacks.append([i, 30, midi_notes[black_flats_label[i]], 0])
                    
            for i in range(len(white_keys)):
                if white_keys[i].collidepoint(event.pos) and not black_key:
                    white_sounds[i].play(0, 1500)
                    active_button_white.append([i, 30])
                    if if_record == True:
                    
                        active_whites.append([i, 30, midi_notes[white_notes_label[i]], 1])
                        track.append(mido.Message('note_on', note=midi_notes[white_notes_label[i]], velocity=100, time=round((sec + time.time() % 1 + mins * 60) * 65)))
                    else:
                        active_whites.append([i, 30, midi_notes[white_notes_label[i]], 0])

        if btn_record.clicked == True:
            print(btn_record.clicked)
            if_record = True
            curr_sec = time.time()//1
            sec = 0
            mins = 0
            
        if btn_stop_record.clicked == True:
            if_record = False
            mid.tracks.append(track)
            mid.save('output.mid')
            track.clear()
            
        if btn_play_music.clicked == True:
            if if_record == True:
                if_record = False
                mid.tracks.append(track)
                mid.save('output.mid')
            pygame.mixer.music.load("output.mid")
            pygame.mixer.music.play()
        
        if btn_stop_music.clicked == True:
            pygame.mixer.music.stop()


        if drop_learn_samples.getSelected() == 1:
            print('Abba')
        if drop_learn_samples.getSelected() == 2:
            print('Konb')
        if drop_learn_samples.getSelected() == 3:
            print('KISH')

        if event.type == pygame.KEYDOWN:
            if event.key in key_list:
                if piano_notes_key[str(event.key)] in black_flats_label:
                    index = black_flats_label.index(piano_notes_key[str(event.key)])
                    black_sounds[index].play(0, 1000)
                    
                    active_button_black.append([index, 30])
                    if if_record == True:
                        active_blacks.append([index, 30, midi_notes[piano_notes_key[str(event.key)]], 1])
                        track.append(mido.Message('note_on', note=midi_notes[piano_notes_key[str(event.key)]], velocity=100, time=round((sec + time.time() % 1 + mins * 60 ) * 65)))
                    else:
                        active_blacks.append([index, 30, midi_notes[piano_notes_key[str(event.key)]], 0])
                
                if piano_notes_key[str(event.key)] in white_notes_label:
                    index = white_notes_label.index(piano_notes_key[str(event.key)])
                    white_sounds[index].play(0, 1000)
                
                    active_button_white.append([index, 30])
                    if if_record == True:
                        active_whites.append([index, 30, midi_notes[piano_notes_key[str(event.key)]], 1])
                        track.append(mido.Message('note_on', note=midi_notes[piano_notes_key[str(event.key)]], velocity=100, time=round((sec + time.time() % 1 + mins * 60) * 65)))
                    else:
                        active_whites.append([index, 30, midi_notes[piano_notes_key[str(event.key)]], 0])
    
    
    
                
    pygame_widgets.update(events)
    screen.blit(lock_image, (WIDTH*(25/31), HEIGHT*(1/120)))
    pygame.display.flip()
#this will quite the  window of the pygame 
pygame.quit()