import pygame

class Laser(pygame.sprite.Sprite):
    def __init__(self,path_disparo, midBottom: tuple,speed,):
        super().__init__() #llamar al constructor 
        #siempre un sprite tiene que tener una image, y un self.fact
        #y tenemos que redefinir un evento update
        self.image = path_disparo[2] 

        self.rect = self.image.get_rect() #guarda el rect de la imagen
        self.rect.midbottom = midBottom 
        
        self.velocidad_y = speed

    def update(self):
        self.rect.y -= self.velocidad_y