import pygame
from random import randint

#abrir la ventana (pop up) 
pygame.init()
Ventana_Altura, Ventana_Ancho =824, 527 #esto define cuanto mide la pantalla
Display_Surface= pygame.display.set_mode((Ventana_Ancho, Ventana_Altura)) #esto saca la pantalla
corriendo= True #esto hace que la pantalla corra

#plain surface
surf= pygame.Surface((100,200))
surf.fill((3,115,17))
x = 100

#importando una imagen
player_Surf= pygame.image.load("Assets\\Buho test.png")
Moneda_surf= pygame.image.load("Assets\\Moneda_test.png")
Moneda_positions = [(randint(0, Ventana_Ancho), randint(0, Ventana_Altura))for i in range(20)]

#titulo e icono
pygame.display.set_caption('Escapa de la UN') #define el titulo de la ventana
Icono= pygame.image.load("Assets\\Icon128.jpg")
pygame.display.set_icon(Icono)

while corriendo:
    #loop de evento
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            corriendo= False

    #dibuja el juego
    Display_Surface.fill((4,17,4)) 
    for pos in Moneda_positions:
        Display_Surface.blit(Moneda_surf,pos)
    x += 0.1
    Display_Surface.blit(player_Surf, (x,150))

    pygame.display.update()

pygame.quit()
