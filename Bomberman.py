from Person import *
from Bomb import *
class Bomberman(Person):
    '''
    This class contains all the states and methods of the
    Bomberman.
    '''
    def __init__(self):
        self.__score = 0
        self.__lifes = 3
        self.__level = 1
        self.__x = 2
        self.__y = 4
        self.__isBomb = False

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def setX(self,x):
        self.__x = x

    def setY(self,y):
        self.__y = y

    def isBomb(self):
        return self.__isBomb

    def setIsBomb(self,boolean):
        self.__isBomb = boolean

    def getScore(self):
        return self.__score

    def setScore(self,x):
        self.__score = x

    def getLifes(self):
        return self.__lifes

    def getLevel(self):
        return self.__level

    def setLifes(self,x):
        self.__lifes = x

    def increaseScore(self,score):
        self.__score+=score

    def decreaseLifes(self):
        self.__lifes-=1

    def increaseLevel(self):
        self.__level+=1

    '''
    This method places the bomberman on the Board
    '''
    def placeBomberman(self,x,y,screen):
        for i in range(x,x+2):
            for j in range(y,y+4):
                screen[i][j]='B'

    '''
    This method moves the bomberman one position to the right
    '''
    def moveRight(self,x,y,screen):
        if self.isMoveRight(x,y,screen):
            for i in range (x,x+2):
                for j in range(y,y+4):
                    screen[i][j] = ' '
            for i in range (x,x+2):
                for j in range(y+4,y+8):
                    screen[i][j] = 'B'
            return True
        return False

    '''
    This method moves the bomberman one position to the left
    '''
    def moveLeft(self,x,y,screen):
        if self.isMoveLeft(x,y,screen):
            for i in range (x,x+2):
                for j in range(y,y+4):
                    screen[i][j] = ' '
            for i in range (x,x+2):
                for j in range(y-4,y):
                    screen[i][j] = 'B'
            return True
        return False

    '''
    This method moves the bomberman one position upwards
    '''

    def moveUp(self,x,y,screen):
        if self.isMoveUp(x,y,screen):
            for i in range (x,x+2):
                for j in range(y,y+4):
                    screen[i][j] = ' '
            for i in range (x-2,x):
                for j in range(y,y+4):
                    screen[i][j] = 'B'
            return True
        return False

    '''
    This method moves the bomberman one position downwards
    '''
    def moveDown(self,x,y,screen):
        if self.isMoveDown(x,y,screen):
            for i in range (x,x+2):
                for j in range(y,y+4):
                    screen[i][j] = ' '
            for i in range (x+2,x+4):
                for j in range(y,y+4):
                    screen[i][j] = 'B'
            return True
        return False

    '''
    This method places the Bomb in the specified position
    '''
    def placeBomb(self,x,y,screen,char):
        bomb=Bomb(x,y)
        bomb.insertBomb(x,y,screen,char)
        return bomb
