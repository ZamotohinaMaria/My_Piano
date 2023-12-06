from music21 import *

# Создание объекта Score
score = stream.Score()

# Создание небольшой мелодии
note1 = note.Note("C#4")
note2 = note.Note("D4")
note3 = note.Note("E-4", duration = duration.Duration(5))

# Добавление нот в объект Score
score.append(note1)
score.append(note2)
score.append(note3)

# Вывод нотной записи в MIDI формате
score.write('midi', fp='my_music.mid')