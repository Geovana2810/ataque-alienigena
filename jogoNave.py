import sys
import pygame

from config import Opcoes
from nave import Nave
from bala import Bala

import funcoes_jogo as FJ
from pygame.sprite import Group


def rodar_jogo():
    pygame.init()

    #Instancias
    opc = Opcoes()

    tela = pygame.display.set_mode((opc.tela_largura, opc.tela_altura))
    pygame.display.set_caption("Invasão Alienigena")

    balas = Group()

    nave = Nave(tela, opc)

    while True:
        FJ.ouvir_eventos(opc, tela, nave, balas)
        FJ.update_tela(opc, tela, nave, balas)
        nave.update()
        balas.update()
        
rodar_jogo()

