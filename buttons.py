import pygame
import pygame_widgets
from pygame_widgets.button import Button
from pygame_widgets.dropdown import Dropdown

start_record_image = pygame.image.load('assets/images/start_record.png')


def create_buttons(screen, WIDTH, HEIGHT):
    start_record_image = pygame.transform.scale(start_record_image, ( WIDTH*(5/31), HEIGHT*(1/20)))
    
    btn_record = Button(
        screen, WIDTH/30, HEIGHT*(1/120), WIDTH*(5/31), HEIGHT*(1/20),

        text='Начать запись', 
        fontSize=50, 
        font = pygame.font.Font('assets/timesnrcyrmt_bold.ttf', 24),
        inactiveColour=(150, 150, 255), 
        hoverColour=(110, 110, 255), 
        pressedColour=(160, 160, 255), 
        radius=7
    )

    btn_stop_record = Button(
        screen, WIDTH*(7/31), HEIGHT*(1/120), WIDTH*(5/31), HEIGHT*(1/20),

        text='Остановить запись', 
        fontSize=50, 
        font = pygame.font.Font('assets/timesnrcyrmt_bold.ttf', 24),
        inactiveColour=(150, 150, 255), 
        hoverColour=(110, 110, 255), 
        pressedColour=(160, 160, 255), 
        radius=7
    )

    btn_play_music = Button(
        screen, WIDTH*(13/31), HEIGHT*(1/120), WIDTH*(5/31), HEIGHT*(1/20), 

        text='Воспроизвести музыку', 
        fontSize=50, 
        font = pygame.font.Font('assets/timesnrcyrmt_bold.ttf', 24),
        inactiveColour=(150, 150, 255), 
        hoverColour=(110, 110, 255), 
        pressedColour=(160, 160, 255), 
        radius=7
    )

    btn_stop_music = Button(
        screen, WIDTH*(19/31), HEIGHT*(1/120), WIDTH*(5/31), HEIGHT*(1/20), 

        text='Остановить музыку',  
        fontSize=50,  
        font = pygame.font.Font('assets/timesnrcyrmt_bold.ttf', 24),
        inactiveColour=(150, 150, 255), 
        hoverColour=(110, 110, 255), 
        pressedColour=(160, 160, 255), 
        radius=7
    )

    drop_learn_samples = Dropdown(
        screen, WIDTH*(25/31), HEIGHT*(1/120), WIDTH*(5/31), HEIGHT*(1/20), name='Играть по нотам',
        choices=[
            'ABBA',
            'Конь',
            'Кукла колдуна',
        ],
        font = pygame.font.Font('assets/timesnrcyrmt_bold.ttf', 24),
        borderRadius=7, 
        colour=(150, 150, 255), values=[1, 2, 2], direction='down'
    )
    
    return btn_record, btn_stop_record, btn_play_music, btn_stop_music, drop_learn_samples