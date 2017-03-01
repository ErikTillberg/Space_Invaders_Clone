import pygame
import BulletClass
from EnemiesControllerClass import EnemiesController

class PlayerShip:

    ShipSpeed = 7

    # Static variable containing all the bullets the ship has fired
    BULLET_RESOURCE = "../Resources/Images/bullet.png"
    Bullets = []

    def __init__(self, imageLocation, screenSize):
        self.shipSprite = pygame.image.load(imageLocation)
        self.shipSprite = pygame.transform.scale(self.shipSprite, (50, 50))
        self.shipRect = self.shipSprite.get_rect()

        self.shipRect.x = 320
        self.shipRect.y = 400

        self.bulletSound = pygame.mixer.Sound("../Resources/Sounds/bullet_sound.wav")

        self.screenSize = screenSize

    def move(self, x, y):

        # Next two if statements constrain the ship to within the bounds of the screen

        if x < 0 and (self.shipRect.x + x) < 0:
            x = PlayerShip.ShipSpeed

        if x > 0 and ((self.shipRect.x+self.shipRect.w) + x) > self.screenSize[0]:
            x = -PlayerShip.ShipSpeed

        speed = [x, y]
        self.shipRect = self.shipRect.move(speed)

    def display(self, screen):
        screen.blit(self.shipSprite, self.shipRect)

    def shoot(self):
        # Create a bullet

        xLoc = self.shipRect.x + self.shipRect.w/4
        yLoc = self.shipRect.y

        bullet = BulletClass.Bullet(xLoc, yLoc, PlayerShip.BULLET_RESOURCE, "player")
        PlayerShip.Bullets.append(bullet)
        self.bulletSound.play()

    def moveBulletsAndDisplay(self, screen):

        collided = self.checkCollisionForEnemyBullets()

        if (collided):
            return True

        for bullet in PlayerShip.Bullets:

            # If the bullet is off screen, remove it from the bullet list

            if bullet.bulletRect.y < 0:
                PlayerShip.Bullets.remove(bullet)
            else: # Otherwise proceed as normal
                bullet.move("player")
                bullet.display(screen)

    def checkCollisionForEnemyBullets(self):

        for enemy in EnemiesController.EnemyList:
            for bullet in enemy.bullets:
                if (bullet.bulletRect.colliderect(self.shipRect)):
                    enemy.bullets.remove(bullet)
                    print("You lose sucka!")
                    return True