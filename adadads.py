#!/bin/env python3
import pyaudio as pa
import numpy as np
import pygame

SAMPLE_RATE = 44100
#                      0       1       2      3        4       5       6
#                      до      ре      ми     фа       соль    ля      си
freq_array = np.array([261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88])
key_names = ['a', 's', 'd', 'f', 'g', 'h', 'j']
key_list = list(map(lambda x: ord(x), key_names))
key_dict = dict([(key, False) for key in key_list])


# signal generation funcs
def square(x):
    return np.clip(np.ceil(np.sin(x)), 0, 0.5)


def saw(x):
    c = x / np.pi - 0.5
    return 0.5 * (c - np.floor(0.5 + c)) + 0.25


def triangle(x):
    return np.abs(x % 6 - 3) / (2 * np.pi)
# end of funcs


gen_func = np.sin
gen_func_list = (
    (np.sin, ord('w')),
    (square, ord('e')),
    (saw, ord('r')),
    (triangle, ord('t'))
)


def generate_sample(freq, duration, volume):
    amplitude = np.round((2 ** 16) * volume)
    total_samples = np.round(SAMPLE_RATE * duration)
    w = 2.0 * np.pi * freq / SAMPLE_RATE
    k = np.arange(0, total_samples)
    return np.round(amplitude * gen_func(k * w))


def generate_tones(duration):
    tones = []
    for freq in freq_array:
        tone = np.array(generate_sample(freq, duration, 1.0), dtype=np.int16)
        tones.append(tone)
    return tones


if __name__ == '__main__':
    duration_tone = 1/64.0
    tones = generate_tones(duration_tone)
    p = pa.PyAudio()
    stream = p.open(format=p.get_format_from_width(width=2),
                    channels=2,
                    rate=SAMPLE_RATE,
                    output=True)
    window_size = 320, 240
    screen = pygame.display.set_mode(window_size)
    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == ord('q'):
                    running = False
                if event.key == ord('-'):
                    duration_tone /= 2
                    print('duration_tone =', duration_tone)
                    tones = generate_tones(duration_tone)
                if event.key == ord('='):
                    duration_tone *= 2
                    print('duration_tone =', duration_tone)
                    tones = generate_tones(duration_tone)
                if event.key == ord('1'):
                    freq_array /= 2
                    print('freq_array =', freq_array)
                    tones = generate_tones(duration_tone)
                if event.key == ord('2'):
                    freq_array *= 2
                    print('freq_array =', freq_array)
                    tones = generate_tones(duration_tone)
                for (function, key) in gen_func_list:
                    if key == event.key:
                        print('gen_function =', function.__name__)
                        gen_func = function
                        tones = generate_tones(duration_tone)
                for (index, key) in enumerate(key_list):
                    if event.key == key:
                        key_dict[key] = True
            if event.type == pygame.KEYUP:
                for (index, key) in enumerate(key_list):
                    if event.key == key:
                        key_dict[key] = False
        for (index, key) in enumerate(key_list):
            if key_dict[key] is True:
                stream.write(tones[index])
    pygame.quit()
    stream.stop_stream()
    stream.close()
    p.terminate()
music_generator.py
from collections import defaultdict
from time import sleep
import pyaudio as pa
import numpy as np

SAMPLE_RATE = 44100

P1 = 16

music_list = [
    ('c5', 8), ('h4', 8), ('P', P1), 
    ('h4', 8), ('a4', 16), ('g4', 16), ('P', P1), 
    ('h4', 8), ('a4', 8), ('P', P1), 
    ('a4', 8), ('P', P1), 
    ('a4', 8), ('g4', 8), ('f4', 8), ('e4', 8), ('P', P1), 
    ('g4', 8), ('f4', 8), ('P', P1), 
    ('e4', 8), ('e4', 8), ('g4', 8), ('f4', 8), ('P', P1),
    ('e4', 8), ('d4', 8), ('c4', 8), ('h3', 8), ('P', P1),
    ('a5', 8), ('c6', 8), ('e5', 8), ('h5', 8), ('P', P1),
    ('h5', 8), ('a5', 16), ('g5', 16), ('P', P1),
    ('h5', 8), ('c5', 8), ('e5', 8), ('a5', 8), ('P', P1),
    ('a5', 8), ('P', P1),
    ('a5', 8), ('a4', 8), ('c5', 8), ('e5', 8), ('g4', 8), ('g5', 8), ('f4', 8), ('f5', 8), ('e4', 8), ('e5', 8), ('P', P1),
    ('g5', 8), ('d5', 8), ('a4', 8), ('f5', 8), ('P', P1),
    ('e5', 8), ('c5', 8), ('e5', 8), ('g5', 8), ('d5', 8), ('f5', 8), ('P', P1),
    ('e4', 8), ('g4', 8), ('h4', 8), ('e5', 8), ('d5', 8), ('c5', 8), ('h4', 8)
]

def generate_sample(freq, duration, volume):
    amplitude     = np.round((2 ** 16) * volume)
    total_samples = np.round(SAMPLE_RATE * duration)
    w = 2.0 * np.pi * freq / SAMPLE_RATE
    k = np.arange(0, total_samples)
    return np.round(amplitude * np.sin(k * w))

class Music:
    def __init__(self, stream, duration):
        self.stream = stream
        self.notes = Music.generate_notes(duration)
        self.duration = duration

    def generate_notes(duration):
        notes = {
            # normal tone
            'C0': 16.352, 'D0': 18.354, 'E0': 20.602, 'F0': 21.827, 'G0': 24.500, 'A0': 27.500, 'H0': 30.868,
            'C1': 32.703, 'D1': 36.708, 'E1': 41.203, 'F1': 43.654, 'G1': 48.999, 'A1': 55.000, 'H1': 61.735,
            'C2': 65.406, 'D2': 73.416, 'E2': 82.407, 'F2': 87.307, 'G2': 97.999, 'A2': 110.00, 'H2': 123.47,
            'C3': 130.81, 'D3': 146.83, 'E3': 164.81, 'F3': 174.61, 'G3': 196.00, 'A3': 220.00, 'H3': 246.94,
            'C4': 261.63, 'D4': 293.66, 'E4': 329.63, 'F4': 349.23, 'G4': 392.00, 'A4': 440.00, 'H4': 493.88,
            'C5': 523.25, 'D5': 587.33, 'E5': 659.26, 'F5': 698.46, 'G5': 783.99, 'A5': 880.00, 'H5': 987.77,
            'C6': 1046.5, 'D6': 1174.7, 'E6': 1318.5, 'F6': 1396.9, 'G6': 1568.0, 'A6': 1760.0, 'H6': 1975.5,
            'C7': 2093.0, 'D7': 2349.3, 'E7': 2637.0, 'F7': 2793.8, 'G7': 3136.0, 'A7': 3520.0, 'H7': 3951.1,
            'C8': 4186.0, 'D8': 4698.6, 'E8': 5274.0, 'F8': 5587.7, 'G8': 6271.9, 'A8': 7040.0, 'H8': 7902.1,
            # half tone up (flat)
            'Cb0': 20.440, 'Db0': 22.942, 'Eb0': 25.752, 'Fb0': 27.284, 'Gb0': 30.625, 'Ab0': 34.375, 'Hb0': 38.585, 
            'Cb1': 40.879, 'Db1': 45.885, 'Eb1': 51.504, 'Fb1': 54.568, 'Gb1': 61.249, 'Ab1': 68.750, 'Hb1': 77.169, 
            'Cb2': 81.758, 'Db2': 91.770, 'Eb2': 103.01, 'Fb2': 109.13, 'Gb2': 122.50, 'Ab2': 137.50, 'Hb2': 154.34, 
            'Cb3': 163.51, 'Db3': 183.54, 'Eb3': 206.01, 'Fb3': 218.26, 'Gb3': 245.00, 'Ab3': 275.00, 'Hb3': 308.68, 
            'Cb4': 327.04, 'Db4': 367.08, 'Eb4': 412.04, 'Fb4': 436.54, 'Gb4': 490.00, 'Ab4': 550.00, 'Hb4': 617.35, 
            'Cb5': 654.06, 'Db5': 734.16, 'Eb5': 824.08, 'Fb5': 873.08, 'Gb5': 979.99, 'Ab5': 1100.0, 'Hb5': 1234.7, 
            'Cb6': 1308.1, 'Db6': 1468.4, 'Eb6': 1648.1, 'Fb6': 1746.1, 'Gb6': 1960.0, 'Ab6': 2200.0, 'Hb6': 2469.4, 
            'Cb7': 2616.2, 'Db7': 2936.6, 'Eb7': 3296.2, 'Fb7': 3492.2, 'Gb7': 3920.0, 'Ab7': 4400.0, 'Hb7': 4938.9, 
            'Cb8': 5232.5, 'Db8': 5873.2, 'Eb8': 6592.5, 'Fb8': 6984.6, 'Gb8': 7839.9, 'Ab8': 8800.0, 'Hb8': 9877.6, 
            # half tone down (sharp)
            'C#0': 12.264, 'D#0': 13.766, 'E#0': 15.452, 'F#0': 16.370, 'G#0': 18.375, 'A#0': 20.625, 'H#0': 23.151, 
            'C#1': 24.527, 'D#1': 27.531, 'E#1': 30.902, 'F#1': 32.741, 'G#1': 36.750, 'A#1': 41.250, 'H#1': 46.301, 
            'C#2': 49.055, 'D#2': 55.062, 'E#2': 61.806, 'F#2': 65.480, 'G#2': 73.500, 'A#2': 82.500, 'H#2': 92.603, 
            'C#3': 98.108, 'D#3': 110.12, 'E#3': 123.61, 'F#3': 130.96, 'G#3': 147.00, 'A#3': 165.00, 'H#3': 185.21, 
            'C#4': 196.22, 'D#4': 220.25, 'E#4': 247.22, 'F#4': 261.92, 'G#4': 294.00, 'A#4': 330.00, 'H#4': 370.41, 
            'C#5': 392.44, 'D#5': 440.50, 'E#5': 494.45, 'F#5': 523.85, 'G#5': 588.00, 'A#5': 660.00, 'H#5': 740.83, 
            'C#6': 784.87, 'D#6': 881.03, 'E#6': 988.88, 'F#6': 1047.7, 'G#6': 1176.0, 'A#6': 1320.0, 'H#6': 1481.6, 
            'C#7': 1569.8, 'D#7': 1762.0, 'E#7': 1977.8, 'F#7': 2095.4, 'G#7': 2352.0, 'A#7': 2640.0, 'H#7': 2963.3, 
            'C#8': 3139.5, 'D#8': 3524.0, 'E#8': 3955.5, 'F#8': 4190.8, 'G#8': 4703.9, 'A#8': 5280.0, 'H#8': 5926.6
        }
        result = defaultdict(np.array)
        for (note, freq) in notes.items():
            result[note] = np.array(generate_sample(freq, duration, 1.0), dtype=np.int16)
        return result

    # duration -- обратная длина ноты (1/8 -- 8, 1/16 -- 16)
    def play_note(self, note, duration):
        if note[0].upper() == 'P':
            sleep(1 / duration)
        else:
            note = self.notes.get(note[0].upper() + note[1:]) 
            if note is not None:
                len_d = len(note) / duration
                self.stream.write(note[:len_d])


if __name__ == '__main__':
    p = pa.PyAudio()
    stream = p.open(format=p.get_format_from_width(width=2), channels=2, rate=SAMPLE_RATE, output=True)
    music = Music(stream, 8)
    for conf in music_list:
        music.play_note(*conf)
    sleep(1)
    stream.stop_stream()
    stream.close()
    p.terminate()