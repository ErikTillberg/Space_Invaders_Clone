import pygame

class Enemy:

    ENEMY_RESOURCE_FILE = "../Resources/Images/enemy.png"
    WIDTH = 50
    HEIGHT = 50

    def __init__(self, x, y):

        self.enemySprite = pygame.image.load(Enemy.ENEMY_RESOURCE_FILE)
        self.enemySprite = pygame.transform.scale(self.enemySprite, (Enemy.WIDTH, Enemy.HEIGHT))
        self.enemySprite = pygame.transform.rotate(self.enemySprite, 180)

        self.enemyRect = self.enemySprite.get_rect()

        self.enemyRect.x = x
        self.enemyRect.y = y

    def display(self, screen):
        screen.blit(self.enemySprite,self.enemyRect)

    def move(self, x, y):
        self.enemyRect = self.enemyRect.move([x, y])