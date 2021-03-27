from PPlay.window import *
from PPlay.sprite import *
from PPlay.mouse import *
from PPlay.keyboard import *
from enum import Enum


def abrir_menu():
    menu = Window(800, 600)
    menu.set_title("Menu")

    mouse = Mouse()
    teclado = Keyboard()

    # jogar
    button_jogar = Sprite("button-jogar.jpg", 1)
    button_jogar.x = menu.width/2 - button_jogar.width/2
    button_jogar.y = menu.height/4

    selected_jogar = Sprite("selected-jogar.jpg", 1)
    selected_jogar.x = menu.width/2 - button_jogar.width/2
    selected_jogar.y = menu.height/4

    # dificuldade

    button_dificuldade = Sprite("button-dificuldade.jpg", 1)
    button_dificuldade.x = menu.width/2 - button_dificuldade.width/2
    button_dificuldade.y = button_jogar.y + 100

    selected_dificuldade = Sprite("selected-dificuldade.jpg", 1)
    selected_dificuldade.x = menu.width/2 - button_dificuldade.width/2
    selected_dificuldade.y = button_jogar.y + 100

    # ranking
    button_ranking = Sprite("button-ranking.jpg", 1)
    button_ranking.x = menu.width/2 - button_ranking.width/2
    button_ranking.y = button_dificuldade.y + 100

    selected_ranking = Sprite("selected-ranking.jpg", 1)
    selected_ranking.x = menu.width/2 - button_ranking.width/2
    selected_ranking.y = button_dificuldade.y + 100

    # sair
    button_sair = Sprite("button-sair.jpg", 1)
    button_sair.x = menu.width/2 - button_sair.width/2
    button_sair.y = button_ranking.y + 100

    selected_sair = Sprite("selected-sair.jpg", 1)
    selected_sair.x = menu.width/2 - button_sair.width/2
    selected_sair.y = button_ranking.y + 100

    while True:
        menu.update()
        menu.set_background_color((32, 37, 71))

        if mouse.is_over_object(button_jogar) and mouse.is_button_pressed(1):
            return 1
        elif mouse.is_over_object(button_dificuldade) and mouse.is_button_pressed(1):
            return 2
        elif mouse.is_over_object(button_ranking) and mouse.is_button_pressed(1):
            return 3
        elif mouse.is_over_object(button_sair) and mouse.is_button_pressed(1):
            return 4

        # desenho
        selected_jogar.draw() if mouse.is_over_object(button_jogar) else button_jogar.draw()
        selected_dificuldade.draw() if mouse.is_over_object(button_dificuldade) else button_dificuldade.draw()
        selected_ranking.draw() if mouse.is_over_object(button_ranking) else button_ranking.draw()
        selected_sair.draw() if mouse.is_over_object(button_sair) else button_sair.draw()

