import pygame
from animaciones import get_animaciones_asteroide

class Asteroide(pygame.sprite.Sprite):
    def __init__(self, centro: tuple, velocidad: float, movimiento_lateral):
        super().__init__()
        self.animaciones = get_animaciones_asteroide()        
        self.indice = 0
        self.timer_animaciones = 0
        self.image = self.animaciones[self.indice]           
        self.rect = self.image.get_rect() #guarda el rect de la imagen
        self.rect.midbottom = centro         
        self.velocidad_y = velocidad
        self.movimiento_lateral = movimiento_lateral

    def update(self):
        
        self.rect.y += self.velocidad_y
        self.rect.x += self.velocidad_y * self.movimiento_lateral
        
        pantalla_ancho = pygame.display.get_surface().get_width()
        if self.rect.right >= pantalla_ancho or self.rect.left <= 0:
            self.movimiento_lateral *= -1  # Invierte la dirección del movimiento lateral
        self.rect.y += self.velocidad_y
        self.rect.x += self.velocidad_y * self.movimiento_lateral
        
        
        self.timer_animaciones += 1 
        if self.indice >= 9:
            self.indice = 0
        elif self.timer_animaciones == 7:
            self.indice += 1
            self.timer_animaciones = 0
        
        self.image = self.animaciones[self.indice]