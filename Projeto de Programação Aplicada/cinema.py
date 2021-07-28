import smtplib
from typing import DefaultDict
import pygame as pg
from sys import exit
from pygame.image import load
from pygame.locals import *

email_de_destino = input('Digite seu email para que posssamos enviar as cadeiras selecionadas: ')

pg.init()

#Valores que serão usados como coordenada do eixo X na exibição das cadeiras na tela      
posicoes_x= [20,40,60,80,100,120,240,260,280,300]

#Variáveis de texto, tela, fonte,...
tela = pg.display.set_mode((500,250))
tela.fill((250,250,250))
fonte = pg.font.SysFont('Times New Roman', 15, True, False)
fonte_2 = pg.font.SysFont('arial', 14, True, False)

vermelho = pg.image.load('vermelho.png')
azul = pg.image.load('azul.jpg')
cadeirante_azul = pg.image.load('cadeiranteazul.png')
cadeirante_vermelho = pg.image.load('cadeirantevermelho.png')

a = fonte_2.render('A',False,(0,0,0))
b = fonte_2.render('B',False,(0,0,0))
c = fonte_2.render('C',False,(0,0,0))
d = fonte_2.render('D',False,(0,0,0))
e = fonte_2.render('E',False,(0,0,0))
finalizar = fonte_2.render('FINALIZAR SELEÇÃO',True,(255,255,255))
disponivel = fonte.render('Disponível',False,(0,0,0))
indisponivel = fonte.render('Indisponível',False,(0,0,0))
telao = fonte_2.render('TELA', True, (255,255,255))
#lista onde seram guardados as posições das cadeiras selecionadas.
ticket = []
#Variáveis das imagens que aparecem na tela(circulos azuis e vermelhos e )
a1 = tela.blit(azul,(posicoes_x[0],10))
a2 = tela.blit(azul,(posicoes_x[1],10))
a3 = tela.blit(azul,(posicoes_x[2],10))
a4 = tela.blit(azul,(posicoes_x[3],10))
a5 = tela.blit(azul,(posicoes_x[4],10))
a6 = tela.blit(azul,(posicoes_x[5],10))
a7 = tela.blit(azul,(posicoes_x[6],10))
a8 = tela.blit(azul,(posicoes_x[7],10))
a9 = tela.blit(azul,(posicoes_x[8],10))

b1 = tela.blit(azul,(posicoes_x[0],40))
b2 = tela.blit(azul,(posicoes_x[1],40))
b3 = tela.blit(azul,(posicoes_x[2],40))
b4 = tela.blit(azul,(posicoes_x[3],40))
b5 = tela.blit(azul,(posicoes_x[4],40))
b6 = tela.blit(azul,(posicoes_x[5],40))
b7 = tela.blit(azul,(posicoes_x[6],40))
b8 = tela.blit(azul,(posicoes_x[7],40))
b9 = tela.blit(azul,(posicoes_x[8],40))

c1 = tela.blit(azul,(posicoes_x[0],70))
c2 = tela.blit(azul,(posicoes_x[1],70))
c3 = tela.blit(azul,(posicoes_x[2],70))
c4 = tela.blit(azul,(posicoes_x[3],70))
c5 = tela.blit(azul,(posicoes_x[4],70))
c6 = tela.blit(azul,(posicoes_x[5],70))
c7 = tela.blit(azul,(posicoes_x[6],70))
c8 = tela.blit(azul,(posicoes_x[7],70))
c9 = tela.blit(azul,(posicoes_x[8],70))

d1 = tela.blit(azul,(posicoes_x[0],100))
d2 = tela.blit(azul,(posicoes_x[1],100))
d3 = tela.blit(azul,(posicoes_x[2],100))
d4 = tela.blit(azul,(posicoes_x[3],100))
d5 = tela.blit(azul,(posicoes_x[4],100))
d6 = tela.blit(azul,(posicoes_x[5],100))
d7 = tela.blit(azul,(posicoes_x[6],100))
d8 = tela.blit(azul,(posicoes_x[7],100))
d9 = tela.blit(azul,(posicoes_x[8],100))

e1 = tela.blit(cadeirante_azul,(posicoes_x[0],160))
e2 = tela.blit(cadeirante_azul,(posicoes_x[3],160))
e3 = tela.blit(cadeirante_azul,(posicoes_x[4],160))
e4 = tela.blit(cadeirante_azul,(posicoes_x[6],160))
e5 = tela.blit(cadeirante_azul,(posicoes_x[7],160))
reservadas = [e1,e2,e3,e4,e5]

#Função que é chamada quando é escolhida uma cadeira
def escolhendo_cadeira(var_imagem,pos_x_imagem,pos_y_imagem,num_cadeira):
    posicao_mouse = pg.mouse.get_pos()
    #Condição que muda a cor da cadeira que está na posição atual do cursor do mouse
    if var_imagem.collidepoint(posicao_mouse) and var_imagem not in reservadas:
        var_imagem = tela.blit(vermelho, (pos_x_imagem,pos_y_imagem))
    #Condições que adicionam na lista ticket a posição das cadeiras escolhidas
        if pos_y_imagem == 10:
            ticket.append(f'A{num_cadeira}')
        elif pos_y_imagem == 40:
            ticket.append(f'B{num_cadeira}')
        elif pos_y_imagem == 70:
            ticket.append(f'C{num_cadeira}')
        elif pos_y_imagem == 100:
            ticket.append(f'D{num_cadeira}')
    #Condiçãõ que executa caso a cadeira selecionada esteja na lista de cadeiras reservadas
    if var_imagem.collidepoint(posicao_mouse) and var_imagem in reservadas:  
        var_imagem = tela.blit(cadeirante_vermelho,(pos_x_imagem,pos_y_imagem))
        if pos_y_imagem == 160:
            ticket.append(f'E{num_cadeira}')

def descelecionando(var_imagem,pos_x_imagem,pos_y_imagem,num_cadeira):
    posicao_mouse = pg.mouse.get_pos()
    #Condição que muda a cor da cadeira que está na posição atual do cursor do mouse
    if var_imagem.collidepoint(posicao_mouse) and var_imagem not in reservadas:
        var_imagem = tela.blit(azul, (pos_x_imagem,pos_y_imagem))
    #Condições que adicionam na lista ticket a posição das cadeiras escolhidas
        if pos_y_imagem == 10:
            indice_a = ticket.index(f'A{num_cadeira}')
            del ticket[indice_a]
        elif pos_y_imagem == 40:
           indice_b = ticket.index(f'B{num_cadeira}')
           del ticket[indice_b]
        elif pos_y_imagem == 70:
            indice_c = ticket.index(f'C{num_cadeira}')
            del ticket[indice_c]
        elif pos_y_imagem == 100:
            indice_d = ticket.index(f'D{num_cadeira}')
            del ticket[indice_d]
    #Condiçãõ que executa caso a cadeira selecionada esteja na lista de cadeiras reservadas
    if var_imagem.collidepoint(posicao_mouse) and var_imagem in reservadas:  
        var_imagem = tela.blit(cadeirante_azul,(pos_x_imagem,pos_y_imagem))
        if pos_y_imagem == 160:
            indice_e = ticket.index(f'E{num_cadeira}')
            del ticket[indice_e]

#Estrutura de repetição responsável por executar o codigo e pegar as entradas do mouse
while True:
    for evento in pg.event.get():
        #condição que fecha a tela caso o 'X' da tela seja apertado
        if evento.type == QUIT:
            #print(ticket)
            exit()
        #condição que envia o email com as cadeiras reservadas
        if evento.type == MOUSEBUTTONUP:
            posicao_mouse = pg.mouse.get_pos()
            if rect_botao_finalizar.collidepoint(posicao_mouse):
                smtpObj = smtplib.SMTP("smtp.gmail.com", 587)
                print(type(smtpObj))

                res_ehlo = smtpObj.ehlo()
                print(res_ehlo)

                res_starttls = smtpObj.starttls()
                print(res_starttls)

                res_login = smtpObj.login("ianfelipihonet@gmail.com", "matematica16")
                print(res_login)

                smtpObj.sendmail('ianfelipinhonet@gmail.com', email_de_destino, f"Subject: --Ingresso--\nCadeiras reservadas --> {ticket} ")

                smtpObj.quit()
        #condição que muda a cor da cadeira caso selecionada
        if evento.type == MOUSEBUTTONDOWN:
            if evento.button == 1:
                escolhendo_cadeira(a1,posicoes_x[0],10,1)
                escolhendo_cadeira(a2,posicoes_x[1],10,2)
                escolhendo_cadeira(a3,posicoes_x[2],10,3)
                escolhendo_cadeira(a4,posicoes_x[3],10,4)
                escolhendo_cadeira(a5,posicoes_x[4],10,5)
                escolhendo_cadeira(a6,posicoes_x[5],10,6)
                escolhendo_cadeira(a7,posicoes_x[6],10,7)
                escolhendo_cadeira(a8,posicoes_x[7],10,8)
                escolhendo_cadeira(a9,posicoes_x[8],10,9)

                escolhendo_cadeira(b1,posicoes_x[0],40,1)
                escolhendo_cadeira(b2,posicoes_x[1],40,2)
                escolhendo_cadeira(b3,posicoes_x[2],40,3)
                escolhendo_cadeira(b4,posicoes_x[3],40,4)
                escolhendo_cadeira(b5,posicoes_x[4],40,5)
                escolhendo_cadeira(b6,posicoes_x[5],40,6)
                escolhendo_cadeira(b7,posicoes_x[6],40,7)
                escolhendo_cadeira(b8,posicoes_x[7],40,8)
                escolhendo_cadeira(b9,posicoes_x[8],40,9)

                escolhendo_cadeira(c1,posicoes_x[0],70,1)
                escolhendo_cadeira(c2,posicoes_x[1],70,2)
                escolhendo_cadeira(c3,posicoes_x[2],70,3)
                escolhendo_cadeira(c4,posicoes_x[3],70,4)
                escolhendo_cadeira(c5,posicoes_x[4],70,5)
                escolhendo_cadeira(c6,posicoes_x[5],70,6)
                escolhendo_cadeira(c7,posicoes_x[6],70,7)
                escolhendo_cadeira(c8,posicoes_x[7],70,8)
                escolhendo_cadeira(c9,posicoes_x[8],70,9)

                escolhendo_cadeira(d1,posicoes_x[0],100,1)
                escolhendo_cadeira(d2,posicoes_x[1],100,2)
                escolhendo_cadeira(d3,posicoes_x[2],100,3)
                escolhendo_cadeira(d4,posicoes_x[3],100,4)
                escolhendo_cadeira(d5,posicoes_x[4],100,5)
                escolhendo_cadeira(d6,posicoes_x[5],100,6)
                escolhendo_cadeira(d7,posicoes_x[6],100,7)
                escolhendo_cadeira(d8,posicoes_x[7],100,8)
                escolhendo_cadeira(d9,posicoes_x[8],100,9)

                escolhendo_cadeira(e1,posicoes_x[0],160,1)
                escolhendo_cadeira(e2,posicoes_x[3],160,2)
                escolhendo_cadeira(e3,posicoes_x[4],160,3)
                escolhendo_cadeira(e4,posicoes_x[6],160,4)
                escolhendo_cadeira(e5,posicoes_x[7],160,5)

            if evento.button == 3:
                descelecionando(a1,posicoes_x[0],10,1)
                descelecionando(a2,posicoes_x[1],10,2)
                descelecionando(a3,posicoes_x[2],10,3)
                descelecionando(a4,posicoes_x[3],10,4)
                descelecionando(a5,posicoes_x[4],10,5)
                descelecionando(a6,posicoes_x[5],10,6)
                descelecionando(a7,posicoes_x[6],10,7)
                descelecionando(a8,posicoes_x[7],10,8)
                descelecionando(a9,posicoes_x[8],10,9)

                descelecionando(b1,posicoes_x[0],40,1)
                descelecionando(b2,posicoes_x[1],40,2)
                descelecionando(b3,posicoes_x[2],40,3) 
                descelecionando(b4,posicoes_x[3],40,4)
                descelecionando(b5,posicoes_x[4],40,5)
                descelecionando(b6,posicoes_x[5],40,6)
                descelecionando(b7,posicoes_x[6],40,7)
                descelecionando(b8,posicoes_x[7],40,8)
                descelecionando(b9,posicoes_x[8],40,9)

                descelecionando(c1,posicoes_x[0],70,1)
                descelecionando(c2,posicoes_x[1],70,2)
                descelecionando(c3,posicoes_x[2],70,3)
                descelecionando(c4,posicoes_x[3],70,4)
                descelecionando(c5,posicoes_x[4],70,5)
                descelecionando(c6,posicoes_x[5],70,6)
                descelecionando(c7,posicoes_x[6],70,7)
                descelecionando(c8,posicoes_x[7],70,8)
                descelecionando(c9,posicoes_x[8],70,9)

                descelecionando(d1,posicoes_x[0],100,1)
                descelecionando(d2,posicoes_x[1],100,2)
                descelecionando(d3,posicoes_x[2],100,3)
                descelecionando(d4,posicoes_x[3],100,4)
                descelecionando(d5,posicoes_x[4],100,5)
                descelecionando(d6,posicoes_x[5],100,6)
                descelecionando(d7,posicoes_x[6],100,7)
                descelecionando(d8,posicoes_x[7],100,8)
                descelecionando(d9,posicoes_x[8],100,9)

                descelecionando(e1,posicoes_x[0],160,1)
                descelecionando(e2,posicoes_x[3],160,2)
                descelecionando(e3,posicoes_x[4],160,3)
                descelecionando(e4,posicoes_x[6],160,4)
                descelecionando(e5,posicoes_x[7],160,5)
    #Linhas do código responsaveis por exibir a letra da fileira, a descrição das cadeiras(disponivel ou indisponivel),
    #o retângulo da tela e do botão finalizar.
    rect_tela = pg.draw.rect(tela, (119,136,153), (15, 220, 287,20))
    tela.blit(telao, (147,220))
    rect_botao_finalizar = pg.draw.rect(tela, (25,25,112), (337,200, 143,40))
    tela.blit(a,(5,9)),tela.blit(a,(305,9))
    tela.blit(b,(5,40)), tela.blit(b,(305,40))
    tela.blit(c,(5,70)),tela.blit(c,(305,70))
    tela.blit(d,(5,100)),tela.blit(d,(305,100))
    tela.blit(e,(5,160)),tela.blit(e,(305,160))
    tela.blit(finalizar,(350,210))
    #tela.blit(telao,(150,260))
    tela.blit(azul,(340,11)),tela.blit(cadeirante_azul,(360,11)),tela.blit(disponivel,(380,11))
    tela.blit(vermelho,(340,40)),tela.blit(cadeirante_vermelho,(360,40)),tela.blit(indisponivel,(380,40))
    pg.display.flip()
