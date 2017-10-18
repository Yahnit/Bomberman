
class Bomb:
    '''
    This class contains the description of a Bomb.
    Several methods have been defined.
    '''
    def __init__(self,x,y):
        self.__bombTimer = 0
        self.__diffuseTimer = 0
        self.__explode = False
        self.__x = x
        self.__y = y
        self.__prevx = -1
        self.__prevy = -1

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def setX(self,x):
        self.__x = x

    def setY(self,y):
        self.__y = y

    def getPrevX(self):
        return self.__prevx

    def getPrevY(self):
        return self.__prevy

    def setPrevX(self,x):
        self.__prevx = x

    def setPrevY(self,y):
        self.__prevy = y

    def resetBombTimer(self):
        self.__bombTimer = 0

    def resetDiffuseTimer(self):
        self.__diffuseTimer = 0

    def incBombTimer(self):
        self.__bombTimer+=1

    def incDiffuseTimer(self):
        self.__diffuseTimer+=1

    def getBombTimer(self):
        return self.__bombTimer

    def getDiffuseTimer(self):
        return self.__diffuseTimer

    def isExplode(self):
        return self.__explode

    def setExplode(self,boolean):
        self.__explode = boolean

    #Method to insert a Bomb at a position
    def insertBomb(self,x,y,screen,char):
        if screen[x][y]=='B':
            return
        for i in range(x,x+2):
            for j in range(y,y+4):
                screen[i][j] = char
    '''
    After 3 frames of placing a bomb, explode Method is called
    It essentially destroys everything surrounding it.
    '''
    def explode(self,x,y,screen,player,enemy_pos):
        if screen[x][y]=='B':
            player.setLifes(0)
            return enemy_pos

        for i in range(x,x+2):
            for j in range(y,y+4):
                screen[i][j] = 'e'

        if screen[x-2][y]=='E':
            for i in range(4):
                if enemy_pos[i][0] == x-2 and enemy_pos[i][1]==y:
                        enemy_pos[i][0],enemy_pos[i][1] = -1,-1
                        break

        for i in range(x-2,x):
            for j in range(y,y+4):
                if i<38 and j<76:
                    if screen[i][j]=='/':
                        player.increaseScore(2.5)
                    elif screen[i][j]=='E':
                        player.increaseScore(12.5)
                    elif screen[i][j]=='B':
                        player.setLifes(0)
                    if screen[i][j]!='X':
                        screen[i][j]= ' '

        if screen[x+2][y]=='E':
            for i in range(4):
                if enemy_pos[i][0] == x+2 and enemy_pos[i][1]==y:
                        enemy_pos[i][0],enemy_pos[i][1] = -1,-1
                        break

        for i in range(x+2,x+4):
            for j in range(y,y+4):
                if i<38 and j<76:
                    if screen[i][j]=='/':
                        player.increaseScore(2.5)
                    elif screen[i][j]=='E':
                        player.increaseScore(12.5)
                    elif screen[i][j]=='B':
                        player.setLifes(0)
                    if screen[i][j]!='X':
                        screen[i][j]= ' '

        if screen[x][y-4]=='E':
            for i in range(4):
                if enemy_pos[i][0] == x and enemy_pos[i][1]==y-4:
                        enemy_pos[i][0],enemy_pos[i][1] = -1,-1
                        break

        for i in range(x,x+2):
            for j in range(y-4,y):
                if i<38 and j<76:
                    if screen[i][j]=='/':
                        player.increaseScore(2.5)
                    elif screen[i][j]=='E':
                        player.increaseScore(12.5)
                    elif screen[i][j]=='B':
                        player.setLifes(0)
                    if screen[i][j]!='X':
                        screen[i][j]= ' '

        if screen[x][y+4]=='E':
            for i in range(4):
                if enemy_pos[i][0] == x and enemy_pos[i][1]==y+4:
                        enemy_pos[i][0],enemy_pos[i][1] = -1,-1
                        break

        for i in range(x,x+2):
            for j in range(y+4,y+8):
                if i<38 and j<76:
                    if screen[i][j]=='/':
                        player.increaseScore(2.5)
                    elif screen[i][j]=='E':
                        player.increaseScore(12.5)
                    elif screen[i][j]=='B':
                        player.setLifes(0)
                    if screen[i][j]!='X':
                        screen[i][j]= ' '

        return enemy_pos

    '''
    After explosion happens, the positions are restored
    '''
    def diffuse(self,x,y,screen):
        for i in range(x,x+2):
            for j in range(y,y+4):
                screen[i][j] = ' '

    '''
    This method checks if bomb should explode or not.
    If the timer is reached, the bomb explodes.
    Else, the timer is increased
    '''
    def checkBombTimer(self,bomb,player,screen,enemy_pos):
        if bomb is not None and bomb.getX()>0 and bomb.getY()>0 and bomb.getBombTimer()!=4:
            bomb.incBombTimer()
            if bomb.getBombTimer()==1:
                bomb.insertBomb(bomb.getX(),bomb.getY(),screen,'3')
            elif bomb.getBombTimer()==2:
                bomb.insertBomb(bomb.getX(),bomb.getY(),screen,'2')
            elif bomb.getBombTimer()==3:
                bomb.insertBomb(bomb.getX(),bomb.getY(),screen,'1')
            elif bomb.getBombTimer()==4:
                bomb.insertBomb(bomb.getX(),bomb.getY(),screen,'0')

        elif bomb is not None and bomb.getBombTimer()==4 and bomb.getX()>0 and bomb.getY()>0:
            enemy_pos = bomb.explode(bomb.getX(),bomb.getY(),screen,player,enemy_pos)
            bomb.setExplode(True)
            bomb.resetBombTimer()
            bomb.resetDiffuseTimer()
            bomb.setPrevX(bomb.getX())
            bomb.setPrevY(bomb.getY())
            bomb.setX(-1)
            bomb.setY(-1)
        return enemy_pos
