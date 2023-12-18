import pygame
import pygame_widgets
from pygame_widgets.button import Button
from pygame_widgets.dropdown import Dropdown


def create_buttons(screen, WIDTH, HEIGHT):
    start_record_image = pygame.image.load('assets/images/start_record.png')
    start_record_image = pygame.transform.scale(start_record_image, ( WIDTH*(1/45),  HEIGHT*(1/25)))
    
    btn_record = Button(
        screen, WIDTH/150 + WIDTH*(1/50), HEIGHT*(1/120), WIDTH*(1/38), HEIGHT*(1/20),
        image = start_record_image,
        inactiveColour=(240, 240, 255), 
        hoverColour=(225, 225, 255), 
        pressedColour=(160, 160, 255), 
        radius=3
    )

    stop_record_image = pygame.image.load('assets/images/stop_record.png')
    stop_record_image = pygame.transform.scale(stop_record_image, ( WIDTH*(1/45),  HEIGHT*(1/25)))
    
    btn_stop_record = Button(
        screen, WIDTH/150 + WIDTH*(3/50), HEIGHT*(1/120), WIDTH*(1/38), HEIGHT*(1/20),

        image = stop_record_image,
        inactiveColour=(240, 240, 255), 
        hoverColour=(225, 225, 255), 
        pressedColour=(160, 160, 255), 
        radius=3
    )

    start_play_image = pygame.image.load('assets/images/play_music-2.png')
    start_play_image = pygame.transform.scale(start_play_image, ( WIDTH*(1/45),  HEIGHT*(1/25)))

    btn_play_music = Button(
        screen, WIDTH/150 + WIDTH*(5/50) , HEIGHT*(1/120), WIDTH*(1/38), HEIGHT*(1/20), 

        image = start_play_image,
        inactiveColour=(240, 240, 255), 
        hoverColour=(225, 225, 255), 
        pressedColour=(160, 160, 255),  
        radius=3
    )

    stop_play_image = pygame.image.load('assets/images/stop_music.png')
    stop_play_image = pygame.transform.scale(stop_play_image, ( WIDTH*(1/45),  HEIGHT*(1/25)))

    btn_stop_music = Button(
        screen, WIDTH/150 + WIDTH*(7/50), HEIGHT*(1/120), WIDTH*(1/38), HEIGHT*(1/20), 

        image = stop_play_image,
        inactiveColour=(240, 240, 255), 
        hoverColour=(225, 225, 255), 
        pressedColour=(160, 160, 255),
        radius=3
    )

    view_sample_image = pygame.image.load('assets/images/note_list.png')
    view_sample_image = pygame.transform.scale(view_sample_image, ( WIDTH*(1/45),  HEIGHT*(1/25)))

    btn_view_sample = Button(
        screen, WIDTH/150 + WIDTH*(38/50), HEIGHT*(1/120), WIDTH*(1/38), HEIGHT*(1/20), 

        image = view_sample_image,
        inactiveColour=(240, 240, 255), 
        hoverColour=(225, 225, 255), 
        pressedColour=(160, 160, 255),
        radius=3
    )
    
    stop_view_sample_image = pygame.image.load('assets/images/close_note_list.png')
    stop_view_sample_image = pygame.transform.scale(stop_view_sample_image, ( WIDTH*(1/45),  HEIGHT*(1/25)))

    btn_stop_view_sample = Button(
        screen, WIDTH/150 + WIDTH*(36/50), HEIGHT*(1/120), WIDTH*(1/38), HEIGHT*(1/20), 

        image = stop_view_sample_image,
        inactiveColour=(240, 240, 255), 
        hoverColour=(225, 225, 255), 
        pressedColour=(160, 160, 255),
        radius=3
    )
    
    input_key = pygame.image.load('assets/images/key.png')
    input_key = pygame.transform.scale(input_key, ( WIDTH*(1/45),  HEIGHT*(1/25)))

    btn_input_key = Button(
        screen, WIDTH/150 + WIDTH*(34/50), HEIGHT*(1/120), WIDTH*(1/38), HEIGHT*(1/20), 

        image = input_key,
        inactiveColour=(240, 240, 255), 
        hoverColour=(225, 225, 255), 
        pressedColour=(160, 160, 255),
        radius=3
    )    

    drop_learn_samples = Dropdown(
        screen, WIDTH/150 + WIDTH*(40/50), HEIGHT*(1/120), WIDTH*(5/31), HEIGHT*(1/20), name='Выбрать композицию',
        choices=[
            'Выбрать композицию',
            'ABBA',
            'Конь',
            'Кукла колдуна',
        ],
        font = pygame.font.Font('assets/timesnrcyrmt_bold.ttf', 24),
        borderRadius=3, 
        inactiveColour=(240, 240, 255), 
        hoverColour=(225, 225, 255), 
        pressedColour=(160, 160, 255),
        values=[None, 'ABBA', 'Konb', 'KISH'], direction='down'
    )
    
    return (btn_record, btn_stop_record, btn_play_music, 
            btn_stop_music, btn_view_sample, btn_stop_view_sample, 
            btn_input_key, drop_learn_samples)