class board:
    '''
    This class contains the description of the board.
    A board has a certain length and breadth.
    It has methods to update its attributes
    '''
    def __init__(self):
        self.__length = 76
        self.__width = 38

    def getLength(self):
        return self.__length

    def getWidth(self):
        return self.__width

    def setLength(self,x):
        self.__length = x

    def setWidth(self,y):
        self.__width = y

    def makeBoard(self):
        board = [[' ' for x in range(0,76)] for y in range(0,38)]
        return board
