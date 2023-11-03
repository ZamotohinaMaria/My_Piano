import pygame
piano_notes = ['A2', 'A#2', 'B2', 'C2', 'C#2', 'D2', 'D#2', 'E2', 'F2', 'F#2', 'G2', 'G#2',
               'A3', 'A#3', 'B3', 'C3', 'C#3', 'D3', 'D#3', 'E3', 'F3', 'F#3', 'G3', 'G#3',
               'A4', 'A#4', 'B4', 'C4', 'C#4', 'D4', 'D#4', 'E4', 'F4', 'F#4', 'G4', 'G#4',
               'A5', 'A#5', 'B5', 'C5', 'C#5', 'D5', 'D#5', 'E5', 'F5', 'F#5', 'G5', 'G#5', 
                                  'C6',
               
               'Db2', 'Eb2', 'Gb2', 'Ab2', 'Bb2',
               'Db3', 'Eb3', 'Gb3', 'Ab3', 'Bb3',
               'Db4', 'Eb4', 'Gb4', 'Ab4', 'Bb4',
               'Db5', 'Eb5', 'Gb5', 'Ab5', 'Bb5']

white_notes = ['C2', 'D2', 'E2', 'F2', 'G2', 'A2', 'B2',
               'C3', 'D3', 'E3', 'F3', 'G3', 'A3', 'B3',
               'C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4',
               'C5', 'D5', 'E5', 'F5', 'G5', 'A5', 'B5',
               'C6']

black_flats = ['Db2', 'Eb2', 'Gb2', 'Ab2', 'Bb2',
               'Db3', 'Eb3', 'Gb3', 'Ab3', 'Bb3',
               'Db4', 'Eb4', 'Gb4', 'Ab4', 'Bb4',
               'Db5', 'Eb5', 'Gb5', 'Ab5', 'Bb5']

black_sharps = ['C#2', 'D#2', 'F#2', 'G#2', 'A#2',
                'C#3', 'D#3', 'F#3', 'G#3', 'A#3',
                'C#4', 'D#4', 'F#4', 'G#4', 'A#4',
                'C#5', 'D#5', 'F#5', 'G#5', 'A#5']


def get_notes_dict() -> dict:
    notes_dict = {
                 f'{pygame.K_PERIOD}': 'A2', f'{pygame.K_SEMICOLON}': 'A3', f'{pygame.K_p}': 'A4', f'{pygame.K_0}': 'A5',
                 f'{pygame.K_SLASH}': 'A#2', f'{pygame.K_QUOTE}': 'A#3', f'{pygame.K_LEFTBRACKET}': 'A#4', f'{pygame.K_MINUS}': 'A#5',
                 f'{pygame.K_COMMA}': 'Ab2', f'{pygame.K_l}': 'Ab3', f'{pygame.K_o}': 'Ab4', f'{pygame.K_0}': 'Ab5',

                 f'{pygame.K_RSHIFT}': 'B2', '13': 'B3', f'{pygame.K_RIGHTBRACKET }': 'B4', f'{pygame.K_EQUALS}': 'B5',
                 f'{pygame.K_SLASH}': 'Bb2', f'{pygame.K_QUOTE}': 'Bb3', f'{pygame.K_LEFTBRACKET}': 'Bb4', f'{pygame.K_MINUS}': 'Bb5',
                 
                 f'{pygame.K_BACKSLASH}': 'C2', f'{pygame.K_a}': 'C3', f'{pygame.K_q}': 'C4', f'{pygame.K_1}': 'C5', f'{pygame.K_BACKSPACE}': 'C6',
                 f'{pygame.K_z}': 'C#2', f'{pygame.K_s}': 'C#3', f'{pygame.K_w}': 'C#4', f'{pygame.K_2}': 'C#5',
                 
                 f'{pygame.K_x}': 'D2', f'{pygame.K_d}': 'D3', f'{pygame.K_e}': 'D4', f'{pygame.K_3}': 'D5',
                 f'{pygame.K_c}': 'D#2', f'{pygame.K_f}': 'D#3', f'{pygame.K_r}': 'D#4', f'{pygame.K_4}': 'D#5',
                 f'{pygame.K_z}': 'Db2', f'{pygame.K_s}': 'Db3', f'{pygame.K_w}': 'Db4', f'{pygame.K_2}': 'Db5',
                 
                 f'{pygame.K_v}': 'E2', f'{pygame.K_g}': 'E3', f'{pygame.K_t}': 'E4', f'{pygame.K_5}': 'E5',
                 f'{pygame.K_c}': 'Eb2', f'{pygame.K_f}': 'Eb3', f'{pygame.K_r}': 'Eb4', f'{pygame.K_4}': 'Eb5',
                 
                 f'{pygame.K_b}': 'F2', f'{pygame.K_h}': 'F3', f'{pygame.K_y}': 'F4', f'{pygame.K_6}': 'F5',
                 f'{pygame.K_n}': 'F#2', f'{pygame.K_j}': 'F#3', f'{pygame.K_u}': 'F#4', f'{pygame.K_7}': 'F#5',
                 
                 f'{pygame.K_m}': 'G2', f'{pygame.K_k}': 'G3', f'{pygame.K_i}': 'G4', f'{pygame.K_8}': 'G5',
                 f'{pygame.K_COMMA}': 'G#2', f'{pygame.K_l}': 'G#3', f'{pygame.K_o}': 'G#4', f'{pygame.K_9}': 'G#5',
                 f'{pygame.K_n}': 'Gb2', f'{pygame.K_j}': 'Gb3', f'{pygame.K_u}': 'Gb4', f'{pygame.K_7}': 'Gb5'}
    
    return notes_dict
    
