# (UniPd 2008818) Mattia Toffolon
# B matrices printer on file

##!/usr/bin/env python
# encoding: utf-8

import numpy as np
import MatricesGenerator as mg

n_parameters = [(16,4,4), (25,5,5), (36,6,6)]
gray_densities = [20.0, 50.0, 80.0]

# D is useless here!
if __name__ == '__main__':
    for n in n_parameters:
        for d in gray_densities:
            B = mg.B_generator(n[0], n[1], n[2])
            f = open(f"Tai_c instances/Tai{n[0]}c_{n[1]}x{n[2]}_{int(d)}.txt", "w")
            f.write(f"{n[1]} {n[2]} {round(n[0]*(d/100))}\n")
            for i in range(B.shape[0]):
                for j in range(B.shape[1]):
                    f.write(f"{B[i, j]} ")
                f.write("\n")
            f.close()