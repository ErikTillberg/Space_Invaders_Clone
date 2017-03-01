import pygame
import EnemyClass
import PlayerShipClass
import random

class EnemiesController:

    INITIAL_ENEMY_COUNT = 10
    EnemyList = []

    FARTHEST_LEFT_ENEMY_LOC_X = 25
    FARTHEST_LEFT_ENEMY_LOC_Y = 25

    ENEMY_X_SPACING = 2*EnemyClass.Enemy.WIDTH
    ENEMY_Y_SPACING = 2*EnemyClass.Enemy.HEIGHT

    ENEMY_SPEED_Y = 1
    ENEMY_FRAME_MOVE = 0
    ENEMY_MOVE_ON_FRAME = 1

    def __init__(self, size):

        self.screenSize = size

        xloc = EnemiesController.FARTHEST_LEFT_ENEMY_LOC_X
        yloc = EnemiesController.FARTHEST_LEFT_ENEMY_LOC_Y

        # Build INITIAL_ENEMY_COUNT number of enemies
        for i in range(0, EnemiesController.INITIAL_ENEMY_COUNT):
            self.createEnemy(xloc, yloc)

            xloc += EnemiesController.ENEMY_X_SPACING
            if (xloc+EnemyClass.Enemy.WIDTH > size[0]):
                xloc = EnemiesController.FARTHEST_LEFT_ENEMY_LOC_X
                yloc += EnemiesController.ENEMY_Y_SPACING

        self.explosionSound = pygame.mixer.Sound("../Resources/Sounds/explosion.wav")

    def createEnemy(self, x, y):
        enemy = EnemyClass.Enemy(x, y, self.screenSize)
        EnemiesController.EnemyList.append(enemy)

    def moveEnemies(self):

        # If there are no more enemies on the screen, add more, and increment the number of enemies added to the screen
        if len(EnemiesController.EnemyList) == 0:
            xloc = EnemiesController.FARTHEST_LEFT_ENEMY_LOC_X
            yloc = EnemiesController.FARTHEST_LEFT_ENEMY_LOC_Y
            EnemiesController.INITIAL_ENEMY_COUNT += 4
            # Build more enemies number of enemies
            for i in range(0, EnemiesController.INITIAL_ENEMY_COUNT):
                self.createEnemy(xloc, yloc)

                xloc += EnemiesController.ENEMY_X_SPACING
                if (xloc + EnemyClass.Enemy.WIDTH > self.screenSize[0]):
                    xloc = EnemiesController.FARTHEST_LEFT_ENEMY_LOC_X
                    yloc += EnemiesController.ENEMY_Y_SPACING

        # This function also allows the enemies to shoot bullets on some chance
        if (EnemiesController.ENEMY_FRAME_MOVE%EnemiesController.ENEMY_MOVE_ON_FRAME == 0):
            for enemy in EnemiesController.EnemyList:

                # If an enemy is off the screen, remove them.
                if (enemy.enemyRect.y > self.screenSize[1]):
                    EnemiesController.EnemyList.remove(enemy)
                    continue

                shouldShoot = random.random() < 0.005  # Shoots 1/200 frames
                if shouldShoot:
                    enemy.shoot()
                enemy.move(0, EnemiesController.ENEMY_SPEED_Y)

        EnemiesController.ENEMY_FRAME_MOVE += 1

        # We'll just check for collisions here, I don't know where else to put this
        self.checkForCollisionsWithBullets()

    def displayEnemies(self, screen):

        for enemy in EnemiesController.EnemyList:
            enemy.display(screen)

    def checkForCollisionsWithBullets(self):

        for enemy in EnemiesController.EnemyList:

            #Convert the list of bullets to a list of bulletRects
            bulletRectList = []
            for bullet in PlayerShipClass.PlayerShip.Bullets:
                bulletRectList.append(bullet.bulletRect)

            # Next line puts the number of collisions between an enemy and bullets into 'collisions'
            collisions = enemy.enemyRect.collidelistall(bulletRectList)

            # If there was a collision, remove the enemy that was collided with
            if (len(collisions) > 0):
                self.explosionSound.play()
                EnemiesController.EnemyList.remove(enemy)

            for collisionIndex in collisions:
                # Now remove the bullets that were collided with
                PlayerShipClass.PlayerShip.Bullets.pop(collisionIndex)