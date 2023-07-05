import pygame
from animaciones import get_animaciones_explosion


class Explosion(pygame.sprite.Sprite):
    def __init__(self,center:tuple):
        super().__init__()
        
        self.animaciones = get_animaciones_explosion()
        self.indice = 0
        self.timer_animaciones = 0
        self.image = self.animaciones[self.indice]
        
        self.rect = self.image.get_rect()
        self.rect.midtop = center
              
    def update(self):
        
        self.timer_animaciones += 1
        if self.indice >= 5:
            self.indice = 0
        elif self.timer_animaciones == 5:    
            self.indice += 1
            self.timer_animaciones = 0
            
        self.image = self.animaciones[self.indice]
        
        match(self.indice):
            case 5:
                self.kill()