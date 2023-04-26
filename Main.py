# (UniPd 2008818) Mattia Toffolon
# QAP problem solver

##!/usr/bin/env python
# encoding: utf-8
from pyomo.environ import *
from pyomo.opt import SolverFactory
import random as rnd
import time
import numpy as np
import MatricesGenerator as mg

n_parameters = [(16,4,4)]
gray_densities = [40.0]

B_matrices = {}
for n in n_parameters:
    B_matrices[n] = mg.B_generator(n[0], n[1], n[2])

# Function that initialize the distance parameters
def init_distances(model, l1, l2):
    return (B_matrices[model.n])[l1, l2]

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
    return sum(model.x[i] for i in model.Locations) == round(model.n[0]*(model.d/100))

def buildmodel(n, d):
    # Model
    model = ConcreteModel()
    # sets
    model.Locations = RangeSet(0, n[0]-1)
    # params
    model.n = n
    model.d = d
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
    N = 5
    avg_times = {}
    tic = time.perf_counter()
    for n in n_parameters:
        for d in gray_densities:
            times = []
            for i in range(N):
                t1 = time.perf_counter()
                model = buildmodel(n, d)
                opt = SolverFactory('cplex_persistent')
                opt.options['randomseed'] = rnd.randrange(0, 2**30)
                opt.set_instance(model)
                res = opt.solve(tee=True)
                t2 = time.perf_counter()
                times.append(t2-t1)
                f = open(f"Solutions/n{n[0]}_{n[1]}_{n[2]}_d{int(d)}.txt", "w")
                f.write(f"{n[1]} {n[2]} {int(d)}\n")
                for p in model.x:
                    print("x[{}] = {}".format(p, value(model.x[p])))
                    f.write(f"{p} {round(value(model.x[p]))}\n")
                f.close()
            avg_times[(n,d)] = sum(times)/len(times)

    toc = time.perf_counter()
    print(f"\n\nAll instances have been solved. \nTotal time: {int((toc-tic)/60)}min {int((toc-tic)%60)}sec\n\n")
    print("Avarage solution time:")
    for t in avg_times:
        print(f"n{t[0]}_d{t[1]} : {int((avg_times[t])/60)}min {int(avg_times[t])%60}sec\n\n")