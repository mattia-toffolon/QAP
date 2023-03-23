# (UniPd 2008818) Mattia Toffolon
# QAP problem solver

##!/usr/bin/env python
# encoding: utf-8
from pyomo.environ import *
from pyomo.opt import SolverFactory
import MatricesGenerator as mg

n  = 16 #USER INPUT
n1 = 4 #USER INPUT
n2 = 4 #USER INPUT
m = 6  #USER INPUT
B = mg.B_generator(n, n1, n2, m)

#...
def init_distances(model, l1, l2):
    return B[l1][l2]

#...
def lin1_rule(model, i, j):
    return model.y[i, j] <= model.x[i]

#...
def lin2_rule(model, i, j):
    return model.y[i, j] <= model.x[j]

#...
def lin3_rule(model, i, j):
    return model.y[i, j] >= model.x[i]+model.x[j]-1

#...
def m_rule(model):
    return sum(model.x[i] for i in model.Locations) == n1

def buildmodel():
    # Model
    model = ConcreteModel()
    # sets
    model.Locations = RangeSet(0, n-1)
    # params
    model.Distances = Param(model.Locations, model.Locations, initialize=init_distances)
    # variables
    model.x = Var(model.Locations, domain=Boolean)
    model.y = Var(model.Locations, model.Locations, domain=Boolean)
    # objective
    model.obj = Objective(expr = sum(model.Distances[i, j] * model.y[i, j] for i in model.Locations for j in model.Locations), sense=minimize)
    # constraints
    model.rule1 = Constraint(model.Locations, model.Locations, rule=lin1_rule)
    model.rule2 = Constraint(model.Locations, model.Locations, rule=lin2_rule)
    model.rule3 = Constraint(model.Locations, model.Locations, rule=lin3_rule)
    model.rule4 = Constraint(rule=m_rule)
    return model

if __name__=="__main__":
    model = buildmodel()
    opt = SolverFactory('cplex_persistent')
    opt.set_instance(model)
    res = opt.solve(tee=True)
    for p in model.x:
        print("x[{}] = {}".format(p, value(model.x[p])))