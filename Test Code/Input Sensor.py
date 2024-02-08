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

# Fenster öffnen
TestScreen = pygame.display.set_mode((640, 480))

# Titel für Fensterkopf
pygame.display.set_caption("Test")

# solange die Variable True ist, soll das Spiel laufen
spielaktiv = True

# Bewegungsgeschwindigkeit
speed = 5

# Bewegungsrichtungen
move_left = False
move_right = False
move_up = False
move_down = False

# Bildschirm Aktualisierungen einstellen
clock = pygame.time.Clock()

# Schleife Hauptprogramm
while spielaktiv:
    # Überprüfen, ob Nutzer eine Aktion durchgeführt hat
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            spielaktiv = False
            print("Spieler hat Quit-Button angeklickt")
        elif event.type == pygame.KEYDOWN:
            # Bewegung starten, wenn die entsprechende Taste gedrückt wird
            if event.key == pygame.K_w:
                move_up = True
            elif event.key == pygame.K_a:
                move_left = True
            elif event.key == pygame.K_s:
                move_down = True
            elif event.key == pygame.K_d:
                move_right = True
        elif event.type == pygame.KEYUP:
            # Bewegung stoppen, wenn die entsprechende Taste losgelassen wird
            if event.key == pygame.K_w:
                move_up = False
            elif event.key == pygame.K_a:
                move_left = False
            elif event.key == pygame.K_s:
                move_down = False
            elif event.key == pygame.K_d:
                move_right = False

    # Kreisposition aktualisieren basierend auf Bewegungsflaggen
    if move_left:
        circleX -= speed
    if move_right:
        circleX += speed
    if move_up:
        circleY -= speed
    if move_down:
        circleY += speed

    # Spielfeld löschen
    TestScreen.fill(WEISS)
    
    #Kreis zeichnen
    pygame.draw.circle(TestScreen, BLAU, (circleX, circleY), 20)

    # Fenster aktualisieren
    pygame.display.flip()

    # Refresh-Zeiten festlegen
    clock.tick(60)

pygame.quit()
