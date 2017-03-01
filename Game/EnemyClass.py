import pygame
from BulletClass import Bullet

class Enemy:

    ENEMY_RESOURCE_FILE = "../Resources/Images/enemy.png"
    BULLET_RESOURCE_FILE = "../Resources/Images/bullet.png"
    WIDTH = 50
    HEIGHT = 50

    def __init__(self, x, y, size):

        self.enemySprite = pygame.image.load(Enemy.ENEMY_RESOURCE_FILE)
        self.enemySprite = pygame.transform.scale(self.enemySprite, (Enemy.WIDTH, Enemy.HEIGHT))
        self.enemySprite = pygame.transform.rotate(self.enemySprite, 180)

        self.enemyRect = self.enemySprite.get_rect()

        self.size = size # This is the screen size

        self.bullets = []

        self.enemyRect.x = x
        self.enemyRect.y = y

    def display(self, screen):
        self.moveBulletsAndDisplay(screen)
        screen.blit(self.enemySprite,self.enemyRect)

    def move(self, x, y):
        self.enemyRect = self.enemyRect.move([x, y])

    def shoot(self):
        newBullet = Bullet(self.enemyRect.x+self.enemyRect.w/4, self.enemyRect.y, Enemy.BULLET_RESOURCE_FILE, "enemy")

        self.bullets.append(newBullet)

    def moveBulletsAndDisplay(self, screen):
        for bullet in self.bullets:
            if (bullet.bulletRect.y > self.size[1]): # If greater than the screen width
                self.bullets.remove(bullet)
            else:
                bullet.move("enemy")
                bullet.display(screen)