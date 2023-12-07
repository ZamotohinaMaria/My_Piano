# ПОРАБОТАТЬ НАД ВТОРОЙ РАСКЛАДКОЙ, ДРУГИМ ВИДОМ И ПРОКРУТКОЙ
# В БУДУЩЕМ - ЗАЩИЩЕННОСТЬ (ФЛЕШКА И КЛЮЧ), ЦВЕТОВАЯ ТЕМА, УЧИТЬСЯ ИГРАТЬ
import pygame
import piano_lists as pl
import piano_list2 as pl2
import functions as f
import mido
from mido import MidiFile, MidiTrack
import time
from music21 import note, stream, duration

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
midi_notes = pl2.midi_notes

white_sounds, black_sounds = f.get_sounds(white_notes_label, black_flats_label)

current_size = screen.get_size()

run = True
if_record = False
sec =0
mins = 0
curr_sec = 0

mid = MidiFile()
track = MidiTrack()
while run: 
    
    timer.tick(fps)
    screen.fill('white')
    white_keys, black_keys, active_whites, active_blacks = f.draw_piano(active_whites, active_blacks, screen, HEIGHT, WIDTH, track, sec, mins)
    f.draw_keyboard(active_button_white, active_button_black, screen, HEIGHT, WIDTH)
    btn_record, btn_stop_record = f.menu(screen, HEIGHT, WIDTH)
    curr_sec, sec, mins = f.record_timer(screen, HEIGHT, WIDTH, if_record, curr_sec, sec, mins)
    
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
                curr_sec = time.time()//1
                sec = 0
                mins = 0
                
            if btn_stop_record.collidepoint(event.pos):
                if_record = False
                mid.tracks.append(track)
                mid.save('output.mid')
                track.clear()
                
        if event.type == pygame.KEYDOWN:
            if event.key in key_list:
                if piano_notes_key[str(event.key)] in black_flats_label:
                    index = black_flats_label.index(piano_notes_key[str(event.key)])
                    black_sounds[index].play(0, 1000)
                    active_blacks.append([index, 30, midi_notes[piano_notes_key[str(event.key)]]])
                    
                    active_button_black.append([index, 30])
                    if if_record == True:
                        track.append(mido.Message('note_on', note=midi_notes[piano_notes_key[str(event.key)]], velocity=64, time=round((sec + time.time() % 1 + mins * 60 ) * 100)))

                
                if piano_notes_key[str(event.key)] in white_notes_label:
                    index = white_notes_label.index(piano_notes_key[str(event.key)])
                    white_sounds[index].play(0, 1000)
                    active_whites.append([index, 30, midi_notes[piano_notes_key[str(event.key)]]])
                
                    active_button_white.append([index, 30])
                    if if_record == True:
                        track.append(mido.Message('note_on', note=midi_notes[piano_notes_key[str(event.key)]], velocity=64, time=round((sec + time.time() % 1 + mins * 60) * 100)))


    pygame.display.flip()
#this will quite the  window of the pygame 
pygame.quit()