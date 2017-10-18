from __future__ import print_function
from colorama import Fore
from termcolor import colored
'''
This class contains all the methods and states of Wall
'''
class Wall:
	'''
	This methods inserts wall on the Board which cannot be
	destroyed in an explosion
	'''
	def insertWall(self,screen):
		for i in range(0,2):
			for j in range(0,76):
				screen[i][j] = 'X'

		for i in range(2,36):
			for j in range(0,4):
				screen[i][j] = 'X'

		for i in range(2,36):
			for j in range(72,76):
				screen[i][j] = 'X'

		for i in range(36,38):
			for j in range(0,76):
				screen[i][j] = 'X'

		for i in range(2,36):
			if i%4==1 or i%4==0:
				for j in range(4,72):
					if j%8==3 or j%8==2 or j%8==1 or j%8==0:
						screen[i][j] = 'X'

	'''
	This method displays the Board, it essentially prints
	the board on the terminal
	'''

	def displayBoard(self,screen):
		for i in range(0,38):
			for j in range(0,76):
				if screen[i][j] == 'X':
					print(Fore.YELLOW+screen[i][j],end='')
				elif screen[i][j] == '/':
					print(Fore.BLUE+screen[i][j],end='')
				elif screen[i][j] == 'B':
					print(Fore.GREEN+screen[i][j],end='')
				elif screen[i][j] == 'E':
					print(Fore.RED+screen[i][j],end='')
				elif screen[i][j] == 'e':
					print(Fore.MAGENTA+screen[i][j],end='')
				else:
					print(Fore.CYAN+screen[i][j],end='')
			print()
