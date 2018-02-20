#8×8 checkerboard

'''
class checkerboard:
    def desk (checkerboard):
        checkerboard = [[0, 1, 0, 1, 0, 1, 0, 1],
                        [1, 0, 1, 0, 1, 0, 1, 0],
                        [0, 1, 0, 1, 0, 1, 0, 1],
                        [1, 0, 1, 0, 1, 0, 1, 0],
                        [0, 1, 0, 1, 0, 1, 0, 1],
                        [1, 0, 1, 0, 1, 0, 1, 0],
                        [0, 1, 0, 1, 0, 1, 0, 1],
                        [1, 0, 1, 0, 1, 0, 1, 0]]
        return checkerboard
'''
from pprint import pprint

black = 1
white = 0
b = black
w = white
row = (b,w)*4
row2=(w,b)*4
#print (row, row2)
board =  ((row, row2)*4)
pprint (board)

