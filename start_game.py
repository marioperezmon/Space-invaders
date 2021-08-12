import pygame
from time import sleep
from nave import nave

black = (0, 0, 0)
white = (255, 255, 255)
red = (252, 3, 23)

pygame.init()

dificultad = 1
delay = 1 / dificultad
# numero de naves por fila
numero_naves = 11 * dificultad

# en funcion de las dimensiones de la pantalla, se adaptan el resto de elementos
# monitor = 1920 x 1080; mac = 1280 x 800
width = 1920
height = 1080

# horizontalmente, el espacio de juego es el 80% de la pantalla (+10% de margen a cada lado)
espacio_juego_hori = int( (80./100) * width )
margen_hori = int((10./100) * width)
margen_ver = int((1./5) * height)

# horizontalmente, el espacio que ocupan las naves es el 75% del espacio de juego (+25% de espacio de desplazamiento)
espacio_naves_hori = int( (75./100) * espacio_juego_hori )

# tamanho total horizontal de las naves = tamanho de la nave + espacio tras ella
tamanho_total_nave = float( espacio_naves_hori / numero_naves )
espacio_tras_nave = float( tamanho_total_nave / 5 )
tamanho_nave_hori = espacio_tras_nave * 4
tamanho_nave_ver = (1./2) * tamanho_nave_hori

print("\n**********  Partida  **********")
print("Dificultad : " + str(dificultad))
print("Delay : " + str(delay) + " seg")
print("\n**********  Tamanos  **********")
print("Pantalla : " + str(width) + " x " + str(height))
print(" ## HORIZONTAL")
print("Margen : " + str(margen_hori))
print("Espacio de juego : " + str(espacio_juego_hori) + " [" + str(margen_hori) + " - " + str(width - margen_hori) + "]")
print("Espacio de naves : " + str(espacio_naves_hori))
print(" ## VERTICAL")
print("Margen : " + str(margen_ver))
print("\n**********   Naves   **********")
print("Numero de naves : " + str(numero_naves))
print("Tamanho total de nave : " + str(tamanho_total_nave))
print("Tamanho de nave (alto x ancho) : " + str(tamanho_nave_hori) + " x " + str(tamanho_nave_ver))
print("Espacio tras nave : " + str(espacio_tras_nave) + "\n")

screen = pygame.display.set_mode((width,height))

v = 0 # TODO

while 1:

    screen.fill(black)

    ev = pygame.event.get()
    for event in ev:
        # al pulsar una tecla
        if event.type == pygame.KEYDOWN:
            pass

    # desplazamiento vertical [0 - 200]
    n_saltos_ver = 10  # TODO
    despl_ver = 300
    movimiento_ver = list(range(0, despl_ver, despl_ver/n_saltos_ver))

    # desplazamiento horizontal [0 - 288 - 0]
    n_saltos_hori = 7
    despl_hori = int( (2./8) * espacio_naves_hori )
    movimiento_hori = list(range(0, despl_hori, despl_hori/n_saltos_hori)
                        + range(despl_hori, 0, -despl_hori/n_saltos_hori))
    
    for m_h in movimiento_hori:

        # cada vez que se completa el movimiento horizontal, las naves descienden
        m_v = movimiento_ver[v]
        if m_h % despl_hori == 0 and v < len(movimiento_ver) - 1:
            v += 1

        screen.fill(black)
        
        # render de las naves
        for n in range(1, numero_naves+1):
            
            # posicion de las naves inicialmente
            #pos_nave_hori = (n - 1) * tamanho_total_nave
        
            # posicion de las naves tras desplazarse
            #pos_nave_hori = (2./8) * espacio_naves_hori + (n - 1) * tamanho_total_nave
            
            # posicion de las naves al desplazarse
            pos_nave_hori = m_h + (n - 1) * tamanho_total_nave
            pos_nave_hori += margen_hori

            pos_nave_ver = m_v + 0 # TODO
            pos_nave_ver += margen_ver
            pos_nave = (pos_nave_hori, pos_nave_ver)

            #print("Nave #" + str(n) + ", pos : " + str(pos_nave))

            render_nave = nave(white, pos_nave_hori, pos_nave_ver,
                            tamanho_nave_hori, tamanho_nave_ver)
            render_nave.draw(screen)

            pygame.draw.circle(screen, red, pos_nave, 4)

        sleep(delay)
        pygame.display.update()

    #print("")
    
