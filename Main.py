##!/usr/bin/env python
# encoding: utf-8

from pyomo.environ import *
from pyomo.opt import SolverFactory

n  = 10 #USER INPUT
m = 3   #USER INPUT

#...
def init_distances(model, l1, l2):
    return 1

#...
def lin1_rule(model, l1, l2):
    return False

#...
def lin2_rule(model, l1, l2):
    return False

#...
def lin3_rule(model, l1, l2):
    return False

#...
def m_rule(model, l1, l2):
    return False

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
    model.obj = Objective(expr = sum(model.Distances[i][j] * model.y[i][j] for i in model.Locations for j in model.Locations), sense=minimize)
    # constraints
    model.rule1(model.Locations, model.Locations, rule=lin1_rule)
    model.rule2(model.Locations, model.Locations, rule=lin2_rule)
    model.rule3(model.Locations, model.Locations, rule=lin3_rule)
    model.rule4(model.Locations, rule=m_rule)
    return model

if __name__=="__main__":
    model = buildmodel()