# (UniPd 2008818) Mattia Toffolon
# Matrices Generator for a QAP problem

##!/usr/bin/env python
# encoding: utf-8

# (Density of grey)
# Function that returns the force value (used later as a distance) between two given unit locations of the matrix: n1 x n2
def force(n1, n2, r, s, t, u):
    m = 0
    for v in {-1, 0, 1}:
        for w in {-1, 0, 1}:
            try:
                m = max(m, 1/((r-t+n1*v)**2 + (s-u+n2*w)**2))
            except ZeroDivisionError:
                return 0
    assert(m >= 0)
    return m

# Function that generates the flows matrix (A)
def A_generator(n, n1, n2, m):
    # Parameters check (n, n1, n2, m)
    try:
        n = int(n)
        assert(n > 0)
        n1 = int(n1)
        n2 = int(n2)
        assert(n1>0 and n2>0 and n1*n2==n)
        m = int(m)
        assert(m>0 and m<n)
    except (ValueError, AssertionError):
        print("Parameters' constraints not satisfied.")
        return

    A = [0]*n
    for i in range(n):
        if(i < m):
            A[i] = [1]*m + [0]*(n-m)
        else:
            A[i] = [0]*n
    return A

# Function that generates the distances matrix (B)
def B_generator(n, n1, n2, m):
    # Parameters check (n, n1, n2, m)
    try:
        n = int(n)
        assert(n > 0)
        n1 = int(n1)
        n2 = int(n2)
        assert(n1>0 and n2>0 and n1*n2==n)
        m = int(m)
        assert(m>0 and m<n)
    except (ValueError, AssertionError):
        print("Parameters' constraints not satisfied.")
        return

    B = [0]*n
    for i in range(n):
        B[i] = [0]*n
    # (note: B is always simmetric)
    scale = 100000
    for r in range(n1):
        for s in range(n2):
            for t in range(n1):
                for u in range(n2):
                    i = n2*(r-1)+s
                    j = n2*(t-1)+u
                    if(B[i][j] != 0):
                        continue
                    else:
                        B[i][j] = round(force(n1, n2, r, s, t, u)*scale)
                        B[j][i] = B[i][j]
    return B