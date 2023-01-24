import gurobipy as gp
from gurobipy import GRB

def addFirstVar(model):
    model.addVar(lb=-100, vtype=GRB.INTEGER, name='x')
    model.update()
def addFirstConstr(model):
    x = model.getVarByName('x')
    model.addConstr(x <= 1)
    model.update()
model = gp.Model()
addFirstVar(model)
addFirstConstr(model)
x = model.getVarByName('x')
model.setObjective(x+1, sense=GRB.MAXIMIZE)
model.optimize()
if model.status == GRB.OPTIMAL:
    print(f"Optimal solution: {x.x}")