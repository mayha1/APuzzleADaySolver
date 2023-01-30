import matplotlib.pyplot as plt
from ortools.sat.python import cp_model
import seaborn as sns
import numpy as np
import math
from BoardnPieces import piecesDict, initBoard

visualSymbols = ['*', '+', '@', '~', '&', '-', '=', '%']
coverMatDict = {}


def boardSizeNPArrMLinExpr():
    arr = np.empty(shape=initBoard.shape, dtype=cp_model.LinearExpr)
    arr[:, :] = 0
    return arr


def inp(smallerSize=False):
    board = initBoard
    if smallerSize:
        return board
    print('Input day number: ')
    day = int(input())
    board[math.floor((day-1)/7+2), (day-1)%7] = 0
    print('Input month number: ')
    month = int(input())
    board[math.floor((month-1)/6), (month-1)%6] = 0
    return board


def getCoverMatAndULCPos(model, piece, pieceName):
    ULCPos = np.empty(initBoard.shape, dtype=cp_model.IntVar)
    for i in range(ULCPos.shape[0]):
        for j in range(ULCPos.shape[1]):
            ULCPos[i, j] = model.NewIntVar(0, 1, f'{pieceName}Var_{i}_{j}')
    # ULCPos[i, j] == 1 means the upper left conner (ulc) lies on [i, j]
    
    coverMat = boardSizeNPArrMLinExpr()
    # CoverMat[i, j] == 1 means [i, j] contained in the piece

    for i in range(initBoard.shape[0] - piece.shape[0] + 1):
        for j in range(initBoard.shape[1] - piece.shape[1] + 1):
            # Loop all posible position of upper left square of the piece
            for u in range(piece.shape[0]):
                for v in range(piece.shape[1]):
                    # Loop all squares in the piece
                    if piece[u, v] == 1:
                        coverMat[i+u, j+v] += ULCPos[i, j]
    coverMatDict[f'{pieceName}CoverMat'] = coverMat
    return coverMat, ULCPos


def isUsed(name, board, solver):
    for i in range(board.shape[0]):
        for j in range(board.shape[1]):
            if solver.Value(coverMatDict[f'{name}CoverMat'][i, j]):
                return True
    return False


if __name__=="__main__":
    board = inp(smallerSize=False)
    model = cp_model.CpModel()
    sumCover = boardSizeNPArrMLinExpr()
    for pieceName in piecesDict:
        sumULCPos = boardSizeNPArrMLinExpr()
        pieceRotationsDict = piecesDict[pieceName]
        for pieceRotation in pieceRotationsDict:
            coverMat, ULCPos = getCoverMatAndULCPos(model,
                                                    pieceRotationsDict[pieceRotation],
                                                    pieceRotation)
            sumCover += coverMat
            sumULCPos += ULCPos
        model.Add(sumULCPos.sum() <= 1)
        # 1 piece only has 1 rotation

    for i in range(board.shape[0]):
        for j in range(board.shape[1]):
            # Every needed square is covered, otherwise non
            if board[i, j] == 1:
                model.Add(sumCover[i, j] == 1)
            else:
                model.Add(sumCover[i, j] == 0)
    
    solver = cp_model.CpSolver()
    status = solver.Solve(model)
    if status == cp_model.FEASIBLE or status == cp_model.OPTIMAL:
        count = 1
        solution = np.zeros(shape=initBoard.shape)
        for pieceName in piecesDict:
            pieceRotationsDict = piecesDict[pieceName]
            for pieceRotation in pieceRotationsDict:
                if isUsed(pieceRotation, board, solver):
                    for i in range(board.shape[0]):
                        for j in range(board.shape[1]):
                            if solver.Value(coverMatDict[f'{pieceRotation}CoverMat'][i, j]) == 1:
                                solution[i][j] = count
            count += 1
        # Visualize solution
        sns.heatmap(solution, cmap='Reds', cbar=False, linewidth = 0.5, 
                    square=True, xticklabels=False, yticklabels=False)
        plt.show()
    else:
        print(f'status code: {status} - {solver.StatusName(status)}')