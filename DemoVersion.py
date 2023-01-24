import gurobipy as gb
import numpy as np
from gurobipy import GRB

BOARDSIZE = (3, 2)

model = gb.Model()

# A1 vars
A1Vars = model.addMVar(lb=0, ub=1, shape=BOARDSIZE,
                       vtype=GRB.INTEGER, name='A1Vars')
MA1 = np.array([
    [A1Vars[0, 0], A1Vars[0, 0]],
    [A1Vars[1, 0], A1Vars[1, 0]],
    [A1Vars[2, 0], A1Vars[2, 0]]
])
for i in range(BOARDSIZE[0]):
    model.addConstr(A1Vars[i, 1] == 0)
# model.addConstr(A1Vars.sum() == 1)

# A2 vars
A2Vars = model.addMVar(lb=0, ub=1, shape=BOARDSIZE,
                       vtype=GRB.INTEGER, name='A2Vars')
for i in range(BOARDSIZE[1]):
    model.addConstr(A2Vars[2, i] == 0)
MA2 = np.array([
    [A2Vars[0, 0],               A2Vars[0, 1]],
    [A2Vars[0, 0] + A2Vars[0, 1], A2Vars[0, 1] + A2Vars[1, 1]],
    [A2Vars[1, 0],               A2Vars[1, 1]]
])
model.addConstr(A1Vars.sum() + A2Vars.sum() == 1)

MA = MA1 + MA2

# B vars
BVars = model.addMVar(lb=0, ub=1, shape=BOARDSIZE,
                      vtype=GRB.INTEGER, name='BVars')
model.update()
MB = np.array([
    [BVars[0, 0],              BVars[0, 0]],
    [BVars[0, 0] + BVars[1, 0], BVars[0, 0] + BVars[1, 0]],
    [BVars[1, 0],              BVars[1, 0]]
])
model.addConstr(BVars.sum() == 1)

# Constraint: moi o deu duoc phu
for i in range(BOARDSIZE[0]):
    for j in range(BOARDSIZE[1]):
        model.addConstr(MA[i, j]+MB[i, j] == 1)

model.update()
model.optimize()
if model.status == GRB.OPTIMAL:
    print("Model is optimized")
    print(f"A1Vars {A1Vars.x}")
    print(f"A2Vars {A2Vars.x}")
    print(f"BVars {BVars.x}")