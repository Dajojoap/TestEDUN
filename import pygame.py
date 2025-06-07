import pygame

#abrir la ventana (pop up) 
pygame.init()
Ventana_Altura, Ventana_Ancho =824, 527 #esto define cuanto mide la pantalla
Display_Surface= pygame.display.set_mode((Ventana_Ancho, Ventana_Altura)) #esto saca la pantalla
corriendo= True #esto hace que la pantalla corra

#surface
surf= pygame.Surface((100,200))
surf.fill((3,115,17))
x = 100

#titulo e icono
pygame.display.set_caption('Escapa de la UN') #define el titulo de la ventana
Icono= pygame.image.load("C:\\Users\\user\\Desktop\\GAME TEST\\ASSETS\\Icon.jpg") #esto nos da el icono de la pantalla (cambiarlo por la direccion de la imagen a usar)
pygame.display.set_icon(Icono)

while True:
    #loop de evento
    for event in pygame.event.get():
        if event.type == pygame.quit:
            corriendo= False
    
    
    #dibuja el juego
    Display_Surface.fill((4,17,4)) #esto define el color de fondo de la pantalla
    x += 0.1
    Display_Surface.blit(surf, (x,150))
    pygame.display.update()

pygame.quit()