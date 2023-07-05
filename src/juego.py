import pygame
import sys
import random

from config import *
from nave import Nave
from asteroide import Asteroide
from animaciones import *
from explosion import Explosion
from power_up import Power_Up

class Juego:
    def __init__(self) -> None:
        pygame.init()
        
        self.speed_asteroide = 1
        
        self.volumen_actual = 0
        
        if self.volumen_actual == 0:
            self.indice_imagen = 0
        if self.volumen_actual == 0.3:
            self.indice_imagen = 1
        elif self.volumen_actual == 0.6:
            self.indice_imagen = 2
        elif self.volumen_actual == 0.9:
            self.indice_imagen = 3
            
        self.imagenes_volumen = [
            pygame.transform.scale(pygame.image.load("src\images\\volumen_0.png").convert_alpha(), SIZE_VOLUMEN),
            pygame.transform.scale(pygame.image.load("src\images\\volumen_1.png").convert_alpha(), SIZE_VOLUMEN),
            pygame.transform.scale(pygame.image.load("src\images\\volumen_2.png").convert_alpha(), SIZE_VOLUMEN),
            pygame.transform.scale(pygame.image.load("src\images\\volumen_3.png").convert_alpha(), SIZE_VOLUMEN)]        
        
        self.pantalla = pygame.display.set_mode(SCREEN)
        self.reloj = pygame.time.Clock()
        self.sonido_laser = pygame.mixer.Sound("src\sounds\sonido_laser_penetrador.mp3")
        
        
        self.nivel = 1
        self.lista_score = []
        self.SCORE = 0 
        self.vida = 3
        self.cronometro = 0

        self.juego_terminado = False
        self.fin_juego = False
        self.inicio = True
        self.finalizado = True
        self.jugando = False
        self.juego_pausa = False
        self.menu_pausa_activo = False
        self.hay_power_up = False
        
        pygame.display.set_caption("Kaboom!")
        pygame.display.set_icon(pygame.transform.scale(pygame.image.load("src\images\\nave.png").convert_alpha(),(SIZE_NAVE)))
        
        self.fondo = pygame.image.load("src\images\\fondo.jpg").convert()
        self.fondo = pygame.transform.scale(self.fondo, SCREEN)
        self.fuente = pygame.font.Font("src\\fonts\\fuente2.ttf",30)
        self.font = pygame.font.match_font(FONT)
        self.musica_juego = pygame.mixer.Sound("src\sounds\sonido_juego.mp3")
        self.sonido_game_over = pygame.mixer.Sound("src\sounds\sonido_game_over.mp3")
        self.explosion = pygame.mixer.Sound("src\sounds\sonido_explosion.mp3")
        self.choque = pygame.mixer.Sound("src\sounds\sonido_choque.mp3")
        self.sonido_vida_extra = pygame.mixer.Sound("src\sounds\\vida_extra.mp3")

        self.sprites = pygame.sprite.Group()

        self.sprites = pygame.sprite.Group()
        self.asteroides = pygame.sprite.Group()
        self.lasers = pygame.sprite.Group() 
        self.powerups = pygame.sprite.Group()
        self.explosions = pygame.sprite.Group()
        self.nave = Nave(lista_animaciones_nave,(ANCHO // 2 , ALTO - 20))
        
        self.agregar_sprite(self.nave)
        
############ DEF SPRITES

    def agregar_sprite(self, sprite):
        self.sprites.add(sprite) 

    def agregar_asteroides(self, asteroide):
        self.asteroides.add(asteroide) 
        
    def agregar_laser(self, laser):
        self.lasers.add(laser) 
        
    def agregar_explosion(self,explosion):
        self.explosions.add(explosion)
        
    def agregar_powerup(self, powerup):
        self.powerups.add(powerup)
        
############ DEF EVENTOS        
    
    def start(self):
        self.menu()

    def comenzar(self, nivel_inicial):
        self.nivel = nivel_inicial
        self.musica_juego.set_volume(self.volumen_actual)
        self.musica_juego.play(-1)
        self.jugando = True

        while self.jugando or not self.juego_terminado:
            self.reloj.tick(FPS)
            self.cronometro += self.reloj.tick(FPS) / 500
            if self.cronometro >= 60:
                self.nivel += 1
                self.cronometro = 0
            self.manejar_eventos()
            self.renderizar_pantalla()
            self.actualizar_elementos()
            if self.fin_juego or self.juego_terminado:
                self.musica_juego.stop()
                self.guardar_score()
                self.mostrar_pantalla_puntaje(nivel_inicial)
                pygame.time.delay(5000)
                pygame.quit()

    def wait(self):
        wait = True
        while wait:
            self.reloj.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    wait = False
                    self.jugando = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if self.jugando == False:
                        wait = False
                        self.menu()
                    else:
                        wait = False
                            
    def stop(self):
        self.musica_juego.stop()
        pygame.display.flip()
        for laser in self.lasers:
            laser.kill()
        for asteroide in self.asteroides:
            asteroide.kill()

        self.jugando = False

    def reiniciar_juego(self):
        self.fin_juego = False
        self.menu_pausa_activo = False
        self.hay_power_up = False
        self.nivel = 1
        self.cronometro = 0
        self.SCORE = 0
        self.vida = 3
        self.speed_asteroide = 1
        self.nave.kill()
        self.sprites.empty()
        self.lasers.empty()
        self.asteroides.empty()
        self.nave = Nave(lista_animaciones_nave, (self.pantalla.get_width() // 2 , self.pantalla.get_height() - 20))
        self.explosions.empty()
        
        self.fondo = pygame.image.load("src\images\\fondo.jpg").convert()
        self.fondo = pygame.transform.scale(self.fondo, SCREEN)
        self.agregar_sprite(self.nave)
        
        
        self.jugando = True
        
    def salir(self):
        pygame.quit()
        sys.exit()    
        
    def pausa(self):
        self.jugando = False
    
    def reanudar_pausa(self):
        self.menu_pausa_activo = False
        self.musica_juego.set_volume(self.volumen_actual)
        self.musica_juego.play(-1)
        self.jugando = True
        self.comenzar(self.nivel)

        
############ DEF TECLADO    

    def manejar_eventos (self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.salir()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.nave.velocidad_x = -SPEED_NAVE
                elif event.key == pygame.K_RIGHT:
                    self.nave.velocidad_x = SPEED_NAVE
                elif event.key == pygame.K_UP:
                    self.nave.velocidad_y = -SPEED_NAVE
                elif event.key == pygame.K_DOWN:
                    self.nave.velocidad_y = SPEED_NAVE
                elif event.key == pygame.K_SPACE:
                    self.nave.disparar(self.sonido_laser,SPEED_LASER,self.sprites,self.lasers)
                elif event.key == pygame.K_p:
                    self.menu_pausa_activo = True
                    if self.menu_pausa_activo:
                        self.musica_juego.stop()
                        self.mostrar_menu_pausa()
                elif event.key == pygame.K_ESCAPE:
                    self.salir()  
                    
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and self.nave.velocidad_x < 0:
                    self.nave.velocidad_x = 0  
                elif event.key == pygame.K_RIGHT and self.nave.velocidad_x > 0:
                    self.nave.velocidad_x = 0 
                if event.key   == pygame.K_UP and self.nave.velocidad_y < 0:
                    self.nave.velocidad_y = 0    
                elif event.key == pygame.K_DOWN and self.nave.velocidad_y > 0:
                    self.nave.velocidad_y = 0
                    
############ DEF ACT ELEMENTOS

    def actualizar_elementos(self):
        self.generar_asteroides(MAX_ASTEROIDES)
        self.sprites.update()
        if self.cronometro >= 60:
            self.fin_juego = True
            self.stop()
        for asteroide in self.asteroides:
            if asteroide.rect.bottom >= ALTO:
                self.SCORE -= self.nivel * 20
                asteroide.kill()    
        if self.volumen_actual == 0:
            self.imagen_volumen = self.imagenes_volumen[self.indice_imagen]
        elif self.volumen_actual == 0.3:
            self.imagen_volumen = self.imagenes_volumen[self.indice_imagen]
        elif self.volumen_actual == 0.6:
            self.imagen_volumen = self.imagenes_volumen[self.indice_imagen]
        elif self.volumen_actual == 0.9:
            self.imagen_volumen = self.imagenes_volumen[self.indice_imagen]
        
        choque_laser_asteroide = pygame.sprite.groupcollide(self.lasers, self.asteroides, True, True)
        for self.laser, asteroides_colisionados in choque_laser_asteroide.items():
            for asteroide in asteroides_colisionados:
                explosion = Explosion(asteroide.rect.center)
                self.explosion.play()
                self.sprites.add(explosion) 
                self.SCORE += 10
                
                if self.vida < 3 and not self.hay_power_up:
                    self.laser_impacta_asteroide(asteroide)
                
        choque_powerup = pygame.sprite.spritecollide(self.nave, self.powerups, True)
        
        for powerup in self.powerups:
            if powerup.rect.bottom >= ALTO:
                self.hay_power_up = False
                powerup.kill()
                
        for powerup in choque_powerup:
            self.hay_power_up = False
            self.sonido_vida_extra.play()
            self.vida += 1
                
        for laser in self.lasers:
            if laser.rect.top <= 0:
                self.SCORE -= 10 * self.nivel
                laser.kill()
                        
        choque_asteroide = pygame.sprite.spritecollide(self.nave, self.asteroides, True)
        
        if len(choque_asteroide) > 0:
            self.choque.play()
            self.vida -= 1          
        
        if self.vida == 0:
            self.generar_explosion(self.nave.rect.center)     
            self.sonido_game_over.play()         
            self.fin_juego = True
            
        if self.nivel > 3:
            self.juego_terminado = True

############ DEF PANTALLA     
   
    def renderizar_pantalla(self):
        self.pantalla.blit(self.fondo, ORIGEN)
        self.pantalla.blit(self.fuente.render("SCORE: " + str(self.SCORE),True,CUSTOM),SCORE_POS)
        self.pantalla.blit(self.fuente.render("NIVEL: " + str(self.nivel),True,CUSTOM),NIVEL_POS)
        self.pantalla.blit(lista_animacion_barra_de_vida[self.vida],VIDA_POSICION)
        tiempo_restante = max(0, 60 - int(self.cronometro))
        self.pantalla.blit(self.fuente.render("Tiempo: " + str(tiempo_restante), True, CUSTOM), TIEMPO_POS)
        self.sprites.draw(self.pantalla)
        pygame.display.flip()
        
        
    def actualizar_pantalla_pausa(self):
        self.pantalla.blit(self.titulo_pausa, (200, 100))
        self.pantalla.blit(self.opcion_reanudar, (ANCHO // 2 - self.opcion_reanudar.get_width() // 2, ALTO // 2 - 50))
        self.pantalla.blit(self.opcion_ajustes, (ANCHO // 2 - self.opcion_ajustes.get_width() // 2, ALTO // 2))
        self.pantalla.blit(self.opcion_salir, (ANCHO // 2 - self.opcion_salir.get_width() // 2, ALTO // 2 + 50))
        self.cambiar_icono_volumen()
        self.pantalla.blit(self.imagen_volumen, VOLUMEN_POS)
        pygame.display.update((30, 555, 70, 70))
        
    def display_text(self, text, size, color, pos_x, pos_y):
        font = pygame.font.Font(self.font, size)
        text = font.render(text, True, color)
        rect = text.get_rect()
        rect.midtop = (pos_x, pos_y)
        self.pantalla.blit(text, rect)
        
    def display_multiline_text(self, text, size, color, pos_x, pos_y):
        font = pygame.font.Font(self.font, size)
        lines = text.split('\n')
        line_height = font.get_linesize()

        for i, line in enumerate(lines):
            text_surface = font.render(line, True, color)
            rect = text_surface.get_rect()
            rect.midtop = (pos_x, pos_y + i * line_height)
            self.pantalla.blit(text_surface, rect)
            
############ DEF EVENTOS JUEGO      

    def generar_explosion(self,posicion):
        explosion = Explosion(posicion)
        self.agregar_sprite(explosion)
        self.agregar_explosion(explosion)

    def laser_impacta_asteroide(self, asteroide):
        explosion = Explosion(asteroide.rect.center)
        self.agregar_explosion(explosion)
        self.explosion.play()
        self.sprites.add(explosion)
        self.SCORE += 10
        
        if not self.hay_power_up:
            if self.nivel == 1:
                PROBABILIDAD_POWERUP = 0.3
            if self.nivel == 2:
                PROBABILIDAD_POWERUP = 0.1
            if self.nivel == 3:
                PROBABILIDAD_POWERUP = 0.06
            if random.random() < PROBABILIDAD_POWERUP:
                powerup = Power_Up(asteroide.rect.center, 1)
                self.agregar_powerup(powerup)
                self.agregar_sprite(powerup) 
                self.hay_power_up = True
    
    def generar_asteroides(self, cantidad):
        if self.nivel==2:
            self.speed_asteroide=1
            cantidad=15
        elif self.nivel==3:
            self.speed_asteroide=1.3
            cantidad=20
        if len(self.asteroides) == 0:
            for i in range(cantidad):
                posicion = (random.randrange(20, ANCHO - 20), random.randrange(-500, 0))
                asteroide = Asteroide(posicion, self.speed_asteroide, 0)
                if self.nivel == 2:
                    movimiento_lateral = random.choice([0, 1])
                    asteroide = Asteroide(posicion, self.speed_asteroide, movimiento_lateral)
                if self.nivel == 3:
                    movimiento_lateral = random.choice([0, 1])
                    movimiento_lateral = random.choice([1, 0])
                    asteroide = Asteroide(posicion, self.speed_asteroide, movimiento_lateral)
                self.agregar_asteroides(asteroide)
                self.agregar_sprite(asteroide)

############ DEF MENUS

    def esta_sobre_opcion(self, posicion_mouse, rectangulo_opcion):
        if rectangulo_opcion.collidepoint(*posicion_mouse):
            return True
        return False

    def menu(self):
        fondo_menu =  pygame.image.load("src\images\\fondo.jpg")
        fondo_menu = pygame.transform.scale(fondo_menu,(ANCHO,ALTO))
        self.screen.blit(fondo_menu,(ORIGEN))
        pygame.display.flip()
    
    def mostrar_instrucciones(self):
        fondo_instrucciones = pygame.image.load("src\images\\fondo.jpg").convert()
        fondo_instrucciones = pygame.transform.scale(fondo_instrucciones,(ANCHO,ALTO))
        self.pantalla.blit(fondo_instrucciones, ORIGEN)
        self.display_multiline_text(INSTRUCCIONES,22,BLANCO,ANCHO//2, ALTO - 600)
        self.display_text('Presiona cualquier tecla para volver al menú', 24, BLANCO, ANCHO // 2, ALTO - 50)
        pygame.display.flip()
        self.wait()
            
    def mostrar_pantalla_puntaje(self, nivel:int):
        fondo = pygame.image.load("src\images\\fondo_game_over.jpg").convert()
        fuente_puntos = pygame.font.Font("src\\fonts\game_over.ttf", 80)
        if not self.juego_terminado:
            texto_game_over = fuente_puntos.render("¡¡ GAME OVER !!", True, (255, 255, 255))
        elif self.juego_terminado:
            texto_game_over = fuente_puntos.render("¡¡ HAS TERMINADO !!", True, (255, 255, 255))
        texto_puntaje = fuente_puntos.render("Puntaje: " + str(self.SCORE), True, (255, 255, 255))
        texto_retry1 = fuente_puntos.render("Presiona: 'R' para volver a jugar", True, (255, 255, 255))
        texto_retry2 = fuente_puntos.render("Presiona: 'Esc' para salir.", True, (255, 255, 255))
        texto_adios = fuente_puntos.render("Gracias por jugar. ¡Hasta luego!", True, (255, 255, 255))
        self.pantalla.blit(fondo, (0, 0))
        self.pantalla.blit(texto_game_over, (180, 100))
        self.pantalla.blit(texto_puntaje, (200, 200))
        self.pantalla.blit(texto_retry1, (100, 300))
        self.pantalla.blit(texto_retry2, (150, 350))
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.salir()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.reiniciar_juego()
                        self.comenzar(nivel)
                    elif event.key == pygame.K_ESCAPE:
                        self.pantalla.blit(texto_adios, (100, 480))
                        pygame.display.flip()
                        pygame.time.wait(2000)
                        self.salir()
    
    def mostrar_menu_pausa(self):
        while self.menu_pausa_activo:
            self.fondo_pausa = pygame.image.load("src\images\\fondo.jpg").convert()
            self.fondo_pausa = pygame.transform.scale(self.fondo, SCREEN)
            self.musica_pausa = pygame.mixer.Sound("src\sounds\sonido_menu.mp3")
            self.musica_pausa.set_volume(self.volumen_actual)

            self.fuente_pausa = pygame.font.Font("src\\fonts\Type.ttf", 30)
            self.titulo_pausa = self.fuente_pausa.render("Menu de pausa", True, (182, 255, 255))
            self.opcion_reanudar = self.fuente_pausa.render("Reanudar", True, (255, 255, 255))
            self.opcion_ajustes = self.fuente_pausa.render("Reiniciar", True, (255, 255, 255))
            self.opcion_salir = self.fuente_pausa.render("Menu", True, (255, 255, 255))

            self.musica_pausa.play()
            self.pantalla.blit(self.titulo_pausa, (200, 100))
            self.pantalla.blit(self.opcion_reanudar, (ANCHO // 2 - self.opcion_reanudar.get_width() // 2, ALTO // 2 - 50))
            self.pantalla.blit(self.opcion_ajustes, (ANCHO // 2 - self.opcion_ajustes.get_width() // 2, ALTO // 2))
            self.pantalla.blit(self.opcion_salir, (ANCHO // 2 - self.opcion_salir.get_width() // 2, ALTO // 2 + 50))
            
            imagen_volumen = self.imagenes_volumen[self.indice_imagen]
            self.pantalla.blit(imagen_volumen, VOLUMEN_POS)

            rectangulo_imagen_volumen = pygame.Rect(30, 555, imagen_volumen.get_width(), imagen_volumen.get_height()) 

            rectangulo_opcion_reanudar = self.opcion_reanudar.get_rect()
            rectangulo_opcion_reanudar.center = (ANCHO // 2, ALTO // 2 - 50)

            rectangulo_opcion_ajustes = self.opcion_ajustes.get_rect()
            rectangulo_opcion_ajustes.center = (ANCHO // 2, ALTO // 2)

            rectangulo_opcion_salir = self.opcion_salir.get_rect()
            rectangulo_opcion_salir.center = (ANCHO // 2, ALTO // 2 + 50)

            pygame.display.flip()
            
            while True:
                for evento in pygame.event.get():
                    if evento.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        if rectangulo_opcion_reanudar.collidepoint(mouse_pos):
                            self.musica_pausa.stop()
                            self.reanudar_pausa()
                        elif rectangulo_opcion_ajustes.collidepoint(mouse_pos):
                            self.musica_pausa.stop()
                            self.musica_juego.stop()
                            self.reiniciar_juego()   
                            self.comenzar(self.nivel)
                        elif rectangulo_opcion_salir.collidepoint(mouse_pos):
                            self.jugando = False
                            self.musica_pausa.stop()
                            self.musica_juego.stop()
                            self.mostrar_menu_principal()
                        if rectangulo_imagen_volumen.collidepoint(mouse_pos):
                            self.actualizar_pantalla_pausa()
                            self.musica_pausa.set_volume(self.volumen_actual)
                            self.musica_juego.set_volume(self.volumen_actual)
                       
    def cambiar_icono_volumen(self):
        self.volumen_actual += 0.3
        if self.volumen_actual > 1:
            self.volumen_actual = 0
        if self.volumen_actual == 0:
            self.imagen_volumen = pygame.transform.scale(pygame.image.load("src\images\\volumen_0.png").convert_alpha(), SIZE_VOLUMEN)
        elif self.volumen_actual == 0.3:
            self.imagen_volumen = pygame.transform.scale(pygame.image.load("src\images\\volumen_1.png").convert_alpha(), SIZE_VOLUMEN)
        elif self.volumen_actual == 0.6:
            self.imagen_volumen = pygame.transform.scale(pygame.image.load("src\images\\volumen_2.png").convert_alpha(), SIZE_VOLUMEN)
        else:
            self.imagen_volumen = pygame.transform.scale(pygame.image.load("src\images\\volumen_3.png").convert_alpha(), SIZE_VOLUMEN)
                       
                       
                            
    def mostrar_menu_principal(self):
        while not KABOOM.jugando:
            pygame.init()
            
            self.screen = pygame.display.set_mode(SCREEN)
            self.fondo_menu =  pygame.image.load("src\images\\fondo.jpg")
            self.fondo_menu = pygame.transform.scale(self.fondo_menu,(ANCHO,ALTO))
            self.color_claro = (82,172,222)
            self.color_oscuro = (100,109,170)
            self.fuente_menu = pygame.font.Font('src\\fonts\\fuente2.ttf',18)
            self.fuente_titulo = pygame.font.Font('src\\fonts\\fuente2.ttf',70)            
            self.titulo = self.fuente_titulo.render("KABOOM!", True, CUSTOM2)
            self.texto_comenzar = self.fuente_menu.render('Comenzar' , True , BLANCO)
            self.texto_niveles = self.fuente_menu.render('Niveles' , True , BLANCO)
            self.texto_instrucciones = self.fuente_menu.render('Instrucciones' , True , BLANCO)
            self.texto_salir = self.fuente_menu.render('Salir' , True , BLANCO)            
            self.musica_menu = pygame.mixer.Sound("src\sounds\sonido_menu.mp3")
            self.musica_menu.set_volume(self.volumen_actual)
            self.efecto_sonido_seleccion = pygame.mixer.Sound("src\sounds\sonido_boton_menu.mp3")  
            while not KABOOM.jugando:
                self.musica_menu.play()                
                self.screen.blit(self.fondo_menu,(ORIGEN))                        
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
                posicion_x_niveles = ANCHO/2 - 45
                posicion_y_niveles = ALTO/2 + 50 
                posicion_x_instrucciones = ANCHO/2 - 55
                posicion_y_instrucciones = 450
                posicion_x_salir = ANCHO/2 - 55
                posicion_y_salir = 500               
                if posicion_x_comenzar <= mouse[0] <= posicion_x_comenzar + rect_ancho and posicion_y_comenzar <= mouse[1] <= posicion_y_comenzar + rect_alto:
                    pygame.draw.rect(self.screen, self.color_claro, [posicion_x_comenzar, posicion_y_comenzar, rect_ancho, rect_alto])
                else:
                    pygame.draw.rect(self.screen, self.color_oscuro, [posicion_x_comenzar, posicion_y_comenzar, rect_ancho, rect_alto])
                if posicion_x_niveles <= mouse[0] <= posicion_x_niveles + rect_ancho and posicion_y_niveles <= mouse[1] <= posicion_y_niveles + rect_alto:
                    pygame.draw.rect(self.screen, self.color_claro, [posicion_x_niveles, posicion_y_niveles, rect_ancho-20, rect_alto])
                else:
                    pygame.draw.rect(self.screen, self.color_oscuro, [posicion_x_niveles, posicion_y_niveles, rect_ancho-20, rect_alto])
                if posicion_x_instrucciones <= mouse[0] <= posicion_x_instrucciones + rect_ancho_instrucciones and posicion_y_instrucciones <= mouse[1] <= posicion_y_instrucciones + rect_alto:
                    pygame.draw.rect(self.screen, self.color_claro, [posicion_x_instrucciones-20, posicion_y_instrucciones, rect_ancho_instrucciones, rect_alto])
                else:
                    pygame.draw.rect(self.screen, self.color_oscuro, [posicion_x_instrucciones-20, posicion_y_instrucciones, rect_ancho_instrucciones, rect_alto])
                if posicion_x_salir <= mouse[0] <= posicion_x_salir + rect_ancho and posicion_y_salir <= mouse[1] <= posicion_y_salir + rect_alto:
                    pygame.draw.rect(self.screen, self.color_claro, [posicion_x_salir, posicion_y_salir, rect_ancho, rect_alto])
                else:
                    pygame.draw.rect(self.screen, self.color_oscuro, [posicion_x_salir, posicion_y_salir, rect_ancho, rect_alto])
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if posicion_x_comenzar <= mouse[0] <= posicion_x_comenzar + rect_ancho and posicion_y_comenzar <= mouse[1] <= posicion_y_comenzar + rect_alto:
                        self.musica_menu.stop()
                        self.efecto_sonido_seleccion.play()
                        pygame.time.delay(300)
                        KABOOM.reiniciar_juego()
                        KABOOM.comenzar(self.nivel)
                    elif posicion_x_niveles <= mouse[0] <= posicion_x_niveles + rect_ancho and posicion_y_niveles <= mouse[1] <= posicion_y_niveles + rect_alto:
                        self.musica_menu.stop()
                        self.efecto_sonido_seleccion.play()
                        self.musica_menu.play()
                        seleccionando_nivel = True
                        while seleccionando_nivel:
                            self.screen.blit(self.fondo_menu,(ORIGEN))
                            nivel1_rect = pygame.Rect(250, 200, 100, 50)
                            nivel2_rect = pygame.Rect(250, 300, 100, 50)
                            nivel3_rect = pygame.Rect(250, 400, 100, 50)
                            atras_rect = pygame.Rect(250, 500, 100, 50)
                            pygame.draw.rect(self.screen, self.color_oscuro, nivel1_rect)
                            pygame.draw.rect(self.screen, self.color_oscuro, nivel2_rect)
                            pygame.draw.rect(self.screen, self.color_oscuro, nivel3_rect) 
                            pygame.draw.rect(self.screen, self.color_oscuro, atras_rect) 
                            self.screen.blit(self.fuente_menu.render("Nivel 1", True, BLANCO), (260, 210)) 
                            self.screen.blit(self.fuente_menu.render("Nivel 2", True, BLANCO), (260, 310))
                            self.screen.blit(self.fuente_menu.render("Nivel 3", True, BLANCO), (260, 410)) 
                            self.screen.blit(self.fuente_menu.render("Atras", True, BLANCO), (270, 510))
                            pygame.display.flip()
                            
                            for evento_niveles in pygame.event.get():
                                if evento_niveles.type == pygame.MOUSEBUTTONDOWN:
                                    if nivel1_rect.collidepoint(evento_niveles.pos):
                                        self.nivel = 1
                                        self.musica_menu.stop()
                                        self.efecto_sonido_seleccion.play()
                                        self.comenzar(self.nivel)
                                        seleccionando_nivel = False
                                    elif nivel2_rect.collidepoint(evento_niveles.pos):
                                        self.nivel = 2
                                        self.musica_menu.stop()
                                        self.efecto_sonido_seleccion.play()
                                        self.comenzar(self.nivel)
                                        seleccionando_nivel = False
                                    elif nivel3_rect.collidepoint(evento_niveles.pos):
                                        self.nivel = 3
                                        self.musica_menu.stop()
                                        self.efecto_sonido_seleccion.play()
                                        self.comenzar(self.nivel)
                                        seleccionando_nivel = False
                                    elif atras_rect.collidepoint(evento_niveles.pos):
                                        self.musica_menu.stop()
                                        self.efecto_sonido_seleccion.play()
                                        self.musica_menu.play()
                                        seleccionando_nivel = False
                                        self.mostrar_menu_principal()
                                        
                    elif posicion_x_instrucciones <= mouse[0] <= posicion_x_instrucciones + rect_ancho and posicion_y_instrucciones <= mouse[1] <= posicion_y_instrucciones + rect_alto:
                        KABOOM.mostrar_instrucciones()
                    elif posicion_x_salir <= mouse[0] <= posicion_x_salir + rect_ancho and posicion_y_salir <= mouse[1] <= posicion_y_salir + rect_alto:
                        pygame.quit()
                        sys.exit()
                        
                self.screen.blit(self.titulo ,(ANCHO//2-170,100))            
                self.screen.blit(self.texto_comenzar ,(250, 355))
                self.screen.blit(self.texto_niveles,(260, 404))
                self.screen.blit(self.texto_instrucciones,(233, 454))
                self.screen.blit(self.texto_salir,(265, 504))
                pygame.display.flip()
                
############ DEF SCORE
    
    def guardar_score(self):
        try:
            with open("Score.csv", "r") as file:
                for i in file:
                    if self.SCORE > int(i):
                        self.mejor_score = self.SCORE
                                      
        except Exception:
            print("No se pudo abrir el archivo")
        
        try:
            with open("Score.csv", "a") as file:
                    file.write(str(self.SCORE) + "\n")
        except Exception:
            print("No se pudo guardar el archivo")

############

KABOOM = Juego()

############

KABOOM.mostrar_menu_principal()