from PPlay.window import *
from PPlay.keyboard import *
from PPlay.sprite import *
from pygame import Surface


def iniciar_jogo(dificuldade, estado):
    if estado == 1:
        jogo = Window(800, 600)
        jogo.set_title("Space Invaders")
        background_jogo = Sprite("images\\background-espacial.jpg")
        teclado = Keyboard()

        ganhou = False
        perdeu = False

        # pontuação
        pontos = 500
        crono_ate_um = 0
        crono_geral = 0

        # nave
        nave = Sprite("images\\navezinha.png", 1)
        nave.x = jogo.width/2 - nave.width/2
        nave.y = jogo.height - 100
        vel_nave = 120 + (30/dificuldade)

        # tiro
        tiro = Sprite("images\\tirinho.png", 1)
        tiro.x = nave.x + nave.width/2 - tiro.width/2 + 1
        tiro.y = nave.y - tiro.height
        tiros = []
        vel_tiro = 100 + 50/dificuldade
        crono = 0

        # matriz de monstros

        monstro = Sprite("images\\monstrinho.png", 1)
        linhas = dificuldade + 1
        colunas = dificuldade + 1
        monstrinhos = []

        for i in range(linhas):
            lin = []
            for j in range(colunas):
                lin.append(Sprite("images\\monstrinho.png", 1))
            monstrinhos.append(lin)
        
        for m in range(linhas):
                for n in range(colunas):
                    monstrinhos[m][n].x = monstro.width*n + monstro.width/2*n
                    monstrinhos[m][n].y = monstro.height*m + monstro.height/2*m
        
        vel_monstros = 100

        # caixa de monstros
        up = 0
        down = monstrinhos[linhas-1][colunas-1].y + monstrinhos[linhas-1][colunas-1].height
        left = 0
        right = monstrinhos[linhas-1][colunas-1].x + monstrinhos[linhas-1][colunas-1].width
        

        while (not ganhou and not perdeu):
            jogo.update()
            jogo.set_background_color((32, 37, 71))
            crono += jogo.delta_time()

            if teclado.key_pressed("esc"):
                break
            
            # pontuação
            crono_geral += jogo.delta_time()
            crono_ate_um += jogo.delta_time()
            if crono_ate_um >= 1:
                crono_ate_um = 0
                pontos -= 1

            # efetuar disparos
            if teclado.key_pressed("SPACE") and crono >= dificuldade/3:
                tir = [Sprite("images\\tirinho.png"),
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

            # movimentos monstros
            collided_right = False
            collided_left = False
            for p in range(linhas):
                for q in range(colunas):
                    monstrinhos[p][q].x += vel_monstros * jogo.delta_time()
                    if monstrinhos[p][q].x + monstro.width > jogo.width and vel_monstros > 0 and monstrinhos[p][q].collided_perfect(background_jogo):
                        collided_right = True
                        vel_monstros *= -1
                        for a in range(linhas):
                            for b in range(colunas):
                                monstrinhos[a][b].y += 20
                    if monstrinhos[p][q].x < 0 and vel_monstros < 0 and monstrinhos[p][q].collided_perfect(background_jogo):
                        vel_monstros *= -1
                        for c in range(linhas):
                            for d in range(colunas):
                                monstrinhos[c][d].y += 20
            
            # update caixa de monstros
            for p in range(linhas):
                for q in range(colunas):
                    if monstrinhos[p][q].y < up and monstrinhos[p][q].collided_perfect(background_jogo):
                        up = monstrinhos[p][q].y
                    if monstrinhos[p][q].y + monstrinhos[p][q].height > down and monstrinhos[p][q].collided_perfect(background_jogo):
                        down = monstrinhos[p][q].y + monstrinhos[p][q].height
                    if monstrinhos[p][q].x < left and monstrinhos[p][q].collided_perfect(background_jogo):
                        left = monstrinhos[p][q].x
                    if monstrinhos[p][q].x + monstrinhos[p][q].width > right and monstrinhos[p][q].collided_perfect(background_jogo):
                        right = monstrinhos[p][q].x + monstrinhos[p][q].width
            
            # ganhar
            monsters_alive = False
            for m in range(linhas):
                for n in range(colunas):
                    if monstrinhos[m][n].collided_perfect(background_jogo):
                        monsters_alive = True
                        break       
                if monsters_alive:
                    break
            
            if not monsters_alive:
                ganhou = True

            # desenho
            background_jogo.draw()
                # tiros
            for t in tiros:
                tiro = t[0]
                tiro.x = t[1]
                tiro.y = t[2]
                tiro.draw()
                if left < t[0].x < right and up < t[0].y < down: 
                    for m in range(linhas):
                        for n in range(colunas):
                            if monstrinhos[linhas-m-1][n].collided_perfect(t[0]):
                                aux = monstrinhos[linhas - m-1][n].x
                                auy = monstrinhos[linhas - m-1][n].y
                                monstrinhos[linhas - m-1][n] = Sprite("images\\vazio.png")
                                monstrinhos[linhas - m-1][n].x = aux
                                monstrinhos[linhas - m-1][n].y = auy
                                tiros.remove(t)
                                pontos += 500 - crono_geral
            # nave
            nave.draw()

            # monstros
            for u in range(linhas):
                for v in range(colunas):
                    if monstrinhos[u][v].collided_perfect(background_jogo) and monstrinhos[u][v].collided_perfect(nave):
                        perdeu = True
                    monstrinhos[u][v].draw()

            # pontos
            jogo.draw_text(f"Pontos: {pontos:.0f}", 10, 10, size = 17, color=(255, 255, 255))
