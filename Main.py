# (UniPd 2008818) Mattia Toffolon
# QAP problem solver

##!/usr/bin/env python
# encoding: utf-8
from pyomo.environ import *
from pyomo.opt import SolverFactory
from cplex import *
import random
import MatricesGenerator as mg

c = Cplex()
seed = random.randrange(0, 2**30)
c.parameters.randomseed.set(seed)
c.parameters.timelimit.set(20.0)
print(c.parameters.randomseed.get(), ' - ', seed)

"""
Parameters constraints:
- n integer, n > 0
- n1 n2 integers, n1*n2==n
- m integer, 0 < m < n
"""
n  = 25
n1 = 5
n2 = 5
m = 11 

B = mg.B_generator(n, n1, n2, m)

# Function that initialize the distance parameters
def init_distances(model, l1, l2):
    return B[l1][l2]

# First function that links the y and x variables
def lin1_rule(model, i, j):
    return model.y[i, j] <= model.x[i]

# Second function that links the y and x variables
def lin2_rule(model, i, j):
    return model.y[i, j] <= model.x[j]

# Third function that links the y and x variables
def lin3_rule(model, i, j):
    return model.y[i, j] >= model.x[i]+model.x[j]-1

# Function that guarantees that the number of assigned facilities is exactly m
def m_rule(model):
    return sum(model.x[i] for i in model.Locations) == m

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
    f = open("log.txt", "x")
    for p in model.x:
        #print("x[{}] = {}".format(p, value(model.x[p])))
        f.write("x[{}] = {}".format(p, value(model.x[p])))
    f.close()