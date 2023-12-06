import pygame
# piano_notes = ['A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2',
#                'A3', 'B3', 'C3', 'D3', 'E3', 'F3', 'G3',
#                'A4', 'B4', 'C4', 'D4', 'E4', 'F4', 'G4',
#                'A5', 'B5', 'C5', 'D5', 'E5', 'F5', 'G5', 
#                            'C6',
               
#                'Db2', 'Eb2', 'Gb2', 'Ab2', 'Bb2',
#                'Db3', 'Eb3', 'Gb3', 'Ab3', 'Bb3',
#                'Db4', 'Eb4', 'Gb4', 'Ab4', 'Bb4',
#                'Db5', 'Eb5', 'Gb5', 'Ab5', 'Bb5']

piano_notes = ['C2', 'D-2', 'D2', 'E-2', 'E2', 'F2', 'G-2', 'G2', 'A-2', 'A2', 'B-2', 'B2',
               'C3', 'D-3', 'D3', 'E-3', 'E3', 'F3', 'G-3', 'G3', 'A-3', 'A3', 'B-3', 'B3',
               'C4', 'D-4', 'D4', 'E-4', 'E4', 'F4', 'G-4', 'G4', 'A-4', 'A4', 'B-4', 'B4',
               'C5', 'D-5', 'D5', 'E-5', 'E5', 'F5', 'G-5', 'G5', 'A-5', 'A5', 'B-5', 'B5', 'C6']

white_notes = ['C2', 'D2', 'E2', 'F2', 'G2', 'A2', 'B2',
               'C3', 'D3', 'E3', 'F3', 'G3', 'A3', 'B3',
               'C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4',
               'C5', 'D5', 'E5', 'F5', 'G5', 'A5', 'B5',
               'C6']

black_flats = ['D-2', 'E-2', 'G-2', 'A-2', 'B-2',
               'D-3', 'E-3', 'G-3', 'A-3', 'B-3',
               'D-4', 'E-4', 'G-4', 'A-4', 'B-4',
               'D-5', 'E-5', 'G-5', 'A-5', 'B-5']

key_list = [pygame.K_PERIOD, pygame.K_SEMICOLON, pygame.K_p, pygame.K_0,
            pygame.K_COMMA, pygame.K_l, pygame.K_o, pygame.K_9,
            pygame.K_RSHIFT, pygame.K_LSHIFT, pygame.K_RIGHTBRACKET, pygame.K_EQUALS,
            pygame.K_SLASH, pygame.K_QUOTE, pygame.K_LEFTBRACKET, pygame.K_MINUS,
            pygame.K_RETURN, pygame.K_a, pygame.K_q, pygame.K_1, pygame.K_BACKSPACE, 
            pygame.K_x, pygame.K_d, pygame.K_e, pygame.K_3,
            pygame.K_z, pygame.K_s, pygame.K_w, pygame.K_2,
            pygame.K_v, pygame.K_g, pygame.K_t, pygame.K_5,
            pygame.K_c, pygame.K_f, pygame.K_r, pygame.K_4,
            pygame.K_b, pygame.K_h, pygame.K_y, pygame.K_6,
            pygame.K_m, pygame.K_k, pygame.K_i, pygame.K_8,
            pygame.K_n, pygame.K_j, pygame.K_u, pygame.K_7
]

white_button_list = {0: [1, 0], 1: [1, 3], 2: [1, 5], 3: [1, 6], 4: [1, 8], 5: [1, 10], 6: [1, 12],
                    7: [2, 1.5], 8: [2, 3.5], 9: [2, 5.5], 10: [2, 6.5], 11: [2, 8.5], 12: [2, 10.5], 13: [2, 12.5],
                    14: [3, 1], 15: [3, 3], 16: [3, 5], 17: [3, 6], 18: [3, 8], 19: [3, 10], 20: [3, 12], 
                    21: [4, 1], 22: [4, 3], 23: [4, 5], 24: [4, 6], 25: [4, 8], 26: [4, 10], 27: [4, 12], 28: [4, 13]}

black_button_list = {0: [1, 2], 1: [1, 4], 2: [1, 7], 3: [1, 9], 4: [1, 11],
                    5: [2, 2.5], 6: [2, 4.5], 7: [2, 7.5], 8: [2, 9.5], 9: [2, 11.5],
                    10: [3, 2], 11: [3, 4], 12: [3, 7], 13: [3, 9], 14: [3, 11], 
                    15: [4, 2], 16: [4, 4], 17: [4, 7], 18: [4, 9], 19: [4, 11]}

not_note_button_list = {0: 'Ctrl', 1: 'Win', 2: 'Alt', 3: 'Space', 4: 'Alt', 5: 'Win', 6: 'Meny', 7: 'Ctrl',  
                        20: 'Caps', 33: 'Tab', 46: '\\', 47: '`/~'}

button_list = ['Ctrl', 'Win', 'Alt', 'Space', 'Alt', 'Win', 'Meny', 'Ctrl',  
               'LShift', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '/', 'RShift',
               'Caps', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';','\'', 'Enter',
               'Tab', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '[', ']', '\\', 
               '`/~', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', '<-']

#2 1.5
# 2 2.5
# 2 3.5
# 2 4.5
# 2 5.5
# 2 6.5
# 2 7.5
# 2 8.5
# 2 9.5
# 2 10.5
# 2 11.5

def get_notes_dict() -> dict:
    notes_dict = {
                 f'{pygame.K_PERIOD}': 'A2', f'{pygame.K_SEMICOLON}': 'A3', f'{pygame.K_p}': 'A4', f'{pygame.K_0}': 'A5',
                 f'{pygame.K_COMMA}': 'A-2', f'{pygame.K_l}': 'A-3', f'{pygame.K_o}': 'A-4', f'{pygame.K_9}': 'A-5',

                 f'{pygame.K_RSHIFT}': 'B2', f'{pygame.K_RETURN}': 'B3', f'{pygame.K_RIGHTBRACKET}': 'B4', f'{pygame.K_EQUALS}': 'B5',
                 f'{pygame.K_SLASH}': 'B-2', f'{pygame.K_QUOTE}': 'B-3', f'{pygame.K_LEFTBRACKET}': 'B-4', f'{pygame.K_MINUS}': 'B-5',
                 
                 f'{pygame.K_LSHIFT}': 'C2', f'{pygame.K_a}': 'C3', f'{pygame.K_q}': 'C4', f'{pygame.K_1}': 'C5', f'{pygame.K_BACKSPACE}': 'C6',
                 
                 f'{pygame.K_x}': 'D2', f'{pygame.K_d}': 'D3', f'{pygame.K_e}': 'D4', f'{pygame.K_3}': 'D5',
                 f'{pygame.K_z}': 'D-2', f'{pygame.K_s}': 'D-3', f'{pygame.K_w}': 'D-4', f'{pygame.K_2}': 'D-5',
                 
                 f'{pygame.K_v}': 'E2', f'{pygame.K_g}': 'E3', f'{pygame.K_t}': 'E4', f'{pygame.K_5}': 'E5',
                 f'{pygame.K_c}': 'E-2', f'{pygame.K_f}': 'E-3', f'{pygame.K_r}': 'E-4', f'{pygame.K_4}': 'E-5',
                 
                 f'{pygame.K_b}': 'F2', f'{pygame.K_h}': 'F3', f'{pygame.K_y}': 'F4', f'{pygame.K_6}': 'F5',
                 
                 f'{pygame.K_m}': 'G2', f'{pygame.K_k}': 'G3', f'{pygame.K_i}': 'G4', f'{pygame.K_8}': 'G5',
                 f'{pygame.K_n}': 'G-2', f'{pygame.K_j}': 'G-3', f'{pygame.K_u}': 'G-4', f'{pygame.K_7}': 'G-5'}
    
    return notes_dict
    
