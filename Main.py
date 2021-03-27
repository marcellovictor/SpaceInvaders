from PPlay import *
from PPlay.sprite import *
from PPlay.mouse import *
from PPlay.keyboard import *
from Menu import *
from Jogo import *
from Dificuldades import *
from time import sleep

nivel_dificuldade = 1

estado = 0
while True:
    option_selected = 0
    if estado == 0:
        option_selected = abrir_menu()

    if option_selected == 1:
        sleep(0.2)
        estado = 1
        iniciar_jogo(nivel_dificuldade)
    elif option_selected == 2:
        sleep(0.2)
        estado = 2
        nivel_dificuldade = selecionar_dificuldade()
    elif option_selected == 3:
        sleep(0.2)
        estado = 3
        print("teste_ranking")
    elif option_selected == 4:
        break
    sleep(0.2)
    estado = 0
