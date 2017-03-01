import sys
import pygame
import PlayerShipClass
import EnemyClass
import EnemiesControllerClass
import time

pygame.init()

pygame.mixer.init()
pygame.font.init()

font = pygame.font.SysFont("Comic Sans MS", 30)

size = width, height = 720, 480
black = 0, 0, 0

screen = pygame.display.set_mode(size)

background = pygame.image.load("../Resources/Images/space.PNG")
backgroundRect = background.get_rect()

playerShip = PlayerShipClass.PlayerShip("../Resources/Images/playerShip.png", size)

enemyController = EnemiesControllerClass.EnemiesController(size)

keyRightDown = False
keyLeftDown = False

timer = pygame.time.Clock()

timeStart = time.clock()

# Primary game loop

running = True

while running:

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
    collided = playerShip.moveBulletsAndDisplay(screen)

    # If you collided, then stop the game, because you lost.
    if (collided):
        running = False
        print("You lasted: " + str(time.clock()-timeStart) + " seconds, wow good job.")

    enemyController.moveEnemies()
    enemyController.displayEnemies(screen)

    playerShip.display(screen)
    pygame.display.flip()
    timer.tick(60)

# This is just the game over screen, you cannot return.

loseStr = "You lasted: " + "{0:.2f}".format(time.clock()-timeStart) + " seconds, wow good job."
loseText = font.render("Game Over.", True, (255, 255, 255))
moreLoseText = font.render(loseStr, True, (255, 255, 255))

while True:
    for event in pygame.event.get():
        # Handle quitting
        if event.type == pygame.QUIT: sys.exit()

    screen.fill(black)
    screen.blit(background, backgroundRect)

    screen.blit(loseText, (size[0]/4, size[1]/4))
    screen.blit(moreLoseText, (size[0]/8, size[1]/2))
    pygame.display.flip()