import numpy as np

# initBoard = np.array([[1, 1],
#                       [1, 1],
#                       [1, 1]], np.int_)

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
# LShape1 = np.array([[1, 1],
#                     [1, 0]], np.int_)

# LShape2 = np.array([[1, 1],
#                     [0, 1]], np.int_)

# LShape3 = np.array([[1, 0],
#                     [1, 1]], np.int_)

# LShape4 = np.array([[0, 1],
#                     [1, 1]], np.int_)

# piecesDict = {
#     'LShape1':{
#         'LShape11': LShape1,
#         'LShape12': LShape2,
#         'LShape13': LShape3,
#         'LShape14': LShape4,
#     },
#     'LShape2':{
#         'LShape21': LShape1,
#         'LShape22': LShape2,
#         'LShape23': LShape3,
#         'LShape24': LShape4,
#     }
# }

initBoard = np.array([[1, 1, 1],
                      [1, 1, 1],
                      [1, 1, 1]], np.int_)

# LShape
LShape1 = np.array([[1, 1, 1],
                    [1, 0, 0]], np.int_)

LShape2 = np.array([[1, 1, 1],
                    [0, 0, 1]], np.int_)

LShape3 = np.array([[1, 0, 0],
                    [1, 1, 1]], np.int_)

LShape4 = np.array([[0, 0, 1],
                    [1, 1, 1]], np.int_)

LShape5 = np.array([[1, 1],
                    [1, 0],
                    [1, 0]], np.int_)

LShape6 = np.array([[1, 0],
                    [1, 0],
                    [1, 1]], np.int_)

LShape7 = np.array([[1, 1],
                    [0, 1],
                    [0, 1]], np.int_)

LShape8 = np.array([[0, 1],
                    [0, 1],
                    [1, 1]], np.int_)

# GunShape
GunShape1 = np.array([[1, 1, 1],
                      [1, 1, 0]], np.int_)

GunShape2 = np.array([[1, 1, 0],
                      [1, 1, 1]], np.int_)

GunShape3 = np.array([[1, 1, 1],
                      [0, 1, 1]], np.int_)

GunShape4 = np.array([[0, 1, 1],
                      [1, 1, 1]], np.int_)

GunShape5 = np.array([[1, 1],
                      [1, 1],
                      [1, 0]], np.int_)

GunShape6 = np.array([[1, 1],
                      [1, 1],
                      [0, 1]], np.int_)

GunShape7 = np.array([[1, 0],
                      [1, 1],
                      [1, 1]], np.int_)

GunShape8 = np.array([[0, 1],
                      [1, 1],
                      [1, 1]], np.int_)

piecesDict = {
    'GunShape':
        {
            'GunShape1': GunShape1,
            'GunShape2': GunShape2,
            'GunShape3': GunShape3,
            'GunShape4': GunShape4,
            'GunShape5': GunShape5,
            'GunShape6': GunShape6,
            'GunShape7': GunShape7,
            'GunShape8': GunShape8
            },
    'LShape':
        {
            'LShape1': LShape1,
            'LShape2': LShape2,
            'LShape3': LShape3,
            'LShape4': LShape4,
            'LShape5': LShape5,
            'LShape6': LShape6,
            'LShape7': LShape7,
            'LShape8': LShape8
            }
    }
