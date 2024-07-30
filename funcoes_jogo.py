import sys
import pygame
from bala import Bala

def ouvir_eventos(opc, tela, nave, balas):
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                ouvir_keydown(event, opc, tela, nave, balas)
            elif event.type == pygame.KEYUP:
                ouvir_keyup(event, nave)

def ouvir_keydown(event, opc, tela, nave, balas):
    if event.key == pygame.K_RIGHT:
        nave.movendoDireita = True
    if event.key == pygame.K_LEFT:
        nave.movendoEsquerda = True
    if event.key == pygame.K_SPACE:
        nova_bala = Bala(opc, tela, nave)
        balas.add(nova_bala)
    

def ouvir_keyup(event, nave):
    if event.key == pygame.K_RIGHT:
        nave.movendoDireita = False
    if event.key == pygame.K_LEFT:
        nave.movendoEsquerda = False

def update_tela(opc, tela, nave, balas):
    tela.fill(opc.cor_fundo)
    nave.blitme()

    for bala in balas.sprites():
        bala.desenha_bala()
        
    pygame.display.flip()