import pygame


class Bullet:

    WIDTH = 25
    HEIGHT = 25

    SPEED = 15

    def __init__(self, x, y, resourceLoc, type):

        self.bulletSprite = pygame.image.load(resourceLoc)
        self.bulletSprite = pygame.transform.scale(self.bulletSprite, (Bullet.WIDTH, Bullet.HEIGHT))

        if type == "enemy":
            self.bulletSprite = pygame.transform.rotate(self.bulletSprite, 180)

        self.bulletRect = self.bulletSprite.get_rect()
        self.bulletRect.x = x
        self.bulletRect.y = y

    def move(self, type):
        # Move up the screen at the speed specified
        if (type == "player"): # Move the bullet upwards if player
            s = -Bullet.SPEED
        else: # Move downwards if enemy
            s = Bullet.SPEED/2

        movement = [0, s]
        self.bulletRect = self.bulletRect.move(movement)

    def display(self, screen):
        screen.blit(self.bulletSprite, self.bulletRect)
