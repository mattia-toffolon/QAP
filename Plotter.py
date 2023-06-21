# (UniPd 2008818) Mattia Toffolon
# Plotter for QAP problems' solutions

##!/usr/bin/env python
# encoding: utf-8

import matplotlib.pyplot as plt
import numpy as np
import random as rnd
import seaborn as sns
import sys

if __name__=='__main__':
    assert(len(sys.argv) == 2)
    f = open(sys.argv[1], 'r')

    params = f.readline().split(' ')
    n1 = int(params[0])
    n2 = int(params[1])    
    n = n1*n2
    d = int(params[2])

    S = np.zeros((n1, n2), dtype=int)
    for i in range(n):
        l = f.readline().split(' ')
        S[int(i/n2), i%n2] = int(l[1])

    f.close()
    
    sns.heatmap(S, linewidths=.5, linecolor='#bcbcbc', cmap='Greys', cbar=False, square=True, annot=np.arange(n).reshape((n1,n2)), xticklabels=False, yticklabels=False)
    plt.savefig(f'/home/mattiatoffolon/UniPd/Tesi/QAP/Document/images/Tai{n}c_{n1}x{n2}_{d}.eps', format='eps', bbox_inches='tight')
    plt.show()