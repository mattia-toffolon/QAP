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

    k = 40
    R = np.zeros((n1*k, n2*k), dtype=int)
    for i in range(n1*k):
        for j in range(n2*k):
            R[i,j] = S[i%n1, j%n2]
    
    plt.subplot(1,2,1)
    sns.heatmap(S, linewidths=.5, linecolor='#bcbcbc', cmap='Greys', cbar=False, square=True, xticklabels=False, yticklabels=False)
    plt.subplot(1,2,2)
    sns.heatmap(R, linewidths=.5, linecolor='#ffffff', cmap='Greys', cbar=False, square=True, xticklabels=False, yticklabels=False)
    plt.subplots_adjust(wspace=0.75)
    plt.savefig(f'/home/mattiatoffolon/UniPd/Tesi/QAP/Document/images/grey_{n}_{d}.eps', format='eps', bbox_inches='tight')
    plt.show()