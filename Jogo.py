from PPlay.window import *
from PPlay.keyboard import *
from PPlay.sprite import *


def iniciar_jogo(dificuldade):
    jogo = Window(800, 600)
    jogo.set_title("Space Invaders")

    # nave
    nave = Sprite("navezinha.png", 1)
    nave.x = jogo.width/2 - nave.width/2
    nave.y = jogo.height - 100
    vel_nave = 120 + (30/dificuldade)

    # tiro
    tiro = Sprite("tirinho.png", 1)
    tiro.x = nave.x + nave.width/2 - tiro.width/2 + 1
    tiro.y = nave.y - tiro.height
    tiros = []
    vel_tiro = 100 + 50/dificuldade
    crono = 0

    teclado = Keyboard()

    while True:
        jogo.update()
        jogo.set_background_color((32, 37, 71))
        crono += jogo.delta_time()

        if teclado.key_pressed("esc"):
            break

        # efetuar disparos
        if teclado.key_pressed("SPACE") and crono >= dificuldade/3:
            tir = [Sprite("tirinho.png"),
                   nave.x + nave.width/2 - tiro.width/2 + 1,
                   nave.y - tiro.height]
            tiros.append(tir)
            crono = 0

        # movimentos tiro
        for t in tiros:
            t[2] -= vel_tiro * jogo.delta_time()

        # desativar tiros
        for t in tiros:
            if t[2] < 0:
                tiros.remove(t)
        # movimentos nave
        if (teclado.key_pressed("a") or teclado.key_pressed("LEFT")) and nave.x > 0:
            nave.x -= vel_nave * jogo.delta_time()
        if (teclado.key_pressed("d") or teclado.key_pressed("RIGHT")) and (nave.x + nave.width) < jogo.width:
            nave.x += vel_nave * jogo.delta_time()

        # desenho
        for t in tiros:
            tiro = t[0]
            tiro.x = t[1]
            tiro.y = t[2]
            tiro.draw()
        nave.draw()
