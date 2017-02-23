import pygame


class Bullet:

    WIDTH = 25
    HEIGHT = 25

    SPEED = 15

    def __init__(self, x, y, resourceLoc):

        self.bulletSprite = pygame.image.load(resourceLoc)
        self.bulletSprite = pygame.transform.scale(self.bulletSprite, (Bullet.WIDTH, Bullet.HEIGHT))

        self.bulletRect = self.bulletSprite.get_rect()
        self.bulletRect.x = x
        self.bulletRect.y = y

    def move(self):
        # Move up the screen at the speed specified
        movement = [0, -Bullet.SPEED]
        self.bulletRect = self.bulletRect.move(movement)

    def display(self, screen):
        screen.blit(self.bulletSprite, self.bulletRect)
