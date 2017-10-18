import random
'''
This class contains the descrition of Blocks which
can be destroyed in an explosion
'''
class Blocks:
    '''
    This class contains only one method to place the
    destroyable blocks on the Board
    '''
    def insertBlocks(self,screen,player):
        blocksInserted = 0
        max_blocks = 10 + 5*player.getLevel() 
        while(blocksInserted<max_blocks):
            x = random.randint(2,34)
            y = random.randint(4,72)
            if ((x%4==2 and y%4==0) or (x%4==0 and y%8==4)) and screen[x][y]==' ':
                for i in range (x,x+2):
                    for j in range(y,y+4):
                        screen[i][j] = '/'
                blocksInserted+=1
