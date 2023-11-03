import pygame
piano_notes = ['A1', 'A#1', 'B1', 'C1', 'C#1', 'D1', 'D#1', 'E1', 'F1', 'F#1', 'G1', 'G#1',
               'A2', 'A#2', 'B2', 'C2', 'C#2', 'D2', 'D#2', 'E2', 'F2', 'F#2', 'G2', 'G#2',
               'A3', 'A#3', 'B3', 'C3', 'C#3', 'D3', 'D#3', 'E3', 'F3', 'F#3', 'G3', 'G#3',
               'A4', 'A#4', 'B4', 'C4', 'C#4', 'D4', 'D#4', 'E4', 'F4', 'F#4', 'G4', 'G#4', 
                                  'C5',
               
               'Bb1', 'Db1', 'Eb1', 'Gb1', 'Ab1',
               'Bb2', 'Db2', 'Eb2', 'Gb2', 'Ab2',
               'Bb3', 'Db3', 'Eb3', 'Gb3', 'Ab3',
               'Bb4', 'Db4', 'Eb4', 'Gb4', 'Ab4']

white_notes = ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1',
               'A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2',
               'A3', 'B3', 'C3', 'D3', 'E3', 'F3', 'G3',
               'A4', 'B4', 'C4', 'D4', 'E4', 'F4', 'G4',
               'C5']

black_flats = ['Bb1', 'Db1', 'Eb1', 'Gb1', 'Ab1',
               'Bb2', 'Db2', 'Eb2', 'Gb2', 'Ab2',
               'Bb3', 'Db3', 'Eb3', 'Gb3', 'Ab3',
               'Bb4', 'Db4', 'Eb4', 'Gb4', 'Ab4']

black_sharps = ['A#1', 'C#1', 'D#1', 'F#1', 'G#1',
                'A#2', 'C#2', 'D#2', 'F#2', 'G#2',
                'A#3', 'C#3', 'D#3', 'F#3', 'G#3',
                'A#4', 'C#4', 'D#4', 'F#4', 'G#4']


def get_notes_dict() -> dict:
    notes_dict = {
                 f'{pygame.K_PERIOD}': 'A1', f'{pygame.K_SEMICOLON}': 'A2', f'{pygame.K_p}': 'A3', f'{pygame.K_0}': 'A4',
                 f'{pygame.K_SLASH}': 'A#1', f'{pygame.K_QUOTE}': 'A#2', f'{pygame.K_LEFTBRACKET}': 'A#3', f'{pygame.K_MINUS}': 'A#4',
                 f'{pygame.K_COMMA}': 'Ab1', f'{pygame.K_l}': 'Ab2', f'{pygame.K_o}': 'Ab3', f'{pygame.K_0}': 'Ab4',

                 f'{pygame.K_RSHIFT}': 'B1', '13': 'B2', f'{pygame.K_RIGHTBRACKET }': 'B3', f'{pygame.K_EQUALS}': 'B4',
                 f'{pygame.K_SLASH}': 'Bb1', f'{pygame.K_QUOTE}': 'Bb2', f'{pygame.K_LEFTBRACKET}': 'Bb3', f'{pygame.K_MINUS}': 'Bb4',
                 
                 f'{pygame.K_BACKSLASH}': 'C1', f'{pygame.K_a}': 'C2', f'{pygame.K_q}': 'C3', f'{pygame.K_1}': 'C4', f'{pygame.K_BACKSPACE}': 'C5',
                 f'{pygame.K_z}': 'C#1', f'{pygame.K_s}': 'C#2', f'{pygame.K_w}': 'C#3', f'{pygame.K_2}': 'C#4',
                 
                 f'{pygame.K_x}': 'D1', f'{pygame.K_d}': 'D2', f'{pygame.K_e}': 'D3', f'{pygame.K_3}': 'D4',
                 f'{pygame.K_c}': 'D#1', f'{pygame.K_f}': 'D#2', f'{pygame.K_r}': 'D#3', f'{pygame.K_4}': 'D#4',
                 f'{pygame.K_z}': 'Db1', f'{pygame.K_s}': 'Db2', f'{pygame.K_w}': 'Db3', f'{pygame.K_2}': 'Db4',
                 
                 f'{pygame.K_v}': 'E1', f'{pygame.K_g}': 'E2', f'{pygame.K_t}': 'E3', f'{pygame.K_5}': 'E4',
                 f'{pygame.K_c}': 'Eb1', f'{pygame.K_f}': 'Eb2', f'{pygame.K_r}': 'Eb3', f'{pygame.K_4}': 'Eb4',
                 
                 f'{pygame.K_b}': 'F1', f'{pygame.K_h}': 'F2', f'{pygame.K_y}': 'F3', f'{pygame.K_6}': 'F4',
                 f'{pygame.K_n}': 'F#1', f'{pygame.K_j}': 'F#2', f'{pygame.K_u}': 'F#3', f'{pygame.K_7}': 'F#4',
                 
                 f'{pygame.K_m}': 'G1', f'{pygame.K_k}': 'G2', f'{pygame.K_i}': 'G3', f'{pygame.K_8}': 'G4',
                 f'{pygame.K_COMMA}': 'G#1', f'{pygame.K_l}': 'G#2', f'{pygame.K_o}': 'G#3', f'{pygame.K_9}': 'G#4',
                 f'{pygame.K_n}': 'Gb1', f'{pygame.K_j}': 'Gb2', f'{pygame.K_u}': 'Gb3', f'{pygame.K_7}': 'Gb4'}
    
    return notes_dict
    
