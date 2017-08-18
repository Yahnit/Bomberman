'''
    This file contains all class definition and their working
    Also a README is specified that cotains all salient features of the implementation.
'''

import numpy as np
import random
import curses
import pygame

'''
    All norms as specified in the questions have been seen to.
    Also lots of new functions have been added.
'''
class Board(object):
    '''
        As told, this contains the basic Board definition and functions for checking and filling pieces
    '''
    def __init__(self):
        super(Board,self).__init__()
        self.board=np.zeros((30,32))
        self.__score__=0
        #this class essentially checks the pices and filling

    def getScore(self):
        return self.__score__

    def checkPiecePos(self,piece,x,y):
        #checking if a piece could be kept @ place with left most co-ordinated X,y
        for i in xrange(4):
            for j in xrange(4):
                if ((i+x>=30) or (j+y>=32)) and (int(piece[i][j])>=1):
                    return 0
                elif (i+x<0) or (j+y<0):
                    pass
                elif (i+x<30) & (j+y<32) & (int(piece[i][j])>=1):
                     if int(self.board[i+x][j+y]):
                         return 0
        return 1

    def fillPiecePos(self,piece,x,y):
        board=np.copy(self.board)
        #fill that part of board with that piece
        for i in xrange(4):
            for j in xrange(4):
                if (i+x<0) or (j+y<0):
                    pass
                elif (i+x>=30) or (j+y>=32) or self.board[i+x][j+y]:
                    pass
                elif (piece[i][j]>=1):
                    board[i+x][j+y]=piece[i][j]
        return board


class Block(object):
    '''
        This class contains the description of the pieces and their motion and also their fitting a situation
    '''
    #this class makes the motion in the pieces
    def __init__(self):
        super(Block,self).__init__()
        self.pieces=[]

        #type 1
        a=np.zeros((4,4))
        for i in xrange(4):
            a[i][2]=1
        self.pieces=np.append(self.pieces,a)

        #type 2
        a=np.zeros((4,4))
        for i in xrange(3):
            a[i][2]=1
        a[2][1]=1
        self.pieces=np.append(self.pieces,a)

        #type 3
        a=np.zeros((4,4))
        for i in xrange(3):
            a[i][1]=1
        a[2][2]=1
        self.pieces=np.append(self.pieces,a)

        #type 4
        a=np.zeros((4,4))
        a[1][1]=1
        a[1][2]=1
        a[2][1]=1
        a[2][2]=1
        self.pieces=np.append(self.pieces,a)

        #type 5
        a=np.zeros((4,4))
        a[1][0]=1
        a[1][1]=1
        a[2][1]=1
        a[2][2]=1
        self.pieces=np.append(self.pieces,a)

        #type 6
        a=np.zeros((4,4))
        a[1][3]=1
        a[1][2]=1
        a[2][1]=1
        a[2][2]=1
        self.pieces=np.append(self.pieces,a)

        #type 7
        a=np.zeros((4,4))
        a[1][2]=1
        for i in xrange(3):
            a[2][i+1]=1
        self.pieces=np.append(self.pieces,a)


        #type 8 - bonus
        a=np.zeros((4,4))
        a[1][1]=2
        self.pieces=np.append(self.pieces,a)

        self.pieces=self.pieces.reshape(8,4,4)

        #all pieces made


    def rotate(self,piece_rot):
        #id is the ID of the piece [1-7]
        piece_rot=np.array(piece_rot)
        piece=np.copy(piece_rot)
        rot=np.copy(piece_rot)
        for i in xrange(4):
            for j in xrange(4):
                rot[i][j]=piece[3-j][i]
        return rot

    def moveLeft(self,x,y):
        if y==0:
            return x,y
        return x,y-1

    def moveRight(self,x,y):
        if y==31:
            return x,y
        return x,y+1

    def showPiece(self,i):
        return self.pieces[i]

    def __draw__(self,matrix):
        #for pygame
        font = pygame.font.SysFont(None, 25)
        def message(gameDisplay,msg, color):
            text = font.render(msg, True, color)
            gameDisplay.blit(text, [0,0])


        matrix=np.array(matrix)
        pygame.init()
        white=(255,255,255)
        black=(0,0,0)
        red=(255,0,0)
        green=(0,255,0)
        grey=(127,127,127)
        row=matrix.shape[0]
        col=matrix.shape[1]
        gameDisplay=pygame.display.set_mode((480,450))
        pygame.display.set_caption('Tetris')
        gameDisplay.fill(black)
        #message(gameDisplay,"Hi",red)
        msg="Score : "+str(self.__score__)+" & level : "+str(self.level)
        message(gameDisplay,msg,white)
        for i in xrange(row):
            for j in xrange(col):
                if int(matrix[i][j])==1:
                    pygame.draw.rect(gameDisplay,red,[j*15,i*15,15,15])
                elif int(matrix[i][j])>1:
                    pygame.draw.rect(gameDisplay,green,[j*15,i*15,15,15])
        pygame.display.update()



'''

    The Gameplay is the main class of the entire show that inherits properties
    from Board and Block
    It contains functions for checking Row completion and defines the speed of
    the particle and also updates score

'''
'''
    *********
    The highlight question that was answered(BONUS) is the presence of a BOMB particle that
    clears the board in such a way that it clears
    all the connected components to its falling position.
    This has been implemented as a DFS(dfs_clear).
    *********
'''

class Gameplay(Board,Block):

    def __init__(self):
        #initialising the class
        super(Gameplay,self).__init__()
        self.level=1

    def checkRowFull(self,row):
        #checking if row is full
        for i in xrange(32):
            if self.board[row][i]!=1:
                return 0
        self.__score__+=100*int(self.level)
        return 1

    def EmptyRow(self,row):
        for i in xrange(row):
            for j in xrange(32):
                self.board[row-i][j]=self.board[row-1-i][j]
        for j in xrange(32):
            self.board[0][j]=0

    def checkRowEmpty(self,row):
        #checking if row is empty
        for i in xrange(32):
            if self.board[row][i]!=0:
                return 0
        return 1

    def updateScore(self,score):
        #updateScore
        self.__score__+=score

    def selectPiece(self):
        #there are 6 possibilities for the next piece
        return random.randint(0,6)

    def drawBoard(self,piece,x,y):
        board=np.copy(self.fillPiecePos(piece,x,y))
        self.__draw__(board)

    def fixPiece(self,piece,x,y):
        for i in xrange(4):
            for j in xrange(4):
                if piece[i][j]>=1:
                    self.board[i+x][j+y]=piece[i][j]

    def getTime(self):
        #gives the time gap between successive blocks
        return 1.0/self.level

    def boardCompleted(self):
        self.board=np.zeros((30,32))
        if self.__score__>200*self.level:
            self.level+=1
            return 1
        return 0

    def dfs_clear(self,x,y):
        if x<0 or x>=30:
            return
        if y<0 or y>=32:
            return
        if self.board[x][y]==0:
            return
        self.board[x][y]=0
        self.dfs_clear(x,y+1)
        self.dfs_clear(x,y-1)
        self.dfs_clear(x+1,y)
        self.dfs_clear(x-1,y)


'''
    Class definition DONE!
'''
