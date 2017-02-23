import pygame
import EnemyClass
import PlayerShipClass

class EnemiesController:

    INITIAL_ENEMY_COUNT = 10
    EnemyList = []

    FARTHEST_LEFT_ENEMY_LOC_X = 25
    FARTHEST_LEFT_ENEMY_LOC_Y = 25

    ENEMY_X_SPACING = 2*EnemyClass.Enemy.WIDTH
    ENEMY_Y_SPACING = 2*EnemyClass.Enemy.HEIGHT

    ENEMY_SPEED_Y = 1
    ENEMY_FRAME_MOVE = 0
    ENEMY_MOVE_ON_FRAME = 5

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

    def createEnemy(self, x, y):
        enemy = EnemyClass.Enemy(x, y)
        EnemiesController.EnemyList.append(enemy)

    def moveEnemies(self):

        if (EnemiesController.ENEMY_FRAME_MOVE%EnemiesController.ENEMY_MOVE_ON_FRAME == 0):
            for enemy in EnemiesController.EnemyList:
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
                EnemiesController.EnemyList.remove(enemy)

            for collisionIndex in collisions:
                # Now remove the bullets that were collided with
                PlayerShipClass.PlayerShip.Bullets.pop(collisionIndex)