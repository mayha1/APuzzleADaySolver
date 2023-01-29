import numpy as np

initBoard = np.array([[1, 1],
                      [1, 1],
                      [1, 1]], np.int_)

# Oshape
# Oshape = np.array([[1,1],
#                    [1,1]], np.int_)

# # Ishape
# IShape1 = np.array([[1,1]], np.int_)

# IShape2 = np.array([[1],
#                     [1]], np.int_)

# piecesDict = {
#     'OShape':{
#         'OShape': Oshape,
#     },
#     'IShape':{
#         'IShape1': IShape1,
#         'IShape2': IShape2,
#     },
# }

# LShape
LShape1 = np.array([[1, 1],
                    [1, 0]], np.int_)

LShape2 = np.array([[1, 1],
                    [0, 1]], np.int_)

LShape3 = np.array([[1, 0],
                    [1, 1]], np.int_)

LShape4 = np.array([[0, 1],
                    [1, 1]], np.int_)

piecesDict = {
    'LShape1':{
        'LShape11': LShape1,
        'LShape12': LShape2,
        'LShape13': LShape3,
        'LShape14': LShape4,
    },
    'LShape2':{
        'LShape21': LShape1,
        'LShape22': LShape2,
        'LShape23': LShape3,
        'LShape24': LShape4,
    }
}