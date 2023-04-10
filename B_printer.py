# (UniPd 2008818) Mattia Toffolon
# B matrices printer on file

##!/usr/bin/env python
# encoding: utf-8

import MatricesGenerator as mg

n_parameters = [(16,4,4), (25,5,5), (36,6,6)]
gray_densities = [20.0, 50.0, 80.0]

if __name__ == '__main__':
    for n in n_parameters:
        for d in gray_densities:
