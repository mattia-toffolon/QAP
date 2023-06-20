# (UniPd 2008818) Mattia Toffolon
# Plotter for QAP problems' solutions

##!/usr/bin/env python
# encoding: utf-8

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import random as rnd
import seaborn as sns
from matplotlib import cm
from matplotlib.colors import LightSource

if __name__=='__main__':
    """z = np.array([[0.17, 0.12, 0.28,  0.59,    0.84,    1.08],
                  [0.14, 0.10, 0.27,  0.85,    5.03,   12.99],
                  [0.05, 0.12, 0.34, 13.00,  296.35,  913.03],
                  [0.04, 0.21, 1.59, 66.86, 1611.01, 4896.74],
                  [0.04, 0.23, 2.59, 18.40,  373.01, 2942.35],
                  [0.06, 0.22, 2.46, 97.72, 2209.48, 6707.95],
                  [0.05, 0.13, 0.68, 70.83, 1641.45, 5853.22],
                  [0.05, 0.12, 0.48,  6.37,   36.44,  158.68],
                  [0.03, 0.13, 0.32,  0.77,    1.30,    5.66]], dtype=float)
    
    y = np.array([9, 16, 25, 36, 42, 45])
    x = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])

    for i in range(len(z)):
        plt.plot(y, z[i])

    labels = []
    for el in x:
        labels.append(str(el)+"%")

    plt.grid(True)
    plt.xlabel("Dimensione dell'istanza n", fontsize=10)
    plt.ylabel("Tempo di risoluzione dell'istanza (s)", fontsize=10)
    plt.legend(labels, title="Densità di grigio d", title_fontsize=10, fontsize=10)
    plt.savefig('/home/mattiatoffolon/UniPd/Tesi/QAP/Document/images/resolution_times2.eps', format='eps')
    plt.show()"""

    y = np.array([9, 16, 25, 36, 42, 45])
    x = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])
    x = np.linspace(x[0], x[len(x)-1], len(x))
    y = np.linspace(y[0], y[len(y)-1], len(y))
    y, x = np.meshgrid(y, x)

    z = np.array([[0.17, 0.12, 0.28,  0.59,    0.84,    1.08],
                  [0.14, 0.10, 0.27,  0.85,    5.03,   12.99],
                  [0.05, 0.12, 0.34, 13.00,  296.35,  913.03],
                  [0.04, 0.21, 1.59, 66.86, 1611.01, 4896.74],
                  [0.04, 0.23, 2.59, 18.40,  373.01, 2942.35],
                  [0.06, 0.22, 2.46, 97.72, 2209.48, 6707.95],
                  [0.05, 0.13, 0.68, 70.83, 1641.45, 5853.22],
                  [0.05, 0.12, 0.48,  6.37,   36.44,  158.68],
                  [0.03, 0.13, 0.32,  0.77,    1.30,    5.66]], dtype=float)
    
    fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))
    ax.set_xlabel("Densità di grigio d", fontsize=8)
    ax.set_ylabel("Dimensione dell'istanza n", fontsize=8)
    ax.set_zlabel("Tempo medio di risoluzione (s)", fontsize=8)
    surf = ax.plot_surface(x, y, z, linewidth=100)

    plt.savefig('/home/mattiatoffolon/UniPd/Tesi/QAP/Document/images/resolution_times.eps', format='eps', bbox_inches='tight', pad_inches=0.2)
    plt.show()