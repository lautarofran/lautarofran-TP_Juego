import pygame
from animaciones import get_animaciones_corazones


class Power_Up(pygame.sprite.Sprite):
    def __init__(self,center:tuple,speed_powerup:float):
        super().__init__()
        
        self.animaciones = get_animaciones_corazones()
        self.indice = 0
        self.timer_animaciones = 0
        self.image = self.animaciones[self.indice]
        
        self.rect = self.image.get_rect()
        self.rect.midbottom = center
              
        self.velocidad_y = speed_powerup
    
    def update(self):
        self.rect.y += self.velocidad_y 
        
        self.timer_animaciones += 1
        if self.indice >= 10:
            self.indice = 0
        elif self.timer_animaciones == 7:    
            self.indice += 1
            self.timer_animaciones = 0
            
        self.image = self.animaciones[self.indice]