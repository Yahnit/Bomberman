'''
    This is the main working code that inherits the classes from the tetris.py and uses them with an object instantiated.
'''
from tetris import *
import threading
import curses
import pygame
from pygame. locals import *
import readchar
import sys

pygame.init()
#Variable declaration
g=Gameplay()
lost=0
clearer=0
tile=g.showPiece(g.selectPiece())
X=0
Y=15
no_p=0
key_a=0
key_d=0
key_s=0
key_space=0

def update():
    ''' This is the function that would be called at regular interval for updating the BOARD and movements '''
    global X,Y,tile,lost,no_p,clearer
    if lost:
        print "score = %s" % g.getScore()
        return
    global key_a,key_d,key_s,key_space
    threading.Timer(g.getTime()/4,update).start()
    '''Repeat this process every second'''
    pygame.init()
    for event in pygame.event.get():
        if event.type==pygame.KEYUP:

            if event.key==pygame.K_d:
                key_d+=1

            if event.key==pygame.K_s:
                #tile=g.rotate(tile)
                key_s+=1

            if event.key==pygame.K_a:
                #print "a"
                key_a+=1

            if event.key==pygame.K_SPACE:
                key_space+=1
    '''checking KEY stroke'''
    if key_a>=2:
        key_a=0
        if g.checkPiecePos(tile,X+1,Y-1):
            Y-=1
    elif key_d>=2:
        key_d=0
        if g.checkPiecePos(tile,X+1,Y+1):
            Y+=1
    elif key_s>=2:
        key_s=0
        if g.checkPiecePos(g.rotate(tile),X+1,Y):
            tile=g.rotate(tile)
    elif key_space>=2:
        key_space=0
        while g.checkPiecePos(tile,int(X+1),int(Y)):
            X+=1

    #print key_s,key_d,key_a
    g.drawBoard(tile,int(X),int(Y))
    for i in xrange(30):
        if g.checkRowFull(i):
            g.EmptyRow(i)

    if (g.checkPiecePos(tile,int(X),int(Y))) & (g.checkPiecePos(tile,int(X+1),int(Y))): # if the block can move down, allow it to do so
        X+=1

    elif (g.checkPiecePos(tile,int(X),int(Y))) & (g.checkPiecePos(tile,int(X+1),int(Y))==0): # if the block cant move downwards,then its saturated and New block needs to be initiated
        no_p+=1
        g.fixPiece(tile,int(X),int(Y))
        #print "selecting piece"
        tile=g.showPiece(g.selectPiece())

        if clearer:#clearer block is on
            for i in xrange(4):
                for j in xrange(4):
                    if X+i>=30 or Y+j>=32:
                        pass
                    if g.board[X+i][Y+j]>1:
                        g.dfs_clear(X+i,Y+j)
                        clearer=0

        if no_p%30==0:# bring down the clearing block
            tile=g.showPiece(7)
            clearer=1
        g.updateScore(10*g.level)
        if g.checkPiecePos(tile,0,15)==0:
            if g.boardCompleted()==0:
                lost=1
            else:
                print "Moving to next round"
        X=0 #default starting point for the blocks
        Y=15



#the calling of the function
update()
