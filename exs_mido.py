import mido

# Создание сообщения для ноты
note_on = mido.Message('note_on', note=60, velocity=64, time=40)

# Воспроизведение ноты
print(mido.get_output_names())
port = mido.open_output('Microsoft GS Wavetable Synth 0')
port.send(note_on)
note_on = mido.Message('note_off', note=60, velocity=64, time=600)