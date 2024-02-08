# Importieren der Pygame-Bibliothek
import pygame

# initialisieren von pygame
pygame.init()

# genutzte Farbe
ORANGE  = ( 255, 140, 0)
ROT     = ( 255, 0, 0)
GRUEN   = ( 0, 255, 0)
SCHWARZ = ( 0, 0, 0)
WEISS   = ( 255, 255, 255)

# Fenster öffnen
TestScreen = pygame.display.set_mode((640, 480))

# Titel für Fensterkopf
pygame.display.set_caption("Test")

# solange die Variable True ist, soll das Spiel laufen
spielaktiv = True

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
            print("Spieler hat Taste gedrückt")

            # Taste für Spieler
            if event.key == pygame.K_w:
                print("Spieler hat Taste w gedrückt")
            elif event.key == pygame.K_a:
                print("Spieler hat Taste a gedrückt")
            elif event.key == pygame.K_s:
                print("Spieler hat Taste s gedrückt")
            elif event.key == pygame.K_d:
                print("Spieler hat Taste d gedrückt")
            elif event.key == pygame.K_SPACE:
                print("Spieler hat Leertaste gedrückt")

        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("Spieler hast Maus angeklickt")
    
    # Spielfeld löschen
    TestScreen.fill(WEISS)
    
    
    #Kreis
    pygame.draw.circle(TestScreen, (0, 0, 255), (0, 0), 75)

    # Spielfeld/figuren zeichnen

    # Fenster aktualisieren
    pygame.display.flip()

    # Refresh-Zeiten festlegen
    clock.tick(60)

pygame.quit()
