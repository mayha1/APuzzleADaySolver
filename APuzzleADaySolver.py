import gurobipy as gb
import numpy as np
from gurobipy import GRB
import math


INITBOARD = np.array([[1, 1, 1, 1, 1, 1, 0],
              [1, 1, 1, 1, 1, 1, 0],
              [1, 1, 1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1, 1, 1],
              [1, 1, 1, 0, 0, 0, 0]], np.int_)

rec1 = np.array([[1,1,1],
                [1,1,1]], np.int_)

rec2 = np.array([[1,1],
                 [1,1],
                 [1,1]], np.int_)

Tshape1 = np.array([[0, 1, 0],
                   [1, 1, 1]], np.int_)
# 0: no piece
# 1: piece

pieceList = {
    'rec': {
        'rec1': rec1,
        'rec2': rec2,
    },
    'Tshape': {
        'Tshape1': Tshape1
    }
}

def boardSizeNPArrMLinExpr():
    arr = np.empty(shape=board.shape, dtype=gb.MLinExpr)
    arr[:, :] = 0
    return arr

def inp():
    board = INITBOARD
    print('Input day number: ')
    day = int(input())
    board[math.floor((day-1)/7+2), (day-1)%7] = 0
    print('Input month number: ')
    month = int(input())
    board[math.floor((month-1)/6), (month-1)%6] = 0
    return board

def getCoverMat(model, piece, pieceName):
    ULCPos = model.addMVar(lb=0, ub=1, shape=board.shape,
                      vtype=GRB.INTEGER, name=pieceName+'Var')
    # a[i, j] == 1 means the upper left conner (ulc) lies on [i, j]
    coverMat = boardSizeNPArrMLinExpr()
    # CoverMat[i, j] == 1 means [i, j] contained in the piece

    for i in range(board.shape[0] - piece.shape[0] + 1):
        for j in range(board.shape[1] - piece.shape[1] + 1):
            # loop all posible position of upper left square of the piece
            for u in range(piece.shape[0]):
                for v in range(piece.shape[1]):
                    # loop all squares in the piece
                    if piece[u, v]:
                        coverMat[i+u, j+v] += ULCPos[i, j]
    
    return coverMat, ULCPos


if __name__=="__main__":
    board = inp()
    model = gb.Model()
    sumCover = boardSizeNPArrMLinExpr()
    for pieceName in pieceList:
        sumULCPos = boardSizeNPArrMLinExpr()
        thisPieceDict = pieceList[pieceName]
        for pieceRotatedName in thisPieceDict:
            coverMat, ULCPos = getCoverMat(model, thisPieceDict[pieceRotatedName], pieceRotatedName)
            sumCover += coverMat
            sumULCPos += ULCPos
        model.addConstr(sumULCPos.sum() <= 1)

    for i in range(board.shape[0]):
        for j in range(board.shape[1]):
            if board[i, j] == 1:
                model.addConstr(sumCover[i, j] == 1)
            else:
                model.addConstr(sumCover[i, j] == 0)
    
    model.update()
    model.optimize()
    print('*********************Covering:********************')
    print(sumCover)