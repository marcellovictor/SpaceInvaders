from PPlay.mouse import *
from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *


def selecionar_dificuldade():
    dificuldades = Window(800, 600)
    dificuldades.set_title("Dificuldades")

    background_dificuldades = GameImage("images\\nave-dificuldades.jpg")
    
    mouse_dificuldades = Mouse()

    # facil
    button_facil = Sprite("images\\button-facil.jpg", 1)
    button_facil.x = dificuldades.width/2 - button_facil.width/2
    button_facil.y = dificuldades.height/3 - button_facil.height

    selected_facil = Sprite("images\\selected-facil.jpg", 1)
    selected_facil.x = dificuldades.width / 2 - button_facil.width / 2
    selected_facil.y = dificuldades.height / 3 - button_facil.height

    # medio
    button_medio = Sprite("images\\button-medio.jpg", 1)
    button_medio.x = dificuldades.width/2 - button_medio.width/2
    button_medio.y = button_facil.y + 150

    selected_medio = Sprite("images\\selected-medio.jpg", 1)
    selected_medio.x = dificuldades.width / 2 - button_medio.width / 2
    selected_medio.y = button_facil.y + 150

    # dificil
    button_dificil = Sprite("images\\button-dificil.jpg", 1)
    button_dificil.x = dificuldades.width/2 - button_dificil.width/2
    button_dificil.y = button_medio.y + 150

    selected_dificil = Sprite("images\\selected-dificil.jpg", 1)
    selected_dificil.x = dificuldades.width / 2 - button_dificil.width / 2
    selected_dificil.y = button_medio.y + 150

    while True:
        dificuldades.update()
        dificuldades.set_background_color((32, 37, 71))

        if mouse_dificuldades.is_over_object(button_facil) and mouse_dificuldades.is_button_pressed(1):
            return 1
        if mouse_dificuldades.is_over_object(button_medio) and mouse_dificuldades.is_button_pressed(1):
            return 2
        if mouse_dificuldades.is_over_object(button_dificil) and mouse_dificuldades.is_button_pressed(1):
            return 3

        # desenho
        background_dificuldades.draw()
        selected_facil.draw() if mouse_dificuldades.is_over_object(button_facil) else button_facil.draw()
        selected_medio.draw() if mouse_dificuldades.is_over_object(button_medio) else button_medio.draw()
        selected_dificil.draw() if mouse_dificuldades.is_over_object(button_dificil) else button_dificil.draw()
