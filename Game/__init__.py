import sys
import pygame
import PlayerShipClass
import EnemyClass
import EnemiesControllerClass

pygame.init()

pygame.mixer.init()

size = width, height = 720, 480
black = 0, 0, 0

screen = pygame.display.set_mode(size)

background = pygame.image.load("../Resources/Images/space.PNG")
backgroundRect = background.get_rect()

playerShip = PlayerShipClass.PlayerShip("../Resources/Images/playerShip.png", size)

enemyController = EnemiesControllerClass.EnemiesController(size)

keyRightDown = False
keyLeftDown = False

# Primary game loop

while True:

    # Event handling

    for event in pygame.event.get():
        # Handle quitting
        if event.type == pygame.QUIT: sys.exit()

        # handle pressing buttons
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                keyLeftDown = True
                keyRightDown = False

            if event.key == pygame.K_RIGHT:
                keyRightDown = True
                keyLeftDown = False

            # Handle shooting
            if event.key == pygame.K_SPACE:
                playerShip.shoot()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                keyLeftDown = False
            if event.key == pygame.K_RIGHT:
                keyRightDown = False

    # Flags are set to handle moving side to side

    if keyLeftDown:
        playerShip.move(-PlayerShipClass.PlayerShip.ShipSpeed, 0)

    if keyRightDown:
        playerShip.move(PlayerShipClass.PlayerShip.ShipSpeed, 0)

    screen.fill(black)
    screen.blit(background, backgroundRect)

    # Handle displaying the bullets
    playerShip.moveBulletsAndDisplay(screen)

    enemyController.moveEnemies()
    enemyController.displayEnemies(screen)

    playerShip.display(screen)
    pygame.display.flip()