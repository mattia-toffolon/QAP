#!/usr/bin/env python
# encoding: utf-8

from pyomo.environ import *
from pyomo.opt import SolverFactory

n = 7
m = 3
profits = [294, 93, 96, 155, 294, 96, 155]
weights = [600, 396, 195, 660, 600, 195, 660]
capacity = 884


def cap_rule(model, i):
	return sum(model.Weights[j] * model.x[i,j] for j in model.Items) <= model.Capacity

def take_rule(model, j):
	return sum(model.x[i,j] for i in model.Containers) <= 1

def buildmodel(**kwargs):
	# Model
	model = ConcreteModel()
	# sets
	model.Items = RangeSet(0, n-1)
	model.Containers = RangeSet(0, m-1)
	# params
	model.Profits = Param(model.Items, initialize=lambda model, j: profits[j])
	model.Weights = Param(model.Items, initialize=lambda model, j: weights[j])
	model.Capacity = capacity
	# variables
	model.x = Var(model.Containers, model.Items, domain=Boolean)
	# objective
	model.obj = Objective(expr = sum(model.Profits[j] * model.x[i,j] for i in model.Containers for j in model.Items), sense=maximize)
	# constraints
	model.capc = Constraint(model.Containers, rule=cap_rule)
	model.takec = Constraint(model.Items, rule=take_rule)
	return model


if __name__ == '__main__':
	model = buildmodel()
	opt = SolverFactory('cplex_persistent')
	opt.set_instance(model)
	res = opt.solve(tee=True)
	for p in model.x:
		print("x[{}] = {}".format(p, value(model.x[p])))