import pygame
import sys
import random

from config import *
from funciones import *
from nave import Personaje
from juego import Juego




while not KABOOM.jugando:
            pygame.init()
            
            screen = pygame.display.set_mode(SCREEN)
            color_claro = (82,172,222)
            color_oscuro = (100,109,170)
            fuente_menu = pygame.font.Font('src\\fonts\\fuente2.ttf',18)
            fuente_titulo = pygame.font.Font('src\\fonts\\fuente2.ttf',70)            
            titulo = fuente_titulo.render("KABOOM!", True, CUSTOM2)
            texto_comenzar = fuente_menu.render('Comenzar' , True , BLANCO)
            texto_instrucciones = fuente_menu.render('Instrucciones' , True , BLANCO)
            texto_salir = fuente_menu.render('Salir' , True , BLANCO)            
            musica_menu = pygame.mixer.Sound("src\sounds\sonido_menu.mp3")
            musica_menu.set_volume(0.04)
            efecto_sonido_seleccion = pygame.mixer.Sound("src\sounds\sonido_boton_menu.mp3")  
            fondo_menu =  pygame.image.load("src\images\\fondo.jpg")
            fondo_menu = pygame.transform.scale(fondo_menu,(ANCHO,ALTO))
            while not KABOOM.jugando:
                musica_menu.play()                
                screen.blit(fondo_menu,(ORIGEN))                        
                for evento in pygame.event.get():                    
                    if evento.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()                    
                    if evento.type == pygame.KEYDOWN:
                        if evento.key == pygame.K_ESCAPE:
                            pygame.quit()
                            sys.exit()                
                mouse = pygame.mouse.get_pos() 
                rect_ancho = 110
                rect_ancho_instrucciones = 150
                rect_alto = 40
                posicion_x_comenzar = ANCHO/2 - 55
                posicion_y_comenzar = ALTO/2
                posicion_x_instrucciones = ANCHO/2 - 55
                posicion_y_instrucciones = ALTO/2 + 50
                posicion_x_salir = ANCHO/2 - 55
                posicion_y_salir = ALTO/2 + 100                
                if posicion_x_comenzar <= mouse[0] <= posicion_x_comenzar + rect_ancho and posicion_y_comenzar <= mouse[1] <= posicion_y_comenzar + rect_alto:
                    pygame.draw.rect(screen, color_claro, [posicion_x_comenzar, posicion_y_comenzar, rect_ancho, rect_alto])
                else:
                    pygame.draw.rect(screen, color_oscuro, [posicion_x_comenzar, posicion_y_comenzar, rect_ancho, rect_alto])

                if posicion_x_instrucciones <= mouse[0] <= posicion_x_instrucciones + rect_ancho_instrucciones and posicion_y_instrucciones <= mouse[1] <= posicion_y_instrucciones + rect_alto:
                    pygame.draw.rect(screen, color_claro, [posicion_x_instrucciones-20, posicion_y_instrucciones, rect_ancho_instrucciones, rect_alto])
                else:
                    pygame.draw.rect(screen, color_oscuro, [posicion_x_instrucciones-20, posicion_y_instrucciones, rect_ancho_instrucciones, rect_alto])

                if posicion_x_salir <= mouse[0] <= posicion_x_salir + rect_ancho and posicion_y_salir <= mouse[1] <= posicion_y_salir + rect_alto:
                    pygame.draw.rect(screen, color_claro, [posicion_x_salir, posicion_y_salir, rect_ancho, rect_alto])
                else:
                    pygame.draw.rect(screen, color_oscuro, [posicion_x_salir, posicion_y_salir, rect_ancho, rect_alto])
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if posicion_x_comenzar <= mouse[0] <= posicion_x_comenzar + rect_ancho and posicion_y_comenzar <= mouse[1] <= posicion_y_comenzar + rect_alto:
                        musica_menu.stop()
                        efecto_sonido_seleccion.play()
                        pygame.time.delay(300)
                        # juego.finalizado = True
                        KABOOM.comenzar()
                    elif posicion_x_instrucciones <= mouse[0] <= posicion_x_instrucciones + rect_ancho and posicion_y_instrucciones <= mouse[1] <= posicion_y_instrucciones + rect_alto:
                        KABOOM.mostrar_instrucciones()
                    elif posicion_x_salir <= mouse[0] <= posicion_x_salir + rect_ancho and posicion_y_salir <= mouse[1] <= posicion_y_salir + rect_alto:
                        pygame.quit()
                        sys.exit()
                screen.blit(titulo ,(ANCHO//2-170,100))            
                screen.blit(texto_comenzar ,(250, 355))
                screen.blit(texto_instrucciones,(233, 404))
                screen.blit(texto_salir,(265, 454))
                pygame.display.flip()