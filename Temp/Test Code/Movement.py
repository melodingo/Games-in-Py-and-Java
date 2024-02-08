# Importieren der Pygame-Bibliothek
import pygame

# initialisieren von pygame
pygame.init()

# genutzte Farbe
WEISS   = (255, 255, 255)
BLAU    = (0, 0, 255)

#Startpositionen
circleX = 250
circleY = 250
screen_width = 1000
screen_height = 480

# Fenster öffnen
TestScreen = pygame.display.set_mode((screen_width, screen_height))

# Titel für Fensterkopf
pygame.display.set_caption("Test")

# solange die Variable True ist, soll das Spiel laufen
spielaktiv = True

# Bewegungsgeschwindigkeit
speed = 5

# Bildschirm Aktualisierungen einstellen
clock = pygame.time.Clock()

# Schleife Hauptprogramm
while spielaktiv:
    # Überprüfen, ob Nutzer eine Aktion durchgeführt hat
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            spielaktiv = False
            print("Spieler hat Quit-Button angeklickt")
    
    # Tastatureingaben überprüfen
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        circleY -= speed
    if keys[pygame.K_a]:
        circleX -= speed
    if keys[pygame.K_s]:
        circleY += speed
    if keys[pygame.K_d]:
        circleX += speed

    # Überprüfen, ob der Kreis die Grenzen des Bildschirms erreicht hat
    if circleX < 0:
        circleX = 0
    elif circleX > screen_width:
        circleX = screen_width
    if circleY < 0:
        circleY = 0
    elif circleY > screen_height:
        circleY = screen_height

    # Spielfeld löschen
    TestScreen.fill(WEISS)
    
    #Kreis zeichnen
    pygame.draw.circle(TestScreen, BLAU, (circleX, circleY), 20)

    # Fenster aktualisieren
    pygame.display.flip()

    # Refresh-Zeiten festlegen
    clock.tick(60)

pygame.quit()
