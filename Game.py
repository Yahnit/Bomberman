#IMPORTS
from __future__ import print_function
import signal
from time import time
from colorama import Fore
import random,os
from Person import *
from alarmexception import *
from Blocks import *
from Bomberman import *
from Enemy import *
from Person import *
from getchunix import *
from Wall import *
from Board import *
from alarmexception import *
getch  = GetchUnix()

'''
The following code initializes the Game
'''
bomb = None
b = board()
Board = b.makeBoard()
wall = Wall()
wall.insertWall(Board)
blocks = Blocks()
player = Bomberman()
blocks.insertBlocks(Board,player)
player.placeBomberman(player.getX(),player.getY(),Board)
enemy = Enemy()
enemy.generateEnemy(Board,enemy.getNumEnemies())

def hello():
    print("Hello")

def alarmHandler(signum, frame):
    raise AlarmException
'''
Function which takes input from the user and returns it
'''
def input_to(timeout=1):
    signal.signal(signal.SIGALRM, alarmHandler)
    signal.alarm(timeout)
    try:
        text = getch()
        signal.alarm(0)
        return text
    except AlarmException:
        print("\n ")
    signal.signal(signal.SIGALRM, signal.SIG_IGN)
    return ''

'''
This function updates the board on the  terminal
'''
def updateBoard():
    os.system('clear')
    wall.displayBoard(Board)
    print(Fore.BLACK+"Press q to exit the game")
    print (Fore.BLACK+"Lifes left: "+ str(int(player.getLifes())))
    print (Fore.BLACK+"Score:" + str(int(player.getScore())))
    print (Fore.BLACK+"Level:" + str(int(player.getLevel())))

updateBoard()

while True:
    #Generate random movement in the enemies
    enemy.randomMotion(enemy.getEnemyPos(),Board,wall,player.getLevel())

    '''
    The below code decreases the number of lifes of a person
    when he collides with an enemy.
    '''


    for i in range(enemy.getNumEnemies()):
        if (enemy.getEnemyPos()[i][0]==player.getX() and enemy.getEnemyPos()[i][1]==player.getY()):
            updateBoard()
            temp = player.getScore()
            b = board()
            Board = b.makeBoard()
            wall = Wall()
            wall.insertWall(Board)
            blocks = Blocks()
            blocks.insertBlocks(Board,player)
            enemy = Enemy()
            enemy.setNumEnemies(4*player.getLevel())
            enemy.generateEnemy(Board,enemy.getNumEnemies())
            player.setIsBomb(False)
            player.decreaseLifes()
            player.setScore(temp)
            player.setX(2)
            player.setY(4)
            player.placeBomberman(player.getX(),player.getY(),Board)
            print("Enemy has killed you!")
            time.sleep(2)
            updateBoard()
            break

    '''
    If the lifes of a person are over, the below code checks if
    the player has more than a cutoff score which takes him to
    the next level.
    If he does'nt reach the cut-off score , the game is over
    '''
    if player.getLifes()==0:
        if player.getScore() > player.getLevel()*200:
            b = board()
            Board = b.makeBoard()
            wall = Wall()
            wall.insertWall(Board)
            blocks = Blocks()
            player.increaseLevel()
            blocks.insertBlocks(Board,player)
            enemy = Enemy()
            player.setIsBomb(False)
            player.setLifes(3)
            player.setScore(0)
            player.setX(2)
            player.setY(4)
            player.placeBomberman(player.getX(),player.getY(),Board)
            enemy.setNumEnemies(4*player.getLevel())
            enemy.generateEnemy(Board,enemy.getNumEnemies())
            enemy.randomMotion(enemy.getEnemyPos(),Board,wall,player.getLevel())
            print("Congrats! You have cleared Level: " +str(player.getLevel()-1) )
            time.sleep(3)
            updateBoard()
        else:
            os.system('clear')
            wall.displayBoard(Board)
            print(Fore.BLACK+"Game Over")
            print (Fore.BLACK+"Score:" + str(int(player.getScore())))
            exit()


    '''
    Below code checks if the bomb is exploded or not.
    If the bomb is exploded, 'e' is displayed in that place
    '''
    if bomb is not None and  bomb.isExplode() and bomb.getDiffuseTimer()==0:
        bomb.incDiffuseTimer()
        bomb.diffuse(bomb.getPrevX(),bomb.getPrevY(),Board)
        player.setIsBomb(False)
        bomb.setExplode(False)
        bomb.setPrevX(-1)
        bomb.setPrevY(-1)
        bomb.resetDiffuseTimer()

    '''
    The below code checks the timer of the bomb.
    If 3 frames are done after the bomb is placed, the bomb is exploded
    Else, the timer of the bomb is increased
    '''
    if player.isBomb():
        bomb.checkBombTimer(bomb,player,Board,enemy.getEnemyPos())
    updateBoard()

    '''
    Below code takes input from the user and does the
    relevant operations
    '''
    timeout = float(1.00/player.getLevel())
    inpt = input_to()
    '''
    If the player presses 's','w','a,'d', respective function is called
    which essentially checks if the player can be moved to
    the position. If there are any obstacles, movement does
    not happen.
    '''
    if inpt == 's' or inpt == 'S':
        if player.moveDown(player.getX(),player.getY(),Board):
            player.setX(player.getX()+2)


    elif inpt == 'w'or inpt=='W':
        if player.moveUp(player.getX(),player.getY(),Board):
            player.setX(player.getX()-2)

    elif inpt == 'a' or inpt == 'A':
        if player.moveLeft(player.getX(),player.getY(),Board):
            player.setY(player.getY()-4)

    elif inpt == 'd' or inpt == 'D':
        if player.moveRight(player.getX(),player.getY(),Board):
            player.setY(player.getY()+4)


    elif inpt == 'b' or inpt == 'B':
        if not player.isBomb():
            bomb = player.placeBomb(player.getX(),player.getY(),Board,'3')
            bomb.setX(player.getX())
            bomb.setY(player.getY())
            bomb.resetBombTimer()
            player.setIsBomb(True)

    if inpt == 'q' or inpt == 'Q':
        exit()
