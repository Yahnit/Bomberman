'''
This class contains all the states and methods of Person
'''
class Person:
    '''
    This method checks if the person can move one step right
    '''
    def isMoveRight(self,x,y,screen):
        for i in range (x,x+2):
            for j in range(y+4,y+8):
                if screen[i][j]!= " " and screen[i][j]!="B":
                    return False
        return True

    '''
    This method checks if the person can move one step left
    '''
    def isMoveLeft(self,x,y,screen):
        for i in range (x,x+2):
            for j in range(y-4,y):
                if screen[i][j]!= " " and screen[i][j]!="B":
                    return False
        return True

    '''
    This method checks if the person can move one step upwards
    '''
    def isMoveUp(self,x,y,screen):
        for i in range (x-2,x):
            for j in range(y,y+4):
                if screen[i][j]!= " " and screen[i][j]!="B":
                    return False
        return True
    '''
    This method checks if the person can move one step downwards
    '''
    def isMoveDown(self,x,y,screen):
        for i in range (x+2,x+4):
            for j in range(y,y+4):
                if screen[i][j]!= " " and screen[i][j]!="B":
                    return False
        return True
