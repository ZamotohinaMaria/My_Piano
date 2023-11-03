piano_notes = ['A0', 'A#0', 'B0', 'C1', 'C#1', 'D1', 'D#1', 'E1', 'F1', 'F#1', 'G1', 'G#1',
               'A1', 'A#1', 'B1', 'C2', 'C#2', 'D2', 'D#2', 'E2', 'F2', 'F#2', 'G2', 'G#2',
               'A2', 'A#2', 'B2', 'C3', 'C#3', 'D3', 'D#3', 'E3', 'F3', 'F#3', 'G3', 'G#3',
               'A3', 'A#3', 'B3', 'C4', 'C#4', 'D4', 'D#4', 'E4', 'F4', 'F#4', 'G4', 'G#4',
               'A4', 'A#4', 'B4', 'C5', 'C#5', 'D5', 'D#5', 'E5', 'F5', 'F#5', 'G5', 'G#5',
               'A5', 'A#5', 'B5', 'C6', 'C#6', 'D6', 'D#6', 'E6', 'F6', 'F#6', 'G6', 'G#6',
               'A6', 'A#6', 'B6', 'C7', 'C#7', 'D7', 'D#7', 'E7', 'F7', 'F#7', 'G7', 'G#7',
               'A7', 'A#7', 'B7', 'C8', 
               'Bb0', 'Db1', 'Eb1', 'Gb1', 'Ab1',
               'Bb1', 'Db2', 'Eb2', 'Gb2', 'Ab2',
               'Bb2', 'Db3', 'Eb3', 'Gb3', 'Ab3',
               'Bb3', 'Db4', 'Eb4', 'Gb4', 'Ab4',
               'Bb4', 'Db5', 'Eb5', 'Gb5', 'Ab5',
               'Bb5', 'Db6', 'Eb6', 'Gb6', 'Ab6',
               'Bb6', 'Db7', 'Eb7', 'Gb7', 'Ab7',
               'Bb7']

white_notes = ['A0', 'B0', 'C1', 'D1', 'E1', 'F1', 'G1',
               'A1', 'B1', 'C2', 'D2', 'E2', 'F2', 'G2',
               'A2', 'B2', 'C3', 'D3', 'E3', 'F3', 'G3',
               'A3', 'B3', 'C4', 'D4', 'E4', 'F4', 'G4',
               'A4', 'B4', 'C5', 'D5', 'E5', 'F5', 'G5',
               'A5', 'B5', 'C6', 'D6', 'E6', 'F6', 'G6',
               'A6', 'B6', 'C7', 'D7', 'E7', 'F7', 'G7',
               'A7', 'B7', 'C8']

black_flats = ['Bb0', 'Db1', 'Eb1', 'Gb1', 'Ab1',
               'Bb1', 'Db2', 'Eb2', 'Gb2', 'Ab2',
               'Bb2', 'Db3', 'Eb3', 'Gb3', 'Ab3',
               'Bb3', 'Db4', 'Eb4', 'Gb4', 'Ab4',
               'Bb4', 'Db5', 'Eb5', 'Gb5', 'Ab5',
               'Bb5', 'Db6', 'Eb6', 'Gb6', 'Ab6',
               'Bb6', 'Db7', 'Eb7', 'Gb7', 'Ab7',
               'Bb7']

black_sharps = ['A#0', 'C#1', 'D#1', 'F#1', 'G#1',
                'A#1', 'C#2', 'D#2', 'F#2', 'G#2',
                'A#2', 'C#3', 'D#3', 'F#3', 'G#3',
                'A#3', 'C#4', 'D#4', 'F#4', 'G#4',
                'A#4', 'C#5', 'D#5', 'F#5', 'G#5',
                'A#5', 'C#6', 'D#6', 'F#6', 'G#6',
                'A#6', 'C#7', 'D#7', 'F#7', 'G#7',
                'A#7']


def get_left_dict(left_oct: int) -> dict:
    left_dict = {'z': f'C{left_oct}', 'a': f'C{left_oct + 1}',
                'x': f'D{left_oct}', 's': f'D{left_oct + 1}',
                'c': f'E{left_oct}', 'd': f'E{left_oct + 1}',
                'v': f'F{left_oct}', 'f': f'F{left_oct + 1}',
                'b': f'G{left_oct}', 'g': f'G{left_oct + 1}',
                'n': f'A{left_oct}', 'h': f'A{left_oct + 1}',
                'm': f'B{left_oct}', 'j': f'B{left_oct + 1}'}
    return left_dict
    
def get_right_dict(right_oct: int) -> dict:
    right_dict = {'q': f'C{right_oct}', '1': f'C{right_oct + 1}',
                    'w': f'D{right_oct}', '2': f'D{right_oct + 1}',
                    'e': f'E{right_oct}', '3': f'E{right_oct + 1}',
                    'r': f'F{right_oct}', '4': f'F{right_oct + 1}',
                    't': f'G{right_oct}', '5': f'G{right_oct + 1}',
                    'y': f'A{right_oct}', '6': f'A{right_oct + 1}',
                    'u': f'B{right_oct}', '7': f'B{right_oct + 1}'}
    return right_dict

def get_black_flats_dict(left_oct: int, right_oct: int) -> dict:
    black_flats_dict = {
        'X': f'Db{left_oct}', 'S': f'Db{left_oct + 1}',
        'C': f'Eb{left_oct}', 'D': f'Eb{left_oct + 1}',
        'B': f'Gb{left_oct}', 'G': f'Gb{left_oct + 1}',
        'N': f'Ab{left_oct}', 'H': f'Ab{left_oct + 1}',
        'M': f'Bb{left_oct}', 'J': f'Bb{left_oct + 1}',
        
        'W': f'Db{right_oct}', '@': f'Db{right_oct + 1}',
        'E': f'Eb{right_oct}', '#': f'Eb{right_oct + 1}',
        'T': f'Gb{right_oct}', '%': f'Gb{right_oct + 1}',
        'Y': f'Ab{right_oct}', '^': f'Ab{right_oct + 1}',
        'U': f'Bb{right_oct}', '&': f'Bb{right_oct + 1}'}
    return black_flats_dict

def get_black_sharps_dict(left_oct: int, right_oct: int) -> dict:
    black_sharps_dict = {
        'Z': f'C#{left_oct}', 'A': f'C#{left_oct + 1}',
        'X': f'D#{left_oct}', 'S': f'D#{left_oct + 1}',
        'V': f'F#{left_oct}', 'F': f'F#{left_oct + 1}',
        'B': f'G#{left_oct}', 'G': f'G#{left_oct + 1}', 
        'N': f'A#{left_oct}', 'H': f'A#{left_oct + 1}',
        
        'Q': f'C#{right_oct}', '!': f'C#{right_oct + 1}',
        'W': f'D#{right_oct}', '@': f'D#{right_oct + 1}',
        'R': f'F#{right_oct}', '$': f'F#{right_oct + 1}',
        'T': f'G#{right_oct}', '%': f'G#{right_oct + 1}',
        'Y': f'A#{right_oct}', '^': f'A#{right_oct + 1}'}
    return black_sharps_dict