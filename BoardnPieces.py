import numpy as np

initBoard = np.array([[1, 1, 1, 1, 1, 1, 0],
                      [1, 1, 1, 1, 1, 1, 0],
                      [1, 1, 1, 1, 1, 1, 1],
                      [1, 1, 1, 1, 1, 1, 1],
                      [1, 1, 1, 1, 1, 1, 1],
                      [1, 1, 1, 1, 1, 1, 1],
                      [1, 1, 1, 0, 0, 0, 0]], np.int_)

# OShape
OShape1 = np.array([[1, 1, 1],
                    [1, 1, 1]], np.int_)

OShape2 = np.array([[1, 1],
                    [1, 1],
                    [1, 1]], np.int_)

# bigZShape
bigZShape1 = np.array([[1, 1, 0],
                       [0, 1, 0],
                       [0, 1, 1]], np.int_)

bigZShape2 = np.array([[0, 1, 1],
                       [0, 1, 0],
                       [1, 1, 0]], np.int_)

bigZShape3 = np.array([[1, 0, 0],
                       [1, 1, 1],
                       [0, 0, 1]], np.int_)

bigZShape4 = np.array([[0, 0, 1],
                       [1, 1, 1],
                       [1, 0, 0]], np.int_)

# UShape
UShape1 = np.array([[1, 1, 1],
                    [1, 0, 1]], np.int_)

UShape2 = np.array([[1, 0, 1],
                    [1, 1, 1]], np.int_)

UShape3 = np.array([[1, 1],
                    [0, 1],
                    [1, 1]], np.int_)

UShape4 = np.array([[1, 1],
                    [1, 0],
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

# LShape
LShape1 = np.array([[1, 1, 1, 1],
                    [1, 0, 0, 0]], np.int_)

LShape2 = np.array([[1, 1, 1, 1],
                    [0, 0, 0, 1]], np.int_)

LShape3 = np.array([[1, 0, 0, 0],
                    [1, 1, 1, 1]], np.int_)

LShape4 = np.array([[0, 0, 0, 1],
                    [1, 1, 1, 1]], np.int_)

LShape5 = np.array([[1, 1],
                    [1, 0],
                    [1, 0],
                    [1, 0]], np.int_)

LShape6 = np.array([[1, 0],
                    [1, 0],
                    [1, 0],
                    [1, 1]], np.int_)

LShape7 = np.array([[1, 1],
                    [0, 1],
                    [0, 1],
                    [0, 1]], np.int_)

LShape8 = np.array([[0, 1],
                    [0, 1],
                    [0, 1],
                    [1, 1]], np.int_)

# JShape
JShape1 = np.array([[1, 1, 1, 1],
                    [0, 1, 0, 0]], np.int_)

JShape2 = np.array([[1, 1, 1, 1],
                    [0, 0, 1, 0]], np.int_)

JShape3 = np.array([[0, 1, 0, 0],
                    [1, 1, 1, 1]], np.int_)

JShape4 = np.array([[0, 0, 1, 0],
                    [1, 1, 1, 1]], np.int_)

JShape5 = np.array([[1, 0],
                    [1, 1],
                    [1, 0],
                    [1, 0]], np.int_)

JShape6 = np.array([[1, 0],
                    [1, 0],
                    [1, 1],
                    [1, 0]], np.int_)

JShape7 = np.array([[0, 1],
                    [0, 1],
                    [1, 1],
                    [0, 1]], np.int_)

JShape8 = np.array([[0, 1],
                    [1, 1],
                    [0, 1],
                    [0, 1]], np.int_)

# ZShape
ZShape1 = np.array([[1, 1, 1, 0],
                    [0, 0, 1, 1]], np.int_)

ZShape2 = np.array([[0, 1, 1, 1],
                    [1, 1, 0, 0]], np.int_)

ZShape3 = np.array([[1, 1, 0, 0],
                    [0, 1, 1, 1]], np.int_)

ZShape4 = np.array([[0, 0, 1, 1],
                    [1, 1, 1, 0]], np.int_)

ZShape5 = np.array([[1, 0],
                    [1, 0],
                    [1, 1],
                    [0, 1]], np.int_)

ZShape6 = np.array([[0, 1],
                    [1, 1],
                    [1, 0],
                    [1, 0]], np.int_)

ZShape7 = np.array([[0, 1],
                    [0, 1],
                    [1, 1],
                    [1, 0]], np.int_)

ZShape8 = np.array([[1, 0],
                    [1, 1],
                    [0, 1],
                    [0, 1]], np.int_)

# VShape
VShape1 = np.array([[1, 1, 1],
                    [1, 0, 0],
                    [1, 0, 0]])

VShape2 = np.array([[1, 0, 0],
                    [1, 0, 0],
                    [1, 1, 1]])

VShape3 = np.array([[1, 1, 1],
                    [1, 0, 0],
                    [1, 0, 0]])

VShape4 = np.array([[1, 1, 1],
                    [1, 0, 0],
                    [1, 0, 0]])

piecesDict = {
    'OShape':
        {
            'OShape1': OShape1,
            'OShape2': OShape2
            },
    'bigZShape':
        {
            'bigZShape1': bigZShape1,
            'bigZShape2': bigZShape2,
            'bigZShape3': bigZShape3,
            'bigZShape4': bigZShape4
            },
    'UShape':
        {
            'UShape1': UShape1,
            'UShape2': UShape2,
            'UShape3': UShape3,
            'UShape4': UShape4
            },
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
            },
    'ZShape':
        {
            'ZShape1': ZShape1,
            'ZShape2': ZShape2,
            'ZShape3': ZShape3,
            'ZShape4': ZShape4,
            'ZShape5': ZShape5,
            'ZShape6': ZShape6,
            'ZShape7': ZShape7,
            'ZShape8': ZShape8
            },
    'JShape':
        {
            'JShape1': JShape1,
            'JShape2': JShape2,
            'JShape3': JShape3,
            'JShape4': JShape4,
            'JShape5': JShape5,
            'JShape6': JShape6,
            'JShape7': JShape7,
            'JShape8': JShape8
            },
    'VShape':
        {
            'VShape1': VShape1,
            'VShape2': VShape2,
            'VShape3': VShape3,
            'VShape4': VShape4
            }
    }
