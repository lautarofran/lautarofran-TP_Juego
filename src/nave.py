import pygame
from laser import Laser
from config import ANCHO,ALTO
from animaciones import get_animaciones_disparo

class Nave(pygame.sprite.Sprite):
    def __init__(self, animaciones:str,midBottom: tuple):
        super().__init__()

        self.animacion = animaciones
        self.indice = 2
        self.image = self.animacion[self.indice]

        self.rect = self.image.get_rect()
        self.rect.midbottom = midBottom 

        self.velocidad_x = 0
        self.velocidad_y = 0
        
        self.tiempo_antirrebote = 0
        self.tiempo_maximo = 100
    
    def update(self):
        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y

        if self.velocidad_x < 0:
            self.indice = 1 
        elif self.velocidad_x > 0:
            self.indice = 2 
        else:
            self.indice = 0 

        if self.rect.left <= 0:
            self.rect.left = 0
        elif self.rect.right >= ANCHO:
            self.rect.right = ANCHO

        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= ALTO:
            self.rect.bottom = ALTO

        self.image = self.animacion[self.indice]

        
    def disparar(self,sonido,speed,sprites,lasers):
        laser = Laser(get_animaciones_disparo(),self.rect.midtop,speed)
        sonido.play() 
        sprites.add(laser)
        lasers.add(laser)