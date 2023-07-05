import pygame
from config import *


pygame.init()
pantalla = pygame.display.set_mode(SCREEN)

lista_animaciones_nave = [
    pygame.transform.scale(pygame.image.load("src\\animations\\nave\\nave_1.png").convert_alpha(),(SIZE_NAVE)),
    pygame.transform.scale(pygame.image.load("src\\animations\\nave\\nave_izq.png").convert_alpha(),(SIZE_NAVE)),
    pygame.transform.scale(pygame.image.load("src\\animations\\nave\\nave_der.png").convert_alpha(),(SIZE_NAVE))]

lista_animacion_barra_de_vida = [
    pygame.transform.scale(pygame.image.load("src\\animations\\vida\\vida_0.png").convert_alpha(),(SIZE_VIDA)),
    pygame.transform.scale(pygame.image.load("src\\animations\\vida\\vida_1.jpg").convert_alpha(),(SIZE_VIDA)),
    pygame.transform.scale(pygame.image.load("src\\animations\\vida\\vida_2.jpg").convert_alpha(),(SIZE_VIDA)),
    pygame.transform.scale(pygame.image.load("src\\animations\\vida\\vida_3.jpg").convert_alpha(),(SIZE_VIDA)) ]

def get_animaciones_asteroide():
    lista_animacion_asteroide = [
        pygame.transform.scale(pygame.image.load("src\\animations\\asteroide\spin-00.png").convert_alpha(),(SIZE_ASTEROIDE)),
        pygame.transform.scale(pygame.image.load("src\\animations\\asteroide\spin-01.png").convert_alpha(),(SIZE_ASTEROIDE)),
        pygame.transform.scale(pygame.image.load("src\\animations\\asteroide\spin-02.png").convert_alpha(),(SIZE_ASTEROIDE)),
        pygame.transform.scale(pygame.image.load("src\\animations\\asteroide\spin-03.png").convert_alpha(),(SIZE_ASTEROIDE)),
        pygame.transform.scale(pygame.image.load("src\\animations\\asteroide\spin-04.png").convert_alpha(),(SIZE_ASTEROIDE)),
        pygame.transform.scale(pygame.image.load("src\\animations\\asteroide\spin-05.png").convert_alpha(),(SIZE_ASTEROIDE)),
        pygame.transform.scale(pygame.image.load("src\\animations\\asteroide\spin-06.png").convert_alpha(),(SIZE_ASTEROIDE)),
        pygame.transform.scale(pygame.image.load("src\\animations\\asteroide\spin-07.png").convert_alpha(),(SIZE_ASTEROIDE)),
        pygame.transform.scale(pygame.image.load("src\\animations\\asteroide\spin-08.png").convert_alpha(),(SIZE_ASTEROIDE)),
        pygame.transform.scale(pygame.image.load("src\\animations\\asteroide\spin-09.png").convert_alpha(),(SIZE_ASTEROIDE)),]
    
    return lista_animacion_asteroide                            

def get_animaciones_corazones():                             
    lista_animacion_power_up_corazon = [
        pygame.transform.scale(pygame.image.load("src\\animations\power_up\corazon_1.png").convert_alpha(),(SIZE_POWER_UP)),
        pygame.transform.scale(pygame.image.load("src\\animations\power_up\corazon_2.png").convert_alpha(),(SIZE_POWER_UP)),
        pygame.transform.scale(pygame.image.load("src\\animations\power_up\corazon_3.png").convert_alpha(),(SIZE_POWER_UP)),
        pygame.transform.scale(pygame.image.load("src\\animations\power_up\corazon_4.png").convert_alpha(),(SIZE_POWER_UP)),
        pygame.transform.scale(pygame.image.load("src\\animations\power_up\corazon_5.png").convert_alpha(),(SIZE_POWER_UP)),
        pygame.transform.scale(pygame.image.load("src\\animations\power_up\corazon_6.png").convert_alpha(),(SIZE_POWER_UP)),
        pygame.transform.scale(pygame.image.load("src\\animations\power_up\corazon_7.png").convert_alpha(),(SIZE_POWER_UP)),
        pygame.transform.scale(pygame.image.load("src\\animations\power_up\corazon_8.png").convert_alpha(),(SIZE_POWER_UP)),
        pygame.transform.scale(pygame.image.load("src\\animations\power_up\corazon_9.png").convert_alpha(),(SIZE_POWER_UP)),
        pygame.transform.scale(pygame.image.load("src\\animations\power_up\corazon_10.png").convert_alpha(),(SIZE_POWER_UP)),
        pygame.transform.scale(pygame.image.load("src\\animations\power_up\corazon_11.png").convert_alpha(),(SIZE_POWER_UP)),        ]
                            
    return lista_animacion_power_up_corazon

def get_animaciones_explosion():
    lista_animaciones_explosion = [
        pygame.transform.scale((pygame.image.load("src\\animations\explosion\explosion(0).png").convert_alpha()),(SIZE_EXPLOSION)),
        pygame.transform.scale((pygame.image.load("src\\animations\explosion\explosion(1).png").convert_alpha()),(SIZE_EXPLOSION)),
        pygame.transform.scale((pygame.image.load("src\\animations\explosion\explosion(2).png").convert_alpha()),(SIZE_EXPLOSION)),
        pygame.transform.scale((pygame.image.load("src\\animations\explosion\explosion(3).png").convert_alpha()),(SIZE_EXPLOSION)),
        pygame.transform.scale((pygame.image.load("src\\animations\explosion\explosion(4).png").convert_alpha()),(SIZE_EXPLOSION)),
        pygame.transform.scale((pygame.image.load("src\\animations\explosion\explosion(5).png").convert_alpha()),(SIZE_EXPLOSION)),
        pygame.transform.scale((pygame.image.load("src\\animations\explosion\explosion(6).png").convert_alpha()),(SIZE_EXPLOSION)),
        pygame.transform.scale((pygame.image.load("src\\animations\explosion\explosion(7).png").convert_alpha()),(SIZE_EXPLOSION)),
        pygame.transform.scale((pygame.image.load("src\\animations\explosion\explosion(8).png").convert_alpha()),(SIZE_EXPLOSION)),
        pygame.transform.scale((pygame.image.load("src\\animations\explosion\explosion(9).png").convert_alpha()),(SIZE_EXPLOSION)),
        pygame.transform.scale((pygame.image.load("src\\animations\explosion\explosion(10).png").convert_alpha()),(SIZE_EXPLOSION)),
        ]
    return lista_animaciones_explosion

def get_animaciones_disparo():
    lista_animaciones_disparo = [
        pygame.transform.scale((pygame.image.load("src\\animations\disparo\disparo.png").convert_alpha()),(SIZE_LASER)),
        pygame.transform.scale((pygame.image.load("src\\animations\disparo\disparo2.png").convert_alpha()),(SIZE_LASER)),
        pygame.transform.scale((pygame.image.load("src\\animations\disparo\disparo3.png").convert_alpha()),(SIZE_LASER))]
    
    return lista_animaciones_disparo

def get_animaciones_disparo_penetrador():
    lista_animaciones_disparo = [
        pygame.transform.scale((pygame.image.load("src\images\laser_penetrador.png").convert_alpha()),(SIZE_LASER))]
    
    return lista_animaciones_disparo