from ortools.sat.python import cp_model
import numpy as np
import math
from BoardnPieces import piecesDict, initBoard

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
            # loop all posible position of upper left square of the piece
            for u in range(piece.shape[0]):
                for v in range(piece.shape[1]):
                    # loop all squares in the piece
                    if piece[u, v] == 1:
                        coverMat[i+u, j+v] += ULCPos[i, j]
    coverMatDict[f'{pieceName}CoverMat'] = coverMat
    return coverMat, ULCPos


def checkIfUsed(name, board, solver):
    for i in range(board.shape[0]):
        for j in range(board.shape[1]):
            if solver.Value(coverMatDict[f'{name}CoverMat'][i, j]):
                return True
    return False


def printPiece(name, board, solver):
    print(name)
    for i in range(board.shape[0]):
        for j in range(board.shape[1]):
            print(solver.Value(coverMatDict[f'{name}CoverMat'][i, j]), end=" ")
        print()


if __name__=="__main__":
    board = inp(smallerSize=False)
    model = cp_model.CpModel()
    sumCover = boardSizeNPArrMLinExpr()
    for pieceName in piecesDict:
        sumULCPos = boardSizeNPArrMLinExpr()
        thisPieceDict = piecesDict[pieceName]
        for pieceRotatedName in thisPieceDict:
            coverMat, ULCPos = getCoverMatAndULCPos(model,
                                                    thisPieceDict[pieceRotatedName],
                                                    pieceRotatedName)
            sumCover += coverMat
            sumULCPos += ULCPos
        model.Add(sumULCPos.sum() <= 1)
        # 1 piece only has 1 rotation

    for i in range(board.shape[0]):
        for j in range(board.shape[1]):
            # every needed square is covered, otherwise non
            if board[i, j] == 1:
                model.Add(sumCover[i, j] == 1)
            else:
                model.Add(sumCover[i, j] == 0)
    
    solver = cp_model.CpSolver()
    status = solver.Solve(model)
    if status == cp_model.FEASIBLE or status == cp_model.OPTIMAL:
        for pieceName in piecesDict:
            thisPieceDict = piecesDict[pieceName]
            for pieceRotatedName in thisPieceDict:
                used = checkIfUsed(pieceRotatedName, board, solver)
                if used:
                    printPiece(pieceRotatedName, board, solver)
    else:
        print(f'status code: {status} - {solver.StatusName(status)}')