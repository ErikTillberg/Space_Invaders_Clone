import pygame


class PlayerShip:

    ShipSpeed = 7

    def __init__(self, imageLocation, screenSize):
        self.shipSprite = pygame.image.load(imageLocation)
        self.shipSprite = pygame.transform.scale(self.shipSprite, (50, 50))
        self.shipRect = self.shipSprite.get_rect()

        self.shipRect.x = 320
        self.shipRect.y = 400

    def move(self, x, y):
        speed = [x, y]
        self.shipRect = self.shipRect.move(speed)

    def display(self, screen):
        screen.blit(self.shipSprite, self.shipRect)
