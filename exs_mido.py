import mido
from mido import MidiFile, MidiTrack

mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

track.append(mido.Message('note_on', note=60, velocity=64, time=500))
track.append(mido.Message('note_off', note=60, velocity=64, time=500))
track.append(mido.Message('note_on', note=70, velocity=64, time=500))
track.append(mido.Message('note_off', note=70, velocity=64, time=500))
mid.save('output.mid')

import pygame
import time
# pygame.init()
# pygame.mixer.init()
# pygame.mixer.music.load("output.mid")
# pygame.mixer.music.play()
# while pygame.mixer.music.get_busy():
#     time.sleep(1)
    
t = time.localtime()
while True:
    print(time.time()%1)
cuurent_time = time.strftime("%H:%M:%S", t)
print(cuurent_time[0])