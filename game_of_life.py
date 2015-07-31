# -*- coding: utf-8 -*-
"""
Conway's Game of Life

Created on Mon Dec 01 13:36:30 2014

@author: davidmarx
"""

import numpy as np
import matplotlib.pyplot as plt

def gen_neighbors(pos, board_shape):
    """
    Given a set of input coordinates, get the coordinates of all neighboring 
    tiles.
    """
    ix2 = np.asarray(zip(*np.where(np.ones([3,3], dtype=int)))) -1
    ix = np.vstack([ix2[:4],ix2[5:]]) + pos
        
    for v in ix:
        if any(v<0) or any(v>=board_shape):
            continue
        yield v
        
def cell_neighbors_sum(cell, board):
    """
    Returns next state of an input cell on a given board.
    """    
    neighbors = np.asarray([n for n in gen_neighbors(cell, board.shape)])
    return board[zip(*neighbors)].sum()
    
def cell_next_state(cell, board):
    status = cell_neighbors_sum(cell, board)
    result = 0
    if not board[cell[0], cell[1]] and status == 3:
        result = 1
    if status in (2,3):
        result = 1
    return result

def next_board(board):
    m,n = board.shape
    newboard = np.empty_like(board, dtype=int)
    # would be nice if I could vectorize this
    for i in range(m):
        for j in range(n):
            result = cell_next_state(np.array([i,j]), board)
            newboard[i,j] = result
    return newboard
            
if __name__ == "__main__":
    import time
    k=50
    board = np.zeros([k,k])
    board[0,:] = np.random.randint(2, size=[1,k])
    board[1,:] = np.random.randint(2, size=[1,k])
    #board = np.random.randint(2, size=[20,20])
    while True:
        print board, '\n\n'

        plt.imshow(board)
        plt.show()
        board = next_board(board)
        time.sleep(.5)