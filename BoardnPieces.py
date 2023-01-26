import numpy as np
# Board
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


# TShape
TShape1 = np.array([[1, 1, 1],
                    [0, 1, 0]], np.int_)

TShape2 = np.array([[0, 1, 0],
                    [1, 1, 1]], np.int_)

TShape3 = np.array([[1, 0],
                    [1, 1],
                    [1, 0]], np.int_)

TShape4 = np.array([[0, 1],
                    [1, 1],
                    [0, 1]], np.int_)


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
                   [1, 0]
                   [1, 0],
                   [1, 0]], np.int_)

LShape6 = np.array([[1, 0],
                   [1, 0]
                   [1, 0],
                   [1, 1]], np.int_)

LShape = np.array([[1, 1],
                   [0, 1]
                   [0, 1],
                   [0, 1]], np.int_)

LShape = np.array([[0, 1],
                   [0, 1]
                   [0, 1],
                   [1, 1]], np.int_)

# JShape
JShape = np.array([[1, 1, 1, 1],
                   [0, 1, 0, 0]], np.int_)

JShape = np.array([[1, 1, 1, 1],
                   [0, 0, 1, 0]], np.int_)

JShape = np.array([[0, 0, 1, 0],
                   [1, 1, 1, 1]], np.int_)

JShape = np.array([[0, 1, 0, 0],
                   [1, 1, 1, 1]], np.int_)

JShape = np.array([[1, 0],
                   [1, 1]
                   [1, 0],
                   [1, 0]], np.int_)

JShape = np.array([[1, 0],
                   [1, 0]
                   [1, 1],
                   [1, 0]], np.int_)

JShape = np.array([[0, 1],
                   [0, 1]
                   [1, 1],
                   [0, 1]], np.int_)

JShape = np.array([[0, 1],
                   [1, 1]
                   [0, 1],
                   [0, 1]], np.int_)

# ZShape
ZShape = np.array([[1, 1, 1, 0],
                   [0, 0, 1, 1]], np.int_)

ZShape = np.array([[0, 1, 1, 1],
                   [1, 1, 0, 0]], np.int_)

ZShape = np.array([[1, 1, 0, 0],
                   [0, 1, 1, 1]], np.int_)

ZShape = np.array([[0, 0, 1, 1],
                   [1, 1, 1, 0]], np.int_)

ZShape = np.array([[1, 0],
                   [1, 0]
                   [1, 1],
                   [0, 1]], np.int_)

ZShape = np.array([[0, 1],
                   [1, 1]
                   [1, 0],
                   [1, 0]], np.int_)

ZShape = np.array([[0, 1],
                   [0, 1]
                   [1, 1],
                   [1, 0]], np.int_)

ZShape = np.array([[1, 0],
                   [1, 1]
                   [0, 1],
                   [0, 1]], np.int_)

# VShape
VShape = np.array([[1, 1, 1],
                   [1, 0, 0],
                   [1, 0, 0]])

VShape = np.array([[1, 0, 0],
                   [1, 0, 0],
                   [1, 1, 1]])

VShape = np.array([[1, 1, 1],
                   [1, 0, 0],
                   [1, 0, 0]])

VShape = np.array([[1, 1, 1],
                   [1, 0, 0],
                   [1, 0, 0]])

