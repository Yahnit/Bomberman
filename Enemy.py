from Person import *
import random, os,time
from Wall import *
from Bomberman import *

class Enemy(Person):
    '''
    This class contains the states and methods defined on Enemy.
    '''
    def __init__(self):
        self.__numEnemies = 4
        self.__enemyPos = []

    def getNumEnemies(self):
        return self.__numEnemies

    def setNumEnemies(self,x):
        self.__numEnemies = x

    def getEnemyPos(self):
        return self.__enemyPos

    def setEnemyPos(self,pos):
        self.__enemyPos = pos


    '''
    This method checks if an enemy can be placed in the given
    position.
    '''
    def isAccomodateEnemy(self,x,y,screen):
        for i in range(x,x+2):
            for j in range(y,y+4):
                if screen[i][j]!=' ' and screen[i][j]!='B':
                    return False
        return True
    '''
    This method generates enemies based on the level of the Game.
    It essentially creates 4*level enemies.
    '''
    def generateEnemy(self,screen,max_enemies):
        num_enemies = 0
        arr = [[0 for x in range(0,2)] for y in range(0,self.getNumEnemies())]
        while(num_enemies<max_enemies):
            x = random.randint(10,36)
            y = random.randint(12,72)
            if self.isAccomodateEnemy(x,y,screen) and  ((x%4==2 and y%4==0) or (x%4==0 and y%8==4)):
                for i in range(x,x+2):
                    for j in range(y,y+4):
                        screen[i][j] = 'E'
                arr[num_enemies][0],arr[num_enemies][1]=x,y
                num_enemies+=1
        self.setEnemyPos(arr)

    '''
    This method moves the enemy one step to the right
    '''

    def moveRight(self,x,y,screen):
        if self.isMoveRight(x,y,screen):
            for i in range (x,x+2):
                for j in range(y,y+4):
                    screen[i][j] = ' '
            for i in range (x,x+2):
                for j in range(y+4,y+8):
                    screen[i][j] = 'E'
            return True
        return False

    '''
    This method moves the enemy one step to the left
    '''
    def moveLeft(self,x,y,screen):
        if self.isMoveLeft(x,y,screen):
            for i in range (x,x+2):
                for j in range(y,y+4):
                    screen[i][j] = ' '
            for i in range (x,x+2):
                for j in range(y-4,y):
                    screen[i][j] = 'E'
            return True
        return False

    '''
    This method moves the enemy one step upwards
    '''
    def moveUp(self,x,y,screen):
        if self.isMoveUp(x,y,screen):
            for i in range (x,x+2):
                for j in range(y,y+4):
                    screen[i][j] = ' '
            for i in range (x-2,x):
                for j in range(y,y+4):
                    screen[i][j] = 'E'
            return True
        return False

    '''
    This method moves the enemy one step downwards
    '''
    def moveDown(self,x,y,screen):
        if self.isMoveDown(x,y,screen):
            for i in range (x,x+2):
                for j in range(y,y+4):
                    screen[i][j] = ' '
            for i in range (x+2,x+4):
                for j in range(y,y+4):
                    screen[i][j] = 'E'
            return True
        return False

    '''
    This method generates random motion in all the enemies
    which are on the board. Number of Enemies depends on the
    level of the game.
    '''
    def randomMotion(self,position,screen,wall,level):
        pos = self.getEnemyPos()
        for i in range(0,self.getNumEnemies()):
            for j in range(1):
                if pos[i][0]>0 and pos[i][1]>0:
                    count = 0
                    while count<30:
                        direction = random.randint(1,5)
                        if direction==1:
                            if self.moveUp(pos[i][0],pos[i][1],screen):
                                pos[i][0]-=2
                                break

                        elif direction==2:
                            if self.moveDown(pos[i][0],pos[i][1],screen):
                                pos[i][0]+=2
                                break

                        elif direction==3:
                            if self.moveRight(pos[i][0],pos[i][1],screen):
                                pos[i][1]+=4
                                break

                        elif direction==4:
                            if self.moveLeft(pos[i][0],pos[i][1],screen):
                                pos[i][1]-=4
                                break
                        count+=1
                    if count==30:
                        x = random.randint(10,36)
                        y = random.randint(12,72)
                        if self.isAccomodateEnemy(x,y,screen) and  ((x%4==2 and y%4==0) or (x%4==0 and y%8==4)):
                            for p in range(x,x+2):
                                for q in range(y,y+4):
                                    screen[p][q] = 'E'
                            pos[i][0],pos[i][1]=x,y
        self.setEnemyPos(pos)
